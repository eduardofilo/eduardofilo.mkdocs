---
layout: default
permalink: /sistemas/emulacion.html
---

# Emulación

## Enlaces

* [Emuladores en OpenELEC](http://misapuntesde.com/post.php?id=502)
* [Configuración PiGRRL-2](http://apuntes.eduardofilo.es/2016/07/21/PIGRRL-2.html)
* [Managing ROMs](https://github.com/retropie/retropie-setup/wiki/Managing-ROMs)
* [MAME FAQ](http://wiki.mamedev.org/index.php/FAQ:Games): Resuelve dudas sobre peculiaridades de algunos juegos. Por ejemplo sobre el arranque de [Joust](http://wiki.mamedev.org/index.php/FAQ:Games#Joust).

## Empaquetado de ROMs MAME

Primero hay que localizar los ficheros que componen la ROM. Hay varios tipos (explicados [aquí](https://github.com/retropie/retropie-setup/wiki/Managing-ROMs#step-5--rebuild-a-rom-set)). Una forma de ir a lo seguro es localizar sus piezas gracias a los hash SHA1 que se pueden encontrar en los ficheros [.DAT](https://github.com/retropie/retropie-setup/wiki/Managing-ROMs#quick-reference) y luego hacer un paquete ZIP sin compresión.

Para generar un archivo ZIP con compresión nula en Linux, se consigue por ejemplo con el siguiente comando lanzado desde el directorio donde se encuentren los ficheros que queremos empaquetar:

```bash
zip -0 rom.zip *
```

El nombre del archivo (en el ejemplo `rom.zip`) es importante para que el emulador reconozca la ROM. También lo obtendremos del fichero `.DAT`.

## Conexión de mando SixAxis en Recalbox

Para que funcione por USB en lugar de por Bluetooth que es como está previsto por defecto, hay que editar el fichero `/recalbox/share/system/recalbox.conf` y cambiar la siguiente propiedad a 0:

    controllers.ps3.enabled=0

Se puede editar entrando por SSH, para lo cual las credenciales predeterminadas son:

* user: root
* password: recalboxroot

Si se hace montando la SD en el ordenador, el fichero se encuentra en la partición `/dev/mmcblk0p8` que se monta en Ubuntu como `share0` en la ruta `./system/recalbox.conf`.

## Backup juego PSX

1. Introducir el disco en la unidad de CD-ROM.
2. Localizar el dispositivo del CD-ROM:

    ```bash
    sudo cdrdao scanbus
    ```

3. Desmontar el dispositivo sin expulsar el disco (suponemos que el comando anterior indica que el dispositivo es `/dev/sr0`):

    ```bash
    sudo umount /dev/sr0
    ```

4. Hacer el backup:

    ```bash
    cdrdao read-cd --device /dev/sr0 --driver generic-mmc-raw --read-raw --datafile nombre_juego.bin nombre_juego.toc
    ```

Con esto obtendremos dos ficheros. En algunas ocasiones nos puede interesar más el fichero `cue` equivalente al `toc`. En ese caso convertirlo así:

```bash
toc2cue nombre_juego.toc nombre_juego.cue
```
