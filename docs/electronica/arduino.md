---
layout: default
permalink: /electronica/arduino.html
---

# Arduino

## Adaptador serie

Se puede utilizar muy fácilmente un Arduino como adaptador USB-UART sin más que puentear el pin de reset (RST) a GND. En ese caso conectar los pines RX, TX (sin cruzar) y GND hacia el dispositivo que queramos conectar.

En caso de que el dispositivo con el que conectemos trabaje a 3.3V (como Raspberry Pi por ejemplo), es necesario montar un divisor de tensión en la línea RX tal y como se ve en [este artículo](https://oscarliang.com/raspberry-pi-and-arduino-connected-serial-gpio/) (en el artículo las líneas RX/TX sí que están cruzadas porque se conecta el puerto UART al microcontrolador Atmel, no al adaptador USB):

![arduino-raspberry-pi-serial-connect](/images/pages/arduino-raspberry-pi-serial-connect-schematics.jpg)
