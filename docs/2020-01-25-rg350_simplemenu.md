title: 2020-01-25 RG350 SimpleMenu
summary: Instalación y configuración de SimpleMenu en RG350.
date: 2020-01-25 17:25:00

!!! Info "Actualización 2020-02-22"
    Se modifica el artículo para que las instrucciones correspondan con la nueva [versión 3.3](https://github.com/fgl82/simplemenu/releases/tag/3.3).

![SimpleMenu](/images/posts/simplemenu.png)

Se ilustra a continuación el proceso de instalación y configuración del launcher [SimpleMenu](https://github.com/fgl82/simplemenu) para RG350. Advertir que este launcher está todavía en una fase inicial de desarrollo y exige una configuración muy manual y tediosa.

!!! warning "Aviso"
    SimpleMenu no arrancará hasta que hayamos realizado una [configuración](#configuracion) funcional, cosa que hay que hacer manualmente tocando los ficheros de configuración. No se trata por tanto de una aplicación que se pueda simplemente instalar para probar.

## Instalación

Desde la versión 3.2 su autor ofrece en los assets de la [release](https://github.com/fgl82/simplemenu/releases/tag/3.3) dos formas de instalación, una empaquetado como OPK y otra manual (con los binarios y recursos en forma de ficheros convencionales). Vamos a ver como utilizar ambas alternativas.

#### Por medio de OPK

La instalación consiste únicamente en copiar el OPK a una de las dos rutas que explora Gmenu2x para mostrar el lanzador, es decir:

* Tarjeta interna: `/media/data/apps`
* Tarjeta externa: `/media/sdcard/apps`

!!! warning "Aviso"
    El [OPK enlazado en los assets de la release](https://github.com/fgl82/simplemenu/releases/download/3.3/SimpleMenu-RG-350.opk), no funciona. Falta el permiso de ejecución en un par de los ficheros que contiene. Se ofrece aquí una copia de dicho OPK con los permisos corregidos. También contiene modificado el fichero de configuración predeterminado con la ruta de las previews para que se corresponda con la misma que utiliza Gmenu2x: [SimpleMenu-RG-350_fixed.opk]((/files/posts/SimpleMenu-RG-350_fixed.opk))

#### Instalación manual

1. Bajar el fichero siguiente de la lista de assets de la release:
	* [SimpleMenu.3.3.-.RG-350.-.2020.22.02](https://github.com/fgl82/simplemenu/releases/download/3.3/SimpleMenu.3.3.-.RG-350.-.2020.22.02.zip)
2. Copiarlo a la raíz de la microSD externa y descomprimirlo de forma que su contenido quede en un directorio de nombre `SimpleMenu`, es decir retirando de su nombre el sufijo `.3.3.-.RG-350.-.2020.22.02`. Si hacemos esto desde la propia consola por SSH tener en cuenta que el comando `unzip` extrae el contenido del ZIP al mismo nivel donde se encuentra éste. Por tanto, crear antes el directorio `SimpleMenu`, mover dentro el ZIP y descomprimirlo allí.
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
	* [frontend_start](https://github.com/fgl82/simplemenu/releases/download/3.3/frontend_start)
2. Copiarlo a la raíz de la microSD externa.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del fichero se encuentra en `/media/sdcard/frontend_start`.
4. Copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![SimpleMenu 3](/images/posts/simplemenu_screenshot003.png)

5. Hacer ejecutable el fichero instalado. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar el siguiente comando desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	```

#### Desde Gmenu2x

Si nos hemos decantado por la [instalación manual](#instalacion-manual) Gmenu2x no mostrará SimpleMenu entre los lanzadores. Tenemos que generar un lanzador manual como sigue:

1. Acudir a la sección `Applications` de Gmenu2x.
2. Pulsar `Select` y seleccionar `Add link in applications`:

	![SimpleMenu 6](/images/posts/simplemenu_screenshot006.png)

3. En el explorador de ficheros seleccionar la ruta `/media/data/SimpleMenu/simplemenu`:

	![SimpleMenu 7](/images/posts/simplemenu_screenshot007.png)

A partir de entonces debería aparecer `simplemenu` como una nueva aplicación que podremos lanzar manualmente:

![SimpleMenu 8](/images/posts/simplemenu_screenshot008.png)

## Configuración

De serie SimpleMenu trae una configuración con varias secciones preconfiguradas, pero como simplemente apunta de forma estática a las rutas de los distintos emuladores y ROMs, es seguro que nos va a tocar ajustar esta configuración a lo que nosotros tengamos instalado en la consola. De hecho hasta que no hagamos estos ajustes SimpleMenu no arrancará. Aún así interesa que lo ejecutemos al menos una vez para que se genere el directorio `.simplemenu` dentro del home de la consola para que tengamos la plantilla sobre la que empezar a modificar.

#### Sistemas

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

El formato del archivo es el que se utiliza habitualmente para los ficheros de configuración tipo [INI](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)).

De los anteriores parámetros, los que tenemos que modificar fundamentalmente son:

* `execDirs`: Directorio donde se encuentra el OPK del emulador.
* `execs`: OPK del emulador.
* `romDirs`: Directorio donde se encuentran las ROMs de este sistema.
* `romExts`: Extensiones de los ficheros que se incluirán en el listado de ROMs.

Una vez que devolvamos el fichero de configuración `sections.cfg` a su lugar en `/usr/local/home/.simplemenu`, el resultado en SimpleMenu será éste:

![SimpleMenu 4](/images/posts/simplemenu_screenshot004.png)

En caso de que necesitemos volver a Gmenu2x, podremos encontrarlo en la sección APPS:

![SimpleMenu 5](/images/posts/simplemenu_screenshot005.png)

Como punto de partida dejo aquí mi fichero de configuración que contiene la mayoría de los emuladores y la [estructura de directorios para las ROMs](/retro-emulacion/rg-350.html#las-roms-y-su-organizacion) que se utilizan habitualmente.

* [sections.cfg](/files/posts/sections.cfg)

#### Configuración general

Dentro de `/usr/local/home/.simplemenu` hay otro fichero que nos interesa modificar. Se trata del `config.cfg`. Su contenido es el siguiente por defecto:

```
#OC VALUES (IGNORED IN RG-350)
408
702
732
#TIMEOUT
30
#CPU FREQ WHEN SLEEPING (IGNORED IN RG-350)
200
#TIDY GAME NAMES
1
#START IN PICTURE MODE
0
#SHUTDOWN ENABLED
1
#MEDIA FOLDER
media
```

Como vemos el primer y tercer parámetro son ignorados en RG350 (en principio son para modificar las frecuencias del procesador). El resto de parámetros sí los podemos modificar. Su significado es el siguiente:

* `TIMEOUT`: Número de segundos a partir del cual salta el salvapantallas. Cuando éste entre la forma de salir es pulsar `Power`.
* `TIDY GAME NAMES`: Obsoleto desde la versión 3.2.
* `START IN PICTURE MODE`: Obsoleto desde la versión 3.2.
* `SHUTDOWN ENABLED`: Si tiene el valor `1` hace que al pulsar `Start+Select` la consola se apague. Si tiene el valor `0` simplemente se cierra SimpleMenu.
* `MEDIA FOLDER`: Directorio donde se buscan las previsualizaciones de las ROMs. Interesa cambiar este valor del `media` que viene por defecto a `.previews` para que sea compatible con la ruta utilizada por Gmenu2x.

!!! warning "Aviso"
    Si queremos modificar los ficheros de configuración, SimpleMenu no puede encontrarse en ejecución. No sirve lanzar Gmenu2x porque SimpleMenu seguirá vivo como proceso padre de éste. Habrá que o bien reiniciar la consola si tenemos configurado el [arranque manual](#desde-gmenu2x) o bien deshacer temporalmente el [arranque automático](#como-lanzador-predeterminado). Si matamos el proceso con `kill` por SSH la consola se apagará si el parámetro `SHUTDOWN ENABLED` vale `1`.

## Previews

SimpleMenu soporta previsualización de las ROMs. Para que aparezcan hay que hacer dos cosas:

1. Colocar las imágenes con el mismo nombre que las ROMs pero con extensión `.png` en un directorio al mismo nivel que las ROMs de nombre `media`. Por ejemplo la previsualización de la ROM `/media/sdcard/roms/GB/DKLAND.gb` iría en `/media/sdcard/roms/GB/media/DKLAND.png`.
2. Activar la visualización de las miniaturas. Para ello hay que pulsar la tecla `Y`. Volviéndola a pulsar volvemos al listado normal.

Como hemos comentado en el apartado de [Configuración general](#configuracion-general), podemos modificar el directorio que se utiliza de forma predeterminada (`media`) por el `.previews` que utiliza Gmenu2x para así hacerlos compatibles y no tener que duplicar las previsualizaciones.

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
