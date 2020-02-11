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

Para que EmulationStation reconozca los distintos sistemas de emulación, deben estar correctamente registrados en uno de los ficheros de configuración que hemos copiado durante la instalación, concretamente el que queda en la ruta `/usr/local/home/.emulationstation/es_systems.cfg`. Desafortunadamente no hay ningún medio para hacer esta configuración automáticamente. Nos va a tocar hacerla manualmente. Estamos en una situación muy similar a la de [SimpleMenu](/2020-01-25-rg350_simplemenu.html). De hecho el apartado de [Configuración](/2020-01-25-rg350_simplemenu.html#configuracion) de ese artículo, es conceptualmente idéntico. Sólo cambia el formato concreto de la configuración que necesita EmulationStation. Se recomienda por tanto hacer como en el caso de [SimpleMenu](/2020-01-25-rg350_simplemenu.html#configuracion), es decir, transferir el fichero de configuración `/usr/local/home/.emulationstation/es_systems.cfg` al ordenador para editarlo allí con un editor que soporte directamente el formato de texto de Linux como [Notepad++](https://notepad-plus-plus.org/).

Las distintas extensiones se añaden separadas por comas o espacios.

## arranque

Para que se arranque por defecto, crear si no existe el fichero `/media/data/local/sbin/frontend_start` o modificarlo con el siguiente contenido:

```
#!/bin/sh
if [ -f /media/data/apps/emulationstation.opk ]; then
    # start EmulationStation as default launcher
    /usr/bin/opkrun /media/data/apps/emulationstation.opk
    # when emulationstation quits -> we start gmenu2x
    /usr/bin/gmenu2x

elif [ -f /media/data/apps/gmenunx.opk ]; then
    /usr/bin/opkrun -m default.gcw0.desktop /media/data/apps/gmenunx.opk
else
    /usr/bin/gmenu2x
fi
```

## Boxart

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

Lista de Scrapers:

* [Steven Selph's Scraper](https://github.com/sselph/scraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#steven-selphs-scraper)
* [Lars Muldjord's Skyscraper](https://github.com/muldjord/skyscraper): [Instrucciones](https://retropie.org.uk/docs/Scraper/#lars-muldjords-skyscraper)
* [Universal XML Scraper](https://github.com/Universal-Rom-Tools/Universal-XML-Scraper)


Para generar `gamelist.xml` hay que ajustar el parámetro `Lista de juegos > Tipo de Lista de Juego` a `EmulationStation gamelist.xml` y como `Lista de juegos > Ruta absoluta de lista de juegos`: `%ROMROOTFOLDER%\gamelist.xml`.
Para que se incluyan las imágenes hay que activar `Media > Enlace a la lista de juegos`: `Enlace desde el nodo '<image>'`.
