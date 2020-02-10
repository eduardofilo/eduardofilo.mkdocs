title: 2020-01-26 RG350 EmulationStation
summary: Instalación y configuración de EmulationStation en RG350.
date: 2020-01-26 17:39:00

![EmulationStation](/images/posts/emulationstation.png)

En este artículo vamos a ver cómo instalar y configurar el frontend EmulationStation en la RG350.

## Instalación

Bajo:

* https://rs97.bitgala.xyz/RG-350/localpack/extra_emulators/EmulationStation%20RG-350%20(Configured).zip
* https://github.com/ManuelSch81/RG350-EmulationStation_configured

Copio `Internal SD Card/emulationstation.opk` a `/media/data/apps`

$ cd Internal\ SD\ Card/
$ scp emulationstation.opk root@10.1.1.2:/media/data/apps

Copio el contenido de `Internal SD Card/data` a `/usr/local/home/.emulationstation`

$ cd data
$ scp -r * root@10.1.1.2:/usr/local/home/.emulationstation


Editar fichero `/usr/local/home/.emulationstation/es_systems.cfg`. Las distintas extensiones se añaden separadas por comas o espacios.

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
