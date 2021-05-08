---
layout: default
permalink: /ingenieria/minipro.html
---

# MiniPRO TL866xx

## Enlaces

* [XGecu T56 Universal programmer](http://www.autoelectric.cn/en/tl866_main.html)
* [minipro](https://gitlab.com/DavidGriffith/minipro): An open source program for controlling the MiniPRO TL866xx series of chip programmers.

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

### Versión

```
edumoreno@eduardo-HP-Folio-13:~$ minipro -V
Supported programmers: TL866A/CS, TL866II+
Found TL866II+ 04.2.125 (0x27d)
Warning: Firmware is newer than expected.
  Expected  04.2.123 (0x27b)
  Found     04.2.125 (0x27d)
minipro version 0.5     A free and open TL866XX programmer
Commit date: 2021-04-16 20:53:59 -0700
Git commit: b52ab70f4411ba4a290835c1fe060c71c90c6759
Git branch: master
TL866A/CS: 14330 devices, 8 custom
TL866II+: 16324 devices, 4 custom
```

### Testeo de hardware

```
edumoreno@eduardo-HP-Folio-13:~$ minipro -t
```
