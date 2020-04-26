---
layout: default
permalink: /electronica/arduino.html
---

# Arduino

## Enlaces

* [Parallax Propeller](https://www.parallax.com/microcontrollers/propeller)

## Adaptador serie

Se puede utilizar muy fácilmente un Arduino como adaptador USB-UART sin más que puentear el pin de reset (RST) a GND. En ese caso conectar los pines RX, TX (sin cruzar) y GND hacia el dispositivo que queramos conectar.

En caso de que el dispositivo con el que conectemos trabaje a 3.3V (como Raspberry Pi por ejemplo), es necesario montar un divisor de tensión en la línea RX tal y como se ve en [este artículo](https://oscarliang.com/raspberry-pi-and-arduino-connected-serial-gpio/) (en el artículo las líneas RX/TX sí que están cruzadas porque se conecta el puerto UART al microcontrolador Atmel, no al adaptador USB):

![arduino-raspberry-pi-serial-connect](/images/pages/arduino-raspberry-pi-serial-connect-schematics.jpg)

## Programación de ATtiny85

El MC ATtiny85 no lleva el bootloader de Arduino que escucha por el puerto serie adaptado a USB ya que ni tiene puerto serie hardware ni suele estar acompañado por el adaptador USB. La única forma de programarlo es por [ISP](https://en.wikipedia.org/wiki/In-system_programming) o mediante un programador de MC adecuado. Esto se puede hacer desde un Arduino (basado en ATmega328p) con el sketch "Arduino ISP" cargado.

Antes de empezar necesitamos cargar en el Arduino IDE las definiciones de placa para soportar ATtiny85 (y algunos de sus hermanos pequeños). Para ello proceder como sigue ([fuente](http://highlowtech.org/?p=1695)):

1. Abrimos el Arduino IDE y nos vamos a la ventana de Preferencias (`Archivo > Preferencias`).
2. En la ventana que aparece introducimos la siguiente URL en el campo `Gestor de URLs Adicionales de Tarjetas`: [https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json](https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json)
3. Pulsamos `OK`.
4. Abrimos el Gestor de tarjetas (`Herramientas > Placa > Gestor de tarjetas...`).
5. Localizamos el módulo `attiny by David A. Mellis` y lo instalamos.

Los pasos para el montaje son los siguientes:

1. Cargamos en el Arduino el sketch "Arduino ISP" que hay en ejemplos.
2. Colocamos un condensador de 10μF entre el pin RESET del Arduino y GND.
3. Cableamos entre el ATtiny85 y el Arduino de la siguiente manera:
    ![arduino-attiny85-connection](/images/pages/attiny85-arduino-isp.png)
    ![arduino-attiny85-connection_esq](/images/pages/attiny85-arduino-isp_esq.png)
4. Configuramos el Arduino IDE con los siguientes parámetros:
    * **Placa**: `ATtiny25/45/85`
    * **Procesador**: `ATtiny85`
    * **Clock**: `Internal 8 MHz`
    * **Programador**: `Arduino as ISP`

A partir de aquí hay varias cosas que podemos hacer.

#### Cambiar el reloj

El ajuste del reloj que va a utilizar el MC es muy importante. Necesitamos conocerla para que el MC responda cuando queramos comunicarnos con él para cargarle un programa. Si en algún momento lo configuramos para que utilice reloj externo, tendremos que conectar uno entre los pines PB3 y PB4 siguiendo el datasheet. El ajuste del reloj se hace cambiando los fuse bits de 3 bytes especiales del MC. Esto desde el Arduino IDE se hace con el comando "Quemar Bootloader" que no hace otra cosa que cambiar estos fuse bits. De fábrica el ATtiny85 viene con el reloj interno de 1MHz configurado. Conviene cambiarlo inicialmente a 8MHz ya que es una configuración más potente (aunque también consumirá más). En caso de cometer algún error configurando los fuse bits y tener problemas para comunicar con el MC, se puede usar un [programador de alto voltaje](/electronica/modulos.html#attiny-high-voltage-programmer) para forzar el cambio de los fusebits.

#### Cargar un sketch

Simplemente utilizaremos el botón para subir el sketch que tengamos abierto en el Arduino IDE.
