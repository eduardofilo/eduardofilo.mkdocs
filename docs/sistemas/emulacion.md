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
* [ZXBaremulator](http://zxmini.speccy.org/es/index.html): Emulador bare-metal completo de los ZX Spectrum 48K/128K/+2A para la Raspberry PI.

## Juegos destacados

### ZX Spectrum

* [Flying Shark](https://www.youtube.com/watch?v=wWBQusR3pIg)
* [Alter ego](http://www.retrosouls.net/?page_id=848)
* [Old Tower](http://www.retrosouls.net/?page_id=848): Vidas infinitas: `POKE 35492,201`
* [Return to Holy Tower](http://www.zxuno.com/ht2/)
* [Mighty Final Fight](https://idpixel.ru/games/mightyfinalfight/)
* [Los amores de Brunilda](http://www.retroworks.es/php/game.php?id=11)
* [The Sword of Ianna](https://theswordofianna.retroworks.es/)
* [Ninja Gaiden Shadow Warriors](http://www.indieretronews.com/2018/01/ninja-gaiden-shadow-warriors-gameboy.html)

### Amstrad CPC

* [Psycho Pig UXB](https://www.amstrad.es/doku.php?id=foraneos:psycho_pigs_uxb)

### NES

* [Faxanadu](https://www.youtube.com/watch?v=p4B2ZuY1fmY)

### Master System

* [Sonic](https://www.youtube.com/watch?v=SQPvA0OvR24)

### NeoGeo Pocket Color

* [Dark Arms](https://www.youtube.com/watch?v=AZ8kcOMvDTU)

### Commodore 64

* [Donkey Kong](https://csdb.dk/release/?id=151272)

### GameBoy

* [Super Mario Land 2](https://www.youtube.com/watch?v=LrxJOasTSDs)
* [The Legend of Zelda: Link's Awakening](https://www.youtube.com/watch?v=UQlP9sHf5Ho)
* [Donkey Kong](https://www.youtube.com/watch?v=7qNvux9KT3Y)
* [Kirby's Dream Land 2](https://www.youtube.com/watch?v=Zstm37Clc5M)
* [Metal Gear Solid](https://www.youtube.com/watch?v=qOIe1bcWAn0)

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

## RG-350

### Enlaces

* [Anbernic RG-350 Wiki](https://github.com/retrogamehandheld/RG-350/wiki)
* [Foro en elotrolado.net](https://www.elotrolado.net/hilo_rg-350-miyoo-new-pocket-go2-y-game-kiddy-gdk350-350h-alternativas-a-la-gcw-zero-con-el-jz4770_2341546). Algunos posts escogidos:
    * [XMAME EN LA SD EXTERNA](https://www.elotrolado.net/hilo_rg-350-miyoo-new-pocket-go2-y-game-kiddy-gdk350-350h-alternativas-a-la-gcw-zero-con-el-jz4770_2341546_s4100#p1748612345)
* [Foro en Dingoonity.org](https://boards.dingoonity.org/retro-game-350rg-350/)
* [Descarga de firmware](https://jutleys.wixsite.com/retrogamers97-90/forum)
* [Emuladores](https://rs97.bitgala.xyz/RG-350/localpack/extra_emulators/)

### Controles pantalla

* Subir brillo: `Power + Volumen+`
* Bajar brillo: `Power + Volumen-`

### Guardar partida en MAME X

* Guardar: `START + Izquierda` luego seleccionar casilla de guardado (por letras, hay 29) y pulsar A.
* Recuperar: `START + Derecha` luego seleccionar casilla donde se guardó y pulsar A.
