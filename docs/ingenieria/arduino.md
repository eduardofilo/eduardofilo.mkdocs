---
layout: default
permalink: /ingenieria/arduino.html
---

# Arduino

## Enlaces

* [Parallax Propeller](https://www.parallax.com/microcontrollers/propeller)

## Adaptador serie

Se puede utilizar muy fácilmente un Arduino como adaptador USB-UART sin más que puentear el pin de reset (RST) a GND. En ese caso conectar los pines RX, TX (sin cruzar) y GND hacia el dispositivo que queramos conectar.

En caso de que el dispositivo con el que conectemos trabaje a 3.3V (como Raspberry Pi por ejemplo), es necesario montar un divisor de tensión en la línea RX tal y como se ve en [este artículo](https://oscarliang.com/raspberry-pi-and-arduino-connected-serial-gpio/) (en el artículo las líneas RX/TX sí que están cruzadas porque se conecta el puerto UART al microcontrolador Atmel, no al adaptador USB):

![arduino-raspberry-pi-serial-connect](/images/pages/arduino-raspberry-pi-serial-connect-schematics.jpg)

## Programación de ATtiny85

El MC ATtiny85 no lleva el bootloader de Arduino que escucha por el puerto serie adaptado a USB ya que ni tiene puerto serie hardware ni suele estar acompañado por el adaptador USB. La única forma de programarlo es por [ISP](https://en.wikipedia.org/wiki/In-system_programming) o mediante un programador de MC adecuado de los que existen varios. Vamos a ver un par de ellos.

Antes de empezar necesitamos cargar en el Arduino IDE las definiciones de placa para soportar ATtiny85 (y algunos de sus hermanos pequeños). Para ello proceder como sigue ([fuente](http://highlowtech.org/?p=1695)):

1. Abrimos el Arduino IDE y nos vamos a la ventana de Preferencias (`Archivo > Preferencias`).
2. En la ventana que aparece introducimos la siguiente URL en el campo `Gestor de URLs Adicionales de Tarjetas`: [https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json](https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json)
3. Pulsamos `OK`.
4. Abrimos el Gestor de tarjetas (`Herramientas > Placa > Gestor de tarjetas...`).
5. Localizamos el módulo `attiny by David A. Mellis` y lo instalamos.

#### Programación con Arduino

Podemos utilizar como programador un Arduino (basado en ATmega328p como el UNO) con el sketch "Arduino ISP" cargado. Los pasos para programar de esta forma son los siguientes:

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

#### Programación con BusPirate

En este caso vamos a utilizar un BusPirate 3.6 como programador y un módulo Digispark para cablear más fácilmente la conexión ISP:

1. Insertar en [módulo Digispark](https://es.aliexpress.com/item/606895785.html). A la tira de pines de 2x4 del módulo le habremos recortado los pines que corresponden a los pines P3 y P4 del ATtiny85, ya que de esta forma la tira de pines se convierte en un conector ISP de 6 pines estándar.

    ![Digispark trimmed](/images/pages/arduino/digispark_trim.jpg)

2. Conectar el cable ISP entre BusPirate y módulo Digispark cableando como sigue (aunque el ATtiny85 funciona a 5V, parece que soporta sin problemas ser programado a 3.3V):

    |Pin ISP|Señal|Pin BusPirate|
    |:------|:----|:------------|
    |1|MISO|Negro:MISO|
    |2|+3.3V|Rojo:+3.3V|
    |3|SCK|Morado:CLK|
    |4|MOSI|Gris:MOSI|
    |5|CS|Blanco:CS|
    |6|GND|Marrón:GND|

    ![BusPirate Digispark 1](/images/pages/arduino/buspirate_digispark_1.jpg)
    ![BusPirate Digispark 2](/images/pages/arduino/buspirate_digispark_2.jpg)
    ![BusPirate Digispark 3](/images/pages/arduino/buspirate_digispark_3.jpg)

3. Configuramos el Arduino IDE con los siguientes parámetros:
    * **Placa**: `ATtiny25/45/85`
    * **Procesador**: `ATtiny85`
    * **Clock**: `Internal 8 MHz`
    * **Programador**: `BusPirate as ISP`

Alternativamente podemos programar con el comando `avrdude` con el argumento `-c buspirate`. Por ejemplo para obtener el estado de los Fuse bits:

```
$ avrdude -c buspirate -P /dev/ttyUSB0 -p attiny85 -v
```

A partir de aquí hay varias cosas que podemos hacer.

#### Programación con MiniPRO TL866xx desde Linux

Teniendo el programa [minipro](https://gitlab.com/DavidGriffith/minipro) instalado, montar el ATtiny85 en el socket ZIP y conectar el cable USB. Interesa antes de empezar, asegurarnos de que el MC es identificado correctamente, lo que nos servirá además para comprobar que las conexiones son correctas, para lo que ejecutamos:

```
edumoreno@eduardo-HP-Folio-13:~$ minipro -p ATTINY85 --read_id
Found TL866II+ 04.2.125 (0x27d)
Chip ID OK: 0x1E930B
```

Una vez que vemos que la comunicación se establece sin problemas, grabamos el MC con el siguiente comando:

```
edumoreno@eduardo-HP-Folio-13:~$ minipro -p ATTINY85 -w PROGRAMA.hex -c code
Found TL866II+ 04.2.125 (0x27d)
Chip ID OK: 0x1E930B
Found Intel hex file.
Erasing... 0.01Sec OK
Writing Code...  1.10Sec  OK
Reading Code...  0.49Sec  OK
Verification OK
```

Para los fuse bits, escribiremos un fichero de texto con el siguiente contenido (los valores de los fusebits que se muestran a continuación son los predeterminados, pero habrá que sustituirlos por los que nos interesen; [esta calculadora](http://eleccelerator.com/fusecalc/fusecalc.php) es muy útil):

```
fuses_lo = 0x62
fuses_hi = 0xdf
fuses_ext = 0xff
lock_byte = 0xff
```

Una vez creado el fichero, cargaremos sus valores en el MC con el siguiente comando:

```
edumoreno@eduardo-HP-Folio-13:~$ minipro -p ATTINY85 -w PROGRAMA.fuses.conf -c config
Found TL866II+ 04.2.125 (0x27d)
Chip ID OK: 0x1E930B
Writing fuses... 0.02Sec  OK
```

#### Cambiar el reloj

El ajuste del reloj que va a utilizar el MC es muy importante. Necesitamos conocerla para que el MC responda cuando queramos comunicarnos con él para cargarle un programa. Si en algún momento lo configuramos para que utilice reloj externo, tendremos que conectar uno entre los pines PB3 y PB4 siguiendo el datasheet. El ajuste del reloj se hace cambiando los fuse bits de 3 bytes especiales del MC. Esto desde el Arduino IDE se hace con el comando "Quemar Bootloader" que no hace otra cosa que cambiar estos fuse bits. En caso de cometer algún error configurando los fuse bits y tener problemas para comunicar con el MC, se puede usar un [programador de alto voltaje](/electronica/modulos.html#attiny-high-voltage-programmer) para forzar el cambio de los fusebits.

#### Cargar un sketch

Simplemente utilizaremos el botón para subir el sketch que tengamos abierto en el Arduino IDE.
