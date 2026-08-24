title: Hermes Agent en un VPS accesible por Tailscale
summary: Instalación y configuración de Hermes Agent, un agente de IA autónomo y de código abierto, en un VPS accesible de forma segura por una red privada Tailscale.
date: 2026-08-23 20:30:00

![Hermes Agent en VPS](images/posts/2026-08-23_hermes_agent_vps/hermes_agent.png)

El artículo anterior de este blog describía cómo montar un entorno de desarrollo agéntico con OpenCode, OmniRoute y Ponytail. Ese montaje te daba un agente de programación en la terminal, alimentado por un *router* de modelos que aprovechaba las capas gratuitas de decenas de proveedores y amansado por un *skill* que recorta la sobre-ingeniería. Pero un agente que se conecta a un proveedor de modelos por API sigue teniendo un punto débil: depende de tu equipo de desarrollo y de que esté encendido.

Ese, precisamente, es el hueco que viene a cubrir [**Hermes Agent**](https://hermes-agent.nousresearch.com/). No es una herramienta más de autocompletado ni un chatbot encerrado en una API: es un **agente autónomo de uso general** que vive donde tú decidas (un VPS, tu servidor casero, una Raspberry Pi) y al que te comunicas desde cualquier lugar. En este artículo voy a explicar qué es, por qué merece la pena probarlo y cómo lo hemos instalado y configurado en un VPS accesible por una red privada Tailscale.

## Qué es Hermes Agent

Hermes Agent es un marco de agente de IA de código abierto creado por **Nous Research**, el laboratorio detrás de los modelos Hermes. Se ejecuta en la terminal, en una aplicación de escritorio, en un panel web y en plataformas de mensajería, siempre con el mismo núcleo agéntico. A lo largo de una conversación es capaz de leer y editar ficheros, ejecutar comandos, buscar en tu historial de sesiones, lanzar tareas programadas o delegar subtareas a subagentes, y todo ello usando herramientas reales sobre el sistema donde corre.

Tres propiedades lo distinguen de la mayoría de alternativas:

* **Aprendizaje persistente entre sesiones.** Mantiene una memoria que cruza sesiones y crea *skills* reutilizables a partir de la experiencia: si resuelve una tarea complicada, puede guardar el procedimiento para reutilizarlo en el futuro.
* **Agnóstico respecto al modelo.** Funciona con OpenRouter, Anthropic, OpenAI, DeepSeek, xAI, modelos locales y más de veinte proveedores. El cambio de modelo se hace sin tocar código. Esto encaja con la filosofía de independencia de proveedor que ya exploramos en el artículo de OmniRoute.
* **Multi-superficie.** El mismo agente atiende a Telegram, Discord, Slack, WhatsApp, el CLI, la app de escritorio o el dashboard web. Está donde tú estás, no te obliga a ir a una herramienta concreta.

No es un *coding copilot* atado a un IDE: es un agente que opera sobre un sistema, y que puedes dejar trabajando en segundo plano mientras tú haces otra cosa.

## Por qué un VPS y por qué Tailscale

La forma más cómoda de tener un agente disponible de forma permanente es dejarlo corriendo en un **VPS**. Un servidor encendido las 24 horas, con una IP pública o de una red privada, se convierte en la casa del agente. Desde cualquier sitio (la mesa del ordenador personal, el portátil de la cocina, el móvil) le escribes un mensaje y trabaja, aunque ese equipo concreto se apague a continuación.

El problema es el acceso. El panel web de administración con el que se controla el agente no conviene exponerlo a la red pública sin más: quien lo conozca podría intentar usarlo. Aquí es donde entra **Tailscale**, una red privada (VPN) basada en WireGuard que une varios equipos tuyos como si todos estuvieran en la misma LAN. La elección es sencilla:

| Opción | Problema |
| --- | --- |
| Exponer el dashboard en `0.0.0.0` | Cualquiera con la IP y el puerto puede intentar entrar. Mal plan. |
| Escuchar solo en `localhost` | Solo accesible desde el propio VPS; puede llegar a usarse estableciendo un túnel SSH, pero es incómodo para el día a día. |
| **Tailscale** | Solo los equipos de tu *tailnet* alcanzan el dashboard. Secreto de red por defecto. |

Con Tailscale el agente se usa por `http://<IP-privada>:9119` desde cualquier dispositivo tuyo, y nada más. La seguridad la pone la red privada, no la esperanza de que nadie encuentre un puerto.

## Cómo se ha configurado

En este apartado resumo lo esencial del montaje. En mi experiencia la parte más delicada no es instalar, sino entender qué pieza habla con quién.

### El modelo principal y las *tools*

Un punto que conviene tener claro desde el principio: **el modelo de razonamiento y las herramientas delegadas son dos cosas separadas**. El agente usa un modelo para razonar, pero muchas de sus herramientas (búsqueda web, generación de imágenes, texto a voz, automatización de navegador) se sirven a través de servicios externos.

En esta configuración:

| Pieza | De dónde sale |
| --- | --- |
| Modelo de razonamiento | **OpenCode Zen**, como *router* de modelos, con una sola API key. |
| Tools delegadas (web, imagen, voz, navegador) | **Nous Portal**, la cuenta de Nous, que actúa como puerta de acceso (*gateway*) a Firecrawl, FAL, OpenAI Audio y Browser Use. |

Ambas conviven sin conflicto: el modelo razona desde un sitio y las herramientas se sirven desde otro. Es un matiz que merece la pena conocer porque, si se prescinde de la cuenta de Nous, las herramientas delegadas dejan de funcionar y hay que reconfigurarlas con otros servicios. Es posible, pero obliga a explorar numerosas alternativas gratuitas que en mi experiencia no han rendido tan bien (sobre todo el TTS) como las tools predeterminadas que carga la cuenta Free de Nous.

### Los pasos, en una sola pasada

Además de la explicación, me gusta dejar el procedimiento condensado para poder repetirlo en otra máquina sin pensarlo dos veces:

```bash
# 1. Instalar Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 2. Modelo + terminal local (editar ~/.hermes/config.yaml)
#    model.provider: opencode, model.base_url: https://opencode.ai/zen/v1
#    terminal.backend: local, proxy.enabled: false

# 3. Tailscale
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up        # → abrir la URL y confirmar el dispositivo

# 4. Cuenta de Nous para las tools delegadas
hermes auth add nous --no-browser
hermes config set web.backend nous
hermes config set tts.provider nous
hermes config set browser.cloud_provider nous --force
hermes config set image_gen.provider nous --force

# 5. Credenciales del dashboard (en ~/.hermes/.env)
#    HERMES_DASHBOARD_BASIC_AUTH_USERNAME, _PASSWORD y _SECRET

# 6. Dependencias del dashboard
cd ~/.hermes/hermes-agent
.venv/bin/pip install "hermes-agent[web,pty]"

# 7. Servicio systemd (escucha solo en la IP de Tailscale, puerto 9119)
systemctl --user daemon-reload
systemctl --user enable hermes-dashboard.service
systemctl --user start hermes-dashboard.service
sudo loginctl enable-linger $USER
```

El agente queda accesible en `http://<IP-de-Tailscale>:9119`, protegido por una autenticación básica de usuario y contraseña.

### El dashboard web

Hermes tiene un **dashboard web** de administración desde donde se controla todo: canales de mensajería, catálogo de herramientas, memoria, y un chat incrustado. Se configura para que escuche únicamente en la IP de Tailscale del VPS, con lo que solo los dispositivos de tu *tailnet* pueden alcanzarlo.

!!! Tip "El secreto de la autenticación"
    El dashboard usa una clave secreta (`HERMES_DASHBOARD_BASIC_AUTH_SECRET`) para firmar las sesiones. Es obligatoria cuando el servidor escucha en una dirección que no es `localhost`, y se genera con `openssl rand -base64 32`. Si se cambia, hay que volver a iniciar sesión.

!!! Warning "Un detalle del navegador con acentos"
    Con Firefox, al escribir en el chat del dashboard las vocales acentuadas aparecían sueltas (el acento sin combinarse). Era un problema de composición de teclado (dead keys) con xterm.js, no del agente. Usar Brave resolvió el tema de forma fiable con el teclado español. Aunque poco después empecé a utilizar Hermes Desktop, así que tampoco fue un problema.

### La app de escritorio

Además del navegador, existe **Hermes Desktop**, una aplicación nativa (Electron) con chat, lista de sesiones, explorador de ficheros y soporte de arrastrar y soltar. Actúa como un cliente: se conecta al mismo backend que sirve el dashboard web del VPS y hereda la sesión y las credenciales, de modo que no es una instalación aislada sino una ventana más hacia el mismo agente.

!!! Warning "Un poco de terminología"
    En Hermes, "gateway" se usa en dos sentidos que conviene no confundir. El *gateway de mensajería* (`hermes gateway`) es el que integra Telegram, Discord, WhatsApp, etc. En cambio, cuando en Hermes Desktop se habla de *Remote gateway* se refiere al propio backend que sirve el dashboard web. La app de escritorio se conecta al **mismo host y puerto** del dashboard; no hay un puerto separado.

#### Instalación

La instalación es la misma que la del agente, con el instalador oficial:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

El instalador gestiona el *venv* y las dependencias de Python, y deja el ejecutable `hermes` en `~/.local/bin`. Un detalle que conviene vigilar es la versión de **Node.js** que exigen las dependencias de la aplicación: deben ser **22.18 o superior, o 24**, y Node 23 no vale. Si el equipo aporta un Node inadecuado (p. ej. el que instala `nvm` por defecto), el instalador puede fallar con un error `EBADENGINE`; la solución es fijar la versión válida con `nvm` antes de proseguir:

```bash
nvm install 22 && nvm use 22
```

#### Conexión al gateway del VPS

Una vez arrancada con `hermes desktop`, la conexión se declara desde **Settings → Gateways → Add connection → Remote gateway**. Se rellena:

* **Name**: un nombre único, p. ej. `VPS Contabo`.
* **Gateway URL**: `http://<IP-de-Tailscale-del-VPS>:9119`.

La ventaja de ir sobre Tailscale es que esa URL solo es alcanzable desde tu *tailnet*; no hay que abrir ningún puerto al exterior. Tras pulsar **Test** (debe responder "Reachable") se inicia sesión con las mismas credenciales del dashboard.

#### El lanzador `.desktop` y un problema en Linux

Hermes Desktop instala una entrada en el menú de aplicaciones (`~/.local/share/applications/hermes.desktop`) con un icono, para poder arrancarla desde el cajón en lugar de la terminal. En las instalaciones Linux este lanzador me dio dos problemas que he tenido que corregir a mano, y que en el momento de escribir estas líneas siguen presentes en la versión que uso (quizá se resuelvan en el futuro, de modo que conviene documentarlos por si reaparecen).

El primero: el `.desktop` que genera el propio Hermes apuntaba al intérprete de Python que instala `uv` (`~/.local/share/uv/python/...`), que **no tiene las dependencias**, en lugar de al *venv* que sí las tiene; al ejecutarlo fallaba con `ModuleNotFoundError`. Y como Hermes **regenera el `.desktop` en cada arranque**, cualquier edición manual se perdía. La solución fue quitar el bit de ejecución del *script* `hermes` del repositorio para que el generador escogiera el *wrapper* de `~/.local/bin` (persistente, que ya resuelve el `venv` correcto):

```bash
chmod -x ~/.hermes/hermes-agent/hermes
```

El segundo: el lanzador del menú ejecuta la aplicación **sin cargar tu shell**, así que el `PATH` no tenía Node (el que aporta `nvm`). Hermes Desktop necesitaba Node y abortaba en silencio. La corrección fue hacer que el *wrapper* `hermes` cargara `nvm` (y fijara la versión 22) antes de invocar su intérprete:

```bash
cat > ~/.local/bin/hermes <<'EOF'
#!/usr/bin/env bash
unset PYTHONPATH
unset PYTHONHOME
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm use 22 --silent >/dev/null 2>&1 || true
exec "$HOME/.hermes/hermes-agent/venv/bin/python" "$HOME/.hermes/hermes-agent/hermes" "$@"
EOF
chmod 755 ~/.local/bin/hermes
```

Tras esos dos pasos, el `Exec=` del `.desktop` queda apuntando al *wrapper* (visible con `cat ~/.local/share/applications/hermes.desktop`), que es lo que hace que el lanzador del menú funcione igual que la terminal.

!!! Warning "Tras cada `hermes update`"
    La actualización hace `git checkout` y restaura el bit de ejecución del *script* `hermes` del repositorio, con lo que el problema del `Exec` puede volver. Basta con repetir el `chmod -x ~/.hermes/hermes-agent/hermes`.

## Qué puedes hacer con él

Una vez montado, el agente deja de ser una curiosidad a la que se le pregunta de todo y pasa a ser un compañero de trabajo que:

* **Redacta y publica.** Puede tomar la documentación de una instalación, convertirla en un post para un blog y realizar el despliegue en el servidor.
* **Gestiona el sistema.** Deja que audite servicios, busque residuos de configuración (como una unidad de systemd huérfana) o limpie credenciales obsoletas.
* **Programa.** Edita código en el repositorio, genera o corrige ficheros y ejecuta los comandos de prueba.
* **Automatiza.** Lanza tareas programadas con entrega a las plataformas que tengas conectadas (un informe diario, una copia de seguridad, una comprobación periódica).
* **Te habla.** Con síntesis de voz de calidad en español y transcripción de notas de voz, desde Telegram olvidas que detrás hay un servidor en un datacenter.

Todo eso se le pide en lenguaje natural, y trabaja mientras tú haces cualquier otra cosa.

## Conclusión

Hermes Agent es la pieza que completa el rompecabezas que empezamos en el artículo de OpenCode: si allí montamos un agente de programación *sobre tu equipo*, aquí tenemos un agente autónomo *siempre disponible* que vive en un VPS y atiende desde tus plataformas habituales. Es software libre, agnóstico respecto al modelo y con un circuito de aprendizaje que lo hace más útil con el paso de las sesiones.

El coste de entrada es cero (el agente en sí es gratuito y el modelo puede salir de una capa gratuita o de un router barato), a cambio de un panel de administración, una memoria persistente y la posibilidad de hablar con tu agente desde cualquier sitio. Si te gusta el desarrollo agéntico y no quieres depender de que tu equipo esté encendido, vale la pena dedicarle una tarde.
