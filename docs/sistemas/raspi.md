---
layout: default
permalink: /sistemas/raspi.html
---

# Raspberry Pi

## Enlaces

* [Gestión usuarios](http://www.raspberrypi.org/documentation/linux/usage/users.md)
* [IP Estática](http://www.electroensaimada.com/ip-estaacutetica.html)
* [Instalación cliente NO-IP](http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client/)
* [Ultimate Raspberry Pi Configuration Guide](http://www.instructables.com/id/Ultimate-Raspberry-Pi-Configuration-Guide/?ALLSTEPS)
* [GitPi: A Private Git Server on Raspberry Pi](http://www.instructables.com/id/GitPi-A-Private-Git-Server-on-Raspberry-Pi/all/?lang=es)
* [PiKISS para Raspberry Pi](http://misapuntesde.com/post.php?id=409): Un puñado de scripts con menú para hacerte la vida más fácil
* [Java JDK para ARM](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-arm-downloads-2187472.html)
* [Cylon.js para Raspberry Pi](http://cylonjs.com/documentation/platforms/raspberry-pi/)
* [BerryBoot](http://www.berryterminal.com/doku.php/berryboot): Menú de arranque que permite arrancar varios sistemas instalados en la propia SD, en un disco duro/pendrive externo o en un almacenamiento en red (NAS).
* [An A to Z Beginners Guide to Installing RetroPie on a Raspberry Pi](http://supernintendopi.wordpress.com/)
* [How to install Oracle Java 8 in Debian via repository (JDK8)](http://www.webupd8.org/2014/03/how-to-install-oracle-java-8-in-debian.html)
* [Adafruit - Learn Raspberry Pi](https://learn.adafruit.com/category/learn-raspberry-pi)
* [Tutorials - The MagPi MagazineThe MagPi Magazine](https://www.raspberrypi.org/magpi/tutorials/)
* [Read-Only Raspberry Pi](https://learn.adafruit.com/read-only-raspberry-pi/)
* [Read-only Raspberry PI with Jessie](https://petr.io/en/blog/2015/11/09/read-only-raspberry-pi-with-jessie/)
* [Imágenes berryboot](https://berryboot.alexgoldcheidt.com/images/)

## Distribuciones

* [Binary Emotions Slideshow](http://www.binaryemotions.com/digital-signage/raspberry-slideshow/): Slideshow de imágenes/vídeos.
* [Binary Emotions Digital Signage](http://www.binaryemotions.com/digital-signage/raspberry-digital-signage/): Slideshow de páginas web.
* [DietPi - Lightweight justice for your SBC](http://dietpi.com/)
* [Flint OS](https://flintos.io/): Versión de ChromeOS con soporte Android.
* [PiMAME](http://pimame.org/): Raspbian con un frontend para lanzar emuladores.
* [Lakka](http://www.lakka.tv/): Lakka is a lightweight Linux distribution that transforms a credit card sized computer into a full blown emulation console.
* [RetroPie](http://blog.petrockblock.com/retropie/)
* [batocera.linux](https://batocera-linux.xorhub.com/): Para construir Recalbox.

## Software

* [Pi-Hole](https://pax0r.com/bloquea-publicidad-molesta-con-pi-hole/): DNS que filtra dominios marcados por la comunidad como "molestos" y conseguiremos una navegación mas limpia y rápida.
* [PiVPN](http://www.pivpn.io/)

## Hardware

* [Lista de hardware verificado](http://elinux.org/RPi_VerifiedPeripherals)
* [Quick2Wire](http://Quick2Wire.com)
* [ESP8266 Serial Esp- 01](http://espressif.com/en/products/esp8266/): Módulo Wifi [por 2,25€](http://es.aliexpress.com/item/2PCS-ESP8266-Serial-Esp-01-WIFI-Wireless-Transceiver-Module-Send-Receive-LWIP-AP-STA/32232009463.html?recommendVersion=1) recomendado por [Fernando](https://twitter.com/m_trombone). [Listado de recursos](http://www.xess.com/blog/esp8266-resources/). Tutorial [conexión a Raspi](http://www.extragsm.com/blog/2014/12/03/connect-esp8266-to-raspberry-pi/).
* [TK2050 50W+50W Dual Channel Class T HIFI Stereo Audio Amplifier Board DC12V 24V](http://www.ebay.com/itm/TK2050-50W-50W-Dual-Channel-Class-T-HIFI-Stereo-Audio-Amplifier-Board-DC12V-24V-/181441180570): Recomendado por Fernando Oroquieta.
* [Using a Console Cable](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable?view=all)
* [Adaptador Wifi (RTL8188CUS)](http://www.raspipc.es/public/home/index.php?ver=tienda&accion=verArticulo&idProducto=1079)
* [Adaptador TDT Conceptronic C08-096 (RTL2832)](http://www.amazon.es/Conceptronic-C08-096-receptor-Dvb-T-radio/dp/B003KCKERE)
* [Receptor infrarrojos](https://energenie4u.co.uk/catalogue/category/PiMote)
* [TP4056 DIY 1A Micro USB Li-Ion Battery Charging Board Charger Module](http://www.dx.com/p/tp4056-diy-1a-micro-usb-li-ion-battery-charging-board-charger-module-blue-373990): Cargador de batería.
* [PowerBoost 500 Charger - Rechargeable 5V Lipo USB Boost](http://www.adafruit.com/product/1944): Alimentación ininterrumpida con batería y gestor de carga.
* [UA0053 ADAPTADOR LOGILINK USB 2.0 AUDIO 5.1](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=255195038&cPath=1295): Adaptador audio USB.
* [2-Channel 3W PAM8403 Audio Amplifier Board](http://www.dx.com/p/2-channel-3w-pam8403-audio-amplifier-board-red-146300): Amplificador audio 3W.
* [Stereo 2.8W Class D Audio Amplifier - I2C Control AGC](http://www.adafruit.com/product/1712): Amplificador audio 2.8W con control I2C.

## Comandos útiles

### Comprobar asignaciones de cliente No-IP

Las asignaciones dejan marca en el log `syslog`:

```bash
edumoreno@raspi-git /var/log $ sudo fgrep noip syslog
Oct 16 12:18:57 raspi-git noip2[2165]: v2.1.9 daemon ended.
Oct 16 12:19:19 raspi-git noip2[2186]: v2.1.9 daemon started with NAT enabled
Oct 16 12:19:35 raspi-git noip2[2186]: eduardofilo.no-ip.biz set to 88.19.216.95
Oct 16 12:53:06 raspi-git noip2[2186]: v2.1.9 daemon ended.
Oct 16 13:15:23 raspi-git noip2[2217]: v2.1.9 daemon started with NAT enabled
Oct 16 13:15:25 raspi-git noip2[2217]: eduardofilo.no-ip.biz was already set to 88.19.216.95.
```

### Utilidad de configuración

```bash
$ sudo raspi-config
```

### Backup de la SD (comprimiendo al vuelo)

```bash
$ #Backup:
$ sudo dd if=/dev/mmcblk0 bs=2M | pv | gzip -9 - > Rpi_8gb_backup.img.gz
$ #Backup sólo de 4GB (si por ejemplo la tarjeta es más grande pero no aprovecha toda la superficie)
$ sudo dd if=/dev/mmcblk0 bs=2M count=2048 | pv -s 4g | gzip -9 - > Rpi_4gb_backup.img.gz
$ #Restauración (comprimido con gzip):
$ gunzip Rpi_8gb_backup.img.gz -c | pv | sudo dd of=/dev/mmcblk0 bs=2M
$ #Restauración (comprimido con xz):
$ xzcat Rpi_8gb_backup.img.xz | pv | sudo dd of=/dev/mmcblk0 bs=2M
$ #Restauración (comprimido con zip):
$ unzip -p Rpi_8gb_backup.zip | pv | sudo dd of=/dev/mmcblk0 bs=2M
```

Para hacer un backup parcial los cálculos se harían así. Primero sacamos los datos de la estructura de la tarjeta con `fdisk`:

```bash
$ sudo fdisk -l /dev/mmcblk0
Disco /dev/mmcblk0: 14,4 GiB, 15502147584 bytes, 30277632 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0xa125a0dc

Dispositivo    Inicio Comienzo    Final Sectores Tamaño Id Tipo
/dev/mmcblk0p1            8192    96663    88472  43,2M  c W95 FAT32 (LBA)
/dev/mmcblk0p2           98304 15550463 15452160   7,4G 83 Linux
```

Aquí vemos que cada sector ocupa 512 bytes. Nos fijamos en el último sector utilizado que en este caso es 15550463. Multiplicando este sector por el tamaño del sector (y sumando 1 al número de sectores por si empiezan a contar en 0) obtendremos el número de bytes que tendremos que copiar. Como el block size que vamos a utilizar es 2MB tendremos que truncar por lo alto (también servirá de medida de seguidad). Los cálculos en este caso resultarían:

    (15550463 + 1) (sector) * 512 (Byte/sector) / 1024 (Byte/KB) / 1024 (KB/MB) / 2 (MB/bloque) = 3796,5 bloques

Por tanto en este caso copiaremos 3797 bloques para cubrir esos 15550464 sectores.

### Backup de la SD (comprimiendo al vuelo y diviendo en trozos el fichero resultante)

```bash
$ #Backup:
$ sudo dd if=/dev/mmcblk0 bs=2M | pv | gzip -9 - | split --bytes=2G - Rpi_8gb_backup.img.gz.part_
$ #Restauración:
$ cat Rpi_8gb_backup.img.gz.part_* | gunzip -c | pv | sudo dd of=/dev/mmcblk0 bs=2M
```

### Control de progreso durante flasheo

```bash
$ sudo pkill -USR1 -n -x dd
```

Como alternativa se puede instalar el comando `dcfldd` para sustituir a `dd`, con lo que obtendremos una indicación del progreso de la copia. `dcfldd` informa cada 256 bloques escritos por defecto. Para que lo haga con más frecuencia hay que pasarle la opción `statusinterval` de esta forma:

```bash
$ #Backup:
$ sudo dcfldd statusinterval=10 if=/dev/mmcblk0 bs=2M | gzip -9 - > Rpi_8gb_backup.img.gz
```

### Gestión de la SWAP

Para redimensionar la Swap predeterminada (fichero de 100MB en `/var/swap`):

```bash
$ sudo nano /etc/dphys-swapfile
$ sudo dphys-swapfile setup
$ sudo dphys-swapfile swapon
```

Para consultar el estado de la swap:

```bash
$ swapon -s
```

Para dejar de usar swap:

```bash
$ sudo swapoff -a
```

Para activar la swap tal y como está definida en ''/etc/fstab'':

```bash
$ sudo swapon -a
```

Para activar swap con un fichero en concreto:

```bash
$ sudo swapon /var/swap
```

### Escaneo de Raspberry Pi's en red

```bash
$ arp -a | grep b8:27:eb
$ sudo nmap -PR -sP 192.168.1.0/24 | fgrep -B 2 "Raspberry"
```

## Pi-top

### Enlaces

* [pi-top-install](https://github.com/rricharz/pi-top-install): Scripts para controlar el hardware del Pi-top (teclas brillo pantalla, power off, etc.) sobre Raspbian oficial.
* [pi-top-battery-status](https://github.com/rricharz/pi-top-battery-status): Muestra el estado de la batería del Pi-top en Raspbian.

## Artículos interesantes de [TheMagPi](http://www.themagpi.com/)

* Librería Python para controlar un puerto USB: Página 14 de #3 de TheMagPi
* Buffer de dispositivos controlados con el GPIO de RPi: Página 19 de #4 de TheMagPi
* Librería wiringPi: Sirve para comandar y leer el GPIO desde bash. Página 14 de #6 de TheMagPi
* Comunicación entre RaspPi y Arduino: Página 4 de #7 de TheMagPi
* Uso de interrupciones para chequear GPIO sin bucles: Página 12 de #7 de TheMagPi
* Librería Nanpy para comunicar RaspPi y Arduino por USB: Página 10 de #8 de TheMagPi
* WebIOPi - Framework REST para controlar el GPIO: Página 8 de #9 de TheMagPi

## Seguridad

### SSH

Editar el fichero `/etc/ssh/sshd_config` y modificar/añadir las siguientes líneas ([fuente](http://blog.zoogon.net/2013/01/protegiendo-un-poco-nuestra-raspberry.html)):

```
PermitRootLogin no
MaxAuthTries 3
MaxStartups 5
AllowUsers edumoreno
```

Medidas de protección:

* [Top 20 OpenSSH Server Best Security Practices](http://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html)
* [Protege tu servidor casero de ataques externos](http://blog.desdelinux.net/protege-tu-servidor-casero-de-ataques-externos/)
* [Protegiendo el servidor SSH con fail2ban](http://blog.zoogon.net/2015/02/protegiendo-el-servidor-ssh-con-fail2ban.html)
* [Pasos para asegurar tu Raspberry Pi frente a posibles amenazas](https://www.redeszone.net/2017/09/14/pasos-asegurar-raspberry-pi-frente-posibles-amenazas/)

### Varios

* Cambiar contraseña predeterminada de usuario `pi` o mejor eliminar la cuenta.
* Instalar paquete `fail2ban`.
* Desinstalar paquete `wolfram-engine` que ocupa mucho y no se suele usar:
  * `sudo apt-get remove wolfram-engine`

## Configuración headless

### Activación de SSH

Crear un fichero vacío con nombre `ssh` en partición boot.

### Conexión a punto de acceso Wifi

Crear un fichero con nombre `wpa_supplicant.conf` en partición boot con el siguiente contenido:

```
country=ES
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="<el_ssid>"
    psk="<el_pwd>"
    key_mgmt=WPA-PSK
}
```

### IP estática

Primero averiguamos el nombre del interfaz al que queremos poner la IP estática consultando `ifconfig`. Luego editamos `/etc/dhcpcd.conf` y al final añadimos:

```
interface <nombre_interfaz>
static ip_address=<ip>/24
static routers=<gateway>
static domain_name_servers=<dns>
```

## Raspad

### Enlaces

* SunFounder Wiki

    * [Replace HDMI cable tutorial](http://wiki.sunfounder.cc/index.php?title=Replace_HDMI_cable_tutorial)
    * [Replace power USB cable tutorial](http://wiki.sunfounder.cc/index.php?title=Replace_power_USB_cable_tutorial)
    * [The touch screen does not work properly FAQ](http://wiki.sunfounder.cc/index.php?title=The_touch_screen_does_not_work_properly_FAQ)
    * [Install the fan for Raspad](http://wiki.sunfounder.cc/index.php?title=Install_the_fan_for_Raspad): [STL's alternativos](https://www.thingiverse.com/thing:3074407).

* Instalación de Android

    * [Install Android on his Raspberry Pi](https://howtoraspberrypi.com/install-android-raspberry-pi/)

* Calibración de pantalla

    * [https://www.facebook.com/groups/192987478051513/permalink/233950007288593/](https://www.facebook.com/groups/192987478051513/permalink/233950007288593/)

* Clic derecho

    * [Raspberry Ri Touch Screen setup right click with twofing – Raspbian Jessie](https://maker-tutorials.com/en/raspberry-ri-touch-screen-setup-right-click-with-twofing/)

### Configuración

#### Sistema base

[Raspbian](https://downloads.raspberrypi.org/raspbian_latest)

#### Digitalizador de pantalla

El equipo recién instalado lleva un firmware bastante deficiente en el digitalizador táctil de la pantalla. Hay que actualizarlo siguiendo los pasos del siguiente artículo del wiki de SunFounder: [The touch screen does not work properly FAQ](http://wiki.sunfounder.cc/index.php?title=The_touch_screen_does_not_work_properly_FAQ)

#### Teclado en pantalla

Instalar el paquete: `matchbox-keyboard`

#### Clic secundario

Para conseguir emular el clic derecho del ratón procedemos como sigue (fuentes: [1](https://maker-tutorials.com/en/raspberry-ri-touch-screen-setup-right-click-with-twofing/) y [2](https://www.diskiopi.com/forum/viewtopic.php?id=30)):

1. Instalamos los siguientes paquetes:

        $ sudo apt-get update && sudo apt-get install build-essential libx11-dev libxtst-dev libxi-dev x11proto-randr-dev libxrandr-dev xserver-xorg-input-evdev xinput-calibrator

2. Descargamos el código de twofing y lo extraemos:

        $ wget http://plippo.de/dwl/twofing/twofing-0.1.2.tar.gz
        $ tar -xvzf twofing-0.1.2.tar.gz
        $ cd twofing-0.1.2

3. Compilamos:

        $ make && sudo make install

4. Creamos el fichero `/etc/udev/rules.d/70-touchscreen-ilitek.rules` con el siguiente contenido:

        SUBSYSTEMS=="usb",ACTION=="add",KERNEL=="event*",ATTRS{idVendor}=="222a",ATTRS{idProduct}=="0001",SYMLINK+="twofingtouch",RUN+="/bin/chmod a+r /dev/twofingtouch"
        KERNEL=="event*",ATTRS{name}=="ILITEK Multi-Touch-V3000",SYMLINK+="twofingtouch",RUN+="/bin/chmod a+r /dev/twofingtouch"

5. Creamos el fichero `/usr/share/X11/xorg.conf.d/90-touchinput.conf` con el siguiente contenido:

        Section "InputClass"
        Identifier "calibration"
        Driver "evdev"
        MatchProduct "ILITEK ILITEK-TP"
        MatchDevicePath "/dev/input/event*"
        Option "Emulate3Buttons" "True"
        Option "EmulateThirdButton" "1"
        Option "EmulateThirdButtonTimeout" "750"
        Option "EmulateThirdButtonMoveThreshold" "30"
        EndSection

6. Creamos el fichero `/etc/udev/rules.d/ 99-input-tagging.rules` con el siguiente contenido:

        ACTION=="add", KERNEL=="event*", SUBSYSTEM=="input", TAG+="systemd", , ENV{SYSTEMD_ALIAS}+="/sys/subsystem/input/devices/$env{ID_SERIAL}"

7. Creamos el fichero `~/.config/autostart/twofing.desktop` con el siguiente contenido:

        [Desktop Entry]
        Type=Application
        Name=Twofing
        Exec=twofing
        StartupNotify=false
