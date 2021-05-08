---
layout: default
permalink: /retro-emulacion/microconsolas.html
---

# Micro consolas

* [uChip Simple VGA Console (uSVC)](https://www.crowdsupply.com/itaca-innovation/usvc)
* [Arduboy](https://arduboy.com/)
* [Hackvision](https://nootropicdesign.com/hackvision/)
* [Uzebox](http://uzebox.org/)

## Uzebox

### Enlaces

* [Home del proyecto](http://belogic.com/uzebox/index.asp)
* [EdUzebox](/2020-02-08-eduzebox.html)
* Getting Started with the Uzebox Video Game Console: [parte 1](https://www.youtube.com/watch?v=vT2TUSZWDf8); [parte 2](https://www.youtube.com/watch?v=SRUv9T9vyQ4)
* [ROMs](http://uzebox.org/wiki/index.php?title=Games_and_Demos). [Pack](http://uzebox.org/forums/download/file.php?id=2045)
* [Foro](http://uzebox.org/forums/index.php). Algunos posts importantes:
    * [Uzebox Quick Start](http://uzebox.org/forums/viewtopic.php?f=8&t=151)
    * [Uzebox SD Gameloader V0.4.5](http://uzebox.org/forums/viewtopic.php?f=3&t=520&start=0): Bootloader con el cargador de juegos desde SD.
* [ATMEGA644 ISP - Uzebox](https://forum.arduino.cc/index.php?topic=206143.0): Instrucciones para flasheo con avrdude en post inicial.

### Instalación de ATmega644 en Arduino IDE

Para que la placa aparezca en el Arduino IDE, instalar las que proporciona el proyecto MightyCore que incluye el ATmega644:

1. Abrir Arduino IDE.
2. Abrir el menú `File > Preferences`.
3. Introducir la siguiente URL en `Additional Boards Manager URLs`:

	```
	https://mcudude.github.io/MightyCore/package_MCUdude_MightyCore_index.json
	```

4. Abrir el menú `Tools > Board > Boards Manager...`.
5. Buscar la entrada correspondiente a MightyCore e instalarla.
