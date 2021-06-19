title: RG350 Instalador RA
summary: Instalador RetroArch para RG350/RG280.
date: 2021-01-16 21:20:00

![Icono](/images/posts/rg350_ra_installer/icon_big.png)

A finales de diciembre empezaron a aparecer distribuciones oficiales de RetroArch para RG350 y RG280. De momento en versión beta en forma de nightly builds que pueden obtenerse de [este sitio](https://buildbot.libretro.com/nightly/dingux/mips32/) para stock/ROGUE o [este otro](https://buildbot.libretro.com/nightly/dingux/mips32-odbeta/) para [ODBeta](http://od.abstraction.se/opendingux/latest/).

Los zips que distribuyen contienen un único OPK, un binario (opcional) y un directorio (con toda la configuración y los cores) destinado a copiarse al home de la consola:

![Files](/images/posts/rg350_ra_installer/files.png)

Una vez que todo está instalado en su sitio, la única manera de ejecutar las ROMs con los cores que incluye la distribución es por medio del único OPK que lanza RetroArch a modo frontend (el interfaz UX que suele decirse en otros emuladores):

![Frontend](/images/posts/rg350_ra_installer/frontend.png)

Para lograr una integración más completa de RetroArch, que respete la experiencia normal de los frontends habituales en RG350/RG280 (GMenu2X, SimpleMenu, PyMenu, EmulationStation, etc.) se pueden crear unos OPKs tipo wrapper que permitan seleccionar las ROMs y lanzar el core de RetroArch correspondiente, ya que el binario opcional admite los mismos argumentos que RetroArch en otras plataformas.

## Wrappers OPK

Para lograrlo, primero hubo que averiguar la forma de parametrizar el core y la ROM. Cargar un core y una ROM desde el propio RetroArch no sirve porque no exterioriza estos datos en forma de argumentos sobre el ejecutable. Lo que se hizo fue suponer que serviría el mismo formato de argumentos que utiliza el binario `retroarch_rg350` (dentro del directorio `bin`; en la distribución correspondiente a ODBeta, el binario es `retroarch_rg350_odbeta`) en otros sistemas como EmuELEC en RG351P. Allí el frontend habitual EmulationStation sí que parametriza el core y la ROM a ejecutar por medio de argumentos en la llamada. Por ejemplo ejecutando Tetris de Game Boy con el core gambatte en EmuELEC sobre RG3551P se encuentra que el proceso se invoca de esta forma:

```
/usr/bin/retroarch -v -L /tmp/cores/gambatte_libretro.so --config /storage/.config/retroarch/retroarch.cfg /storage/roms/gb/Tetris (World) (Rev A).7z
```

Por tanto la idea es por un lado instalar el binario opcional `retroarch_rg350` en una ruta accesible (se elige `/media/data/local/bin`) y luego construir distintos OPKs que invoque un script al que se le pase como argumento la ROM a ejecutar. Dentro del script podemos montar la llamada completa a `retroarch_rg30`. Por ejemplo para el sistema Game Boy el script podría ser el siguiente:

```bash
#!/bin/sh
/media/data/local/bin/retroarch_rg350 -v -L /media/data/local/home/.retroarch/cores/gambatte_libretro.so --config /media/data/local/home/.retroarch/retroarch.cfg "$1"
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

Los cores que ofrece la última versión de RetroArch publicada en el momento de escribir este artículo (2021-06-18) son los siguientes:

|Core|Sistema|Extensiones soportadas|Observaciones|
|:---|:------|:---------------------|:------------|
|fbalpha2012_cps1_libretro.so|CPS1|zip| |
|fbalpha2012_cps2_libretro.so|CPS2|zip| |
|fbalpha2012_neogeo_libretro.so|Neo Geo|zip| |
|fceumm_libretro.so|NES|fds, nes, unif, unf|Disk System necesita BIOS: `disksys.rom` (md5: `ca30b50f880eb660a320674ed365ef7a`)|
|gambatte_libretro.so|GB/GBC|gb, gbc, dmg|BIOS opcional: `gb_bios.bin` (md5: `32fbbd84168d3482956eb3c5051637f5`), `gbc_bios.bin` (md5: `dbfce9db9deaa2567f6a84fde55f9680`)|
|genesis_plus_gx_libretro.so|MD, MS, GG, SEGA CD|mdx, md, smd, gen, bin, cue, iso, sms, bms, gg, sg, 68k, chd, m3u|SEGA CD necesita BIOS: `bios_CD_E.bin`, `bios_CD_U.bin`, `bios_CD_J.bin`|
|genesis_plus_gx_wide_libretro.so|MD, MS, GG, SEGA CD|mdx, md, smd, gen, bin, cue, iso, sms, bms, gg, sg, 68k, chd, m3u|SEGA CD necesita BIOS: `bios_CD_E.bin`, `bios_CD_U.bin`, `bios_CD_J.bin`|
|gpsp_libretro.so|GBA|gba, bin|BIOS opcional: `gba_bios.bin` (md5: `a860e8c0b6d573d191e4ec7db1b1e4f6`)|
|handy_libretro.so|LYNX|lnx, o|Necesita BIOS: `lynxboot.img` (md5: `fcd403db69f54290b51035d82f835e7b`)|
|mednafen_pce_fast_libretro.so|PCE, PCE CD|pce, cue, ccd, chd, toc, m3u|PCE CD necesita BIOS: `syscard3.pce` (md5: `38179df8f4ac870017db21ebcbf53114`)|
|mednafen_wswan_libretro.so|WS|ws, wsc, pc2| |
|mgba_libretro.so|GBA|gb, gbc, gba|BIOS opcional: `gba_bios.bin` (md5: `a860e8c0b6d573d191e4ec7db1b1e4f6`)|
|mrboom_libretro.so|MrBoom| | |
|picodrive_libretro.so|MD, MS, SEGA CD, SEGA 32X|bin, gen, smd, md, 32x, chd, cue, iso, sms, 68k, m3u|SEGA CD necesita BIOS: `bios_CD_U.bin` (md5: `2efd74e3232ff260e371b99f84024f7f`), `bios_CD_E.bin` (md5: `e66fa1dc5820d254611fdcdba0662372`), `bios_CD_J.bin` (md5: `278a9397d192149e84e820ac621a8edd`)|
|pokemini_libretro.so|POKEMINI|min|Necesita BIOS: `bios.min` (md5: `1e4fb124a3a886865acb574f388c803d`)|
|prboom_libretro.so|DOOM|wad, iwad, pwad|Necesita ficheros de juego|
|quicknes_libretro.so|NES|nes| |
|race_libretro.so|NGP|ngp, ngc, ngpc, npc| |
|snes9x2005_libretro.so|SNES|smc, fig, sfc, gd3, gd7, dx2, bsx, swc| |
|snes9x2005_plus_libretro.so|SNES|smc, fig, sfc, gd3, gd7, dx2, bsx, swc| |
|tyrquake_libretro.so|QUAKE|pak|Necesita ficheros de juego|
|vice_x64_libretro.so|C64|d64, d71, d80, d81, d82, g64, g41, x64, t64, tap, prg, p00, crt, bin, zip, gz, d6z, d7z, d8z, g6z, g4z, x6z, cmd, m3u, vfl, vsf, nib, nbz, d2m, d4m| |
|stella2014_libretro.so|Atari 2600|a26, bin| |
|prosystem_libretro.so|Atari 7800|a78, bin|BIOS opcional: `7800 BIOS (U).rom` (md5: `0763f1ffb006ddbe32e52d497ee848ae`)|
|scummvm_libretro.so|ScummVM|<ver fichero en core_info>| |
|tic80_libretro.so|TIC-80|tic| |
|potator_libretro.so|Watara Supervision|bin, sv| |
|dosbox_pure_libretro.so|DOSBox|zip, dosz, exe, com, bat, iso, cue, ins, img, ima, vhd, m3u, m3u8| |
|o2em_libretro.so|Magnavox Odyssey2, Phillips Videopac+|bin|Necesita BIOS: `o2rom.bin` (md5: `562d5ebf9e030a40d6fabfc2f33139fd`)|
|mame2003_libretro.so|MAME2003|zip| |
|mame2003_plus_libretro.so|MAME2003|zip| |

Adicionalmente, se ha incluido la compilación de cores no oficiales hecha por [Poligraf](https://github.com/Poligraf/opendingux_ra_cores_unofficial) (**ADVERTENCIA** Esta compilación es un experimento de su autor; algunos cores como `hatari` o `puae` no han sido testeados; el feedback es bienvenido). Esto implica que se han añadido los siguientes cores a la lista anterior:

|Core|Sistema|Extensiones soportadas|Observaciones|
|:---|:------|:---------------------|:------------|
|81_libretro.so|Sinclair ZX81|p, tzx, t81| |
|bk_libretro.so|Elektronika - BK-0010/BK-0011|bin|Necesita BIOS: `bk/BASIC10.ROM` (md5: `3fa774326d75410a065659aea80252f0`), `bk/FOCAL10.ROM` (md5: `5737f972e8638831ab71e9139abae052`), `bk/MONIT10.ROM` (md5: `95f8c41c6abf7640e35a6a03cecebd01`)|
|cannonball_libretro.so|SEGA Outrun|game, 88|Necesita ficheros de juego y un fichero dummy con la extensión `.game`|
|cap32_libretro.so|Amstrad CPC|dsk, sna, zip, tap, cdt, voc, cpr, m3u| |
|freechaf_libretro.so|Fairchild ChannelF|bin, chf|Necesita BIOS: `sl31253.bin` (md5: `ac9804d4c0e9d07e33472e3726ed15c3`), `sl31254.bin` (md5: `da98f4bb3242ab80d76629021bb27585`), `sl90025.bin` (md5: `95d339631d867c8f1d15a5f2ec26069d`)|
|fuse_libretro.so|Sinclair ZX Spectrum|tzx, tap, z80, rzx, scl, trd, dsk| |
|gme_libretro.so|Game Music Emu|ay, gbs, gym, hes, kss, nsf, nsfe, sap, spc, vgm, vgz, zip| |
|hatari_libretro.so|Atari ST|st, msa, zip, stx, dim, ipf, m3u|Necesita BIOS: `tos.img` (md5: `c1c57ce48e8ee4135885cee9e63a68a2`). Configuración complicada. Se ha conseguido cierto éxito con RG350M pero no con RG350P|
|mednafen_vb_libretro.so|Nintendo Virtual Boy|vb, vboy, bin|Rendimiento pobre|
|nxengine_libretro.so|Cave Story|exe|Necesita ficheros de juego|
|puae_libretro.so|Commodore Amiga|adf, adz, dms, fdi, ipf, hdf, hdz, lha, slave, info, cue, ccd, nrg, mds, iso, chd, uae, m3u, zip, 7z|Necesita BIOS: `kick34005.A500` (md5: `82a21c1890cae844b3df741f2762d48d`)|
|reminiscence_libretro.so|Flashback|map, aba, seq, lev|Necesita ficheros de juego|
|theodore_libretro.so|Thomson - MO/TO|fd, sap, k7, m7, m5, rom|Configuración complicada. Se ha conseguido cierto éxito con el modelo MO5 de máquina, en ODBeta con RG350M, pero no en stock/ROGUE|
|uzem_libretro.so|Uzebox|uze|Rendimiento pobre|

Por lo tanto habrá que hacer al menos un OPK para cada uno de ellos. Decimos *al menos* porque se puede plantear la opción de hacer un OPK por cada combinación "core/sistema a emular".

## Instalador

Como son varias las piezas necesarias para que funcione el conjunto, se ha creado un instalador para instalar de una sola vez todo lo necesario. En concreto el instalador integra:

* OPKs para lanzar de manera independiente desde distintos frontends (GMenu2X, SimpleMenu, PyMenu, EmulationStation, etc) los distintos cores seleccionando previamente la ROM.
* Binario `retroarch_rg350` (o `retroarch_rg350_odbeta` para ODBeta) en localización común (`/media/data/local/bin`) para no tener que repetirlo dentro de los OPKs anteriores.
* Configuraciones de todos los cores diferenciados por pantalla, es decir se instalan unas configuraciones adecuadas para 320x240 o para 640x480 en función de la pantalla detectada. Las configuraciones se han adoptado de las recomendaciones de Retro Game Corps en [esta guía](https://retrogamecorps.com/2020/12/24/guide-retroarch-on-rg350-and-rg280-devices/).
* Filtros de GMenu2X por extensión para cada sistema.
* Sección nueva con el icono de RetroArch en todos los skins instalados en GMenu2X donde aparecen todos los lanzadores de los OPKs.

Cuando se lanza, pregunta por dos opciones que están desactivadas por defecto:

![Installing options](/images/posts/rg350_ra_installer/installing_options.png)

* Install config: Para instalar las configuraciones comentadas en el tercer punto de la lista anterior. Se recomienda instalar las configuraciones la primera vez y no instalarlas en reinstalaciones posteriores para evitar la pérdida de los ajustes personales hechos sobre la configuración básica.
* Install unofficial cores: Para instalar los 14 nuevos pero no oficiales cores compilados por [Poligraf](https://github.com/Poligraf/opendingux_ra_cores_unofficial).

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

## Canal Telegram

Se ha creado este canal de Telegram para comunicar más fácilmente las actualizaciones de este instalador: [https://t.me/RG350_ra_installer](https://t.me/RG350_ra_installer)
