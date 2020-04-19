---
layout: default
permalink: /retro-emulacion/zx-spectrum.html
---

# ZX Spectrum

## Carga de audio

* [Amplificador sonido entrada EAR](http://trastero.speccy.org/cosas/JL/ampli/Amplificador.html)
* [Loading ZX Spectrum tape audio in a post-cassette world](https://retrocomputing.stackexchange.com/questions/773/loading-zx-spectrum-tape-audio-in-a-post-cassette-world)
* Variantes TZXDuino:
    * [Proyecto original](https://github.com/sadken/TZXDuino)
    * MEGADuino:
        * [Placa](https://github.com/merlinkv/MegaDuino_v2.8)
        * [Firmware](https://github.com/merlinkv/MaxDuino_1.54M)
        * [Carcasa v2](https://www.thingiverse.com/thing:4290318)
        * [Tutorial programación firmware](https://www.winuaespanol.com/phpbb3/viewtopic.php?p=5116#p5116)
        * [Probando el TZXDuino](https://www.va-de-retro.com/foros/viewtopic.php?t=5541)
        * [Probando el TSXDuino MEGA](https://www.va-de-retro.com/foros/viewtopic.php?t=8488)
        * [Tirada MegaDuino](https://www.va-de-retro.com/foros/viewtopic.php?t=8496)
        * [Tutorial programación](https://www.winuaespanol.com/phpbb3/viewtopic.php?p=5116#p5116)

## Componentes / Repuestos

* [Módulo de memoria baja](http://zx.zigg.net/LRR/)
* [Regulador de conmutación Traco Power, entrada 6.5 → 36V dc, Salida 5V, 1A, 5W](https://es.rs-online.com/web/p/reguladores-de-conmutacion/6664379/)

## Homebrew

* [The Curse of Trasmoz](https://volcanobytes.itch.io/the-curse-of-trasmoz)

## Flash de MegaDuino

1. Bajar librería [LiquidCrystal_I2C](https://github.com/merlinkv/MaxDuino_Libraries_for_1.54M)
2. Copiar el contenido del repositorio anterior a un directorio de nombre `LiquidCrystal_I2C` y colocarlo dentro del directorio `libraries` del directorio de sketches de Arduino IDE.
3. Instalar mediante el **Gestor de Librerías** la librería `SdFat` de Bill Greiman.
4. Bajar código de [repositorio](https://github.com/merlinkv/MaxDuino_1.54M)
5. Abrir el sketch `MaxDuino_1.54M.ino`
6. Editar la linea 178 del sketch anterior para corregir el nombre del fichero de cabecera `userMAXconfig.h` (originalmente pone `userMaxconfig.h`).
7. Editar el fichero `userMAXconfig.h` y descomentar las líneas siguientes:

    ```
    #define OLED_SETCONTRAS   0xcf      // Override default value inside Diplay.ino, bigger to increase output current per segment
    #define OLED1306                      // Set if you are using OLED 1306 display
    #define OLED1306_128_64         // 128x64 resolution with 8 rows
    #define OLED1106_1_3            // Use this line as well if you have a 1.3" OLED screen
    ```

8. Seleccionar en el Arduino IDE:

    * Placa: `Arduino Mega or Mega 2560`
    * Procesador: `ATmega2560 (Mega 2560)`
    * Puerto: El que corresponda

9. Pulsar el botón `Subir`.
