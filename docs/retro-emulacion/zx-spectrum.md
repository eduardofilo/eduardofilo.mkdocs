---
layout: default
permalink: /retro-emulacion/zx-spectrum.html
---

# ZX Spectrum

## Enlaces

* [ZX Design Info](http://www.zxdesign.info/): A site dedicated to the reverse engineering of the ZX Spectrum and related projects.
* Tiendas:
    * [RetroRadionics](https://retroradionics.co.uk/)
    * [ByteDelight](https://www.bytedelight.com/)
    * [ZX Renew](https://zxrenew.co.uk/)
* Clones/recreaciones:
    * [Superfo Harlequin 48K](http://trastero.speccy.org/cosas/JL/Harlequin/superfo1.html)
    * [Superfo Harlequin 128K](http://trastero.speccy.org/cosas/JL/Superfo-Harlequin-128K/128K.html)
    * [Humble48](https://www.8bits4ever.net/product-page/humble48)
    * [Sizif-128](https://github.com/UzixLS/zx-sizif-128): Easy-to-build minimalistic ZX Spectrum clone.
    * [Sizif-512](https://github.com/UzixLS/zx-sizif-512): Another CPLD-based ZX Spectrum clone for 48K rubber case with some sweet features.
    * [N-Go (Next clon)](https://manuferhi.com/c/n-go)
* Emulación:
    * [ZXBaremulator](https://zxmini.speccy.org/es/index.html): Emulador bare-metal completo de los ZX Spectrum 48K/128K/+2A para la Raspberry PI.
    * [ZX-ESPectrum](https://github.com/dcrespo3d/ZX-ESPectrum-Wiimote/tree/lilygo-ttgo-vga32): An emulation of the ZX-Spectrum computer on an [Lilygo TTGo VGA32](https://es.aliexpress.com/item/33014937190.html).

## Carga de audio

* [Amplificador sonido entrada EAR](http://trastero.speccy.org/cosas/JL/ampli/Amplificador.html)
* [Loading ZX Spectrum tape audio in a post-cassette world](https://retrocomputing.stackexchange.com/questions/773/loading-zx-spectrum-tape-audio-in-a-post-cassette-world)
* [z802tzx](https://github.com/rcmolina/z802tzx3): Conversor de TAP a TZX (también en modo turbo).
* Variantes TZXDuino:
    * [Proyecto original](https://github.com/sadken/TZXDuino)
    * MEGADuino:
        * [Placa](https://github.com/merlinkv/MegaDuino_PM_1.3)
        * [Firmware](https://github.com/merlinkv/MegaDuino_1.0_Firmware)
        * [Carcasa v2](https://www.thingiverse.com/thing:4290318)
        * [Tutorial programación firmware](https://www.winuaespanol.com/phpbb3/viewtopic.php?p=5116#p5116)
        * [Probando el TZXDuino](https://www.va-de-retro.com/foros/viewtopic.php?t=5541)
        * [Probando el TSXDuino MEGA](https://www.va-de-retro.com/foros/viewtopic.php?t=8488)
        * [Tirada MegaDuino](https://www.va-de-retro.com/foros/viewtopic.php?t=8496)
        * [Tutorial programación](https://www.winuaespanol.com/phpbb3/viewtopic.php?p=5116#p5116)
        * [Fix en v2 para cargar mejor CDTs en Amstrad](https://www.winuaespanol.com/phpbb3/viewtopic.php?p=5309#p5309)

## Componentes / Repuestos

* [Módulo de memoria baja](http://zx.zigg.net/LRR/)
* [Regulador de conmutación Traco Power, entrada 6.5 → 36V dc, Salida 5V, 1A, 5W](https://es.rs-online.com/web/p/reguladores-de-conmutacion/6664379/)

## Homebrew

* [The Curse of Trasmoz](https://volcanobytes.itch.io/the-curse-of-trasmoz)

## MegaDuino

#### Flash de MegaDuino

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

#### Opciones MegaDuino

* Baud: Velocidad de reproducción de los archivos `CAS` y `TSX` de MSX.
* Motor: Indica si el control de motor está activado/desactivado. Sólo útil para plataformas que permiten control del datasette como Amstrad, MSX y BBC Micro. En el resto de equipos nos permitirá seleccionar manualmente los bloques para programas multicarga por ejemplo.
* TSXCzx: Indica si la opción TSXCzxpUEFSW está activada/desactivada. Sirve para tres cosas:
    * Activar la carga turbo (bloques 4B) de los archivos `CAS` y `TSX` de MSX.
    * Cambiar la polaridad de la señal de audio de los archivos de Spactrum y Amstrad.
    * Cambiar la polaridad de la señal de audio de los archivos `UEF` de Acorn Electron y BBC Micro.
* Skip2A: ???
