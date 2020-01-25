title: 2020-01-25 RG350 SimpleMenu
summary: Instalación y configuración de SimpleMenu en RG350.
date: 2020-01-25 17:25:00

![SimpleMenu](/images/posts/simplemenu.png)

Se ilustra a continuación el proceso de instalación y configuración del launcher SimpleMenu para RG350. Advertir que este launcher está todavía en un proceso inicial de desarrollo y exige una configuración muy manual y tediosa.

## Instalación

1. Bajar los dos ficheros siguientes de la lista de assets de la release:
	* [SimpleMenu.3.0.-.RG-350.-.2019-01-16.zip](https://github.com/fgl82/simplemenu/releases/download/3.0/SimpleMenu.3.0.-.RG-350.-.2019-01-16.zip)
	* [frontend_start](https://github.com/fgl82/simplemenu/releases/download/3.0/frontend_start)
2. Copiar los dos ficheros bajados a la raíz de la microSD externa descomprimiendo el primero de forma que su contenido quede en un directorio de nombre `SimpleMenu`.
3. Una vez montada en la RG350, la ruta del directorio donde hemos descomprimido se encuentra en `/media/sdcard/SimpleMenu`. Debe quedar como se ve en el pantallazo:

	![copia SimpleMenu 1](/images/posts/simplemenu_screenshot001.png)

4. Copiar el directorio `SimpleMenu` a la ruta `/media/data` que pertenece a la microSD interna:

	![copia SimpleMenu 2](/images/posts/simplemenu_screenshot002.png)

5. Copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![copia SimpleMenu 3](/images/posts/simplemenu_screenshot003.png)

6. Si existía de una instalación anterior borrar el directorio `/usr/local/home/.simplemenu` ya que parece que el formato de los ajustes que aquí se almacenan ha cambiado respecto de las versiones anteriores.

7. Hacer ejecutables algunos de los ficheros instalados. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar los siguientes comandos desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	# chmod +x /media/data/SimpleMenu/simplemenu
	# chmod +x /media/data/SimpleMenu/scripts/reset_fb
	# chmod +x /media/data/SimpleMenu/invoker.dge
	```

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

El resultado en SimpleMenu será éste:

![copia SimpleMenu 4](/images/posts/simplemenu_screenshot004.png)

En caso de que necesitemos Gmenu2x para lanzar o configurar algo, podremos encontrarlo en la sección APPS:

![copia SimpleMenu 5](/images/posts/simplemenu_screenshot005.png)

## Controles

A continuación se muestran algunos de los controles interesantes de este lanzador:

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
|`X`|Añade un juego a favoritos|
|`Select+Start`|Apaga la consola|
