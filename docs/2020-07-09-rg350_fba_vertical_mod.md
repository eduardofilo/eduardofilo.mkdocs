title: 2020-07-09 RG350 FBA mod
summary: Integración en frontends y mejora en la gestión del modo vertical en FBA.
date: 2020-07-09 17:00:00

![FBA Logo](/images/posts/fba_logo.png)

## Descripción del problema

FBA permite rotar la pantalla para poder jugar más cómodamente los juegos verticales (modo TATE). De hecho detecta automáticamente este tipo de juegos y los muestra rotados por defecto. El problema es que lo hace hacia la parte izquierda de la consola y al menos en la RG350/M resultaría más cómodo que lo hiciera hacia la derecha donde están los botones en lugar de la cruceta.

Por ejemplo al arrancar 1941 aparece así:

![1941 Left](/images/posts/fba_mod/1941_left.png)

En la versión [r19](https://github.com/nobk/fba-sdl/releases/tag/r19) de FBA están duplicados todos los settings para poder ajustar los juegos verticales de forma independiente:

![FBA Settings](/images/posts/fba_mod/fba_settings.png)

En concreto en `Default Vertical Run Game settings` podemos encontrar el parámetro para rotar la pantalla. Allí nos interesa poner el valor `-180` en el parámetro `Rotate vertical game`:

![FBA Vertical Settings](/images/posts/fba_mod/fba_vertical_settings.png)

Tras hacerlo, si lanzamos el juego desde el interfaz propio de FBA conseguimos la orientación deseada:

![1941 Right](/images/posts/fba_mod/1941_right.png)

Hasta aquí bien. El problema viene cuando integramos FBA en frontends como SimpleMenu o PyMenu. En esos casos el emulador se lanzará por linea de comando pasando como argumento la ruta de la ROM. Cuando se lanzan así los juegos, FBA no aplica los ajustes que hemos podido hacer en su interfaz propio. Así siempre se van a ver girados hacia la izquierda.

Como en otros artículos, a partir de aquí voy a mostrar detalles técnicos del problema que hay debajo de lo anterior y cómo se ha hecho la modificación del emulador. Si no te interesan y sólo quieres aprovechar la modificación del emulador puedes saltar hasta el apartado [Utilización del mod de FBA](#utilizacion-del-mod-de-fba).

## Descripción técnica del problema

En el Readme que hay dentro del OPK puede leerse lo siguiente:

```
FBA SDL could be used as a standalone application when invoked with
rom zip with full path as a parameter:

./fbasdl.dge ./roms/dino.zip

Full path and extension are obligatory.


Commandline interface
---------------------

FBA SDL can also be invoked with command line options.
The options are as follows;

./fbasdl.dge <game> [<parameters>]

<game>                  - The game's romname with full path and extension.
--no-sound              - Just be silent
--sound-sdl             - Use SDL for sound (mutex syncro)
--sound-sdl-old         - Use SDL for sound
--sound-ao              - Use libao for sound
--samplerate=<Hz>       - Valid values are: 11025, 16000, 22050, 32000 and 44100
--sense=<value>         - Analog sensitivity: 0..100
--showfps               - Show frames per second while play
--vsync                 - Syncronize video refresh on 60Hz
--68kcore=<value>       - Choose Motorola 68000 emulation core.
                          0 - C68k, 1 - Musashi M68k, 2 - A68k

Example:

./fbasdl.dge ./roms/dino.zip --sound-sdl --samplerate=44100 --68kcore=0
```

Así pues como vemos, el ejecutable que hay dentro del OPK (`fbasdl.dge`) está preparado para aceptar parámetros. Aquí podemos detectar dos problemas:

1. El emulador sólo tiene un lanzador (fichero `.desktop` en el interior del OPK) que es el que sirve para abrir el interfaz propio de FBA. Necesitaríamos el típico lanzador que tienen la mayoría de los emuladores que muestra un explorador de ficheros para seleccionar la ROM que luego se pasa como argumento al ejecutable.
2. Entre las opciones que vemos en el Readme no parece estar contemplada la que sirve para rotar la pantalla.

Vamos a ocuparnos de estos problemas uno a uno.

## 1. Nuevo lanzador con explorer

Lo primero que hacemos es bajar el OPK. Vamos a partir de [éste](https://github.com/nobk/fba-sdl/releases/download/r19/fba-RG350-r19-8e351b8b.opk).

A continuación lo desenlatamos para ver su interior. En Windows creo que se puede utilizar WinRAR o 7Zip (no lo tengo claro). En Linux lo haremos por linea de comando:

```
$ unsquashfs fba-RG350-r19-8e351b8b.opk
Parallel unsquashfs: Using 4 processors
9 inodes (241 blocks) to write

[=====================================================================================================================================|] 241/241 100%

created 8 files
created 2 directories
created 0 symlinks
created 0 devices
created 0 fifos
```

Si miramos lo que hay en el interior del OPK vemos que efectivamente sólo contiene un lanzador:

```
$ ls -l
total 29972
-rw-rw-r-- 1 edumoreno edumoreno      193 ene  4  2020 default.gcw0.desktop
-rw-rw-r-- 2 edumoreno edumoreno      795 ene  4  2020 fba_icon.png
-rwxrwxr-x 1 edumoreno edumoreno 30666200 ene 22 03:50 fbasdl.dge
-rw-rw-r-- 1 edumoreno edumoreno     8819 ene 22 03:46 readme.txt
drwxrwxr-x 2 edumoreno edumoreno     4096 ene  4  2020 skin
```

Visualizando el fichero `default.gcw0.desktop` (es un fichero de texto) el lanzador lo único que hace es ejecutar FBA sin argumentos, es decir el binario `fbasdl.dge`:

```
[Desktop Entry]
Name=FBA-RG350
Comment=Arcade machine emulator
Exec=fbasdl.dge
Terminal=false
Type=Application
StartupNotify=true
Icon=fba_icon
Categories=emulators;
X-OD-NeedsDownscaling=true
```

Lo primero que haremos es renombrar el fichero para reservar el nombre `default.gcw0.desktop` para el lanzador que crearemos a continuación. También cambiaremos el parámetro `Name` por `FBA UX` para indicar que este lanzador es el que lanza el interfaz (UX = User eXperience) propio de FBA. Así pues terminaremos con un fichero de nombre `fba_ux.gcw0.desktop` y el siguiente contenido:

```
[Desktop Entry]
Name=FBA UX
Comment=Arcade machine emulator
Exec=fbasdl.dge
Terminal=false
Type=Application
StartupNotify=true
Icon=fba_icon
Categories=emulators;
X-OD-NeedsDownscaling=true
```

Ahora creamos un segundo `.desktop` para ejecutar FBA como un emulador más convencional con selección previa de ROM. Crearemos un fichero de nombre `default.gcw0.desktop` y el siguiente contenido:

```
[Desktop Entry]
Name=FBA Explorer
Comment=Arcade machine emulator
Exec=fbasdl.dge %f
Terminal=false
Type=Application
StartupNotify=true
Icon=fba_icon
Categories=emulators;
X-OD-NeedsDownscaling=true
```

En él vemos que el comando a ejecutar tiene previsto el argumento `%f` donde se insertará el fichero de la ROM seleccionada con el explorador de ficheros.

Una vez hechos estos cambios volvemos a enlatar el OPK. En Linux lo haremos con el siguiente comando:

```
$ mksquashfs squashfs-root/ fba-RG350-r19-mod.opk -all-root -noappend -no-exports -no-xattrs
```

Si sustituimos el OPK original instalado en la consola por el que acabamos de re-ensamblar con el comando anterior, veremos que ahora nos aparecen dos lanzadores en GMenu2X:

![FBA New launchers](/images/posts/fba_mod/fba_new_launchers.png)

El que tiene la etiqueta `FBA UX` se comportará como el original y el nuevo `FBA Explorer` mostrará un explorador de ficheros como la mayoría de los emuladores:

![FBA Explorer launcher](/images/posts/fba_mod/fba_explorer_launcher.png)

Con esto tendríamos resuelto el primer problema dado que ahora launchers como SimpleMenu, PyMenu o EmulationStation podrán integrar este OPK modificado de FBA para ejecutar los juegos.

## 2. Localizar opción para rotar pantalla

El segundo problema podía no haber tenido solución pero hubo suerte. Como veíamos, según el Readme no parecía haber un parámetro que permitiera controlar la rotación de la pantalla por linea de comando. A pesar de ello echando un vistazo al código fuente de FBA encontramos la siguiente estructura en el fichero [src/sdl-dingux/main.cpp](https://github.com/nobk/fba-sdl/blob/master/src/sdl-dingux/main.cpp):

```c
	static struct option long_opts[] = {
		{"sound-sdl-old", 0, &options.sound, 3},
		{"sound-sdl", 0, &options.sound, 2},
		{"sound-ao", 0, &options.sound, 1},
		{"no-sound", 0, &options.sound, 0},
		{"samplerate", required_argument, 0, 'r'},
		{"frameskip", required_argument, 0, 'c'},
		{"vsync", 0, &options.vsync, 1},
		{"scaling", required_argument, 0, 'a'},
		{"rotate", required_argument, 0, 'o'},
		{"hwscaling", required_argument, 0, 'h'},
		{"sense", required_argument, 0, 'd'},
		{"showfps", 0, &options.showfps, 1},
		{"no-showfps", 0, &options.showfps, 0},
		{"create-lists", 0, &options.create_lists, 1},
		{"68kcore", required_argument, 0, 's'},
		{"z80core", required_argument, 0, 'z'},
	};
```

Esto parece indicar que hay más opciones sin documentar en el Readme. Así pues sin revisar más a fondo el código, haciendo una prueba incorporando la opción `rotate` al `.desktop` de tipo Explorer se comprueba que es efectiva. Concretamente lo que hay que añadir al comando de ejecución es:

```
Exec=fbasdl.dge %f --rotate=2
```

El valor 2 se obtiene de observar el valor que toma el parámetro `FBA_ROTATE` en los ficheros que aparecen en `/media/data/local/home/.fba/configs` y que son los que aplican cuando ejecutamos los juegos desde el interfaz propio de FBA (`FBA UX`).

Ya sabemos cómo podemos indicar por linea de comando cómo rotar la pantalla. Ahora tenemos un último problema y es que este parámetro sólo nos interesa para los juegos en vertical. Si ponemos este argumento en los juegos horizontales, veremos la pantalla de esta forma:

![Metal Slug](/images/posts/fba_mod/metal_slug.png)

Una opción sería crear un tercer `.desktop` con la opción (dejando el que hemos creado antes sin la opción) y utilizar ese lanzador para los juegos verticales pero esto nos obligaría a separar en secciones distintas los juegos verticales de los horizontales en los frontends como SimpleMenu. La solución por la que se ha optado aquí es intercalar un pequeño script que analice si el juego es vertical o no y en función de eso aplique la opción `--rotate=2` o no. La forma de averiguar si el juego es vertical será declarándolo en un pequeño fichero de texto en el directorio de las ROMs.

Lo primero que haremos será modificar el `default.gcw0.desktop` para que en lugar de ejecutar el binario del emulador directamente se ejecute un pequeño script:

```
[Desktop Entry]
Name=FBA Explorer
Comment=Arcade machine emulator
Exec=v_detector.sh %f
Terminal=false
Type=Application
StartupNotify=true
Icon=fba_icon
Categories=emulators;
X-OD-NeedsDownscaling=true
```

Finalmente incorporaremos dentro del OPK el script que discrimina los juegos verticales como hemos comentado. Su nombre será `v_detector.sh` y su contenido el siguiente:

```
#!/bin/sh

V_GAMES_FILE=$(dirname "$1")/vertical_games.txt
if [ -f "$V_GAMES_FILE" ]
then
    V_GAME_NAME=$(basename "$1")
    if grep -q $V_GAME_NAME $V_GAMES_FILE
    then
        ./fbasdl.dge $1 --rotate=2
    else
        ./fbasdl.dge $1
    fi
else
    ./fbasdl.dge $1
fi
```

No hay que olvidarse de dar permiso de ejecución (`+x`) al script anterior.

```
$ chmod +x v_detector.sh
```

Con todos estos cambios, volvemos a empaquetar el OPK como hemos visto antes:

```
$ mksquashfs squashfs-root/ fba-RG350-r19-mod.opk -all-root -noappend -no-exports -no-xattrs
```

Lo instalamos en la consola y a partir de ahora sólo tendremos que incluir el nombre del fichero de la ROM (extensión `.zip` incluida) en un fichero de nombre `vertical_games.txt` en el mismo directorio donde se encuentren las ROMs. Por ejemplo algunos de los juegos candidatos a encontrarse en este listado son:

```
1941.zip
19xx.zip
dimahoo.zip
mercs.zip
varth.zip
```

## Utilización del mod de FBA

Vamos a dar instrucciones para utilizar el emulador FBA modificado a lo largo de este artículo.

Una versión empaquetada con todas las modificaciones ya hechas puede descargarse de [aquí](/files/posts/fba_mod/fba-RG350-r19-mod.opk).

Una vez instalado en la consola, veremos que ahora aparecen dos lanzadores (al menos en GMenu2X):

![FBA New launchers](/images/posts/fba_mod/fba_new_launchers.png)

El lanzador `FBA UX` se comporta como el habitual, es decir muestra el interfaz propio de FBA donde podemos hacer el ajuste de la rotación de la pantalla (y muchos otros) antes de lanzar los juegos. El nuevo `FBA Explorer` será el que nos permitirá seleccionar la ROM por medio del explorador de archivos de GMenu2X, de la misma forma que hacen la mayoría de los emuladores:

![FBA Explorer launcher](/images/posts/fba_mod/fba_explorer_launcher.png)

Si queremos que el juego rote la pantalla -180º para que se puedan utilizar los controles de la parte derecha de la pantalla, sólo tendremos que crear un fichero de texto de nombre `vertical_games.txt` en el mismo directorio donde se encuentren las ROMs, e incorporar a él los nombres de las ROMs que queramos girar, uno por línea y con la extensión `.zip` incluida. Por ejemplo:

<iframe width="640" height="480" src="https://www.youtube.com/embed/7KNSdOCnF1w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Si todo va bien, al ejecutar uno de estos juegos desde `FBA Explorer` o desde SimpleMenu veremos lo siguiente y podremos utilizar los controles de la parte derecha de la consola:

<iframe width="823" height="480" src="https://www.youtube.com/embed/rZrfgNhhPYU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
