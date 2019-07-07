---
layout: default
permalink: /sistemas/android_system.html
---

# Android

## Enlaces

* [Mount a filesystem read-write](http://android-tricks.blogspot.com/2009/01/mount-filesystem-read-write.html)
* [HTC Super Tool](http://forum.xda-developers.com/showthread.php?t=1343114)
* [Unlock Root](http://www.unlockroot.com/)
* [Link2SD](https://market.android.com/details?id=com.buak.Link2SD)
* [Como Desrootear tu terminal](http://4ndroid.com/como-desrootear-tu-telefono-androi/)
* [Simple ADB Backup - Full backup without root](http://forum.xda-developers.com/showthread.php?p=36499906)
* [Desbloquea el bootloader de tu HTC fácilmente con Firewater S-Off](http://www.elandroidelibre.com/2014/02/desbloquea-el-bootloader-de-tu-htc-facilmente-con-firewater-s-off.html)
* [Los móviles perfectos a los que instalar CyanogenMod y que te duren muchos años](http://www.elandroidelibre.com/2016/11/telefonos-instalar-cyanogenmod.html)

## Aplicaciones interesantes

* [KK Easy Launcher(Big Launcher)](https://play.google.com/store/apps/details?id=com.big.launcher)
* [Files Go](https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.files): Ayuda a limpiar el sistema.
* [SD Maid](https://play.google.com/store/apps/details?id=eu.thedarken.sdm): Ayuda a limpiar el sistema.

## Dispositivos

### OnePlus 5

#### Enlaces

* [Cómo evitar que OnePlus recopile información del usuario sin conocimiento](https://www.movilzona.es/2017/10/11/como-evitar-que-oneplus-recopile-informacion-del-usuario-sin-conocimiento/)
* [Cómo instalar Android Oreo 8.0 en el OnePlus 5](https://amp.andro4all.com/2017/10/instalar-android-oreo-8-0-oneplus-5)

#### Eliminación servicio `OnePlus System Service`

Este servicio recopila información privada como [ha reconocido la propia OnePlus](https://www.teknofilo.com/oneplus-responde-a-las-acusaciones-de-espiar-a-sus-usuarios/amp/). La forma de desinstalarlo es abriendo una shell por ADB y ejecutando un comando:

```
$ ./adb shell
OnePlus5:/ $ pm uninstall -k --user 0 net.oneplus.odm
Success
```

Previamente se recomienda hacer un backup de este paquete por si tras desinstalarlo el sistema queda inestable. Esto lo podemos hacer localizando el directorio del apk con [App Inspector](https://play.google.com/store/apps/details?id=bg.projectoria.appinspector) y lanzando el siguiente comando:

```
$ ./adb pull <ruta>
```

### OnePlus One

#### Enlaces

* [How to Unlock Bootloader, Install Custom Recovery and Root](https://forums.oneplus.net/threads/guide-oneplus-one-how-to-unlock-bootloader-install-custom-recovery-and-root.64487/)
* [OxygenOS is here [Installation Guide]](https://forums.oneplus.net/threads/oxygenos-is-here-installation-guide.289398/)
* [OnePlus One Update: Manually Install CyanogenMod OS 12 CM12 [TUTORIAL]](http://www.latintimes.com/oneplus-one-update-manually-install-cyanogenmod-os-12-cm12-tutorial-309788)
* [Mirrors for official Cyanogen roms and OTA updates](http://forum.xda-developers.com/oneplus-one/general/official-cm11s-roms-ota-updates-t2906746)
* [TWRP for bacon](https://dl.twrp.me/bacon/)
* [Cyanogem Support](https://cyngn.com/support): Imágenes de fábrica para Oneplus One y el resto de dispositivos que tienen soporte de Cyanogen.
* [Plasma Mobile on Oneplus One](https://forum.kde.org/viewtopic.php?f=297&t=127502)

#### Modos arranque

* Recovery: `V-` + `Power`
* Fastboot: `V+` + `Power`

#### Flasheo de ROM

Cuando el móvil avise de la disponibilidad de una nueva actualización, si está rooteado se producirá un error durante el arranque al aplicarla. En ese caso hay que obtener la rom completa (no sirven los parches incrementales) e instalar manualmente desde recovery siguiendo estos pasos ([fuente](http://www.droidviews.com/how-to-update-cyanogen-os-12-1-to-yog4pas2ql-on-oneplus-one/)):

1. **Download** the required ROM (full ROM) file for your device from the download section.
2. Now transfer the ROM into your device’s internal storage. Place the file where you can easily locate it.
3. Now reboot into **TWRP**. To boot into TWRP, power off your phone and press and hold volume down button and power button at the same time.
4. It is highly recommended that you perform a **nandroid backup**. To backup your ROM, tap on the backup option and select the following elements: **System, Data, Boot, Recovery, EFS** and swipe the confirmation action to backup.
5. You can skip this step, but if after the installation system doesn’t boot, try this step. After performing the ROM backup, return to the TWRP main menu and tap the **Wipe** button and select **Advanced Wipe**. Then wipe **Dalvik Cache**, **System**, and **Cache**. (If after the complete process system does not boot, try wiping the Data as well. But its will remove all your data)
6. Go back to the TWRP main menu again and tap on **Install** option. Navigate to the ROM file and select it.
7. Swipe the confirmation button to proceed with the installation. The ROM will be installed.
8. Once installed, **reboot to system**.

#### Reseteo de estadísticas de batería desde TWRP

1. Cargar la batería hasta el 100%
2. Arrancar el TWRP recovery
3. Seguir la ruta: Advanced / File Manager
4. Ir a la ruta: /data/system/
5. Pulsar sobre el fichero batterystats.bin
6. Pulsar Delete
7. Reiniciar el sistema
8. Descargar la batería hasta el 2 - 5 %
9. Volver a cargar la batería hasta el 100%

#### Instalación LineageOS

([Fuente](https://wiki.lineageos.org/devices/bacon/install))

1. Si no está ya, instalar el recovery [TWRP](https://dl.twrp.me/bacon/) siguiendo [estas instrucciones](https://wiki.lineageos.org/devices/bacon/install#installing-a-custom-recovery-using-fastboot-1).
2. Descargar de [aquí](https://download.lineageos.org/bacon).
    * Opcionalmente bajar las [GApps](https://wiki.lineageos.org/gapps.html) en edición ARM.
3. Copiar los ficheros al directorio `/sdcard` (en caso de haber perdido la partición de almacenamiento interno por haber instalado UBPorts por ejemplo, copiar los ficheros a un pendrive y pincharlo con un adaptador OTG; el pendrive se verá como `/sdcard` desde el Recovery).
4. Arrancar en modo Recovery (`V-` + `Power`).
5. Seleccionar `Wipe` y después `Advanced Wipe`.
6. Seleccionar las particiones `Cache`, `System` y `Data` y después `Swipe to Wipe`.
7. Vuelve al menú principal y selecciona `Install`.
8. Navega a `/sdcard` y seleciona el .zip de LineageOS.
9. Sigue las instrucciones en pantalla.
10. (Opcional) Instala el resto de paquetes. Si se van a instalar las GApps, hay que hacerlo antes del primer arranque.
11. Vuelve al menú principal y selecciona `Reboot`, y después `System`.

### Motorola Moto E (XT1021)

#### Enlaces

* [Info Cyanogenmod](http://wiki.cyanogenmod.org/w/Condor_Info)
* [Downloads Cyanogenmod](https://download.cyanogenmod.org/?device=condor)

#### Modos arranque

* Recovery: Apagado pulsar `Power` mientras se pulsa `Volume-`. Cuando salga el logo de Android tumbado con el triángulo rojo pulsar `Volume+` mientras se mantiene pulsado `Power`.

### Geeksphone One

#### Enlaces

* [Reset manual](https://groups.google.com/forum/#!topic/geeksphone/Nj4KXaAhbKE)
* [Tutorial ROM y Google Apps](https://sites.google.com/site/gappsone/)

#### ROMs

* [SuperAosp 8.6, Rom Basada en Android Open Source Gingerbread](http://forum.geeksphone.com/index.php?topic=1604.0)
* [CyanogenMod](http://download.cyanogenmod.com/?type=stable&device=one)
* [RCMod 3.0.4](http://forum.geeksphone.com/index.php?topic=961.0)
* [RCMod 4.0.0](http://forum.geeksphone.com/index.php?topic=1294.0)

#### Configuración A-GPS

Teóricamente, el server es: `h-slp.mncXXX.mccYYY.pub.3gppnetwork.org`  
En el puerto: 3425  
XXX lo cambias por el MNC de tu operador, e YYY por el MCC. En el caso de Simyo MCC=214 y MNC=19

### NVSBL P4D Sirius

#### Enlaces

* [SuperOSR ICS v1.4.6 para P4D Sirius](http://www.unusual-tech.com/community/forum/tablets/nvsbl-p4d-sirius/actualizaciones-by-superteam/2627-superosr-ics-v1-4-6-para-p4d-sirius)

### Samsung Galaxy mini2 (GT-S6500D)

#### Enlaces

* [Backup EFS folder without rooting](http://forum.xda-developers.com/showthread.php?t=2044941)
* [Samsung Galaxy mini2 Blog](http://galaxy-mini-2.blogspot.com.es/)
* [Root y unroot Galaxy Mini 2](http://galaxy-mini-2.blogspot.com.es/2012/12/rootear-galaxy-mini-2_22.html)
* [HOW TO CHANGE CSC CODE ON SAMSUNG GALAXY GRAND DUOS I9082/I9082L](http://forum.xda-developers.com/showthread.php?t=2342328)
* [Liberar Galacy Mini 2](http://galaxy-mini-2.blogspot.com.es/p/liberar-galaxy-mini-2.html)
* [Cambiar CSC (Country Specific Code)](http://galaxy-mini-2.blogspot.com.es/2013/02/megatutorial-cambiar-csc-country.html)
* [StockRoms S6500/D/L/T para flashear por CWM](http://galaxy-mini-2.blogspot.mx/2013/07/stockroms-para-flashear-por-cwm.html)
* [CyanogenMod 10 Thewhisp](http://galaxy-mini-2.blogspot.com.es/2013/01/cyanogenmod-10-thewhisp_12.html)
* [XDA - Galaxy Mini II Android Development](http://forum.xda-developers.com/galaxy-mini/mini-2-dev)
* [XDA - Galaxy Mini II Q&A, Help & Troubleshooting](http://forum.xda-developers.com/galaxy-mini/mini-2-help)

#### Modos arranque

* Recovery: V+ V- Home Power
* Download: V- Home Power

### HTC Desire

Los datos originales del HBOOT de un Desire sin manipular eran:

```
BRAVO PVT4 SHIP S-ON
HBOOT-0.93.0001
MICROP-051d
RADIO-5.11.05.14
Aug 10 2010,17:52:18
```

#### Modos de arranque

 * Se arranca en HBOOT manteniendo el Volume- mientras se pulsa Power.

#### Enlaces

* [Cómo rootear HTC Desire](http://www.htcmania.com/mediawiki/index.php/C%C3%B3mo_rootear_HTC_Desire)
* [Unlock Bootloader (HTC oficial)](http://www.htcdev.com/bootloader/)
* [MIUI-XJ 2.1.6 Gingerbread 2.3.7 para HTC Desire](http://4ndroid.com/miui-xj-2-1-6-gingerbread-2-3-7-para-htc-desire/)
* [Ice Cream Sandwich con toques de CyanogenMod para HTC Desire](http://4ndroid.com/ice-cream-sandwich-con-toques-de-cyanogenmod-para-htc-desire/)
* [Las mejores ROMs para HTC Desire](http://www.elandroidelibre.com/2011/07/las-mejores-roms-para-htc-desire-htc-desire-hd-y-desire-z.html)
* [Las mejores Roms para HTC Desire](http://hispadroid.blogspot.com/2011/05/las-mejores-roms-para-htc-desire.html)
* [ICS for Desire](http://forum.xda-developers.com/showthread.php?t=1355660)
* [Chromium](http://www.htcmania.com/showthread.php?t=309312)
* [AOKP for Bravo - Beta 3! - Stock HBOOT only](http://forum.xda-developers.com/showthread.php?t=1484648)
* [Cómo flashear un Recovery en HTC Desire](http://www.htcmania.com/mediawiki/index.php/C%C3%B3mo_flashear_un_Recovery#Actualizar_el_Recovery_con_fastboot)

#### Proceso de instalación de ROM

1. Hacer S-OFF con [revolutionary](http://revolutionary.io/) (ejecutarlo con sudo).
2. Hacer root siguiendo los pasos de [El Androide Libre](http://www.elandroidelibre.com/2011/08/revolutionary-finalmente-trae-el-root-y-s-off-en-1-click-para-htc-desire-wildfire-sensation-evo-y-muchos-ms.html).
3. Instalar el HBOOT Bravo CM7 r2 de [AlphaRev](http://alpharev.nl/). Se hace descargando el fichero de la columna "PB99IMG", renombrándolo a “PB99IMG.zip”, copiándolo a la raíz de la SD y reiniciando en modo HBOOT.
4. Borrar caché, Data y Dalvik.
5. Formatear SD desde Recoveery con 1024MB para la ext y 0MB para el swap.
6. Instalar InsertCoin de tipo CM7: [http://insertcoin-roms.org/](http://insertcoin-roms.org/)

### Samsung Galaxy Note II

#### Enlaces

* [DN4 (Ditto Note 4) ROM from E-team](http://forum.xda-developers.com/showthread.php?t=2504016)
* [Electron Team (creadores de DN3 y DN4)](http://electron-team.com/)

### Sony Xperia T

#### Menú de servicio

```
*#*#7378423#*#*
```

#### Modos de Reset

* Volume Up + POWER (for 10 seconds) -> Battery reset [Device will vibrate once]
* Volume Up + POWER (for 15 seconds) -> Hard reset [Device will vibrate three times]

#### Dispositivos de almacenamiento 4.0

* /mnt/sdcard: Memoria interna (16GB)
* /mnt/ext_card: Tarjeta SD

#### Dispositivos de almacenamiento 4.1

* /mnt/int_storage        10.9G     2.6G     8.3G   4096
* /storage/sdcard0        10.9G     2.6G     8.3G   4096
* /storage/sdcard1        29.7G     2.7G    27.0G   32768

#### Historial firmware

| Fecha | Versión |
|:----- |:------- |
| 2013-07-02 | 9.1.A.1.141 |
| 2014-04 | 9.2.A.1.199 |

#### Enlaces

* [Unlock your boot loader](http://developer.sonymobile.com/unlockbootloader/unlock-yourboot-loader/)
* [Full rooting guide for xperia t lt30p build 7.0.A.3.195](http://forum.xda-developers.com/showthread.php?t=2000188)
* [Xperia Roms](http://uploaded.net/f/bd4cif)
* [Creacion de perfiles completos con Smart Tags + NFC Task Launcker + Tasker](http://www.htcmania.com/showthread.php?t=371570)
* [¿A cuantos os ha fallado el Xperia T? y soluciones.](http://www.htcmania.com/showthread.php?t=562022)
* [Servicio Técnico](http://www.ststella.es/reparaciones.asp)
* [Flash tool for Xperia™ devices](http://developer.sonymobile.com/downloads/tool/flash-tool-for-xperia-devices/)
* [Lista de Firmwares certificados](http://www.ptcrb.com/vendor/complete/view_complete_request_guest.cfm?modelid=21834)
* [Xperia T software updates](http://www.sonymobile.com/es/software/phones/xperia-t/)
* [TWRP 2.7 - Sony Xperia T page](http://teamw.in/project/twrp2/143)
* [[4.4 ROM Flash] bypass set_metadata_xxx fails](http://forum.xda-developers.com/showthread.php?t=2532300&__utma=248941774.1292881775.1408312691.1408813670.1409161154.3&__utmb=248941774.1.10.1409161154&__utmc=248941774&__utmx=-&__utmz=248941774.1409161154.3.3.utmcsr=android.stackexchange.com%7Cutmccn=(referral)%7Cutmcmd=referral%7Cutmcct=/questions/62985/how-do-i-install-cyanogenmod-11-on-a-samsung-galaxy-tab-2-gt-p5113/62986&__utmv=-&__utmk=239226752)
* [Disable Fast dormancy on sony smarthphones](http://forum.xda-developers.com/showthread.php?t=2382680)
* [[MOD] Speakerphone whistle fix + volume boost](http://forum.xda-developers.com/showthread.php?t=2783028)
* [Charging a dead Xperia T](http://forum.xda-developers.com/showpost.php?p=56886609&postcount=243)

#### ROMs

* [CyanogenMod](http://download.cyanogenmod.org/?device=mint)
* [FreeXperia Project](http://fxpblog.co/cyanogenmod/cyanogenmod-11/)
* [OmniROM](http://forum.xda-developers.com/showthread.php?t=2525714)
* [ROM(Unlocked)(KITKAT) Plain AOSP for Xperia T](http://forum.xda-developers.com/showthread.php?t=2729509)
* [ROM(4.4.4)(T/TX) Carbon Rom KK Unofficial](http://forum.xda-developers.com/showthread.php?t=2708186)
* [ROM(T)(4.3) Ultimate PureXT v4.5](http://forum.xda-developers.com/showthread.php?t=2691629)  (**)
* [ROM(4.3)(T)(LB/UB) OMeGa v2.2](http://forum.xda-developers.com/xperia-t-v/t-development/rom-omega-v1-0-26-10-2014-t2918750)  (**)
* [DooMKernel {JB}(v12)(20140604)](http://forum.xda-developers.com/showthread.php?t=2170580)
* Stock ROMs para el Xperia T: [HTCMania](http://www.htcmania.com/showthread.php?t=520551) - [XDA](http://forum.xda-developers.com/showthread.php?t=2648320)
* [GAPPS(4.4.x) OFFICIAL Up-to-Date PA-GOOGLE APPS (All ROM's) (2014-08-18)](http://forum.xda-developers.com/showthread.php?t=2397942)

#### Repuestos

* [Tapa posterior](http://www.amazon.co.uk/gp/offer-listing/B00DEDYERA/ref=dp_olp_refurbished?ie=UTF8&condition=refurbished&m=A1OQZT23BTDFUS&qid=1381596165&sr=1-1)

#### Instrucciones de instalación de ROMs

1. power off the phone:
2. hold vol+ and plug usb to boot into fastboot (blu led)
3. fastboot flash boot boot.img (from cm10 zip)
4. fastboot reboot
5. enter recovery, on boot led will be violet for 3'', during this period press vol+
6. flash rom zip
7. flash gapps zip
8. wipe
9. reboot

#### Desactivar fast-dormancy (pepephone MCC= 214, MNC= 06)

In /system/etc/fast-dormancy/fd_custm_conf.txt replace the 0s with your MNC and MCC from your APN setting.

#### Solucion al problema de permisos de la memoria interna ([fuente](http://forum.xda-developers.com/showthread.php?t=2794704))

```bash
$ su
# cd /mnt/media_rw
# busybox chown -R 2800:2800 sdcard0
# chmod 0770 sdcard0
```

### Sony Xperia U

#### Menú de servicio

```
*#*#7378423#*#*
```

#### Enlaces

* [Unlock your boot loader](http://developer.sonymobile.com/unlockbootloader/unlock-yourboot-loader/)
* [DESBLOQUEAR COMPLETAMENTE tu Xperia y poder ROOTEARLO★Aplicar MODS★ROMS](http://www.htcmania.com/showthread.php?t=396318)
* [Sobre el Bootloader](http://comunidad.movistar.es/t5/Ayuda-Gestiones-Contratos-y/Desbloquear-Bootloader-Sony-Xperia-S/m-p/640867#M85761)

#### ROMS

* [XDA-Developers Rom List](http://forum.xda-developers.com/xperia-u/#romList)
* [(ROM)(UB)(4.4.4)(W37-S4)(XperiaSTE Team) CyanogenMod 11.0](http://forum.xda-developers.com/xperia-u/u-development/rom-cyanogenmod-11-0-t2528466)

### Rikomagic MK802-IIIs

#### Enlaces

* [PicUntu](http://ubuntu.g8.net/)
* [MK802 Ubuntu Images with optional Droidmote](https://www.miniand.com/forums/forums/development/topics/install-ubuntu-linux-12-04-now-including-droidmote)
* [MK802 IIIs en AndroidPC.es](http://androidpc.es/blog/tag/mk802-iiis/)
* [ROMS no oficiales funcionando al 100% para meter en los MK802IIIs](http://foro.androidpc.es/showthread.php?tid=130)
* [Foro MK802-IIIS Rikomagic en AndroidPC.es](http://foro.androidpc.es/forumdisplay.php?fid=53)
* [Las mejores tiendas de aplicaciones alternativas a Google Play](http://www.xatakandroid.com/play-store/las-mejores-tiendas-de-aplicaciones-alternativas-a-google-play)
* [Configuraciones para mandos y método para cambiar funciones de las teclas](http://foro.androidpc.es/showthread.php?tid=120)

#### ROMs

* [NEOTV](http://androidpc.es/blog/2013/04/28/neotv-mk802iiis-18/)
* [Rom Finless 1.5 para MK802-IIIs](http://androidpc.es/blog/2013/01/09/rom-imito-finless-15/)
* [Finless rom 1.8 para MK802-III y UG802](http://androidpc.es/blog/2013/03/11/finless-rom-1-8-para-mk802-iii-ug802/)
* [Rom Finless 2.0 con Android 4.2.2 para MX1/MX2 y MK802-IIIS con BT](http://androidpc.es/blog/2013/05/22/finless-2-0-android-4-2-2-mx2-y-mk802-iiis-bt/)

#### Software

* [RetroArch, el Todo-en-1 de emuladores: Playstation, SNES, GBA y muchos más](http://www.elandroidelibre.com/2013/02/retroarch-el-todo-en-1-de-emuladores-playstation-snes-gba-y-muchos-mas.html)
* [Sopcast](http://www.sopcast.com/download/android.html)
* [Null Input Method](https://play.google.com/store/apps/details?id=com.apedroid.hwkeyboardhelperfree)

#### TDT

* [Televisión conectando un USB-TDT en tu AndroidPC con chip RK3066](http://androidpc.es/blog/2012/12/21/television-conectando-un-usb-tdt-en-tu-androidpc-con-chip-rk3066/)

#### Hardware

* [Adaptador USB LAN + USB HUB](http://www.playocio.net/adaptador-usb-lan-usb-hub-3-puertos-usb-p-4649.html)

#### Flasheo de Firmware oficial

1. Bajar la última versión de la [página oficial](http://www.rikomagic.co.uk/support.html).
2. En el paquete recien bajado (en el directorio 0121-IIIS8B\0121-IIIS8B\RKBatchTool1.5en\Driver) se encuentran los drivers de modo Flashboot para Windows. Para Windows8 se pueden encontrar [aquí](http://foro.androidpc.es/showthread.php?tid=142).
3. Conectar un cable microUSB-USB a la ranura OTG. El otro extremo (USB) lo introducimos en un puerto libre del ordenador mientras a la vez con un palillo o clip desenrollado pulsamos el botón de reset que se adivina por una de las rejillas de ventilación. Si Windows muestra un bocadillo pidiendo drivers, le damos a elegir la ruta en disco y apuntas al directorio comentado anteriormente que contenga la versión de los drivers que nos interese. Si Windows no reacciona habrá que entrar en el Administrador de dispositivos y forzar la actualización sobre alguno de los "Dispositivos desconocidos" que veamos. En el directorio "0121-IIIS8B\0121-IIIS8B" del paquete con el firmware viene una explicación detallada (incluye fotos) del proceso de instalación de los drivers y de la conexión al ordenador por el puerto OTG mientras se pulsa el reset.
4. Una vez instalados los drivers lo mejor será reiniciar Windows.
5. Volvemos a conectar el MK802 por el puerto OTG mientras mantenemos pulsado el botón de reset como en el paso 3.
6. Abrimos la aplicación de flasheo (RKBatchTool). Deberíamos ver en azul el cuadrado inferior izquierdo marcado con un 1. Si no es así es que el proceso de instalación de drivers y/o conexión del MK802 al PC no ha ido bien.
7. Seleccionamos el fichero con la imagen de la ROM (extensión .img).
8. Pulsamos el botón "Upgrade".
9. Esperamos a que el proceso termine satisfactoriamente. Puede tardar entre 1 y 3 minutos.

#### Flasheo ROM Finless

1. Bajar el paquete de [aquí](http://www.freak-tab.de/finless/imito_mx1_finless_1_5.zip).
2. Instalar los drivers Windows (ver pasos en instalación ROM oficial).
3. Descomprimir el paquete con la ROM.
4. Conectar el Rikomagic al PC por USB como comentamos en el otro procedimiento, es decir conectando al puerto OTG y mientras se mantiene presionado el microbotón de reset oculto entre las rendijas de ventilación.
5. Abrir el programa "ROM Flash Tool.exe" que hay en el primer nivel de directorios del paquete que hemos descomprimido.
6. En la ventana que aparece se ve una serie de ficheros que se toman del subdirectorio "FinlessROM". Dentro de ese directorio hay varias opciones para los ficheros "parameter", "kernel" y "boot". El primero yo lo dejaría como viene por defecto. Los ficheros "kernel" y "boot" tienen que ir parejos. Hay dos versiones de cada, una para 720p y otra para 1080p. Recomiendan la 720p y por la potencia del Rikomagic (que va justito para los 1080p) yo también creo que no merece la pena el 1080p. Como por defecto viene seleccionado el 1080p, hay que cambiarlo. Para ello hay que hacer click en la fila correspondiente de la última columna, la que tiene el rótulo "...".
7. Antes de empezar a flashear hay que comprobar que el programa se comunica con el Rikomagic. Para ello tiene que indicar abajo del todo en letra grande "Found RKAndroid...". Si pone "No Found RKAndroid rock usb" es que hay algún problema con la conexión o los drivers. Simplemente volver a intentar la conexión (pulsando el botoncito).
8. Le damos al botón "Erase NAND (IDB)" y luego cuando ese proceso termine le damos a "Flash ROM".

### ZTE Skate / Orange Montecarlo

#### Enlaces

* [Backup original ROM?](http://www.modaco.com/topic/351269-backup-original-rom/?p=1892809)
* [How to Install CyanogenMod on ZTE Skate ("skate")](http://wiki.cyanogenmod.org/w/Install_CM_for_skate)
* [Tutorial Como instalar ClockWorkMod Recovery,Rootear e instalar roms en ZTE skate/OMC](http://www.htcmania.com/archive/index.php/t-643421.html)
* [[ROM][ZTE Skate] H3 Holo (Dolby Audio + Linaro optimized kernel + frandom + ROW I/O scheduler)](http://www.modaco.com/topic/366117-romzte-skate-h3-holo-dolby-audio-linaro-optimized-kernel-frandom-row-io-scheduler/)

### HTC Wildfire

#### Modos de arranque

* Se arranca en HBOOT manteniendo el Volume- mientras se pulsa Power.

#### Enlaces

* [Las mejores ROMs para HTC Wildfire](http://www.google.com/url?q=http%3A%2F%2Fwww.elandroidelibre.com%2F2011%2F08%2Flas-mejores-roms-para-htc-legend-wildfire-y-tattoo.html&sa=D&sntz=1&usg=AFQjCNHspaT7ir10u60GonFdKd_75YiOlQ)
* [S-OFF y rootear para instalar Rom](http://www.foro.htcmania.com/showthread.php?t=228979)
* [HTC Wildfire: Full Update Guide](http://wiki.cyanogenmod.com/wiki/HTC_Wildfire:_Full_Update_Guide)
* [Nuestras 4 ROM favoritas del 2011 para la HTC Desire](http://4ndroid.com/nuestras-4-rom-favoritas-del-2011-para-la-htc-desire/)
* [Unlock Bootloader (HTC oficial)](http://www.htcdev.com/bootloader/)

### HTC Wildfire S

#### Enlaces

* [Unlock Bootloader (HTC oficial)](http://www.htcdev.com/bootloader/)
* [HTC Wildfire S ROMs](http://theunlockr.com/category/roms-2/android-roms-2/htc-wildfire-s-roms/)
* [CM9-marvel-KANG](http://forum.xda-developers.com/showthread.php?t=1444554)
* [MIUI V4 |CM9|ICS 4.0.3|](http://forum.xda-developers.com/showthread.php?t=1533696)
* [Nuevo método para conseguir ROOT en el HTC Wildfire S y algunas ROMs](http://www.elandroidelibre.com/2012/03/nuevo-mtodo-para-conseguir-root-en-el-htc-wildfire-s-y-algunas-roms.html)
* [CyanogenMod 9.0.0-RC0-Marvel-Alpha2](http://www.htcmania.com/showthread.php?t=376284)

### Motorola Milestone 2

#### Modos de arranque

* Se arranca en Recovery encendiendo mientras se mantiene pulsada la tecla X del teclado físico. Luego, en Froyo hay que pulsar @. En Gingerbread las dos teclas de volumen a la vez.
* Se arranca en HBOOT encendiendo mientras se mantiene pulsada la tecla de cursor "Arriba" del teclado físico.

#### Basebands

* Teléfono original: EPU93_U_00.60.00
* ICS 4.0.4 2012-08-15: EPU93ST2_U_03.0C.01

#### Kernels

* 2.3.4: 2.6.32.9-g7d2667a
* ICS 4.0.4 2012-08-15: 2.6.32.9-g7d2667a
* Recomendado por Tezet para JB 4.1.1:
    * 2.6.32.9-g5db7937
    * a17140@zch68lnxdroid63 #1
    * Fri Sep 16 17:57:00 CST 2011

#### Enlaces

* [sbf_flash: Utilidad Linux/Mac para flashear una ROM](http://blog.opticaldelusion.org/search/label/sbf_flash)
* [Motorola Android Software Upgrade News](https://supportforums.motorola.com/community/manager/softwareupgrades)
* [Miledropedia](http://www.droid-developers.org/wiki/Main_Page)
* [SBF Files](http://and-developers.com/sbf)
* [Milestone2 en XDA-developers](http://forum.xda-developers.com/archive/index.php/f-958.html)
* [Milestone 2 Actualizacion Gingerbread, CyanogenMOD y MIUI](http://www.taringa.net/posts/celulares/12089987/Milestone-2-Actualizacion-Gingerbread_-CyanogenMOD-y-MIUI.html)
* [Rootear Motorola Milestone 2](http://www.grupoandroid.com/topic/11683-rootear-motorola-milestone-2/)
* [CWM: Clockworkmod Recovery - Droid 2 Bootstrapper](http://www.grupoandroid.com/topic/10293-mod-cwm-clockworkmod-recovery-droid-2-bootstrapper/)
* [Hacer backup sólo de System](http://motomilestone2.com/modding/nandroid-backup.aspx)
* [Cyanogenmod 7.1 for Motorola Milestone 2](http://forum.xda-developers.com/showthread.php?t=1338183)
* [Cyanogenmod 7.1 for Motorola Milestone 2](http://forum.xda-developers.com/showthread.php?t=1239778)
* [Cyanogenmod 9 for Motorola Milestone 2](http://forum.xda-developers.com/showthread.php?t=1374497)
* [MOTO Milestone 2 » ROM MIUI 1.12.9](http://miui.es/moto-milestone-2-%C2%BB-rom-miui-1-12-9)
* [The Noob Handbook for Bricked Phones](http://forum.xda-developers.com/showthread.php?p=21819093)
* [Instalación verificada de CM7](http://forum.xda-developers.com/showpost.php?p=21823320&postcount=13)
* [HOW TO install CyanogenMod/MIUI to your phone](http://forum.xda-developers.com/showthread.php?t=1310641)
* [ROM Argen2Stone 2.7 RE (Based on Ms2Ginger 2.0)](http://forum.xda-developers.com/showthread.php?t=1336588)
* [How to install Argen2Stone?](http://forum.xda-developers.com/showthread.php?t=1473263)
* [Titanium Backup, The Easy Way!](http://forums.androidcentral.com/verizon-galaxy-nexus-rooting-roms-hacks/192528-how-tibu-easy-way.html)
* [MIUI 2.5.25 GB 2.3.7 + ICS Multilanguage for Milestone 2!](http://forum.xda-developers.com/showthread.php?t=1258073)
* [CyanogenMod 10 for Motorola Milestone 2 (Android 4.1.1)](http://forum.xda-developers.com/showthread.php?t=1827801) !!!
* [CyanogenMod 9 for Motorola Milestone 2 (Android 4.0.4)](http://forum.xda-developers.com/showthread.php?t=1623385)
* [MIUI v4 2.7.27](http://forum.xda-developers.com/showthread.php?t=1614328)
* [Baseband switcher](http://forum.xda-developers.com/showthread.php?p=29580375&highlight=baseband#post29580375)
* [Please come in,if your ms2 can't contect the GSM](http://forum.xda-developers.com/showthread.php?t=1182050)
* [Kernel downgrade method for EU/BR/AR Gingerbread (only for BL=3)](http://forum.xda-developers.com/showthread.php?t=1497263)
* [Multipack (alternativa a gapps)](http://www.elandroidelibre.com/2012/12/multipack-google-apps-y-optimizaciones-para-jelly-bean.html)

#### Instalación SBF

1. Bajar el SBF de [aquí](http://and-developers.com/sbf:milestone2).
2. Aplicarlo con: `sudo sbf_flash rom.sbf`
3. Rootear con [DoomLoRD](http://forum.xda-developers.com/showthread.php?t=1321582).
4. Instalar [bootmenu](http://forum.xda-developers.com/showthread.php?t=1196590) con droid2bootstrap sacado de [aquí](http://forum.xda-developers.com/showthread.php?t=1310641).

#### Instalación de [ROM JB 4.1.1 de tezet](http://forum.xda-developers.com/showthread.php?t=1827801)

* Hacer el downgrade del kernel flasheando el sbf que hay [aquí](http://forum.xda-developers.com/showthread.php?t=1497263)
* Al reiniciar debería entrar en CWM
* Hacer wipe de cahé
* Hacer wipe de Dalvik
* Instalar el Kernel CH GB que indica tezet [aquí](http://forum.xda-developers.com/showthread.php?t=1827801)
* Instalar la ROM
* Hacer wipe de cahé
* Hacer wipe de Dalvik

### Sony Ericsson Xperia X8

#### Enlaces

* [Root Sony Ericsson Xperia X8 With SuperOneClick](http://www.addictivetips.com/mobile/root-sony-ericsson-xperia-x8-with-superoneclick/)
* [How To Install Latest xRecovery to Sony Ericsson Xperia X10](http://www.addictivetips.com/mobile/how-to-install-latest-xrecovery-to-sony-ericsson-xperia-x10/)
* [CM7.1.0 FXP043 - FreeXperia Project](http://forum.xda-developers.com/showthread.php?t=973753)
* [Tutorial para reparar/desbrickear terminales Sony Ericsson](http://android.scenebeta.com/tutorial/tutorial-para-reparardesbrickear-terminales-sony-ericsson)
* [How to install GingerXperiaV8 on Sony Ericsson X8](http://www.youtube.com/watch?v=AVbARESQvcw)
* [GingerDX para Xperia X8](http://android.scenebeta.com/noticia/gingerdx-para-xperia-x8)
* [GingerDX](http://forum.xda-developers.com/showthread.php?t=1188486)
* [Como instalar un Rom a un Xperia X8](http://www.librosytutoriales.org/como-instalar-cooked-rom-xperia-x8)
* [Las mejores ROMs para Sony Ericsson Xperia X8](http://www.elandroidelibre.com/2012/02/las-mejores-roms-para-samsung-galaxy-ace-sony-ericsson-xperia-x8-y-lg-optimus-black.html)
* [How to rescue our bricked phone](http://forum.xda-developers.com/showthread.php?t=1011071)
* [Hard brick warning - read before boot loader unlock](http://forum.xda-developers.com/showthread.php?t=1481630)
* [SE Tweaker Tool v4.0 (16/2/12) Unlock Bootloader+Kernel Guide](http://forum.xda-developers.com/showthread.php?t=1462278)
* [Bootloader and kernel guide](http://forum.xda-developers.com/showthread.php?t=1254225)
* [Desbloquear el Bootloader para Novatos X8](http://www.grupoandroid.com/topic/29153-desbloquear-el-bootloader-para-novatos-x8-%E2%94%82w8-%E2%94%82-x10-mini-%E2%94%82-x10-mini-pro/)
* [Unlocking the boot loader (Oficial)](http://unlockbootloader.sonymobile.com/)

#### Debrick

* [Phone-lab Barcelona](http://www.gsmspain.com/foros/showthread.php?s=&threadid=306742)
* [Movical Santiago de Compostela](http://www.movical.net/)
* [Liberar.es](http://www.liberar.es/)
* [http://forum.xda-developers.com/showthread.php?t=1292705&page=2](http://forum.xda-developers.com/showthread.php?t=1292705&page=2)
* [http://forum.xda-developers.com/showthread.php?t=1399381&page=2](http://forum.xda-developers.com/showthread.php?t=1399381&page=2)
* [http://support.setool.net/showthread.php?3-UPDATES-AND-NEWS/page23](http://support.setool.net/showthread.php?3-UPDATES-AND-NEWS/page23)
* [http://forum.xda-developers.com/showthread.php?t=986697&highlight=flash+tool](http://forum.xda-developers.com/showthread.php?t=986697&highlight=flash+tool)
* [ Problem unlocking X8 with new bootloader [Solved]](http://www.gsmcure.com/forum/showthread.php?t=2644)
* [Solución en el hilo de XDA "Hard brick warning - read before boot loader unlock"](http://forum.xda-developers.com/showpost.php?s=3bcbbefae118eb0828e200c0c5449608&p=27942435&postcount=205)
* [Xperia testpoint instructions and pictures](http://www.gsmcure.com/forum/showthread.php?t=2329)
* [Unlock Bootloader.Test Point](http://forum.xda-developers.com/showthread.php?t=1730874)
* [Libera BOOTLOADER POR 15€ OMNIUS O S1TOOL GRATIS](http://www.htcmania.com/showthread.php?t=330743)

## Técnicas varias

### Conectar el mando de la PS3

([Fuente](http://fandroides.com/conecta-tu-mando-de-la-ps3-con-tu-dispositivo-android-mediante-wireless))

#### Requisitos

*  Nuestro dispositivo Android
*  Deberemos ser Root
*  Dualshock 3 (Sixaxis)
*  [Sixaxis Compatibility Checker](https://play.google.com/store/apps/details?id=com.dancingpixelstudios.sixaxiscompatibilitychecker)
*  [Sixaxis Controller](https://play.google.com/store/apps/details?id=com.dancingpixelstudios.sixaxiscontroller)
*  SixaxisPairTool, que puedes descargarlo desde [aquí](http://www.mediafire.com/download/p2bl654bw6qn3v6/SixaxisPairToolSetup-0.2.3.exe).

#### Configuración

 1.  Abrimos el **Sixaxis Compatibility Checker**
 2.  Nos aparecerá un mensaje y pulsaremos sobre **OK**
 3.  Pulsaremos sobre Start y le daremos permisos de Superusuario
 4.  Si nuestro dispositivo es compatible recibiremos un mensaje diciéndonos si nuestro dispositivo es compatible. En caso que de que así sea pulsamos sobre Stop y salimos de la aplicación.
 5.  En caso de no recibir el mensaje de compatibilidad podemos para aquí o seguir y probar suerte ;-)
 6.  Ahora abrimos **Sixaxis Controller App** y clicamos sobre start. Le daremos permisos de superusuario al igual que a la otra aplicación. Entonces obtendremos una dirección de Bluetooth local.
 7.  Abriremos en nuestro ordenador el **Sixaxis Pair Tool** y la instalaremos. Después la abriremos como administrador (botón derecho sobre el icono).
 8.  Con el programa abierto enchufaremos el Sixaxis en nuestro PC mediante el cable USB.
 9.  En el Sixaxis Pair Tool veremos una caja vacía. Ahí escribiremos la dirección Bluetooth Local que habíamos obtenido antes.
 10.  Cuando esto esté hecho pulsaremos sobre Update y veremos como la dirección se ha actualizado.
 11.  Desconectaremos el Sixaxis de nuestro PC.
 12.  Pulsaremos sobre el botón PS y veremos que ocurre…
 13.  Nuestro Sixaxis ya debería estar emparejado con nuestro dispositivo Android.


### ADB en Linux y arrancar settings

1. Instalar el SDK.
2. Sacar id de fabricante de lsusb (http://bradchow.wordpress.com/2009/02/16/adb-on-windows-and-ubuntu-linux/) y crear rule udev.
3. Reiniciar adb server:
  * `adb kill-server`
  * `sudo adb start-server`
  * `adb devices`
4. Ejecutar:
  * `sudo adb shell`
  * `am start -a android.intent.action.MAIN -n com.android.settings/.Settings`

### Montar system en rw:

```bash
# mount -o remount,rw /system
# cd /system/app
# mount -o remount,ro /system
# reboot recovery
```

### Desinstalar aplicaciones de sistema sin root

[Fuente](https://elandroidelibre.elespanol.com/2017/07/desactiva-cualquier-aplicacion-movil.html)

1. Activa el modo de depuración en tu Android.
2. Conecta tu Android al ordenador por USB y acepta la clave RSA.
3. Abre una ventana de comandos y escribe `adb devices` sin las comillas. Tu dispositivo debería detectarse apareciendo a modo de código.
4. Una vez conectado escribe `adb shell`.
55. Ahora necesitas eliminar una a una las aplicaciones que desees. Utiliza App Inspector para saber el nombre del paquete.
6. Pega este código en la ventana de comandos: `pm uninstall -k -user 0 nombre.del.paquete`. Sin las comillas y cambiando “nombre.del.paquete” por el de la aplicación que deseas (Google Chrome es `com.android.chrome`, por ejemplo).
7. Acepta el comando y si el ordenador te devuelve un `Success` es que se ha eliminado de manera satisfactoria.
