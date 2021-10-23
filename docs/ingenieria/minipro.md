---
layout: default
permalink: /ingenieria/minipro.html
---

# MiniPRO TL866xx

## Enlaces

* [XGecu T56 Universal programmer](http://www.autoelectric.cn/en/tl866_main.html)
* [minipro](https://gitlab.com/DavidGriffith/minipro): An open source program for controlling the MiniPRO TL866xx series of chip programmers. [Instalación en Linux](https://gitlab.com/DavidGriffith/minipro#installation-on-linux)

## Actualización firmware

1. Descargar el último paquete del fabricante desde [este enlace](https://www.mediafire.com/folder/hfg5kfj7euw5j/xgecu), que incluye la utilidad de interfaz de usuario para Windows y el fichero `.dat` con el firmware.
2. Descomprimir el .exe que lleva dentro. Ese exe a su vez es un paquete autodescomprimible, por lo que se puede abrir con un descompresor como WinRAR o el Gestor de archivadores de Linux. Extraer de él el fichero `updateII.dat`. Por algún motivo da error con el Gestor de archivadores de Linux. Se puede descomprimir con [Archive Extractor Online](https://extract.me/).
3. Flashear el fichero `updateII.dat` con la utilidad [minipro](https://gitlab.com/DavidGriffith/minipro):

    ```
    edumoreno@eduardo-HP-Folio-13:~$ minipro -F updateII.dat
    Found TL866II+ 04.2.86 (0x256)
    Warning: Firmware is out of date.
      Expected  04.2.123 (0x27b)
      Found     04.2.86 (0x256)
    updateII.dat contains firmware version 4.2.125 (newer)

    Do you want to continue with firmware update? y/n:y
    Switching to bootloader... OK
    Erasing... OK
    Reflashing... 100%
    Resetting device... OK
    Reflash... OK
    ```

## Uso de utilidad [minipro](https://gitlab.com/DavidGriffith/minipro) de linea de comando

* Versión firmware y utilidad: `minipro -V`
* Testeo dispositivo: `minipro -t`
* Búsqueda de integrados compatibles: `minipro -L <search>`
* Indicar modelo de programador `TL866II+` en comandos: `minipro -q tl866ii`
* Programar integrado (ejemplo con ATTiny85): `minipro -p ATTINY85 -w <filename>`
* Leer integrado (ejemplo con ATTiny85; además del volcado de la flash, genera un par de ficheros adicionales, uno con el volcado de la EEPROM y otro con la configuración de fuse bits): `minipro -p ATTINY85 -r <filename>`
* Leer tipo de memoria concreta (posibles valores: code, data, config) en integrado (ejemplo con ATTiny855): `minipro -p ATTINY85 -r <filename> -c <type>`
