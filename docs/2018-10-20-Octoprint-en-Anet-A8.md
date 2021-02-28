title: Octoprint en Anet A8
summary: Instalación de Raspberry Pi sobre impresora 3D Anet A8 para ejecutar Octoprint.
date: 2018-10-20 21:30:00

![Octoprint](/images/posts/octoprint.jpg)

Instalación de Raspberry Pi sobre impresora 3D Anet A8 para ejecutar Octoprint.

## Imágen de sistema

Aunque es posible [instalar manualmente Octoprint](https://discourse.octoprint.org/t/setting-up-octoprint-on-a-raspberry-pi-running-raspbian/2337) sobre una instalación Raspbian estándar, existe una [imágen para grabar directamente sobre la tarjeta microSD llamada OctoPi](https://octoprint.org/download/). Dado que la Raspberry Pi y por tanto su sistema se va dedicar exclusivamente para esta función, se prefiere esta alternativa.

## Modelo de Raspberry Pi elegido

A pesar de que la utilización de una Raspberry Pi Zero no está recomendada por problemas de rendimiento que pueden terminar afectando a las impresiones, en mi experiencia no he sufrido ningún percance y la forma y bajo consumo de la Raspberry Pi Zero (que permite alimentarla desde la misma fuente de la impresora) resulta perfecta para esta instalación.

Sospecho que los posibles problemas están relacionados con el uso de la webcam. Eligiendo la cámara adecuada (que soporte MJPG de forma nativa) y no abusando del vídeo en streaming creo que se deja un margen de seguridad adecuado para poder aprovechar las ventajas de la versión Zero W de la Raspberry Pi.

## Conexión serie entre Anet A8 y Raspberry Pi

Octoprint se comunica con la impresora por medio de una conexión serie. Esta conexión puede fácilmente establecerse a través de USB. De hecho el puerto serie del microcontrolador Atmel que gobierna la impresora está puenteado a un adaptador serie/USB que hay sobre la placa (CH340G). Utilizar esta conexión USB resulta muy aparatoso por el tipo de conectores que implica, así que se ha preferido liberar el puerto serie del microcontrolador para poder utilizarlo directamente.

Estudiando el [esquemático de la placa](/images/posts/octoprint_ANET3D_Board_Schematic.png) se ve que las siguientes secciones son las implicadas en este asunto (se han marcado en azul las zonas de más interés):

![Puerto serie](/images/posts/octoprint_puerto_serie.png)

Podemos ver cómo el puerto serie del microcontrolador (pines `AOFI` y `AIFO`) está puenteado al chip CH340G (U6) por medio de un par de resistencias de 0Ω que actúan como puente. Tendremos que retirar de la placa dichas resistencias R52 y R53.

Una vez hecho, soldaremos unos pines en la ubicación J8 de la placa (al menos la mía venía con los agujeros en la PCB sin los pines soldados). En esta [foto de alta resolución de la placa](/images/posts/octoprint_hires_pcb.jpg) podemos ver bien tanto la ubicación de los puentes J8 como las resistencias que hay que retirar:

![Sección de la PCB](/images/posts/octoprint_hires_pcb_subsection.jpg)

Sólo queda poner un par de jumpers entre los pines siguientes de J8:

* 3-5
* 4-6

Con esto conseguimos que el puerto serie del microcontrolador aparezca disponible en el conector J3. Si antes utilizábamos el puerto USB de la PCB para algún cometido, hay que entender que al realizar esta modificación deja de estar disponible, pero tenemos la opción de reactivarlo cambiando los jumpers a la siguiente disposición:

* 1-3
* 2-4

Como la orientación de la PCB en la impresora es distinta a la del esquemático, se muestra ahora con claridad el resultado final, es decir cómo deben disponerse los dos jumpers para que el puerto serie aparezca en el conector J3 y el hueco dejado por las resistencias R52 y R53:

![Puentes](/images/posts/octoprint_puentes.jpg)

Como vemos los puentes deben apuntar hacia el rótulo BLE. Seguramente se designa así porque la sustitución habitual del puerto USB sería un adaptador Bluetooth que podría adaptarse al conector J3.

Sólo queda localizar en el conector J3 los pines del puerto serie del microcontrolador recien redirijidos y los de alimentación (5V y GND). En este punto podríamos conectar la Raspberry Pi con simples cables de pin, pero dada la cercanía en el GPIO de la Raspberry Pi del puerto serie y de los terminales de alimentación, me decidí a preparar una pequeña placa adaptadora para el conector J3 de la PCB de la impresora.

El conector J3 de la impresora según el [esquemático](/images/posts/octoprint_ANET3D_Board_Schematic.png) tiene el siguiente pineado:

![Esquemático Conector J3](/images/posts/octoprint_j3.png)

De nuevo es necesario orientar el conector correctamente para interpretar el esquemático. Para evitar confusiones se indica a continuación la numeración de los pines sobre el conector:

![Pines Conector J3](/images/posts/octoprint_conector_j3.jpg)

La conexión de estos pines con los del GPIO de la Raspberry Pi será así:

* `J3: 1 (J3_TX) <-> PIN#08 (GPIO14 UART0_TXD) :Raspberry`
* `J3: 2 (J3_RX) <-> PIN#10 (GPIO15 UART0_RXD) :Raspberry`
* `J3: 4 (+5V)   <-> PIN#04 (5V)               :Raspberry`
* `J3: 8 (GND)   <-> PIN#06 (Ground)           :Raspberry`

![Raspberry Pi GPIO Layout Model B+](/images/posts/Raspberry-Pi-GPIO-Layout-Model-B-Plus.png)

Puede generar confusión ver que las conexiones entre ambos conectores son TX-TX y RX-RX, cuando las conexiones TX y RX deben cruzarse. La confusión viene de que en el conector J3 lo que se indica es a dónde se debe conectar y no el terminal del puerto serie del microcontrolador. Si tiramos del hilo en el esquemático vemos que por ejemplo el pin 1 del conector J3 sigue la secuencia:

    J3_TX - AIFO - RXD0

Por tanto en realidad sí estamos cruzando las señales.

El adaptador realizado es el siguiente:

![Adaptador J3-GPIO](/images/posts/octoprint_adaptador1.jpg)

![Adaptador J3-GPIO](/images/posts/octoprint_adaptador2.jpg)

A continuación se puede ver soldado sobre la Raspberry:

![Adaptador J3-Raspberry](/images/posts/octoprint_adaptador_raspberry1.jpg)

![Adaptador J3-Raspberry](/images/posts/octoprint_adaptador_raspberry2.jpg)

![Adaptador J3-Raspberry](/images/posts/octoprint_adaptador_raspberry3.jpg)

Finalmente montado sobre la PCB de la impresora queda así:

![Raspberry sobre PCB impresora](/images/posts/octoprint.jpg)

## Desactivación de BT y activación de puerto serie

La Raspberry Pi Zero W (en Raspberry Pi 3 sucede lo mismo) trae un adaptador Bluetooth que tanto en la distribución Raspbian como en la imágen OctoPi utilizada está conectado precisamente a los pines #08 y #10 a los que hemos conectado el puerto serie de la impresora. Antes de continuar necesitamos liberar esta conexión. Para ello debemos editar el fichero `config.txt` que hay en la partición `boot` y añadir (al final por ejemplo) lo siguiente:

```
dtoverlay=pi3-disable-bt
```

Esto podemos hacerlo sin necesidad de arrancar el sistema, montando la microSD en el ordenador. Para el siguiente paso sí necesitamos arrancar el sistema de la tarjeta en la Raspberry. Una vez estemos en la consola (por SSH o conectando una pantalla/teclado/ratón de alguna manera), ejecutaremos:

```
sudo raspi-config
```

Allí acudiremos a la sección `Interfacing options > Serial` y responderemos de la siguiente forma a las dos preguntas que nos hará:

* Would you like a login shell to be accessible over serial? -> No
* Would you like the serial port hardware to be enabled?     -> Yes

Reiniciaremos y ya podremos pasar a trabajar sobre la consola web de Octoprint a la que accederemos abriendo en un navegador la IP de la Raspberry.

## Configuración conexión en Octoprint

Por defecto Octoprint espera encontrar la impresora en un puerto USB de la Raspberry. Al haber cambiado a un puerto serie convencional, tenemos que ayudarle a encontrarlo. Para ello acudimos a Settings (llave inglesa) de Octoprint y en la sección `Serial Connection` añadimos lo siguiente en el cuadro `Additional serial ports`:

    /dev/ttyAMA0

![Octoprint Settings](/images/posts/octoprint_settings.png)

Tras esto podremos volver a la ventana principal y seleccionar dicho puerto en el apartado Connection:

![Octoprint Connection](/images/posts/octoprint_connection.png)

Tras pulsar el botón Connect oiremos cómo la impresora reacciona (al menos en la mía el ventilador de capa se revoluciona unos segundos, aunque también puede suceder por el firmware que tengo instalado) y ya podremos empezar a utilizar Octoprint.

## Webcam

Un complemento muy bueno para Octoprint es una webcam para poder hacer un mejor seguimiento de las impresiones. Tras haber probado con una webcam convencional conectada por USB (aquí se ve una de las ventajas de haberlo dejado libre al conectar la Raspberry a la impresora), me di cuenta de que la cámara oficial de Raspberry se puede encontrar barata (4€) y resulta más adecuada. Adquiriendo [dicha cámara](https://es.aliexpress.com/item/Free-Shipping-5MP-New-Raspberry-pi-2-Camera-Module-Board-REV-1-3-5MP-Webcam-Video/32522482332.html) junto con la versión del [cable especial para Raspberry Pi Zero](https://es.aliexpress.com/item/Raspberry-Pi-Zero-Camera-Cable-16-cm-30-cm-FFC-Cable-for-RPI-Zero-Pi0-Raspberry/32820301186.html), se puede montar fácilmente al chasis de la impresora. En concreto para la Anet A8 se diseña esta pequeña pieza:

[https://www.thingiverse.com/thing:3142521](https://www.thingiverse.com/thing:3142521)
