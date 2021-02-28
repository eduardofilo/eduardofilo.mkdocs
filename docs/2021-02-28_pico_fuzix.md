title: FUZIX en Raspberry Pi Pico
summary: Montaje e instalación de FUZIX (variante UNIX) en Raspberry Pi Pico.
date: 2021-02-28 20:00:00

![Raspberry Pi Pico](/images/posts/fuzix/raspberry-pi-pico.jpg)

En el sitio de la Fundación Raspberry Pi apareció hace poco [este artículo](https://www.raspberrypi.org/blog/how-to-get-started-with-fuzix-on-raspberry-pi-pico/) explicando cómo instalar la variante UNIX llamada FUZIX en el microcontrolador de reciente aparición Raspberry Pi Pico. Al parecer FUZIX es un proyecto surgido en torno al microprocesador de 8 bit Z-80 al que tengo un cariño especial ya que es el único procesador del que he llegado a conocer su código máquina. Decidido a realizar el montaje para probarlo, encontré que se puede simplificar bastante en tres puntos:

1. El dump que proporcionan para la microSD es de la segunda partición, cuando podrían haber proporcionado una imagen de la tarjeta completa que ahorraría los pasos de la sesión con `fdisk` para crear sus particiones y el posterior `dd` para cargar el dump.
2. El módulo que utilizan para conectar la microSD no es en realidad necesario ya que al funcionar Raspberry Pi Pico a 3,3V no hace falta ninguna adaptación de las señales, es decir se puede cablear directamente la microSD a Raspberry Pi Pico.
3. Como adaptador para el puerto serie, en lugar de utilizar una Raspberry Pi, utilizo un Arduino Nano con el típico truco de puentear el pin de RESET a GND. En este caso sí que habrá que adaptar la linea RX ya que Arduino trabaja a 5V. Esto se puede hacer mejor con un buen módulo UART-USB capaz de trabajar a 3,3V, pero no contaba con él en el momento de escribir este artículo.

Sin más veamos los pasos simplificados para ejecutar FUZIX en Raspberry Pi Pico.

## Lector microSD

Como comentaba antes, la conexión de una tarjeta microSD se puede hacer realizando el patillaje directo y correcto entre los terminales de la microSD y los pines 16 a 20 de Raspberry Pi Pico. En esos pines se encuentra uno de los puertos SPI que tiene el microcontrolador. Las tarjetas SD y microSD pueden funcionar en dos modos, el nativo SD y como puerto SPI. Utilizaremos pues éste último. Tan sólo necesitamos conocer el patillaje a utilizar en este modo. Haciendo una búsqueda rápida en cualquier buscador, en la modalidad de imágenes, por ejemplo por la cadena "spi microsd pinout", encontramos la respuesta:

![Microsd_pinout](/images/posts/fuzix/Microsd_pinout.png)

En la tabla anterior se ve además la correspondencia entre los pines de las tarjetas en formato SD y microSD. Vamos a aprovechar esta correspondencia para construir un lector de tarjetas microSD utilizando uno de los típicos adaptadores que suelen venir con las tarjetas microSD. Soldaremos directamente 7 cables entre los terminales 1 y 7 que más tarde conectaremos a Raspberry Pi Pico. La correspondencia entre los terminales del adaptador SD y Raspberry Pi Pico es como sigue:

|Pin adaptador SD|SPI|Raspberry Pi Pico|
|:---------------|:--|:----------------|
|1|CS|Pin 17 (GP13)|
|2|MOSI|Pin 20 (GP15)|
|3|GND|Pin 18 (GND)|
|4|3,3V|Pin 36 (3V3 OUT)|
|5|SCK|Pin 19 (GP14)|
|6|GND|Pin 18 (GND)|
|7|MISO|Pin 16 (GP12)|
|8|-|-|
|9|-|-|

Haciendo un cableado sobre una tira de pin de 1x6 (unificamos los dos terminales GND de la SD) reordenando los cables para que los pines de Raspberry Pi Pico queden en secuencia (pin 16 a 20) y dejando el pin de 3,3V a continuación del pin 20, podremos conectar el adaptador directamente. El adaptador resultante es el siguiente:

![Adaptador](/images/posts/fuzix/adaptador.jpg)

Se puede incluso hacer más fácil y flexible el conexionado aprovechando que la separación de los terminales de la SD es de una décima de pulgada, como en las típicas tiras de pin y las breadboard, por lo que puede soldarse directamente una tira de pin. La idea y la foto siguiente están sacadas de [este sitio](https://www.esp8266.com/viewtopic.php?t=16016):

![led_matrix_SmartMatrix_Micro_SD_Pinout_1](/images/posts/fuzix/led_matrix_SmartMatrix_Micro_SD_Pinout_1.jpg)

El adaptador construido se puede conectar directamente a Raspberry Pi Pico. Observad que el pin que recibe la alimentación de 3,3V (cable rojo) queda fuera de la planta de Raspberry Pi Pico de manera que por medio de un par de puentes blancos se lleva hasta el pin 36 que es de donde obtenemos los 3,3V de alimentación.

![conexion_adaptador](/images/posts/fuzix/conexion_adaptador.jpg)

## Imagen de la microSD

En las instrucciones del [artículo original](https://www.raspberrypi.org/blog/how-to-get-started-with-fuzix-on-raspberry-pi-pico/) se incluye un proceso que por medio del comando `fdisk` utilizado desde una Raspberry Pi (desde cualquier Linux en realidad), permite construir dos particiones en la microSD (una para la swap y otra para el sistema de archivos). Se nos ofrece un dump de la segunda partición que se carga con el comando `dd`. Todo esto se podría haber evitado generando el dump de las dos particiones juntas. Es lo que puede encontrarse en el siguiente fichero que podremos flashear directamente sobre una microSD con programas como [Balena Etcher](https://www.balena.io/etcher/).

> [card.img.gz](/files/posts/fuzix/card.img.gz)

En Linux podemos flashear directamente con el siguiente comando, sustituyendo el dispositivo (`/dev/mmcblk0` en el ejemplo) por el que corresponda:

```
gunzip card.img.gz -c | sudo dd of=/dev/mmcblk0 bs=1M status=progress conv=fsync
```

## Firmware para Raspberry Pi Pico

Aunque puede encontrarse en el [artículo original](https://www.raspberrypi.org/blog/how-to-get-started-with-fuzix-on-raspberry-pi-pico/) lo incluyo aquí de nuevo para que todo el proceso pueda seguirse sin salir de aquí:

> [fuzix.uf2](/files/posts/fuzix/fuzix.uf2)

La forma de cargar el firmware en Raspberry Pi Pico es conectar por USB al ordenador mientras se mantiene pulsada la tecla `BOOTSEL`. En ese momento se montará una unidad de almacenamiento externa en el ordenador donde copiaremos el fichero anterior.

## Conexión serie

Ya tenemos todo instalado y preparado. Tan sólo necesitamos una manera de conectar con el sistema. El único medio para conectar con él es por medio del puerto serie que hay en los pines 1 y 2 (GP0 y GP1 respectivamente) de Raspberry Pi Pico. Desconzco si hay algún motivo que haya impedido utilizar el puerto USB de Pico para este propósito. Desde luego hubiera sido mucho más cómodo.

Para conectar el puerto serie de Pico al ordenador, lo mejor es utilizar un módulo adaptador USB como [éste](https://www.banggood.com/RobotDyn-USB-TTL-UART-Serial-Adapter-CP2102-5V-3_3V-USB-A-Module-p-1244766.html). Al no tener uno a mano utilicé el típico [truco de usar un Arduino en modo RESET permanente](/ingenieria/arduino.html#adaptador-serie). Si utilizamos esta técnica nos tocará montar un divisor de tensión con un par de resistencias para adaptar el nivel de tensión para que la linea RX de Pico no reciba directamente los 5V con que trabaja Arduino. En la linea TX no será necesario, ya que los 3,3V de Pico son suficientes para que Arduino interprete ese nivel de tensión como un 1 digital en 5V.

El siguiente esquema completo muestra el divisor de tensión así como la forma de alimentar Raspberry Pi Pico desde los 5V de salida que ofrece Arduino en uno de sus pins. Llevaremos esos 5V hasta el pin VSYS de Pico que admite entre 1,8V y 5,5V. Las resistencias del divisor de tensión pueden ser prácticamente de cualquier valor con tal de que la que está en serie en la linea RX tenga aproximadamente la mitad de valor que la que deriva a GND.

![Esquema](/images/posts/fuzix/fuzix_bb.png)

Ya sólo queda conectar por USB el Arduino al ordenador y conectar con nuestro cliente serie favorito a 115200 baudios. Por ejemplo en Linux puede hacerse con el siguiente comando:

```
screen /dev/ttyUSB0 115200 8N1
```

Si todo va bien, en pantalla veremos lo siguiente. El sistema, antes de pedirnos el usuario (`root`) y password (vacío) nos pedirá el día y hora para poner la fecha al sistema:

```
FUZIX version 0.4pre1
Copyright (c) 1988-2002 by H.F.Bower, D.Braun, S.Nitschke, H.Peraza
Copyright (c) 1997-2001 by Arcady Schekochikhin, Adriano C. R. da Cunha
Copyright (c) 2013-2015 Will Sowerbutts <will@sowerbutts.com>
Copyright (c) 2014-2020 Alan Cox <alan@etchedpixels.co.uk>
Devboot
64kB total RAM, 64kB available to processes (15 processes max)
Enabling interrupts ... ok.
SD drive 0: hda: hda1 hda2
Mounting root fs (root_dev=2, ro): OK
Starting /init
init version 0.9.0ac#1
Cannot open file
Current date is Wed 2021-02-17
Enter new date: 2021-02-28
Current time is 22:21:10
Enter new time: 19:54

 ^ ^
 n n   Fuzix 0.3.1
 >@<
       Welcome to Fuzix
 m m

login: root

Welcome to FUZIX.
#

```
