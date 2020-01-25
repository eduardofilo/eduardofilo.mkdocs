title: 2020-01-25 RG350 SimpleMenu
summary: Instalación y configuración de SimpleMenu en RG350.
date: 2020-01-25 17:25:00

![SimpleMenu](/images/posts/simplemenu.png)

Se ilustra a continuación el proceso de instalación y configuración del launcher SimpleMenu para RG350. Advertir que este launcher está todavía en un proceso inicial de desarrollo y exige una configuración muy manual y tediosa.

## Instalación

1. Bajar el fichero siguiente de la lista de assets de la release:
	* [SimpleMenu.3.0.-.RG-350.-.2019-01-16.zip](https://github.com/fgl82/simplemenu/releases/download/3.0/SimpleMenu.3.0.-.RG-350.-.2019-01-16.zip)
2. Copiarlo a la raíz de la microSD externa y descomprimirlo de forma que su contenido quede en un directorio de nombre `SimpleMenu`.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del directorio donde hemos descomprimido se encuentra en `/media/sdcard/SimpleMenu`:

	![SimpleMenu 1](/images/posts/simplemenu_screenshot001.png)

4. Copiar el directorio `SimpleMenu` a la ruta `/media/data` que pertenece a la microSD interna:

	![SimpleMenu 2](/images/posts/simplemenu_screenshot002.png)

5. Si existía de una instalación anterior, borrar el directorio `/usr/local/home/.simplemenu` ya que parece que el formato de los ajustes que aquí se almacenan ha cambiado respecto de las versiones anteriores.

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
	* [frontend_start](https://github.com/fgl82/simplemenu/releases/download/3.0/frontend_start)
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

El fichero clave es el que se encontrará en la ruta `/usr/local/home/.simplemenu/sections.cfg` una vez que hayamos ejecutado SimpleMenu al menos una vez (reiniciando después de haber hecho la [Instalación](#instalacion) por ejemplo). Lo mejor será transferirlo al ordenador de alguna manera (pasándolo a la tarjeta externa con DinguxCmdr si no se conoce otra forma más directa) y editarlo allí con un editor que soporte los retornos de carro y la codificación utilizada habitualmente en sistemas Linux (como [Notepad++](https://notepad-plus-plus.org/)).

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

En caso de que necesitemos Gmenu2x para lanzar o configurar algo, podremos encontrarlo en la sección APPS:

![SimpleMenu 5](/images/posts/simplemenu_screenshot005.png)

## Controles

La página de documentación de controles es [ésta](https://github.com/fgl82/simplemenu/wiki/Controls), pero resulta un poco confusa, por lo que se listan a continuación:

|Shortcut|Función|
|:-------|:------|
|`R1` / `L1`|Cambia de sección desde la lista de ROMs|
|`Arriba` / `Abajo`|Selecciona la ROM anterior/siguiente|
|`Izquierda` / `Derercha`|Avanza 10 ROMs anteriores/siguientes|
|`B+Izquierda` / `B+Derercha`|Cambia de sección|
|`B+Arriba` / `B+Abajo`|Pasa a la letra anterior/siguiente|
|`Y`|Alterna entre modo menú y modo preview (desconozco dónde se buscan las previews)|
|`A`|Lanza la ROM seleccionada|
|`B+Select`|Lanza una ROM aleatoria|
|`B`|Fuera de la sección Favoritos añade una ROM a la misma; Dentro de la sección Favoritos borra la ROM de la misma|
|`L2`|Muestra la sección de Favoritos|
|`Select+Start`|Apaga la consola|
