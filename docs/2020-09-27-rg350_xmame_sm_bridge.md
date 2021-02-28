title: RG350 Interfaz xMAME SimpleMenu
summary: Interfaz de ajustes para las ROMs de xMAME lanzadas desde SimpleMenu.
date: 2020-09-27 02:30:00

![Icono](/images/posts/xmame_sm_bridge/icon.png)

[xMAME](/2020-04-15-rg350_xmame.html) tiene un frontend propio que intercala una pantalla de ajustes entre la selección de la ROM y la ejecución final de la misma. Ésta:

![xMAME ROM Settings](/images/posts/xmame_sm_bridge/xmame_rom_settings.png)

Cuando se integra xMAME en SimpleMenu se pierde esta pantalla de ajustes y la ROM es ejecutada con las opciones predeterminadas. Para mejorar esta situación se ha desarrollado una especie de clon de la pantalla de ajustes de xMAME que se puede integrar entre SimpleMenu y los binarios de xMAME que ejecutan al final la ROM.

Vamos a ver aquí cómo instalar y utilizar este interfaz. Al final se describen también los aspectos técnicos de la solución para los que estén interesados. Funciona en los dos modelos de pantalla de la RG350, es decir que sirve tanto para el modelo original como los nuevos RG350P y RG350M.

## Instalación

La instalación se hace por medio de un OPK que sitúa los ficheros necesarios dentro de la ruta donde se encuentra xMAME (en concreto en el subdirectorio `/media/data/local/share/xmame/sm_bridge`). También hace las modificaciones automáticamente en los ficheros de configuración de SimpleMenu. Naturalmente, antes tendremos que tener instalados [xMAME](/2020-04-15-rg350_xmame.html) y [SimpleMenu](/2020-01-25-rg350_simplemenu.html).

El OPK con el instalador se puede descargar desde el siguiente enlace: [https://github.com/eduardofilo/RG350_xmame_sm_bridge/releases/download/1.2/xmame_sm_bridge_installer_1.2.opk](https://github.com/eduardofilo/RG350_xmame_sm_bridge/releases/download/1.2/xmame_sm_bridge_installer_1.2.opk)

Una vez instalado en la RG350 (como cualquier otro OPK; ver instrucciones [aquí](/2020-07-02-rg350_primeros_pasos.html#dondecomo-instalo-el-fichero-opk-del-emulador-que-he-bajado) en caso de dudas), lo deberemos encontrar en nuestro lanzador en la sección de aplicaciones. Por ejemplo:

![GMenu2X](/images/posts/xmame_sm_bridge/gmenu2x.png)
![SimpleMenu](/images/posts/xmame_sm_bridge/simplemenu.png)
![PyMenu](/images/posts/xmame_sm_bridge/pymenu.png)

Una vez instalado lo abriremos y encontraremos un sencillo aviso para confirmar la instalación seleccionando el botón `<Yes>` y pulsando `Start`:

![Install](/images/posts/xmame_sm_bridge/install.png)

Con esto el pequeño interfaz de ajustes habrá quedado instalado.

## Utilización

A partir de entonces, al ejecutar una ROM con el sistema xMAME integrado en SimpleMenu, nos aparecerá un pequeño interfaz muy parecido al que muestra el interfaz propio de xMAME justo después de seleccionar la ROM.

<iframe width="640" height="480" src="https://www.youtube.com/embed/1OH2ENqr1tA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Se han replicado los controles de la pantalla de ajustes de xMAME que, al igual que en ella, se indican en la leyenda inferior. Básicamente son estos:

* **Arriba/Abajo**: Para seleccionar el ajuste que se quiere modificar.
* **Izquierda/Derecha**: Para cambiar el valor del ajuste seleccionado.
* **A**: Confirmar el arranque del juego.
* **B**: Cancelar el arranque del juego, es decir volver a SimpleMenu.

Los ajustes, una vez hechos, en el momento de arrancar el juego (no así si volvemos atrás con `B`), se guardan en el mismo fichero que utiliza xMAME. Por tanto los ajustes que hagamos persistirán entre distintas sesiones. Además serán compatibles con los ajustes que hayamos hecho en xMAME.

Como se ha mencionado, se muestran los mismos ajustes que en xMAME y el manejo de la pantalla es idéntico, pero hay dos excepciones:

* En el ajuste **Video Rotation** hay un valor posible adicional. En xMAME los valores posibles eran: `Auto`, `Landscape` y `Portrait`. En este nuevo interfaz el valor `Portrait` se ha desdoblado en dos: `Portrait (L)` y `Portrait (R)`. Esto es así porque internamente xMAME soporta dos opciones de pantalla horizontal (girada hacia la izquierda y hacia la derecha). Por algún motivo en el interfaz original de xMAME sólo se ofrece uno de los dos. Aquí pues se muestran los dos. Hay un problema sin embargo y es que el fichero de configuración donde se almacenan los ajustes para cada juego no soporta este modo adicional `Portrait (R)`, por lo que si se utiliza, al volver a intentar lanzar el juego nos encontraremos el valor más cercano al seleccionado `Portrait (L)`.
* El ajuste **Save state** no funciona ni siquiera en xMAME (se cierra el emulador al cambiar el valor predeterminado `None`), por lo que en esta reimplementación de la pantalla de ajustes se ha optado por desactivarlo. Por ese motivo aparece en gris.

## Aspectos técnicos

Se mencionan aquí los detalles de funcionamiento interno del interfaz de ajustes para quien tenga interés. Si sólo te interesa instalarlo y utilizarlo, puedes dejar de leer aquí.

### Análisis previo

Este interfaz de ajustes para xMAME ha sido posible por la peculiar arquitectura que tiene este emulador. No es como los emuladores habituales en que todo está implementado en un único binario o ejecutable (normalmente empaquetado en un OPK, aunque esa no es la clave de la diferencia). xMAME, haciendo honor a su nombre, sigue un poco más la filosofía UNIX en la que las distintas partes del sistema se encuentran en distintos binarios que se invocan unos a otros lanzando procesos con los parámetros necesarios. En concreto, xMAME tiene los siguientes binarios principales:

* `/media/data/local/share/xmame/xmame.dge`
* `/media/data/local/share/xmame/xmame52/xmame.SDL.52`
* `/media/data/local/share/xmame/xmame69/xmame.SDL.69`
* `/media/data/local/share/xmame/xmame84/xmame.SDL.84`

El primero es el interfaz normal (el de la pantalla de fondo verde) que es el que muestra la lista de ROMs de los distintos romsets y la pantalla de ajustes una vez que seleccionamos una ROM:

![xMAME 1](/images/posts/xmame_sm_bridge/xmame_1.png)
![xMAME 2](/images/posts/xmame_sm_bridge/xmame_rom_settings.png)

Tras la segunda pantalla se ejecuta el proceso correspondiente al romset elegido al principio, que se corresponde con uno de los tres procesos restantes de la lista anterior. Por ejemplo, tal y como se ha ajustado el juego que se selecciona en los dos pantallazos anteriores, el proceso que se ejecuta finalmente es:

```
xmame.SDL.84 bombjack -ipu_scaler 2 -nodirty -triplebuf -rol
```

Así pues tenemos todo el poder en nuestras manos para ejecutar una ROM con los ajustes que deseemos siempre que se conozca la correspondencia entre los distintos ajustes con los argumentos a pasar al proceso a la hora de ejecutarlo. Esto fue lo primero que fue necesario hacer. El resultado está codificado en la estructura de datos que se ve a partir de la linea 36 de este fichero fuente: [https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/settings.py](https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/settings.py)

Como ejemplo vamos a ver cómo se interpreta la parte correspondiente al ajuste `Video Rotation`:

```json
{
    "file_pos": 0,
    "desc": "Video Rotation",
    "enabled": True,
    "values": [0, 1, 2, 3],
    "descs": ["Auto", "Landscape", "Portrait (L)", "Portrait (R)"],
    "args": ["-autoror", "", "-rol", "-ror"],
    "value": 0
},
```

Los valores de las claves `values`, `descs` y `args` se corresponden entre sí según el orden en que aparecen. Es decir:

|Descripción|Auto|Landscape|Portrait (L)|Portrait (R)|
|:----------|:---|:--------|:-----------|:-----------|
|Valor|0|1|2|3|
|Argumento|-autoror| |-rol|-ror|

Valor (o `values` en la codificación JSON) es el dato que luego se almacena en el pequeño fichero de configuración que deja xMAME en los siguientes directorios en función del romset:

* `/media/data/local/share/xmame/xmame52/frontend`
* `/media/data/local/share/xmame/xmame69/frontend`
* `/media/data/local/share/xmame/xmame84/frontend`

Por ejemplo el fichero que aparece cuando configuramos el juego del ejemplo del romset 84 como se veía en los pantallazos anteriores es `/media/data/local/share/xmame/xmame84/frontend/bombjack.cfg` y tiene el siguiente contenido:

```
2,0,0,0,0,0,0,0,0,0,0,0,0,1,0
```

El parámetro `file_pos` del JSON nos indica en qué posición se almacena el ajuste. Por ejemplo el ajuste `Video Rotation` que estamos utilizando de ejemplo está en la posición `0` (el primero). Como vemos en el fichero tiene el valor `2` que según la tabla anterior corresponde a `Portrait (L)`.

Finalmente el argumento será el que se añada a la hora de ejecutar el emulador con la ROM. En el caso del ejemplo será el argumento `-rol` que veíamos en el proceso que se ejecuta al final y que repetimos de nuevo:

```
xmame.SDL.84 bombjack -ipu_scaler 2 -nodirty -triplebuf -rol
```

La forma de averiguar todos los valores posibles fue ajustándolos uno a uno cambiando uno cada vez y analizando el proceso ejecutado al final con el comando `ps` de Linux.

### Programación

Una vez reunida toda la información llegó el momento de programar. La idea era reproducir de la forma más fiel posible el interfaz de ajustes de la ROM que tiene xMAME. Para la programación se ha elegido el entorno Python más la librería [`pygame`](https://www.pygame.org/wiki/about) que ofrece primitivas para dibujar en pantalla y controlar eventos (básicamente es una envoltura Python a la librería SDL). Ambos se encuentran preinstalados en OpenDingux.

El código puede encontrarse en este repositorio: [https://github.com/eduardofilo/RG350_xmame_sm_bridge](https://github.com/eduardofilo/RG350_xmame_sm_bridge)

El programa realizado en Python/pygame tan solo muestra las opciones y permite cambiarlas. Al seleccionar la ROM en SimpleMenu (que le llega como argumento) hace dos cosas:

1. Persiste los ajustes en el fichero de configuración de xMAME correspondiente (subdirectorio `frontend` del directorio de cada romset).
2. Genera un fichero `/tmp/run` que contiene el proceso a ejecutar, es decir el binario del emulador del romset elegido junto a los argumentos correspondientes a los ajustes hechos.

Todo esto está envuelto con tres pequeños shell scripts, uno por cada romset, que son los que se configuran en SimpleMenu en el fichero donde tengamos definido el sistema xMAME. Los tres scripts son los siguientes:

* [https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.52](https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.52)
* [https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.69](https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.69)
* [https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.84](https://github.com/eduardofilo/RG350_xmame_sm_bridge/blob/master/romset.84)

Todos los ficheros necesarios deben instalarse en la ruta siguiente en el sistema de la consola:

```
/media/data/local/share/xmame/sm_bridge
```

Así pues la configuración de SimpleMenu para integrar este sistema debería invocar los scripts anteriores instalados en esta ruta, por ejemplo:

```ini
[MAME]
execs = /media/data/local/share/xmame/sm_bridge/romset.84,/media/data/local/share/xmame/sm_bridge/romset.69,/media/data/local/share/xmame/sm_bridge/romset.52
romDirs = /media/data/roms/ARCADE/
romExts = .zip,.ZIP
aliasFile = /media/home/.simplemenu/alias.txt
```

El instalador comentado al principio de este artículo se encarga tanto de copiar los ficheros necesarios a la ruta indicada antes, como de ajustar los ficheros de definición de sistemas de SimpleMenu para que se llame a los scripts que lanzan el interfaz de ajustes.
