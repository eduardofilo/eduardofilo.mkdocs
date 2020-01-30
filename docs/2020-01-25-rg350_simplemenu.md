title: 2020-01-25 RG350 SimpleMenu
summary: Instalación y configuración de SimpleMenu en RG350.
date: 2020-01-25 17:25:00

!!! Info "Actualización 2020-01-30"
    Se modifica el artículo para que las instrucciones correspondan a la nueva versión 3.1.

![SimpleMenu](/images/posts/simplemenu.png)

Se ilustra a continuación el proceso de instalación y configuración del launcher SimpleMenu para RG350. Advertir que este launcher está todavía en un proceso inicial de desarrollo y exige una configuración muy manual y tediosa.

## Instalación

1. Bajar el fichero siguiente de la lista de assets de la release:
	* [SimpleMenu.3.1.-.RG350.-.2020.28.01.zip](https://github.com/fgl82/simplemenu/releases/download/3.1/SimpleMenu.3.1.-.RG350.-.2020.28.01.zip)
2. Copiarlo a la raíz de la microSD externa y descomprimirlo de forma que su contenido quede en un directorio de nombre `SimpleMenu`. Si hacemos esto desde la propia consola por SSH tener en cuenta que el comando `unzip` extrae el contenido del ZIP al mismo nivel donde se encuentra éste. Por tanto, crear antes el directorio `SimpleMenu`, mover dentro el ZIP y descomprimirlo allí.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del directorio donde hemos descomprimido se encuentra en `/media/sdcard/SimpleMenu`:

	![SimpleMenu 1](/images/posts/simplemenu_screenshot001.png)

4. Copiar el directorio `SimpleMenu` a la ruta `/media/data` que pertenece a la microSD interna:

	![SimpleMenu 2](/images/posts/simplemenu_screenshot002.png)

5. Entre las versiones de la rama 3.x los ficheros de configuración son compatibles. Si teníamos instalada una versión anterior a la 3.0 habrá que borrar el directorio `/usr/local/home/.simplemenu` ya que el formato de los ajustes que aquí se almacenan cambió completamente en esa versión.

6. Hacer ejecutables algunos de los ficheros instalados. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar los siguientes comandos desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/SimpleMenu/simplemenu
	# chmod +x /media/data/SimpleMenu/scripts/reset_fb
	# chmod +x /media/data/SimpleMenu/invoker.dge
	```

## Arranque

Tenemos dos opciones para utilizar este lanzador, convertirlo en el lanzador predeterminado o abrirlo desde Gmenu2x. Vamos a ver cómo configurar las dos situaciones:

#### Como lanzador predeterminado

1. Bajar el fichero siguiente de la lista de assets de la release:
	* [frontend_start](https://github.com/fgl82/simplemenu/releases/download/3.1/frontend_start)
2. Copiarlo a la raíz de la microSD externa.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del fichero se encuentra en `/media/sdcard/frontend_start`.
4. Copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![SimpleMenu 3](/images/posts/simplemenu_screenshot003.png)

5. Hacer ejecutable el fichero instalado. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar el siguiente comando desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	```

#### Desde Gmenu2x

1. Acudir a la sección `Applications` de Gmenu2x.
2. Pulsar `Select` y seleccionar `Add link in applications`:

	![SimpleMenu 6](/images/posts/simplemenu_screenshot006.png)

3. En el explorador de ficheros seleccionar la ruta `/media/data/SimpleMenu/simplemenu`:

	![SimpleMenu 7](/images/posts/simplemenu_screenshot007.png)

A partir de entonces debería aparecer `simplemenu` como una nueva aplicación que podremos lanzar manualmente:

![SimpleMenu 8](/images/posts/simplemenu_screenshot008.png)

## Configuración

De serie SimpleMenu trae una configuración con varias secciones preconfiguradas, pero como simplemente apunta de forma estática a las rutas de los distintos emuladores y ROMs, es seguro que nos va a tocar ajustar esta configuración a lo que nosotros tengamos instalado en la consola.

El fichero clave es el que se encontrará en la ruta `/usr/local/home/.simplemenu/sections.cfg` una vez que hayamos ejecutado SimpleMenu al menos una vez. Lo mejor será transferirlo al ordenador de alguna manera (pasándolo a la tarjeta externa con DinguxCmdr si no se conoce otra forma más directa) y editarlo allí con un editor que soporte los retornos de carro y la codificación utilizada habitualmente en sistemas Linux (como [Notepad++](https://notepad-plus-plus.org/)).

En este fichero tenemos al principio la lista de secciones en la propiedad `consoleList` del apartado `[CONSOLES]`. En esta propiedad se van añadiendo las distintas secciones separadas por comas.

```
[CONSOLES]
consoleList = GAME BOY,GAME BOY COLOR,GAME BOY ADVANCE,NES,SNES,GAME GEAR,MASTER SYSTEM,SEGA GENESIS,PLAYSTATION,PC ENGINE,NEO GEO POCKET,NEO GEO POCKET COLOR,NEO-GEO,ARCADE,FINAL BURN ALPHA,WONDERSWAN,GAMES,APPS
```

Luego por cada sección tenemos un bloque como el siguiente (lo que se ve ya está ajustado a mi instalación del emulador y ROMs de Game Boy):

```
[GAME BOY]
execDirs = /media/sdcard/apps/
execs = gambatte-opendingux-r572u3-20191201-204032(GB).opk
romDirs = /media/sdcard/roms/GBGBC/GB/
romExts = .gb
headerBackGround = 8E8A99
headerFont = 29278C
bodyBackground = E2D7D2  
bodyFont = 000000
selectedItemBackground = AC396B
selectedItemFont = FFFFFF
logo = ./resources/gb/logo.png
aliasFile =
category = all
onlyFileNamesNoPathOrExtension = no
```

De los anteriores parámetros, los que tenemos que modificar fundamentalmente son:

* `execDirs`: Directorio donde se encuentra el OPK del emulador.
* `execs`: OPK del emulador.
* `romDirs`: Directorio donde se encuentran las ROMs de este sistema.
* `romExts`: Extensiones de los ficheros que se incluirán en el listado de ROMs.

El resultado en SimpleMenu será éste:

![SimpleMenu 4](/images/posts/simplemenu_screenshot004.png)

En caso de que necesitemos volver a Gmenu2x, podremos encontrarlo en la sección APPS:

![SimpleMenu 5](/images/posts/simplemenu_screenshot005.png)

Como punto de partida dejo aquí mi fichero de configuración que contiene la mayoría de los emuladores y la [estructura de directorios para las ROMs](/retro-emulacion/rg-350.html#las-roms-y-su-organizacion) que se utilizan habitualmente.

* [sections.cfg](/files/posts/sections.cfg)

!!! warning "Aviso"
    Si queremos modificar el fichero `sections.cfg`, SimpleMenu no puede encontrarse en ejecución. No sirve lanzar Gmenu2x porque SimpleMenu seguirá vivo como proceso padre de éste. Habrá que o bien reiniciar la consola si tenemos configurado el [arranque manual](#desde-gmenu2x) o bien deshacer temporalmente el [arranque automático](#como-lanzador-predeterminado). Si matamos el proceso con `kill` por SSH la consola se apagará.

## Previews

SimpleMenu soporta previsualización de las ROMs. Para que aparezcan hay que hacer dos cosas.

Primero colocar las imágenes con el mismo nombre que las ROMs pero con extensión `.png` en un directorio al mismo nivel que las ROMs de nombre `media`. Por ejemplo la previsualización de la ROM `/media/sdcard/roms/GB/DKLAND.gb` iría en `/media/sdcard/roms/GB/media/DKLAND.png`.

Lo segundo que hay que hacer es activar la visualización de las miniaturas. Para ello hay que pulsar la tecla `Y`. Volviéndola a pulsar volvemos al menú normal.

Desafortunadamente el directorio necesario para las previsualizaciones no es el mismo que necesita Gmenu2x (`.previews`). Si alguien tiene el entorno para compilarlo, el sitio donde está definido el directorio es la linea 130 del fichero [simplemenu/src/logic/screen.c](https://github.com/fgl82/simplemenu/blob/UNIVERSAL/simplemenu/src/logic/screen.c). De momento he optado por duplicar el directorio. En mi caso lo hice con la siguiente sesión de terminal por SSH:

```
RG350:/media/sdcard/roms # find . -name .previews
./FBA/.previews
./GBA/.previews
./PCE/.previews
./GGSMS/SMS/.previews
./GGSMS/GG/.previews
./FC/.previews
./WSC/.previews
./CPC/.previews
./SFC/.previews
./PS/.previews
./GBGBC/GBC/.previews
./GBGBC/GB/.previews
./MD/.previews
./NGP/.previews
./ZX/.previews
RG350:/media/sdcard/roms # cp -r ./FBA/.previews ./FBA/media
RG350:/media/sdcard/roms # cp -r ./GBA/.previews ./GBA/media
RG350:/media/sdcard/roms # cp -r ./PCE/.previews ./PCE/media
RG350:/media/sdcard/roms # cp -r ./GGSMS/SMS/.previews ./GGSMS/SMS/media
RG350:/media/sdcard/roms # cp -r ./GGSMS/GG/.previews ./GGSMS/GG/media
RG350:/media/sdcard/roms # cp -r ./FC/.previews ./FC/media
RG350:/media/sdcard/roms # cp -r ./WSC/.previews ./WSC/media
RG350:/media/sdcard/roms # cp -r ./CPC/.previews ./CPC/media
RG350:/media/sdcard/roms # cp -r ./SFC/.previews ./SFC/media
RG350:/media/sdcard/roms # cp -r ./PS/.previews ./PS/media
RG350:/media/sdcard/roms # cp -r ./GBGBC/GBC/.previews ./GBGBC/GBC/media
RG350:/media/sdcard/roms # cp -r ./GBGBC/GB/.previews ./GBGBC/GB/media
RG350:/media/sdcard/roms # cp -r ./MD/.previews ./MD/media
RG350:/media/sdcard/roms # cp -r ./NGP/.previews ./NGP/media
RG350:/media/sdcard/roms # cp -r ./ZX/.previews ./ZX/media
```

El resultado:

<iframe width="853" height="480" src="https://www.youtube.com/embed/5bD8v_8Q0CE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Controles

La página de documentación de controles es [ésta](https://github.com/fgl82/simplemenu/wiki/Controls), pero resulta un poco confusa porque mezcla varias máquinas, por lo que se listan a continuación de forma explícita los controles para RG350:

|Shortcut|Función|
|:-------|:------|
|`R1` / `L1`|Cambia de sección desde la lista de ROMs. Cuando estamos en modo preview se muestra el logotipo de los sistemas|
|`Arriba` / `Abajo`|Selecciona la ROM anterior/siguiente|
|`Izquierda` / `Derercha`|Avanza 10 ROMs anteriores/siguientes|
|`B+Izquierda` / `B+Derecha`|Cambia de sección mostrando el logotipo de los sistemas|
|`B+Arriba` / `B+Abajo`|Pasa a la letra anterior/siguiente|
|`Y`|Alterna entre modo menú y modo preview|
|`A`|Lanza la ROM seleccionada|
|`B+Select`|Lanza una ROM aleatoria|
|`B`|Fuera de la sección Favoritos añade una ROM a la misma; Dentro de la sección Favoritos borra la ROM de la misma|
|`L2`|Muestra la sección de Favoritos|
|`Select+Start`|Apaga la consola|
