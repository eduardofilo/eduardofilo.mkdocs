title: RG350 Instalador RA
summary: Instalador RetroArch para RG350/RG280.
date: 2021-01-16 21:20:00

![Icono](/images/posts/rg350_ra_installer/icon.png)

A finales de diciembre empezaron a aparecer distribuciones oficiales de RetroArch para RG350 y RG280. De momento en versión beta en forma de nightly builds que pueden obtenerse de [este sitio](https://buildbot.libretro.com/nightly/dingux/mips32/).

Los zips que distribuyen contienen un único OPK y un directorio (con toda la configuración y los cores) destinado a copiarse al home de la consola:

![Files](/images/posts/rg350_ra_installer/files.png)

Una vez que todo está instalado en su sitio, la única manera de ejecutar las ROMs con los cores que incluye la distribución es por medio del único OPK que lanza RetroArch a modo frontend (el interfaz UX que suele decirse en otros emuladores):

![Frontend](/images/posts/rg350_ra_installer/frontend.png)

Para lograr una integración más completa de RetroArch, que respete la experiencia normal de los frontends habituales en RG350/RG280 (GMenu2X, SimpleMenu, PyMenu, EmulationStation, etc.) se pueden crear unos OPKs tipo wrapper que permitan seleccionar las ROMs y lanzar el core de RetroArch correspondiente, ya que el binario/ejecutable `retroarch` que hay dentro del OPK admite los mismos argumentos que RetroArch en otras plataformas.

## Wrappers OPK

Para lograrlo, primero hubo que averiguar la forma de parametrizar el core y la ROM. Cargar un core y una ROM desde el propio RetroArch no sirve porque no exterioriza estos datos en forma de argumentos sobre el ejecutable. Lo que se hizo fue suponer que serviría el mismo formato de argumentos que utiliza el ejecutable `retroarch` en otros sistemas como EmuELEC en RG351P. Allí el frontend habitual EmulationStation sí que parametriza el core y la ROM a ejecutar por medio de argumentos en la llamada. Por ejemplo ejecutando Tetris de Game Boy con el core gambatte en EmuELEC sobre RG3551P se encuentra que el proceso se invoca de esta forma:

```
/usr/bin/retroarch -v -L /tmp/cores/gambatte_libretro.so --config /storage/.config/retroarch/retroarch.cfg /storage/roms/gb/Tetris (World) (Rev A).7z
```

Por tanto la idea es por un lado instalar el ejecutable/binario de RetroArch que hay dentro del OPK en una ruta accesible (se elige `/media/data/local/bin`) y luego construir distintos OPKs que invoque un script al que se le pase como argumento la ROM a ejecutar y que termine llamando al ejecutable de RetroArch anterior. Por ejemplo para el sistema Game Boy el script podría ser el siguiente:

```bash
#!/bin/sh
/media/data/local/bin/retroarch -v -L /media/data/local/home/.retroarch/cores/gambatte_libretro.so --config /media/data/local/home/.retroarch/retroarch.cfg "$1"
```

Introducimos el script anterior junto con un icono adecuado al sistema que va a lanzar y un `.desktop` que invoque el script pasando como argumento la ROM que vamos a lanzar, por ejemplo:

```
[Desktop Entry]
Name=Nintendo GB (RA)
Comment=Nintendo GB in RetroArch
Exec=exec.sh %f
Terminal=false
Type=Application
StartupNotify=true
Icon=icon
Categories=retroarch;
X-OD-NeedsDownscaling=true
```

Los cores que ofrece la última versión de RetroArch publicada en el momento de escribir este artículo son los siguientes:

* fbalpha2012_cps1_libretro: CPS1
* fbalpha2012_cps2_libretro: CPS2
* fbalpha2012_neogeo_libretro: Neo Geo
* fceumm_libretro: NES
* gambatte_libretro: GB/GBC
* genesis_plus_gx_libretro: MD, MS, GG, SEGA CD
* gpsp_libretro: GBA
* handy_libretro: LYNX
* mednafen_pce_fast_libretro: PCE, PCE CD
* mednafen_wswan_libretro: WS
* mgba_libretro: GBA
* mrboom_libretro: MrBoom
* picodrive_libretro: MD, MS, SEGA CD, SEGA 32X
* pokemini_libretro: POKEMINI
* prboom_libretro: DOOM
* quicknes_libretro: NES
* race_libretro: NGP
* snes9x2005_libretro: SNES
* snes9x2005_plus_libretro: SNES
* tyrquake_libretro: QUAKE
* vice_x64_libretro: C64

Por lo tanto habrá que hacer al menos un OPK para cada uno de ellos. Decimos al menos porque se puede plantear la opción de hacer un OPK por cada combinación "core/sistema a emular".

## Instalador

Como son varias las piezas necesarias para que funcione el conjunto, se ha creado un instalador para instalar de una sola vez todo lo necesario. En concreto el instalador integra:

* OPKs para lanzar de manera independiente desde distintos frontends (GMenu2X, SimpleMenu, PyMenu, EmulationStation, etc) los distintos cores seleccionando previamente la ROM.
* Binario `retroarch` en localización común (`/media/data/local/bin`) para no tener que repetirlo dentro de los OPKs anteriores.
* Configuraciones de todos los cores diferenciados por pantalla, es decir se instalan unas configuraciones adecuadas para 320x240 o para 640x480 en función de la pantalla detectada. Las configuraciones se han adoptado de las recomendaciones de Retro Game Corps en [esta guía](https://retrogamecorps.com/2020/12/24/guide-retroarch-on-rg350-and-rg280-devices/).
* Filtros de GMenu2X por extensión para cada sistema.
* Sección nueva con el icono de RetroArch en todos los skins instalados en GMenu2X donde aparecen todos los lanzadores de los OPKs.

El OPK con el instalador puede obtenerse en las releases de [este repositorio](https://github.com/eduardofilo/RG350_ra_installer/releases/latest).

## Hotkeys

En el fichero de configuración de RetroArch que instala el instalador, se han definido los siguientes controles:

|Función|Shortcut|
|:-------|:-------|
|Pausa|`Select + A`|
|Reset|`Select + B`|
|Menú RetroArch|`Select + X`|
|Avance rápido|`Select + Y`|
|Guardar savestate|`Select + R1`|
|Cargar savestate|`Select + L1`|
|Cambiar disco|`Select + R2`|
|Abrir bandeja CD|`Select + L2`|
|Cerrar juego|`Select + Start`|
|Cambiar slot savestate|`Select + ←→`|
|Cambiar volumen|`Select + ↑↓`|
