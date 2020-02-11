title: 2020-01-26 RG350 EmulationStation
summary: Instalación y configuración de EmulationStation en RG350.
date: 2020-01-26 17:39:00

![EmulationStation](/images/posts/emulationstation.png)

En este artículo vamos a ver cómo instalar y configurar el frontend EmulationStation en la RG350.

## Instalación

Empezamos por la instalación. Desgraciadamente además de copiar un OPK como habitualmente, hay que mover unos cuantos ficheros a una ruta de la tarjeta interna. A continuación los detalles paso a paso (las operaciones de copiado de ficheros se muestran con DinguxCmdr por ser accesible para todo el mundo, pero naturalmente se pueden hacer por FTP o SSH):

1. Bajar [este archivo](https://github.com/ManuelSch81/RG350-EmulationStation_configured/archive/master.zip) y descomprimirlo.
2. Dentro veremos el directorio `Internal SD Card` (el resto no los utilizaremos para nada) que hay que copiar a la tarjeta externa de la consola (montándola en el PC con un adaptador o lector de tarjetas o por FTP).
3. Desmontar la SD del PC para devolverla a la ranura externa de la consola.
4. Abrir DinguxCmdr. Moverse por la estructura de ficheros hasta localizar a la izquierda la ruta `/media/sdcard/Internal SD Card` y a la derecha `/media/sdcard/apps`. La ruta de la derecha es donde vamos a instalar el OPK. En este caso hemos indicado la ruta de los OPKs que se leen de la tarjeta externa. Alternativamente se puede utilizar la ruta `/media/data/apps` si se prefiere instalar en la interna:

    ![EmulationStation Instalación 1](/images/posts/emulationstation_install1.png)

5. Seleccionar el fichero `emulationstation.opk` en el panel izquierdo y pulsar `X`. En el menú que aparece seleccionar `Copy >` y confirmar con `A`:

    ![EmulationStation Instalación 2](/images/posts/emulationstation_install2.png)

6. Seleccionar el directorio `data` en el panel izquierdo y pulsar `X`. En el menú que aparece seleccionar `Rename` y confirmar con `A`. Nos aparecerá un teclado virtual con el que lo renombraremos a `.emulationstation` (ojo al punto inicial). Para borrar utilizamos `Y` y para escribir seleccionamos la letra o el punto con la cruceta y confirmamos con `A`. Terminamos seleecionando `OK`:

    ![EmulationStation Instalación 3](/images/posts/emulationstation_install3.png)

7. Cambiar en el panel derecho la ruta a `/media/data/local/home`:

    ![EmulationStation Instalación 4](/images/posts/emulationstation_install4.png)

8. Seleccionar en el panel izquierdo el directorio que hemos renombrado en el paso 6 y pulsar `X`. En el menú que aparece seleccionar `Copy >` y confirmar con `A`:

    ![EmulationStation Instalación 5](/images/posts/emulationstation_install5.png)

9. Finalmente salir de `DinguxCmdr` pulsando `Y` y seleccionando `Quit`:

    ![EmulationStation Instalación 6](/images/posts/emulationstation_install6.png)

Con esto finaliza la instalación de la aplicación.

## Configuración

Para que EmulationStation reconozca los distintos sistemas de emulación, deben estar correctamente registrados en uno de los ficheros de configuración que hemos copiado durante la instalación, concretamente el que queda en la ruta `/usr/local/home/.emulationstation/es_systems.cfg`. Desafortunadamente no hay ningún medio para hacer esta configuración automáticamente. Nos va a tocar hacerla manualmente.

Estamos en una situación muy similar a la de [SimpleMenu](/2020-01-25-rg350_simplemenu.html). De hecho el apartado de [Configuración](/2020-01-25-rg350_simplemenu.html#configuracion) de ese artículo, conceptualmente nos sirve aquí. Sólo cambia el formato concreto de la configuración que necesita EmulationStation. Se recomienda por tanto hacer como en el caso de [SimpleMenu](/2020-01-25-rg350_simplemenu.html#configuracion), es decir, transferir el fichero de configuración `/usr/local/home/.emulationstation/es_systems.cfg` al ordenador para editarlo allí con un editor que soporte directamente el formato de texto de Linux como [Notepad++](https://notepad-plus-plus.org/).

El fichero `es_systems.cfg`, aunque no lo indique la extensión, internamente tiene formato XML. Se trata por tanto de una serie de bloques anidados que comienzan y terminan con etiquetas encerradas entre los símbolos `<` y `>`. El bloque raíz se define con la etiqueta `<systemList>` y dentro de él hay un bloque `<system>` para cada emulador. Dentro de este bloque ya directamente se encuentran los distintos parámetros del emulador. Como vemos la filosofía es muy similar a la del fichero de configuración de SimpleMenu, sólo que en éste último el formato del archivo no era XML, sino el que se utiliza habitualmente para los ficheros de configuración tipo [INI](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)).

Un bloque `<system>` de un sistema como Game Boy podría ser el siguiente:

```xml
<system>
    <name>gb</name>
	<fullname>Gameboy</fullname>
	<path>/media/sdcard/roms/Gameboy</path>
	<extension>.gb</extension>
	<command>"opkrun" "/media/sdcard/apps/gambatte.opk" %ROM%</command>
	<platform>gb</platform>
</system>
```

Vamos a detallar el significado de cada parámetro (la documentación original puede encontrarse [aquí](https://emulationstation.org/gettingstarted.html#config)):

* `name`: Nombre corto del sistema. Usado en algunas estructuras de directorios y mensajes de error.
* `fullname`: Nombre descriptivo. Es el que aparece en el frontend. Esta etiqueta es opcional. Si no está se usará `name` en su lugar.
* `path`: Ruta de las ROMs.
* `extension`: Extensiones de las ROMs que se listarán dentro del sistema. Las distintas extensiones se separan por comas o espacios.
* `command`: Comando con el que se lanzará el emulador cuando seleccionemos una ROM. Lo normal será que contenga algunos parámetros que serán sustituidos, como por ejemplo `%ROM%` que se convertirá en la ruta de la ROM seleccionada.
* `platform`: Plataforma utilizada cuando se hace scraping. Esta etiqueta es opcional. La lista completa de los códigos de plataforma se encuentra en la [página de documentación de EmulationStation](https://emulationstation.org/gettingstarted.html#config). Se pueden poner varias plataformas separadas por comas, por ejemplo `genesis,megadrive`.

Una vez que devolvamos el fichero de configuración `es_systems.cfg` a su lugar en `/usr/local/home/.emulationstation`, el resultado en SimpleMenu será éste:

![EmulationStation Running 1](/images/posts/emulationstation_running1.png)
![EmulationStation Running 2](/images/posts/emulationstation_running2.png)

Como punto de partida dejo aquí mi fichero de configuración que contiene la mayoría de los emuladores y la [estructura de directorios para las ROMs](/retro-emulacion/rg-350.html#las-roms-y-su-organizacion) que se utilizan habitualmente.

* [es_systems.cfg](/files/posts/es_systems.cfg)

## Arranque

EmulationStation aparecerá como aplicación en la sección `Emulators` de GMenu2X (no como [SimpleMenu](/2020-01-25-rg350_simplemenu.html#desde-gmenu2x) cuyo lanzador tenemos que añadir a mano). Si queremos que EmulationStation se autoarranque en el inicio de la consola tenemos que proceder como sigue:

1. Bajar el fichero [frontend_start](/files/posts/frontend_start).
2. Copiarlo a la raíz de la microSD externa.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del fichero se encuentra en `/media/sdcard/frontend_start`.
4. Copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![SimpleMenu 3](/images/posts/simplemenu_screenshot003.png)

5. Hacer ejecutable el fichero instalado. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar el siguiente comando desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	```

## Boxart

Una de las funcionalidades más interesantes de EmulationStation es su capacidad para adornar la presentación del listado de ROMs con previsualizaciones de los juegos y con metainformación (fecha de publicación, compañía desarrolladora, número de jugadores, etc.). Esta funcionalidad se basa en un fichero de texto llamado `gamelist.xml` en formato XML (parecido al que hemos visto antes para la configuración de los sistemas). El fichero puede estar en varios sitios, pero la ubicación más conveniente es el propio directorio de las ROMs. Deberá haber un fichero `gamelist.xml` por sistema, es decir por directorio de ROMs.

Como siempre que hablamos de este tema, interesa utilizar una herramienta que automatice el proceso, ya que normalmente tendremos muchas ROMs por cada sistema y aparte de largo y tedioso, escribir manualmente ficheros XML supone casi con toda seguridad introducir errores en su estructura. Así pues será conveniente utilizar un Scraper como los siguientes:

* [Steven Selph's Scraper](https://github.com/sselph/scraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#steven-selphs-scraper)
* [Lars Muldjord's Skyscraper](https://github.com/muldjord/skyscraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#lars-muldjords-skyscraper)
* [Universal XML Scraper](https://github.com/Universal-Rom-Tools/Universal-XML-Scraper)
* [Skraper](http://skraper.net/)

Vamos a detallar el uso de los dos últimos para generar los ficheros `gamelist.xml` y las imágenes de previsualización de los sistemas que tengamos instalados en la consola.

#### Universal XML Scraper

1. Extraer la tarjeta externa de la RG350 y montarla con un adaptador o lector en el PC.
2. Descargar [Universal XML Scraper V2](https://github.com/Universal-Rom-Tools/Universal-XML-Scraper/releases) y ejecutar.
3. En la especie de asistente que aparece seleccionar `Recalbox` como Sistema Operativo:

Pantallazo

4. En la segunda pantalla del asistente seleccionar el tipo de previsualización que más nos guste.

Pantallazo

5. Lo siguiente es localizar la ruta de las ROMs. Seleccionaremos `Localy` y acto seguido localizamos el diretorio `roms` de la tarjeta montada en el punto 1.

Pantallazo

6. Nos pregunta si estamos registrados en ScreenScraper. Si en el pasado seguimos los pasos del [artículo sobre este servicio](/2020-01-11-rg350_scraper.html), ya tendremos la cuenta creada. Si no, nos permite continuar sin cuenta.

Pantallazo

7. Por último aparece una última pantalla de confirmación para inciar el scraping.

Pantallazo

8. Al comenzar se nos preguntará por el sistema del que queremos hacer el scraping.

Pantallazo

9. Por último pulsamos el botón `Scrape` en la ventana principal.

10. Tras un tiempo durante el cual se generarán y bajarán las previsualizaciones, cerraremos el programa. En ese momento veremos que junto a las ROMs del sistema seleccionado se habrán creado dos cosas:

    * Un directorio llamado `downloaded_images` que contendrá las imágenes.
    * Un fichero llamado `gamelist.xml` con la metainformación y las rutas de las imágenes asociadas a cada ROM.

11. Editamos el fichero `gamelist.xml` y sustituimos todas las ocurrencias del directorio `downloaded_images` por `boxart`.

12. Copiamos todas las imágenes generadas por Universal XML Scraper a un directorio de nombre `boxart`




Ver esta serie de videos: https://www.youtube.com/channel/UC8c9cH_XB7JMEGInq1-LWLg/videos




Para generar `gamelist.xml` hay que ajustar el parámetro `Lista de juegos > Tipo de Lista de Juego` a `EmulationStation gamelist.xml` y como `Lista de juegos > Ruta absoluta de lista de juegos`: `%ROMROOTFOLDER%\gamelist.xml`.
Para que se incluyan las imágenes hay que activar `Media > Enlace a la lista de juegos`: `Enlace desde el nodo '<image>'`.
