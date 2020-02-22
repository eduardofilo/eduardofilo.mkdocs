title: 2020-02-13 RG350 EmulationStation
summary: Instalación y configuración de EmulationStation en RG350.
date: 2020-02-13 00:00:00

![EmulationStation](/images/posts/emulationstation.png)

!!! Warning "Advertencia"
    Comentar antes de empezar, que EmulationStation es pesado de configurar y el resultado final con frecuencia resulta lento (sobre todo si se tiene un gran número de emuladores y ROMs en la consola). También es propenso a [errores extraños](https://www.reddit.com/r/RG350/comments/f12llb/emulationstation_crashes_with_some_roms_with/). Se encuentran problemas con ROMs concretas y sobre todo con los ficheros `gamelist.xml` que aparecen con el scraping por exigencias en el formato del mismo que no están claras. A menudo la única forma de solucionarlos es por ensayo/error introduciendo las ROMs o los `gamelist.xml` por lotes para aislar los problemas. Además en la [última versión de FBA](https://github.com/nobk/fba-sdl/releases/tag/r19) no es capaz de lanzar las ROMs de FBA directamente, aunque aquí el responsble es el propio FBA que [no permite lanzar la ejecución de una ROM por comando](https://boards.dingoonity.org/retro-game-350rg-350/fba-for-rg-350-by-nobk-with-new-features-since-jan-2-to-jan-11/msg193105/#msg193105).

En este artículo vamos a ver cómo instalar y configurar el frontend EmulationStation en la RG350.

## Instalación

Empezamos por la instalación. Desgraciadamente además de copiar un OPK como habitualmente, hay que mover unos cuantos ficheros a una ruta de la tarjeta interna. A continuación los detalles paso a paso (las operaciones de copiado de ficheros se muestran con `DinguxCmdr` por ser accesible para todo el mundo, pero naturalmente se pueden hacer por FTP o SCP):

1. Bajar [este fichero](https://github.com/ManuelSch81/RG350-EmulationStation_configured/archive/master.zip) y descomprimirlo. Dentro veremos un par de directorios y un README. Nos fijamos en el directorio `Internal SD Card` (el resto no los utilizaremos para nada).
2. Abrir el directorio `Internal SD Card` y renombrar el directorio `data` que allí veremos a `.emulationstation` (si lo hacemos en Linux, el directorio desaparecerá a no ser que tengamos activa la opción de mostrar archivos ocultos).
3. Abrir el directorio que acabamos de renombrar en el paso anterior. Dentro veremos dos directorios y algunos ficheros. Borrar el directorio `gamelists` (ya que contiene listados de ROMs que tenía el autor del repositorio en su consola, lo que hará más lenta la carga de EmulationStation).
4. Subir un par de niveles de directorios hasta volver a tener a la vista el directorio `Internal SD Card`.
5. Copiar este directorio a la tarjeta externa de la consola (montándola en el PC con un adaptador o lector de tarjetas o por FTP, SCP, ...).
6. Desmontar la SD del PC para devolverla a la ranura externa de la consola.
7. Abrir `DinguxCmdr`. Moverse por la estructura de ficheros hasta localizar a la izquierda la ruta `/media/sdcard/Internal SD Card` y a la derecha `/media/sdcard/apps`. La ruta de la derecha es donde vamos a instalar el OPK. En este caso hemos indicado la ruta donde están los OPKs en la tarjeta externa. Alternativamente se puede utilizar la ruta donde están los OPKs en la interna que es `/media/data/apps`, si se prefiere instalar en esta tarjeta:

    ![EmulationStation Instalación 1](/images/posts/emulationstation_install1.png)

8. Seleccionar el fichero `emulationstation.opk` en el panel izquierdo y pulsar `X`. En el menú que aparece seleccionar `Copy >` y confirmar con `A`:

    ![EmulationStation Instalación 2](/images/posts/emulationstation_install2.png)

9. Cambiar en el panel derecho la ruta a `/media/data/local/home`:

    ![EmulationStation Instalación 4](/images/posts/emulationstation_install4.png)

10. Seleccionar en el panel izquierdo el directorio `.emulationstation` y pulsar `X`. En el menú que aparece seleccionar `Copy >` y confirmar con `A`:

    ![EmulationStation Instalación 5](/images/posts/emulationstation_install5.png)

11. Finalmente salir de `DinguxCmdr` pulsando `Y` y seleccionando `Quit`:

    ![EmulationStation Instalación 6](/images/posts/emulationstation_install6.png)

Con esto finaliza la instalación de la aplicación.

## Configuración

Para que EmulationStation reconozca los distintos sistemas de emulación, deben estar correctamente registrados en uno de los ficheros de configuración que hemos copiado durante la instalación, concretamente el que queda en la ruta `/usr/local/home/.emulationstation/es_systems.cfg`. Desafortunadamente no hay ningún medio para hacer esta configuración automáticamente. Nos va a tocar hacerlo manualmente.

Estamos en una situación muy similar a la de [SimpleMenu](/2020-01-25-rg350_simplemenu.html). De hecho el apartado de [Configuración](/2020-01-25-rg350_simplemenu.html#configuracion) de ese artículo, conceptualmente nos sirve aquí. Sólo cambia el formato concreto de la configuración que necesita EmulationStation. Se recomienda por tanto hacer como en el caso de [SimpleMenu](/2020-01-25-rg350_simplemenu.html#configuracion), es decir, transferir el fichero de configuración `/usr/local/home/.emulationstation/es_systems.cfg` al ordenador para editarlo allí con un editor que soporte directamente el formato de texto de Linux. Por ejemplo [Notepad++](https://notepad-plus-plus.org/). En realidad podemos aprovechar la copia que todavía tendremos en la tarjeta externa que hay dentro de la carpeta `.emulationstation` que renombramos durante la instalación.

El fichero `es_systems.cfg`, aunque no lo indique la extensión, internamente tiene formato XML. Se trata por tanto de una serie de bloques anidados que comienzan y terminan con etiquetas encerradas entre los símbolos `<` y `>`. El bloque raíz se define con la etiqueta `<systemList>` y dentro de él hay un bloque `<system>` para cada emulador. Dentro de este bloque ya directamente se encuentran los distintos parámetros del emulador. Como vemos la filosofía es muy similar a la del fichero de configuración de SimpleMenu, sólo que en éste último el formato del archivo no era XML, sino el que se utiliza habitualmente para los ficheros de configuración tipo [INI](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)). De hecho si ya tenemos SimpleMenu instalado y configurado, podemos utilizar su fichero de configuración como plantilla para transplantar todos los parámetros (que son prácticamente los mismos) a `es_systems.cfg`.

Un bloque `<system>` de un sistema como Game Boy podría ser el siguiente:

```xml
<system>
    <name>gb</name>
	<fullname>Gameboy</fullname>
	<path>/media/sdcard/roms/Gameboy</path>
	<extension>.gb</extension>
	<command>opkrun "/media/sdcard/apps/gambatte.opk" %ROM%</command>
	<platform>gb</platform>
</system>
```

Es recomendable poner entre comillas la ruta del OPK para así no tener que *escapar* caracteres especiales como los espacios y los paréntesis.

Vamos a detallar el significado de cada parámetro (la documentación original puede encontrarse [aquí](https://emulationstation.org/gettingstarted.html#config)):

* `name`: Nombre corto del sistema. Usado en algunas estructuras de directorios y mensajes de error.
* `fullname`: Nombre descriptivo. Es el que aparece en el frontend. Esta etiqueta es opcional. Si no está se usará `name` en su lugar.
* `path`: Ruta de las ROMs.
* `extension`: Extensiones de las ROMs que se listarán dentro del sistema. Las distintas extensiones se separan por comas o espacios.
* `command`: Comando con el que se lanzará el emulador cuando seleccionemos una ROM. Lo normal será que contenga algunos parámetros que serán sustituidos, como por ejemplo `%ROM%` que se convertirá en la ruta de la ROM seleccionada.
* `platform`: Plataforma utilizada cuando se hace scraping. Esta etiqueta es opcional. La lista completa de los códigos de plataforma se encuentra en la [página de documentación de EmulationStation](https://emulationstation.org/gettingstarted.html#config). Se pueden poner varias plataformas separadas por comas, por ejemplo `genesis,megadrive`.

Una vez que devolvamos el fichero de configuración `es_systems.cfg` a su lugar en `/usr/local/home/.emulationstation`, el resultado al abrir EmulationStation será éste:

![EmulationStation Running 1](/images/posts/emulationstation_running1.png)
![EmulationStation Running 2](/images/posts/emulationstation_running2.png)

Como se ve en las fotos, al menos en mi sistema algunos de los textos se ven ligeramente distorsionados. Esto se puede solucionar o mejorar cambiando el tema. La instalación que hemos hecho lleva 4 temas preinstalados. Desafortunadamente, el que viene por defecto y que produce esos pequeños defectos gráficos es el que me parecería más recomendable si no fuera por este problema.

Como punto de partida dejo aquí mi fichero de configuración que contiene la mayoría de los emuladores y la [estructura de directorios para las ROMs](/retro-emulacion/rg-350.html#las-roms-y-su-organizacion) que se utilizan habitualmente.

* [es_systems.cfg](/files/posts/es_systems.cfg)

## Arranque

EmulationStation aparecerá como aplicación en la sección `Emulators` de GMenu2X (no como [SimpleMenu](/2020-01-25-rg350_simplemenu.html#desde-gmenu2x) cuyo lanzador tenemos que añadir a mano). Si queremos que EmulationStation se autoarranque en el inicio de la consola tenemos que proceder como sigue:

1. Bajar el fichero [frontend_start](https://raw.githubusercontent.com/ManuelSch81/RG350-EmulationStation_configured/master/frontend_start/frontend_start).
2. Copiarlo a la raíz de la microSD externa.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del fichero que acabamos de copiar, se encuentra en `/media/sdcard/frontend_start`.
4. Abrir `DinguxCmdr`y copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![Copiando frontend_start](/images/posts/simplemenu_screenshot003.png)

5. Hacer ejecutable el fichero instalado. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar el siguiente comando desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	```

Tal y como está diseñado el script de arranque que acabamos de copiar, si salimos de EmulationStation (tecla `Start` y luego eligiendo `Quit` y `Quit EmulationStation`), se abrirá GMenu2X.

Para el último paso merece la pena intentar conectar por SSH ya que las últimas versiones de Windows 10 ya incorporan el cliente de forma predeterminada. Para ello, estando la RG350 conectada por USB2 al ordenador, abrir una terminal o consola (buscando en el menú inicio o en Cortana `cmd`) y teclear lo siguiente:

```
ssh root@10.1.1.2
```

Si nos aparece lo siguiente es que hemos conseguido abrir una terminal dentro del sistema de la RG350. Desde allí podremos ejecutar directamente el comando del punto 5 de la lista anterior.

```
edumoreno@pceduardo:~$ ssh root@10.1.1.2
 _________________________
< Welcome to ROGUE resistance ! >
 -------------------------
           |\
        <=--===\>   -------
          ==0=[]=>>
        <=--===/>   -------
           |/

RG350:/media/data/local/home # chmod +x /media/data/local/sbin/frontend_start
```

## Boxart

Una de las funcionalidades más interesantes de EmulationStation es su capacidad para adornar la presentación del listado de ROMs con previsualizaciones de los juegos y con metainformación (fecha de publicación, compañía desarrolladora, número de jugadores, etc.). Esta funcionalidad se basa en un fichero de texto llamado `gamelist.xml` en formato XML (parecido al que hemos visto antes para la configuración de los sistemas). El fichero puede estar en varios sitios, pero la ubicación más conveniente es el propio directorio de las ROMs. Deberá haber un fichero `gamelist.xml` por sistema, es decir por directorio de ROMs.

Como siempre que hablamos de este tema, interesa utilizar una herramienta que automatice el proceso, ya que normalmente tendremos muchas ROMs por cada sistema y aparte de largo y tedioso, escribir manualmente ficheros XML supone casi con toda seguridad introducir errores en su estructura. Así pues será conveniente utilizar un Scraper como los siguientes:

* [Steven Selph's Scraper](https://github.com/sselph/scraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#steven-selphs-scraper)
* [Lars Muldjord's Skyscraper](https://github.com/muldjord/skyscraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#lars-muldjords-skyscraper)
* [Skraper](http://skraper.net/)
* [Universal XML Scraper](https://github.com/Universal-Rom-Tools/Universal-XML-Scraper)

Vamos a detallar el uso de los dos últimos para generar los ficheros `gamelist.xml` y las imágenes de previsualización de los sistemas que tengamos instalados en la consola. Skraper ofrece más posibilidades de configuración y mejor experiencia que Universal XML Scraper. Incluyo el segundo por ofrecer más posibilidades (por ejemplo Skraper no se ofrece compilado en versión 32 bit).

#### Skraper

Seguiremos los 8 pasos vistos en el post anterior [RG350 Scraper](/2020-01-11-rg350_scraper.html), añadiendo las siguientes opciones al paso 7:

* Apartado `Lista de juegos`
    * `Tipo de Lista de Juego`: `EmulationStation gamelist.xml`
    * `Ruta absoluta de lista de juegos`: `%ROMROOTFOLDER%\gamelist.xml`
* Apartado `Media`:
    * `Enlace a la lista de juegos`: `Enlace desde el nodo '<image>'`

De esta forma, además de las imágenes en los subdirectorios `.previews` dentro de los directorios de ROMs de los sistemas (compatible por tanto en este caso con las previsualizaciones de GMenu2X), aparecerá también el fichero `gamelist.xml` que contiene la metainformación de los juegos y el enlace a las imágenes. A partir de que se incorpore el fichero `gamelist.xml` en los distintos sistemas empezaremos a ver el menú de ROMs correspondiente con la metainformación y las imágenes:

![EmulationStation Boxart](/images/posts/emulationstation_boxart.png)

#### Universal XML Scraper

1. Extraer la tarjeta externa de la RG350 y montarla con un adaptador o lector en el PC.
2. Descargar [Universal XML Scraper V2](https://github.com/Universal-Rom-Tools/Universal-XML-Scraper/releases) y ejecutar.
3. Al abrirlo lo primero que se nos pregunta es por el idioma. Elegir `English (US)` porque en todas las pruebas que hice en `Español` EmulationStation se cerraba cuando seleccionaba un juego en cuya descripción había acentos:

	![UXS 1](/images/posts/uxs_1.png)

4. Después se inicia una especia de asistente. En él seleccionar `Recalbox` como Sistema Operativo:

	![UXS 2](/images/posts/uxs_2.png)

5. En la segunda pantalla del asistente seleccionar el tipo de previsualización que más nos guste y si es un mix el tipo de mix:

	![UXS 3](/images/posts/uxs_3.png)
	![UXS 4](/images/posts/uxs_4.png)

6. Lo siguiente es localizar la ruta de las ROMs. Seleccionaremos `Localy` (imagen de PC) y acto seguido localizamos el diretorio `roms` de la tarjeta montada en el punto 1:

	![UXS 5](/images/posts/uxs_5.png)
	![UXS 6](/images/posts/uxs_6.png)

7. Nos pregunta si estamos registrados en ScreenScraper. Si en el pasado seguimos el post anterior [RG350 Scraper](/2020-01-11-rg350_scraper.html), ya tendremos la cuenta creada. Si no, nos permite continuar sin cuenta:

	![UXS 7](/images/posts/uxs_7.png)
	![UXS 8](/images/posts/uxs_8.png)

8. Por último aparece una última pantalla de confirmación para inciar el scraping:

	![UXS 9](/images/posts/uxs_9.png)

9. Al comenzar se nos preguntará por el directorio de ROMs del que queremos hacer el scraping y el sistema al que pertenece:

	![UXS 10](/images/posts/uxs_10.png)
	![UXS 11](/images/posts/uxs_11.png)

10. Sobre la ventana principal veremos el progreso del scraping:

	![UXS 12](/images/posts/uxs_12.png)

11. Tras un tiempo durante el cual se generarán y bajarán las previsualizaciones, cerraremos el programa. En ese momento veremos que junto a las ROMs del sistema seleccionado se habrán creado dos cosas:

    * Un directorio llamado `downloaded_images` que contendrá las imágenes.
    * Un fichero llamado `gamelist.xml` con la metainformación y las rutas de las imágenes asociadas a cada ROM.

Podríamos pensar que renombrando el directorio `downloaded_images` por `.previews` conseguiremos que las previsualizaciones sean compatibles con GMenu2X, pero no es así porque los nombres de las imágenes incluyen el sufijo `-image` antes de la extensión.

Ya podemos extraer la microSD del PC y devolverla a la RG350. Ya deberíamos poder ver las previsualizaciones y la metainformación de los juegos scrapeados:

![EmulationStation Boxart UXS](/images/posts/emulationstation_boxart_uxs.png)

## Temas

Por último vamos a hacer un muestrario de los temas que trae precargados la versión de EmulationStation que acabamos de instalar. El tema se cambia dentro de la sección `UI Settings` del `Main Menu` que aparece al pulsar `Start`:

![EmulationStation Tema 1](/images/posts/emulationstation_tema1.png)

Es la última opción de esa pantalla:

![EmulationStation Tema 2](/images/posts/emulationstation_tema2.png)

Los temas disponibles son estos cuatro, aunque los dos últimos parecen ser el mismo:

![EmulationStation Tema 3](/images/posts/emulationstation_tema3.png)

Vamos a ver ejemplos de cada uno:

#### PixelPerfect

![EmulationStation Tema 6](/images/posts/emulationstation_tema6.png)
![EmulationStation Tema 7](/images/posts/emulationstation_tema7.png)

#### Pixel

![EmulationStation Tema 8](/images/posts/emulationstation_tema8.png)
![EmulationStation Tema 9](/images/posts/emulationstation_tema9.png)

#### Simple y SimpleGCW

![EmulationStation Tema 4](/images/posts/emulationstation_tema4.png)
![EmulationStation Tema 5](/images/posts/emulationstation_tema5.png)

## Personalización de los Temas

Los temas se encuentran instalados en la ruta `/media/data/local/home/.emulationstation/themes`. Dentro de ella encontramos un directorio por cada tema disponible:

```
RG350:/media/data/local/home/.emulationstation/themes # ls -l
drwx------   69 root     root          4096 Feb 10 21:38 _PixelPerfect (Default)
drwx------   64 root     root          4096 Feb 10 21:38 pixel
drwx------   62 root     root          4096 Feb 10 21:38 simple
drwx------   64 root     root          4096 Feb 10 21:38 simplegcw
```

El nombre del directorio será el que luego aparezca en el listado de temas en los ajustes de ES:

![EmulationStation Tema 3](/images/posts/emulationstation_tema3.png)

Dentro de cada uno de los temas encontramos los siguientes elementos:

* Fichero `simple.xml`: Configuración general del tema. El nombre del fichero puede ser cualquiera pero hay que tener en cuenta que se hace referencia a él dentro de la configuración particular de cada sistema que luego veremos, por lo que si ya hemos empezado a adaptar los mismos no podremos cambiar su nombre a no ser que lo reemplacemos en todos ellos.
* Directorio `art` con recursos generales del tema como tipos de letra e imágenes. En realidad este directorio es más conveniente que necesario, es decir, los recursos que contienen están enlazados dentro del fichero `simple.xml`, por lo que podrían estar en otro lugar.
* Directorios de cada sistema: Por cada plataforma que queramos mostrar en ES tendremos un directorio con su nombre. Los nombres de las plataformas pueden ser cualquiera que hayamos utilizado en el parámetro `platform` del fichero `es_systems.cfg`, aunque se recomienda utilizar las que aparecen en el apartado **Platform Names** que hay en [esta página](https://emulationstation.org/gettingstarted.html#config):

En el siguiente listado podemos ver todos estos elementos (se ocultan la mayoría de los sistemas para que no quede muy voluminoso):

```
RG350:/media/data/local/home/.emulationstation/themes/simple # ls -l
drwx------    3 root     root          4096 Feb 10 21:38 3do
drwx------    3 root     root          4096 Feb 10 21:38 amiga
drwx------    3 root     root          4096 Feb 10 21:38 amstradcpc
drwx------    3 root     root          4096 Feb 10 21:38 apple2
drwx------    2 root     root          4096 Feb 10 21:38 art
drwx------    3 root     root          4096 Feb 10 21:38 atari2600
drwx------    3 root     root          4096 Feb 10 21:38 atari5200
...
drwx------    3 root     root          4096 Feb 10 21:38 segacd
drwx------    3 root     root          4096 Feb 10 21:38 sfc
-rw-r--r--    1 root     root          2785 Feb 10 21:38 simple.xml
drwx------    3 root     root          4096 Feb 10 21:38 snes
drwx------    3 root     root          4096 Feb 10 21:38 vectrex
...
drwx------    3 root     root          4096 Feb 10 21:38 zxspectrum
```

Si por ejemplo queremos añadir un sistema nuevo, tan sólo tendremos que crear un nuevo directorio con un fichero `theme.xml` y resto de ficheros a los que luego se haga referencia en él. Por ejemplo este es el contenido del directorio correspondiente a Game Boy en el tema `Simple`:

```
RG350:/media/data/local/home/.emulationstation/themes/simple/gb # find .
.
./art
./art/gb_art.png
./art/gb.svg
./art/gb_art_blur.jpg
./theme.xml
```

Como vemos junto al fichero XML hay un directorio `art` que contiene tres imágenes. Al igual que con los recursos generales del tema, este directorio se utiliza por organización, no por necesidad. Los recursos que contienen están enlazados dentro de `theme.xml`, por lo que podrían estar en otro lugar.

El fichero `theme.xml` puede contener mucha información. Lo mejor es clonar todo el directorio de otro sistema y adaptar las imágenes y las referencias a éstas dentro de `theme.xml`.
