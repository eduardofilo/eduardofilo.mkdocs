---
layout: default
permalink: /sistemas/kodi.html
---

# Kodi/OpenELEC

## Desactivar un canal de PelisALaCarta
Si durante las búsquedas, alguno de los canales bloquea el progreso, seguramente habrá habido algún cambio en el código del sitio que el plugin no es capaz de interpretar. Habrá que esperar a que salga una nueva versión del plugin, pero mientras tanto se puede desactivar ese canal acudiendo a la ruta siguiente:

    /storage/.kodi/addons/plugin.video.pelisalacarta/channels

Allí localizamos el archivo .xml correspondiente al canal, lo editamos y ponemos a `false` la propiedad `active`.

## Mapeo de teclas del mando a distancia
En ocasiones alguna de las teclas del mando deja de funcionar. A mi me ha ocurrido varias veces con la tecla Back. Con el tiempo se soluciona solo (algunas veces reiniciar ayuda pero no siempre). Desconozco el mecanismo que estropea el mapeo de esta tecla, pero la solución es modificar el fichero `/storage/.kodi/userdata/keymaps/remote.xml`. En él, dentro de la sección `<keymap><global><remote>`, cuando deja de funcionar la tecla back me encuentro:

    <back>RunScript(special://userdata/keymaps/test.py)</back>

La solución es reponer el valor:

    <back>Back</back>

## Scrap manual de una serie
Si al intentar forzar el contenido de una carpeta con una serie, no nos localiza la serie y ésta está dada de alta en TheTVDB (me ocurrió por ejemplo con [Ramón y Cajal](http://thetvdb.com/?tab=series&id=290587&lid=16)), incluir un fichero en la raíz del directorio de la serie con el nombre `tvshow.nfo` y el siguiente contenido ([fuente](http://kodi.wiki/view/NFO_files/TV_shows#Video_.nfo_files_containing_a_URL)):

    http://thetvdb.com/index.php?tab=series&id=290587

## Script autoarranque para reproducir una lista

Situar en la ruta `.kodi/userdata/` un fichero con el nombre `autoexec.py`. Allí insertar el código:

```python
import xbmc

playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playlist.load('/storage/.kodi/userdata/playlists/video/Africa.m3u')
xbmc.Player().play(item=playlist)
```
