title: Instalación OpenCode, OmniRoute y Ponytail
summary: Instalación y configuración de OpenCode con OmniRoute y Ponytail para programar con agentes de IA minimizando cuotas y costes.
date: 2026-07-26 12:00:00

![OpenCode + OmniRoute](images/posts/2026-07-26_opencode_omniroute/opencode_omniroute.png)

El desarrollo asistido por IA empezó siendo un autocompletado inteligente del código a nivel de línea. Pasó a ser una "segunda opinión" que revisaba el código a nivel de fichero y sugería cambios. En los últimos dos años se ha dado un importante paso más allá hasta llegar al paradigma actual, el *desarrollo agéntico*: un agente que lee el repositorio completo, edita ficheros, ejecuta comandos, realiza por sí solo los cambios que antes solo se sugerían, lanza los tests e itera hasta cerrar la tarea. El problema es que todas las herramientas comerciales de este tipo (Claude Code, Cursor, Devin, Copilot, Codex, etc.) comparten dos limitaciones: una suscripción mensual y unas cuotas que se agotan justo cuando la sesión se está poniendo interesante.

Hay además un tercer problema, más silencioso pero también caro: los agentes tienden a **sobre-construir**. Se les pide un selector de fechas y acaban instalando una librería, escribiendo un componente envoltorio y una hoja de estilos. Cada línea de más se paga dos veces, en tokens al generarla y en tokens cada vez que vuelve a entrar en el contexto.

En este artículo se describe cómo montar un entorno de desarrollo agéntico completo combinando tres proyectos de código abierto que resuelven precisamente esas limitaciones:

* [**OpenCode**](https://opencode.ai/): el agente de programación en terminal.
* [**OmniRoute**](https://omniroute.online/): el router/gateway de modelos que alimenta al agente.
* [**Ponytail**](https://github.com/DietrichGebert/ponytail): el *skill* que impone al agente disciplina de código mínimo.

## Descripción de los productos

### OpenCode

OpenCode es un agente de programación que se ejecuta en la terminal (TUI), de código abierto y, lo más importante para nuestro propósito, **agnóstico respecto al proveedor de modelos**. A diferencia de Claude Code (atado a Anthropic) o Codex (atado a OpenAI), OpenCode permite configurar cualquier proveedor, incluidos los que exponen una API compatible con OpenAI, que a día de hoy son prácticamente todos.

Sus características principales:

* Interfaz de terminal con sesiones persistentes, gestión de contexto y *undo* de los cambios aplicados.
* Acceso a herramientas: lectura y escritura de ficheros, ejecución de comandos, búsqueda en el repositorio, control de versiones.
* Fichero de contexto por proyecto (`AGENTS.md`) que se genera con `/init` y que sirve para instruir al agente sobre las convenciones del repositorio.
* Soporte de MCP (*Model Context Protocol*) para añadir herramientas externas.
* Modo no interactivo o CLI (`opencode run "..."`) para automatizaciones y scripts.
* Agentes especializados y modos de trabajo (por ejemplo un modo *plan* que no hace cambios pensado para la fase de planificación previa).

### OmniRoute

OmniRoute es un *gateway* de IA local y de código abierto. Se instala en la propia máquina (o en un VPS), levanta un endpoint compatible con la API de OpenAI y un panel web de administración, y desde ahí enruta cada petición hacia cualquiera de los cientos de proveedores que tiene catalogados, de los que unos 90 disponen de capa gratuita.

Lo interesante no es el catálogo en sí, sino lo que hace con él:

* **Enrutado automático**: usando el modelo virtual `auto`, OmniRoute construye un *combo* con los proveedores que tengamos conectados y elige uno en cada petición según su puntuación en vivo. Existen variantes: `auto/coding` (calidad para generar código), `auto/fast` (menor latencia), `auto/cheap` (menor coste por token) y `auto/offline` (mayor margen de cuota disponible).
* **Fallback en cascada**: cuando un proveedor devuelve un error de cuota, un *rate limit* o un 5xx, la petición se reintenta contra el siguiente proveedor de la lista de forma transparente para el cliente. Esto es lo que evita el clásico "se acabó tu cuota, vuelve en cinco horas".
* **Compresión de contexto**: una batería de motores que recortan el prompt (deduplicación, poda de historial, compactado de ficheros) y que permiten ahorros importantes de tokens, especialmente valiosos cuando se trabaja contra capas gratuitas medidas en tokens/día.
* **Panel de control** en `http://localhost:20128` con estadísticas de uso por proveedor, gestión de claves API y configuración asistida de las herramientas CLI más habituales.
* **Local-first**: las claves de los proveedores y el tráfico se quedan en la máquina; OmniRoute no es un servicio en la nube al que haya que suscribirse.

### Ponytail

Ponytail no es un programa que se ejecute ni un servicio: es un ***skill***, es decir un conjunto de instrucciones que se inyectan en el contexto del agente en cada turno para modificar su comportamiento. Su cometido es uno solo, combatir la sobre-ingeniería, y lo hace obligando al agente a recorrer una escalera de decisión antes de escribir una sola línea, deteniéndose en el primer peldaño que resuelva el problema:

```txt
1. ¿Esto necesita existir?          → no: no lo hagas (YAGNI)
2. ¿Ya está en este repositorio?    → reutilízalo, no lo reescribas
3. ¿Lo hace la librería estándar?   → úsala
4. ¿Es una función nativa de la plataforma? → úsala
5. ¿Hay una dependencia ya instalada?       → úsala
6. ¿Cabe en una línea?              → una línea
7. Sólo entonces: lo mínimo que funcione
```

El ejemplo canónico del proyecto lo resume bien: ante la petición de un selector de fechas, el resultado deja de ser una librería más un componente y pasa a ser, gracias a Ponytail, `<input type="date">`.

Dos matices importantes:

* La escalera se aplica **después** de entender el problema, no en lugar de entenderlo. El agente sigue obligado a leer el código afectado y a seguir el flujo real antes de elegir peldaño. Perezoso con la solución, nunca con la lectura.
* Hay cuatro cosas que nunca se recortan: validación en las fronteras de confianza, gestión de pérdida de datos, seguridad y accesibilidad. La regla no es "menos tokens", es "sólo lo que la tarea necesita".

Según el *benchmark* que publica el proyecto (sesiones reales de un agente sobre un repositorio FastAPI + React, con y sin el *skill*), los resultados frente a la línea base son un 54% menos de líneas de código, un 22% menos de tokens, un 20% menos de coste y un 27% menos de tiempo, sin penalización en las comprobaciones de seguridad. Como siempre con los *benchmarks*, conviene tomarlos como orden de magnitud y no como promesa: el ahorro es enorme donde hay una trampa clara de sobre-construcción y casi nulo donde el código ya era mínimo.

Ponytail funciona en un buen número de agentes (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, Devin...), y OpenCode es uno de los que tiene soporte de primera clase mediante *plugin*.

### El valor de la combinación

Por separado cada pieza es útil, pero es al combinarlas cuando desaparecen las limitaciones que mencionábamos al principio. Cada una cubre una capa distinta y no se solapan: OmniRoute decide **quién** responde, OpenCode decide **qué** se hace, y Ponytail decide **cuánto** código se escribe.

| Problema | Cómo lo resuelve la combinación |
| --- | --- |
| Suscripción mensual | OpenCode es gratuito y OmniRoute se conecta a capas gratuitas de decenas de proveedores. El coste de entrada es 0 €. |
| Agotamiento de cuota | El fallback de OmniRoute salta al siguiente proveedor sin interrumpir la sesión del agente. |
| Dependencia de un proveedor | El agente sólo conoce un endpoint (`localhost:20128/v1`); cambiar de modelo o de proveedor no requiere tocar el agente. |
| Consumo excesivo de tokens | Los motores de compresión de OmniRoute reducen el tamaño de los prompts que envía el agente, que suelen ser grandes por el contexto del repositorio. |
| Falta de visibilidad del gasto | El panel de OmniRoute centraliza el consumo de todos los proveedores y de todas las herramientas conectadas. |
| Código sobredimensionado | Ponytail recorta lo que el agente construye, lo que a su vez reduce el código a revisar, mantener y volver a meter en el contexto en las siguientes sesiones. |

La combinación de las tres piezas tiene un efecto multiplicador sobre la cuota disponible: Ponytail reduce los tokens de salida (menos código generado), la compresión de OmniRoute reduce los de entrada (menos contexto enviado) y el fallback aprovecha la cuota de todos los proveedores conectados. Con capas gratuitas medidas en tokens/día esto es la diferencia entre trabajar una hora y trabajar toda la tarde.

Un beneficio adicional: como OmniRoute expone un endpoint estándar, el mismo gateway sirve simultáneamente a OpenCode en la terminal, a una extensión de VSCode o a cualquier otro cliente compatible con la API de OpenAI. Se configura una vez y lo aprovecha todo el entorno.

!!! Tip "Modelos modestos, mejores resultados"
    Un efecto colateral interesante de Ponytail es que hace más viable trabajar con los modelos gratuitos, que suelen ser más pequeños. Cuanto menor es el volumen de código que se le pide generar a un modelo, menos oportunidades tiene de equivocarse; el *skill* reduce precisamente el tamaño de lo que se le encarga en cada paso.

!!! Warning "Sobre las capas gratuitas"
    Las condiciones de las capas gratuitas de los proveedores cambian con frecuencia y algunas desaparecen sin previo aviso. La ventaja del enfoque con OmniRoute es que esos cambios se absorben en el gateway (conectando otro proveedor) sin tocar la configuración del agente. Conviene también revisar las políticas de privacidad de cada proveedor gratuito antes de enviarles el código de un proyecto sensible.

## Instalación

Todo el procedimiento se ha realizado sobre Linux. En Windows y macOS los pasos son equivalentes, cambiando la forma de instalar los requisitos.

Los tres proyectos se distribuyen vía npm, así que el único requisito común es disponer de Node.js reciente (versión 22 o superior).

```bash
node --version
```

### Instalación de OpenCode

La forma recomendada es el script oficial de instalación:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Alternativamente, según el sistema:

```bash
npm install -g opencode-ai                  # npm (también bun, pnpm o yarn)
brew install anomalyco/tap/opencode         # macOS / Linux con Homebrew
sudo pacman -S opencode                     # Arch Linux (repositorios oficiales)
paru -S opencode-bin                        # Arch Linux (AUR, última versión)
```

Comprobamos la instalación lanzando el agente dentro de cualquier directorio:

```bash
opencode
```

En este punto OpenCode arrancará pero pedirá credenciales de algún proveedor. No hace falta darle ninguna todavía: ese hueco lo va a ocupar OmniRoute.

### Instalación de OmniRoute

```bash
npm install -g omniroute
omniroute
```

El comando `omniroute` levanta a la vez la API y el panel web en el puerto `20128`:

* Panel: `http://localhost:20128`
* API compatible con OpenAI: `http://localhost:20128/v1`

Existen también otras formas de despliegue, útiles si se quiere dejar el gateway funcionando de forma permanente:

```bash
docker run omniroute                        # contenedor
```

Además del paquete npm y el contenedor, el proyecto distribuye una aplicación de escritorio (Electron), imágenes para arm64 (funciona en una Raspberry Pi) y es ejecutable en Android bajo Termux. Una opción interesante es dejar OmniRoute corriendo en un VPS o en un servidor casero y apuntar contra él desde todos los equipos de desarrollo.

### Instalación de Ponytail

Ponytail no se instala en el sistema, se declara como *plugin* de OpenCode. Basta con añadir esta entrada al fichero de configuración `opencode.json` (en el apartado siguiente se muestra el fichero completo con las tres piezas):

```json
{ "plugin": ["@dietrichgebert/ponytail"] }
```

OpenCode descarga el paquete desde npm la primera vez que arranca con esa configuración. Si se prefiere trabajar sobre una copia local del repositorio, para poder modificar las reglas, se clona y se apunta al fichero del *plugin*:

```bash
git clone https://github.com/DietrichGebert/ponytail.git ~/ponytail
```

```json
{ "plugin": ["/home/usuario/ponytail/.opencode/plugins/ponytail.mjs"] }
```

Las rutas relativas (del tipo `./.opencode/plugins/ponytail.mjs`) se resuelven respecto al `opencode.json` que las declara, de modo que para compartir un mismo *checkout* entre varios proyectos hay que usar la ruta absoluta, como en el ejemplo.

!!! Tip "Sin plugin también funciona"
    El repositorio incluye las reglas en formato `AGENTS.md` y en los formatos de rules de Cursor, Devin, Cline, Kiro, Copilot, etc. Copiando ese fichero al proyecto se obtiene el comportamiento siempre activo en prácticamente cualquier agente. Lo que añade el *plugin* de OpenCode son los comandos `/ponytail` y los niveles de intensidad.

## Configuración conjunta

La integración consiste en que OpenCode deje de hablar con los proveedores y hable únicamente con OmniRoute, y en que Ponytail se inyecte en cada turno de la conversación. Son cinco pasos.

### 1. Conectar proveedores en OmniRoute

Con `omniroute` en marcha, abrimos `http://localhost:20128` y vamos a la sección **Providers** (recomiendo configurar el interfaz en idioma `English` ya que si no aparecen numerosas cadenas precedidas de la partícula `__MISSING__`). Ahí aparece el catálogo con un indicador de cuáles tienen capa gratuita. Conviene conectar **varios**, ya que el valor del sistema está justamente en la redundancia: cuando uno agota su cuota, el resto siguen disponibles. Los proveedores sin necesidad de clave (`No Auth`) están conectados por defecto.

El catálogo está clasificado por **categorías**, y la categoría marca el procedimiento de conexión:

| Categoría | Cómo se conecta |
| --- | --- |
| *No Auth* | Nada que hacer, están activos desde el primer arranque. |
| *Free Tier* | Capa gratuita que sí requiere darse de alta en el proveedor y pegar una clave de API. |
| *OAuth* | Botón de inicio de sesión para proveedores en los que ya tengamos cuenta: OmniRoute abre el flujo del proveedor y guarda el *token* resultante. |
| *API Key* | Proveedores de pago (algunos con crédito inicial de regalo); se pega la clave. |
| *Local* | Modelos que corren en la propia máquina (Ollama, LM Studio, vLLM…); se indica la URL local. |

El filtro de la parte superior de la pantalla permite quedarse sólo con las que interesan, y el buscador acepta el nombre o el identificador del proveedor.

#### Proveedores con clave de API gratuita

El procedimiento es siempre el mismo, cambiando únicamente el sitio del que se obtiene la clave:

1. Darse de alta en el proveedor y generar una clave de API en su panel.
2. En OmniRoute, **Providers** → buscar el proveedor → botón de conectar/configurar.
3. Pegar la clave en el formulario y guardar.
4. Pulsar el botón de **Test** de la tarjeta del proveedor. Si responde correctamente, sus modelos pasan a formar parte del catálogo del gateway y entran automáticamente en el *pool* del modelo `auto`.

Algunos candidatos con capa gratuita y sin tarjeta de crédito pueden encontrarse [aquí](https://github.com/diegosouzapw/OmniRoute/wiki/Providers-Guide#best-free-providers) y [aquí](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.49/docs/getting-started/FREE-TIERS-GUIDE.md).

#### Proveedores OAuth

Con estos no hay clave que copiar: se pulsa el botón de conexión de la tarjeta, se abre el flujo de inicio de sesión del proveedor en el navegador, y al terminar OmniRoute guarda las credenciales cifradas en su base de datos local. Es el caso de las cuentas de herramientas que ya se estén usando (Copilot, Cursor, Kilo Code, Qoder, etc.).

!!! Warning "Revisa los términos de servicio"
    Varios de estos proveedores son en realidad servicios pensados para consumirse desde su propio cliente, y algunos prohíben expresamente en sus condiciones el uso a través de *proxies* o clientes de terceros. La ficha del proveedor en OmniRoute lo advierte cuando es el caso. Conviene leer esos avisos antes de conectar una cuenta que interese conservar.

#### Todo desde la línea de comandos

Si se prefiere no pasar por el navegador, los proveedores de clave de API se pueden gestionar íntegramente desde la CLI, lo que resulta muy práctico para reproducir la configuración en otra máquina o dejarla en un script:

```bash
omniroute providers available --category free      # ver el catálogo de capa gratuita
omniroute providers available --search cerebras    # buscar uno concreto

omniroute setup --add-provider \
  --provider cerebras \
  --api-key 'csk-...' \
  --test-provider                                  # añadirlo y probarlo de una vez

omniroute providers list                           # conexiones ya configuradas
omniroute providers test-all                       # probar todas de golpe
```

`providers test-all` es el comando que conviene lanzar de vez en cuando: informa de un vistazo sobre qué proveedores han dejado de responder, ya sea por cuota agotada, por credenciales caducadas o porque el servicio ha cambiado sus condiciones.

### 2. Crear una clave de API de OmniRoute

En el panel, sección **API Manager** → **Create API Key**. Le damos un nombre descriptivo (por ejemplo `opencode`) y copiamos la clave generada, con formato `sk-xxxxxxxx-xxxxxxxx`.

Esta clave es local: es la que usarán nuestros clientes para autenticarse contra el gateway, y no tiene nada que ver con las claves de los proveedores, que quedan custodiadas por OmniRoute.

Podemos verificar que el gateway responde y ver qué modelos ofrece:

```bash
curl http://localhost:20128/v1/models -H "Authorization: Bearer sk-tu-clave-omniroute"
```

### 3. Declarar OmniRoute como proveedor en OpenCode

OpenCode admite cualquier proveedor compatible con OpenAI declarándolo en su fichero de configuración. Para que la configuración aplique a todos los proyectos, la escribimos en `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@dietrichgebert/ponytail"],
  "provider": {
    "omniroute": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "OmniRoute",
      "options": {
        "baseURL": "http://localhost:20128/v1",
        "apiKey": "sk-tu-clave-omniroute"
      },
      "models": {
        "auto": { "name": "Auto (equilibrado)" },
        "auto/coding": { "name": "Auto (calidad para código)" },
        "auto/cheap": { "name": "Auto (menor coste)" },
        "auto/fast": { "name": "Auto (menor latencia)" },
        "auto/offline": { "name": "Auto (máxima cuota disponible)" }
      }
    }
  },
  "model": "omniroute/auto/coding"
}
```

Los puntos importantes de esta configuración:

* `npm`: el adaptador `@ai-sdk/openai-compatible` es el que se usa con endpoints `/v1/chat/completions`, que es el caso de OmniRoute.
* `options.baseURL`: el endpoint del gateway. Si OmniRoute está en otra máquina, aquí va su IP o dominio.
* `options.apiKey`: la clave de API que creamos en OmniRoute.
* `models`: no hace falta enumerar modelos concretos de proveedores; basta con declarar los modelos virtuales `auto`, que son los que activan el enrutado inteligente y el fallback. Si se quiere fijar un modelo concreto, se puede añadir con el identificador que devuelve `/v1/models`, la consulta del [punto anterior](#2-crear-una-clave-de-api-de-omniroute).
* `model`: modelo por defecto al arrancar. `auto/coding` es una buena elección para desarrollo; `auto/offline` resulta útil cuando lo prioritario es no quedarse sin cuota.
* `plugin`: la lista de *plugins* de OpenCode, donde entra Ponytail.

!!! Tip "Clave fuera del fichero de configuración"
    Si el fichero de configuración se va a versionar (por ejemplo en un repositorio de *dotfiles*), es preferible no escribir la clave en él. OpenCode permite almacenar credenciales con el comando `/connect` (opción *Other*, id `omniroute`), en cuyo caso se puede omitir `options.apiKey` del JSON.

También es posible ubicar el fichero como `opencode.json` en la raíz de un proyecto concreto, en cuyo caso su configuración se combina con la global. Esto resulta práctico para forzar un modelo distinto en un proyecto determinado.

### 4. Ajustar el nivel de Ponytail

Ponytail no necesita fichero de configuración: funciona nada más declararlo como *plugin*. Lo único que conviene decidir es el **nivel de intensidad**, que se cambia en caliente desde la TUI:

```txt
/ponytail            → informa del nivel actual
/ponytail lite       → recorte suave
/ponytail full       → nivel por defecto
/ponytail ultra      → recorte agresivo
/ponytail off        → desactivado para esta sesión
```

El nivel por defecto es `full`. Para fijar otro en todas las sesiones nuevas se usa la variable de entorno `PONYTAIL_DEFAULT_MODE` o el campo `defaultMode` de `~/.config/ponytail/config.json`:

```bash
export PONYTAIL_DEFAULT_MODE="full"
```

Mientras está activo, el conjunto de reglas se inyecta también en los subagentes que lance el agente principal. Si interesa excluir a alguno (por ejemplo los subagentes de búsqueda, que no escriben código), se puede acotar con una expresión regular contra el tipo de subagente:

```bash
export PONYTAIL_SUBAGENT_MATCHER="build|code"
```

### 5. Verificar la integración

Arrancamos el agente y comprobamos que aparece el proveedor:

```bash
opencode
```

Dentro de la TUI, el comando `/models` debe mostrar las entradas de OmniRoute. Una prueba rápida en modo no interactivo o CLI:

```bash
opencode run "Resume en tres líneas qué hace este repositorio" --model omniroute/auto/coding
```

Mientras se ejecuta, en el panel de OmniRoute puede verse en tiempo real qué proveedor ha atendido la petición (`Monitoring > Logs`), cuántos tokens se han consumido y cuántos ha ahorrado la compresión. Si un proveedor falla, en el registro se aprecia el salto automático al siguiente.

Para comprobar que Ponytail está cargado basta con ejecutar `/ponytail` en la TUI, que responde con el nivel activo, o `/ponytail-help`, que lista sus comandos. El propio arranque de la sesión muestra también el modo actual.

!!! Tip "Variables de entorno para el resto de herramientas"
    Exportando estas variables en el `.bashrc` o `.zshrc`, cualquier otra herramienta que respete la convención de OpenAI usará también el gateway sin configuración adicional:

    ```bash
    export OPENAI_BASE_URL="http://localhost:20128/v1"
    export OPENAI_API_KEY="sk-tu-clave-omniroute"
    ```

## Tipos de proyectos y operativa

Una vez montado el entorno, la operativa es esencialmente la misma con independencia del lenguaje, del tamaño del proyecto o de la naturaleza de la tarea. Lo que cambia entre unos casos y otros no es el procedimiento, sino el modelo que conviene seleccionar, el nivel de recorte que interesa y la cantidad de contexto que hay que preparar. Por eso describimos primero el flujo común y después los ajustes por tipo de proyecto.

### Operativa común

1. **Situarse en el repositorio y arrancar el agente**:

    ```bash
    cd mi-proyecto
    opencode
    ```

2. **Generar el fichero de contexto** la primera vez, con el comando `/init` dentro de la TUI. OpenCode explora el repositorio y escribe un `AGENTS.md` con la descripción del proyecto, los comandos de compilación y test y las convenciones detectadas. Merece la pena revisarlo y completarlo a mano: es el documento que más influye en la calidad de los resultados posteriores, y conviene versionarlo con el proyecto.

3. **Planificar antes de ejecutar**. Para cualquier cambio que no sea trivial, pedir primero un plan en lugar de la implementación directa. OpenCode dispone de un modo de planificación que no escribe en disco, y revisar el plan cuesta mucho menos que revisar un *diff* equivocado de 400 líneas.

4. **Iterar en pasos pequeños**, validando con las herramientas del propio proyecto (compilador, *linter*, tests) tras cada paso. El agente puede ejecutar esos comandos por sí mismo si están documentados en `AGENTS.md`.

5. **Pasar la revisión de Ponytail** antes de dar la tarea por buena, con `/ponytail-review`. Analiza el *diff* actual buscando sobre-ingeniería y devuelve una lista de cosas a borrar. Es el paso que más rápido amortiza el tiempo invertido.

6. **Revisar el `diff` y confirmar** con el control de versiones. Conviene trabajar siempre sobre una rama y hacer *commits* pequeños: es la red de seguridad natural cuando quien escribe el código es un agente.

7. **Limpiar el contexto entre tareas** con `/new`. Arrastrar el contexto de una tarea terminada empeora los resultados y dispara el consumo de tokens. En el apartado siguiente se detalla la gestión de sesiones.

8. **Vigilar el panel de OmniRoute** de vez en cuando para ver qué proveedores se están usando, cuáles se han agotado y si el ahorro por compresión es el esperado.

### Gestión de sesiones en OpenCode

Al empezar a trabajar con OpenCode sorprende comprobar que, por mucho que se salga de la TUI con `Ctrl-D` o con `/exit`, las sesiones siguen apareciendo en el listado. No es un problema de cierre incompleto ni un proceso que se quede colgado: es que **una sesión no es un proceso, es una conversación persistida**. Salir de la TUI termina la interfaz, pero el historial de la conversación (mensajes, herramientas ejecutadas, ficheros tocados, consumo de tokens) se guarda en la base de datos local de OpenCode para poder retomarlo después. Y como cada invocación de `opencode` sin argumentos abre una sesión nueva, en un par de días de uso el listado tiene decenas de entradas.

Dicho de otra forma: "cerrar" no significa "borrar". Lo que hay que adquirir es la costumbre de reutilizar y de podar.

#### Retomar en lugar de crear

Lo primero es dejar de arrancar siempre en blanco. Estas son las tres formas de continuar un trabajo previo:

```bash
opencode --continue                  # retoma la última sesión del proyecto actual (-c)
opencode --session <sessionID>       # retoma una sesión concreta (-s)
opencode --session <sessionID> --fork # la bifurca en una copia, dejando la original intacta
```

Y desde dentro de la TUI, el comando `/sessions` (alias `/resume` y `/continue`, atajo `Ctrl-X L`) abre el selector para saltar de una sesión a otra sin salir del programa.

La opción `--fork` es especialmente útil cuando una conversación ha llegado a un punto interesante y se quiere probar dos caminos distintos: se bifurca y cada rama sigue por su lado, igual que con `git branch`.

#### Cerrar bien cada tarea

Dentro de la TUI hay dos comandos que marcan el final de una tarea:

* `/new` (alias `/clear`, atajo `Ctrl-X N`): abre una sesión nueva y limpia. Es lo que hay que usar al cambiar de tarea, en lugar de seguir escribiendo en la conversación anterior.
* `/compact` (alias `/summarize`, atajo `Ctrl-X C`): resume la conversación actual para liberar ventana de contexto sin perder el hilo. Es la alternativa cuando se quiere continuar con la misma tarea pero el contexto se ha vuelto pesado.

Si de una sesión interesa conservar el resultado, `/export` vuelca la conversación a Markdown y la abre en el editor, y `opencode export <sessionID>` hace lo propio en JSON desde la línea de comandos.

#### Inventariar y podar

Desde fuera de la TUI se gestiona el inventario completo:

```bash
opencode session list                # listado de sesiones
opencode session list -n 20          # limitar el número de entradas
opencode session list --format json  # salida procesable por script
opencode session delete <sessionID>  # eliminar una sesión
```

Y para ver el coste de lo acumulado, que en este montaje es lo que determina cuánta cuota gratuita se está quemando:

```bash
opencode stats                       # consumo de tokens y coste
opencode stats --days 7 --models     # últimos 7 días, desglosado por modelo
opencode stats --project             # sólo el proyecto actual
```

#### Un flujo que funciona

Reuniendo lo anterior, la rutina que mantiene el listado bajo control es:

1. **Una sesión por tarea**, no por jornada ni por proyecto. La unidad natural es lo que acaba en un *commit*.
2. **Retomar con `-c`** cuando se vuelve a una tarea a medias, en vez de arrancar `opencode` a secas y volver a explicar el contexto (que además se paga en tokens).
3. **`/new` al cambiar de tarea** y `/compact` si la tarea se alarga pero sigue siendo la misma.
4. **Exportar lo que merezca la pena** antes de dar por cerrada una sesión con conclusiones valiosas.
5. **Poda periódica**, por ejemplo semanal, revisando `opencode session list` y borrando con `opencode session delete` todo lo que ya esté commiteado y no aporte nada.
6. **Revisar `opencode stats`** en esa misma poda, para tener la foto del consumo junto a la del panel de OmniRoute.

!!! Tip "Las sesiones van por proyecto"
    OpenCode asocia las sesiones al directorio de trabajo desde el que se lanzó, así que `--continue` retoma la última sesión *de ese proyecto*, no la última en términos absolutos. Es un detalle que ayuda: trabajar siempre desde la raíz del repositorio mantiene los listados ordenados por proyecto de forma natural.

### Comandos de Ponytail

Más allá del nivel de intensidad, el *skill* aporta un puñado de comandos que encajan en distintos momentos del flujo anterior:

| Comando | Para qué sirve |
| --- | --- |
| `/ponytail [lite \| full \| ultra \| off]` | Ajusta la intensidad o la desactiva. Sin argumento informa del nivel actual. |
| `/ponytail-review` | Revisa el *diff* actual en busca de sobre-ingeniería y devuelve una lista de borrado. |
| `/ponytail-audit` | Lo mismo, pero sobre todo el repositorio en lugar de sobre el *diff*. |
| `/ponytail-debt` | Recopila en un registro los atajos marcados con `ponytail:` que se hayan ido aplazando. |
| `/ponytail-gain` | Muestra el marcador de impacto medido (menos código, menos coste, más velocidad). |
| `/ponytail-help` | Referencia rápida de los comandos anteriores. |

Cuando el agente decide no construir algo, deja un comentario del tipo `ponytail: browser has one` explicando el peldaño de la escalera en el que se detuvo. Esos comentarios son los que después recoge `/ponytail-debt`, de forma que las decisiones de "esto ya se hará si hace falta" quedan registradas en lugar de perderse.

### Ajustes según el tipo de proyecto

Lo único que varía de forma apreciable entre escenarios es la elección de modelo y la preparación del contexto:

* **Proyectos nuevos desde cero (*greenfield*)**. Hay poco contexto que cargar y mucho código que generar. Es el escenario ideal para las capas gratuitas: `auto/cheap` o `auto/offline` dan buen resultado y el consumo de tokens de entrada es bajo. Conviene empezar pidiendo el andamiaje del proyecto y el fichero de dependencias, y sólo después las funcionalidades. También es donde más se nota Ponytail, porque es donde el agente tiene más libertad para inventar estructura de más.

* **Mantenimiento y evolución de código existente**. Aquí el cuello de botella es el contexto: el agente necesita leer bastante código antes de tocar nada. Interesa un `AGENTS.md` detallado, activar la compresión de contexto de OmniRoute y usar `auto/coding` para las tareas de modificación. Es también el caso donde más se nota el fallback, porque las sesiones son largas. El peldaño "¿ya está en este repositorio?" de Ponytail resulta especialmente valioso, ya que evita el clásico duplicado de un helper que ya existía tres directorios más allá.

* **Depuración de errores**. El flujo es el mismo, pero funciona mucho mejor si se le proporciona al agente una forma de reproducir el fallo (un test que falle, la traza completa, el comando exacto). Modelos con capacidad de razonamiento explícito dan mejores resultados; en OmniRoute se pueden seleccionar las variantes *thinking* de los modelos que las ofrezcan. Un nivel `lite` de Ponytail, o incluso `off`, puede ser preferible aquí: al depurar interesa entender, no recortar.

* **Scripting y automatización**. Aquí interesa el modo no interactivo, que permite integrar el agente en scripts, *hooks* de git o tareas programadas:

    ```bash
    opencode run "Actualiza el CHANGELOG con los commits desde la última etiqueta" \
      --model omniroute/auto/fast
    ```

* **Refactorizaciones amplias y repetitivas**. Trocear el trabajo en tareas independientes y lanzarlas por separado, en lugar de pedir un cambio masivo en una sola sesión. Además de dar mejores resultados, evita agotar la ventana de contexto y la cuota de un proveedor de una sentada. Si lo que se busca es precisamente adelgazar código heredado, `/ponytail-audit` sobre el repositorio completo y `/ponytail ultra` son el punto de partida natural.

* **Proyectos con código sensible**. Si no se puede enviar el código a terceros, la misma configuración sirve conectando en OmniRoute un proveedor local (Ollama o LM Studio en la propia máquina) en lugar de los servicios gratuitos. Cambia el proveedor conectado en el panel; ni OpenCode ni el flujo de trabajo se tocan.

## Conclusión

La combinación de OpenCode, OmniRoute y Ponytail proporciona un entorno de desarrollo agéntico completo con coste de entrada nulo y sin las interrupciones por cuota agotada que caracterizan a las alternativas comerciales. Cada pieza ataca un frente distinto: el agente aporta las capacidades, el gateway la cuota y la independencia de proveedor, y el *skill* la disciplina para que el código generado sea el mínimo necesario. Y las tres se declaran en un único fichero de configuración de unas veinte líneas.

El precio a pagar es una configuración inicial algo más laboriosa que la de un producto cerrado y la necesidad de revisar de vez en cuando qué proveedores gratuitos siguen operativos. A cambio se obtiene algo que las suscripciones no dan: independencia respecto al proveedor, visibilidad completa de lo que consume el agente y menos código del que arrepentirse.
