title: 2018-10-18 Crankshaft - AndroidAuto sobre Raspberry Pi
summary: Montaje de una Raspberry Pi con pantalla táctil de 7" en la consola de un Opel Corsa modelo D.
date: 2018-10-18 22:30:00

![Crankshaft](/images/posts/crankshaft.jpg)

Se describe a continuación el montaje de una Raspberry Pi con pantalla táctil de 7" en la consola de un Opel Corsa modelo D (2012), en sustitución del radio CD que llevaba de serie, para ser utilizada como terminal compatible de AndroidAuto.

La pantalla consiste en la oficial táctil de 7" de la fundación Raspberry Pi que tiene aproximadamente las medidas del hueco 2DIN que deja el radio CD del coche. Para su sujección en el hueco de la radio se crean un par de piezas que se fabrican con una impresora 3D.

## Componentes

* [Extractor radio](https://es.aliexpress.com/item/1-Pair-90mm-Car-Radio-Stereo-Removal-Key-Tool-For-Vauxhall-Opel-Corsa-C-Meriva-PC5/32767508369.html)
* [Raspberry Pi 3](https://www.amazon.es/dp/B01CD5VC92)
* [Pantalla de 7" táctil oficial Raspberry Pi](https://es.rs-online.com/web/p/kits-de-desarrollo-de-display-de-graficos/8997466/)
* [Micrófono USB](https://es.aliexpress.com/item/Mini-Condenser-Microphone-USB-Lavalier-Microfone-for-Computer-PC-Laptop-etc-with-USB-connector/32805808159.html)
* [Circuito de alimentación](https://www.mausberrycircuits.com/collections/frontpage/products/3a-car-supply-switch-1)
* Tarjeta microSD
* LED
* Resistencia 220Ω
* 4x Tornillo M3x10
* [Cable con conector JST](https://es.aliexpress.com/store/product/2-10Pairs-100-150mm-2-Pin-Connector-JST-Plug-Cable-Male-Female-For-RC-BEC-Battery/1994020_32870752993.html)
* [Cables de pin hembra-hembra](https://es.aliexpress.com/item/Electrical-Durable-Cables-40pcs-20cm-2-54mm-1p-1p-Pin-Female-to-Female-Color-Breadboard-Cable/32697942452.html)
* [Piezas plásticas de sujección impresas en 3D](https://www.thingiverse.com/thing:3162930)

## Preparación sistema

El sistema que cargaremos en la tarjeta microSD va a ser una versión especial de Raspbian con el paquete [OpenAuto](https://github.com/f1xpl/openauto) preinstalado que se llama Crankshaft y cuya imágen puede descargarse de [aquí](https://github.com/opencardev/crankshaft/releases). Transferimos la imagen a la microSD con un programa como [Etcher](https://etcher.io/).

## Retirando el radio CD

Esto es lo que vamos a perder:

![Opel Radio CD](/images/posts/crankshaft_opel_radio_cd.jpg)

Para extraerlo necesitamos la herramienta que se incluye en la lista de componentes, que se introduce por los agujeros que hay a ambos lados (en la foto, los del lado izquierdo están tapados por el control remoto del manos libres y el tag NFC). El radio CD saldrá limpiamente salvo por los cables de la antena y el conector principal que tendremos que desconectar.

## Circuito de alimentación

La correcta alimentación de la Raspberry Pi a partir de la batería del coche supone uno de los problemas más complejos de resolver en este proyecto. Más adelante planteamos los puntos conflictivos. Empezaremos localizando en el conector del radio CD los terminales de masa (GND), +12V constantes y de +12V asociados al contacto. Para empezar el terminal de +12V asociados al contacto no parece estar presente.

![Conector Radio CD](/images/posts/crankshaft_conector_radio_cd.jpg)

Seguramente el coche informa al Radio CD de que el contacto se ha quitado por medio del CAN bus. Afortunadamente mi coche traía montado de serie un manos libres Parrot en cuya instalación se hizo una conexión con los 12V asociados al contacto en el mazo de cables del vehículo. En otro caso tocará empalmar un cable en algún lugar donde sepamos que existe esa señal (en el conector de mechero por ejemplo).

Una vez localizados los tres cables indicados, podemos plantear la alimentación de muchas formas. Incialmente opté por la vía simple y compré un pequeño y barato [circuito conversor de 12V a 5V](https://es.aliexpress.com/item/1PCS-power-module-Adjustable-MP1584EN-DC-DC3A-power-step-down-descending-output-module-12-v9v5v3-LM2596/32624261712.html) (en realidad la salida es regulable entre 0.8V y 20V) y lo conecté directamente al cable de contacto. De esta forma al dar contacto en el coche, la Raspberry Pi se encendía y al quitarlo se apagaba. Funcionó muy bien, pero este montaje tiene el inconveniente de que si no se apaga previamente la Raspberry desde los menús, se corre el riesgo de que el sistema instalado en la microSD se corrompa. Pensé que recordaría hacerlo cada vez que fuera a parar el coche, pero la realidad fue que aproximadamente la mitad de las veces olvidaba hacerlo, así que pasé a un sistema más sofisticado. Creo que las últimas versiones de Crankshaft montan la tarjeta microSD en modo sólo lectura, por lo que las desconexiones abruptas puede que en realidad no sean un problema, pero me quedo más tranquilo con el montaje que adopté posteriormente y que describo a continuación.

Me hice con el circuito de Mausberry Circuits que hay en la lista de componentes. Decir que se agota fácilmente. De hecho cuando fui a comprarlo no estaba disponible, pero me apunté a la notificación por mail que informa cuando vuelve a haber stock y aproximadamente en un mes pude adquirirlo. Hay varios circuitos alternativos (como [éste otro](https://bluewavestudio.io/index.php/bluewave-shop/power-supply/bws-car-ps-v1-usb-detail)) pero el de Mausberry Circuits me gusta más porque tiene un doble canal de comunicación con la Raspberry de manera que no sólo avisa a ésta de que debe apagarse controladamente, sino que cuando se da cuenta de que ya lo ha hecho, corta la alimentación completamente. Otros circuitos mantienen la alimentación, lo que produce un consumo de standby que en mis mediciones ronda los 50mA, lo que puede drenar la batería en alrededor de 4 semanas.

![Mausberry Circuits Car Switch](/images/posts/crankshaft_car_switch.jpg)

Las conexiones de entrada al Car Switch de Mausberry Circuits serán pues las 3 mencionadas antes, que debemos localizar en el hueco de la consola que deja el radio CD:

* GND (cable negro)
* +12V constantes (cable amarillo)
* +12V contacto (cable rojo)

Comentar en este punto que es muy recomendable situar un fusible en la toma o tomas de 12V que utilicemos del coche. Afortunadamente contaba con varios cables con fusible integrado de viejas instalaciones de manos libres que he acumulado con los años.

En cuanto a las salidas, los 5V que necesitamos para la Raspberry los podemos coger de uno de los dos puertos USB pero yo preferí soldar cables tanto en el Car Switch como en la Raspberry. Primero para evitar la aparatosidad de un cable microUSB en el interior del salpicadero y segundo para evitar que se produzcan desconexiones con las vibraciones del coche. Así pues soldé un cable con conector rápido (de [tipo JST](https://es.aliexpress.com/store/product/2-10Pairs-100-150mm-2-Pin-Connector-JST-Plug-Cable-Male-Female-For-RC-BEC-Battery/1994020_32870752993.html)) a las salidas 5V y GND que se ven en la parte inferior derecha de la foto del Car Switch. Soldé también en paralelo en estos mismos pines un LED con su correspondiente resistencia de protección (la resistencia de 220Ω que se indicaba en la lista de componentes) para así tener indicación visual de si el Car Switch ha cortado definitivamente la alimentación y poder abandonar el coche tranquilo.

Por último colocamos dos cables en los pines IN y OUT de la parte superior derecha que más adelante conectaremos el GPIO de la Raspberry.

El resultado final es éste:

![Mausberry Circuits Car Switch](/images/posts/crankshaft_car_switch2.jpg)

Una de las piezas diseñadas para imprimir en 3D que enlazo más adelante, es una caja para proteger el conjunto del Car Switch y sus conexiones. La caja tiene una pequeña ventana que queda a la altura de uno de los dos puertos USB. Conectando un alargador USB (hembra-macho) a través de ese hueco, aseguramos que el circuito no se mueva del interior de la caja. Este cable alargador lo pasé hacia la parte baja junto con el cable USB normal donde conectaremos el teléfono, para así tener un puerto de carga USB normal "para invitados" o para cualquier otra necesidad (por ejemplo carga rápida del móvil, ya que el Car Switch es capaz de dar 3A). En caso de no situar este cable alargador, se recomienda utilizar algún tipo de cinta para evitar que el Car Switch se salga de la caja.

Por último, el otro extremo del conector de alimentación (JST) se suelda en la Raspberry Pi en los puntos designados con PP2 (+5V; en la foto el rótulo está tapado por el propio cable) y PP5 (GND). Las siguientes fotos corresponden a la Raspberry Pi 3 Model B. En el Model B+ he podido comprobar que los puntos están en la misma posición. En [este artículo](https://raspberrypi.stackexchange.com/questions/76653/powering-raspberry-pi-with-broken-micro-usb-connector) se puede consultar el esquemático que detalla los varios puntos de alimentación que existen.

![Alimentación Raspberry](/images/posts/crankshaft_raspberry_alimentacion1.jpg)

![Alimentación Raspberry](/images/posts/crankshaft_raspberry_alimentacion2.jpg)

Para que el circuito Car Switch y la Raspberry Pi se comuniquen, además de situar los dos cables de pin, hay que instalar un script en el sistema de la Raspberry para que monitorice el pin que le informa del estado del contacto del coche. El sistema que instalamos en uno de los primeros apartados (Crankshaft) está basado en Raspbian, así que se puede instalar el script siguiendo las instrucciones correspondientes a este sistema en la sección "Installing the script" de la página [Car Setup](http://mausberrycircuits.com/pages/car-setup).

También se puede instalar manualmente copiando el script en la ruta `/etc/switch.sh`, dándole permisos de ejecución y añadiendo lo siguiente al final del fichero `/etc/rc.local` (justo antes del `exit 0`) para que se ejecute en el arranque:

```
/etc/switch.sh &
```

El script es éste:

```bash
#!/bin/bash

#this is the GPIO pin connected to the lead on switch labeled OUT
GPIOpin1=23

#this is the GPIO pin connected to the lead on switch labeled IN
GPIOpin2=24

#Enter the shutdown delay in minutes
delay=0

echo "$GPIOpin1" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio$GPIOpin1/direction
echo "$GPIOpin2" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$GPIOpin2/direction
echo "1" > /sys/class/gpio/gpio$GPIOpin2/value
let minute=$delay*60
SD=0
SS=0
SS2=0
while [ 1 = 1 ]; do
power=$(cat /sys/class/gpio/gpio$GPIOpin1/value)
uptime=$(</proc/uptime)
uptime=${uptime%%.*}
current=$uptime
if [ $power = 1 ] && [ $SD = 0 ]
then
SD=1
SS=${uptime%%.*}
fi

if [ $power = 1 ] && [ $SD = 1 ]
then
SS2=${uptime%%.*}
fi

if [ "$((uptime - SS))" -gt "$minute" ] && [ $SD = 1 ] && [ $power = 1 ]
then
poweroff
SD=3
fi

if [ "$((uptime - SS2))" -gt 20 ] && [ $SD = 1 ]
then
SD=0
fi

sleep 1
done
```

En el script podemos ver los pines del GPIO que utilizaremos y al que por tanto conectaremos los dos cables de pin que vienen del Car Switch:

* `Car Switch: IN  <-> GPIO24 :Raspberry`
* `Car Switch: OUT <-> GPIO23 :Raspberry`

En el listado anterior hemos indicado los pines del GPIO de Raspberry con su nombre, no con su número (una confusión muy habitual). En la siguiente imágen los nombres están en el exterior del rectángulo rojo y los números en el interior (rodeados a su vez por un círculo).

![Raspberry Pi GPIO Layout Model B+](/images/posts/Raspberry-Pi-GPIO-Layout-Model-B-Plus.png)

## Montaje de Raspberry Pi sobre pantalla

La pantalla que utilizaremos tiene un soporte para la Raspberry Pi en la parte trasera. Atornillaremos los separadores y colocaremos el cable de cinta que une la pantalla con el conector Display de la Raspberry. Falta colocar unos cables de pin para alimentar y comunicar la pantalla con la Raspberry, cosa que se puede hacer con simples cables de pin hembra-hembra (que de hecho vienen con la pantalla). Para evitar desconexiones por las vibraciones de la marcha del coche, en lugar de utilizar los cables de pin preparé un pequeño cable con un par de tiras de pin hembra (una simple para el lado de la pantalla y otra doble para el lado de la Raspberry). El resultado es más compacto y seguro y tiene este aspecto:

![Cable pantalla](/images/posts/crankshaft_cable_pantalla1.jpg)

![Cable pantalla](/images/posts/crankshaft_cable_pantalla2.jpg)

El pineado es como sigue:

* `Pantalla: 5V  <-> PIN#02 :Raspberry`
* `Pantalla: GND <-> PIN#06 :Raspberry`
* `Pantalla: SCL <-> PIN#05 :Raspberry`
* `Pantalla: SDA <-> PIN#03 :Raspberry`

En el listado anterior hemos indicado los pines del GPIO de Raspberry con su número, no con su nombre (al contrario de cuando hemos descrito los cables de pin que comunican con Car Switch).

## Cableado

Se describe a continuación el conjunto de conexiones que haremos entre todos los componentes justo antes de hacer la sujección final de la pantalla que se describe en el apartado siguiente:

1. Conexión del Car Switch a las tomas de alimentación del coche tal y como hemos comentado en el apartado correspondiente:
    * Toma 12V constantes
    * Toma 12V contacto
    * Toma de masa
2. Conexión de pines entre Car Switch y Raspberry Pi también descrito antes:
    * `Car Switch: IN  <-> GPIO24 :Raspberry`
    * `Car Switch: OUT <-> GPIO23 :Raspberry`
3. Conector JST de alimentación de Raspberry Pi.
4. Micrófono USB conectado a Raspberry Pi.
5. Cable micro USB (o type-C en mi caso) conectado a Raspberry Pi y que pasaremos por el interior de la consola para poder conectar el móvil en la zona de la bandeja sujeta vasos que hay delante de la palanca de marchas.
6. (Opcional) Cable alargador USB (macho-hembra) conectado a Car Switch y que pasaremos por el interior de la consola para tener un puerto de carga rápido en la zona de la bandeja sujeta vasos que hay delante de la palanca de marchas.

## Sujección pantalla a consola coche

Para fijar el conjunto pantalla-Raspberry al hueco de la consola dejado por el radio CD, utilizaremos unas piezas impresas en 3D. El enlace para descargar los STL's (y scad por si se quieren modificar) es el siguiente:

[https://www.thingiverse.com/thing:3162930](https://www.thingiverse.com/thing:3162930)

Básicamente son dos piezas, la que fija la pantalla al hueco y un marco para esconder los huecos que quedan alrededor de la pantalla y para que el conjunto se integre estéticamente en la consola del coche. Hay dos versiones de la pieza que fija la pantalla, una completa y otra dividida en varias para facilitar su impresión sin necesidad de soportes. En caso de imprimir la versión dividida en varias piezas (se recomienda), no es necesario pegar las parte ya que por su disposición se apoyan unas a otras sin que ocurra prácticamente desplazamiento. Una aclaración sobre una pieza que puede parecer extraña, me refiero a una estrecha y sobre todo fina lámina de unos 10cm de largo. Sirve para equilibrar el apoyo de la pantalla, que en el lado opuesto a donde se coloca esta pieza (el izquierdo mirándola de frente), tiene una lámina (creo que tiene que ver con el digitalizador táctil) que sobresale por este lado. Al ser una lámina tan fina, si se prefiere se puede obviar.

Una vez aplicada la pieza o piezas a la pantalla, queda así:

![Soporte pantalla](/images/posts/crankshaft_soporte_pantalla.jpg)

Los tornillos utilizados son M3x10. La pieza soporte queda fija en el hueco por las 3 lengüetas superiores y la inferior más larga. La forma de extraer el conjunto es introducir una espátula como las que se utilizan para untar la mantequilla por el hueco que hay cerca de la lengüeta inferior. Haciendo palanca de manera que la lengüeta se desenganche, y haciendo bascular el conjunto desde abajo, debería ser posible sacar la pantalla y su soporte.

A ambos lados del soporte y cerca del borde superior, quedan dos huecos por los que podremos sacar los cables del micrófono y el LED.

![Hueco soporte](/images/posts/crankshaft_hueco_soporte.jpg)

La electrónica del micrófono comprado está en el conector USB, lo que lo hace aparatoso y grande. Para evitar que el cable chocase con la pared interior del hueco, se modificó la salida del cable para hacerla acodada. Además se cortó el cable que sólo necesitamos que tenga unos 20cm y se aprovechó para retirar el chasis del micrófono (el pequeño cilindro metálico que se ve en la foto) que no se necesita.

![Micrófono](/images/posts/crankshaft_mic1.jpg)

![Micrófono](/images/posts/crankshaft_mic2.jpg)

El resultado de la primera versión del marco (todavía sin el LED que incorporé al cambiar el circuito de alimentación) puede verse a continuación. Es conveniente imprimir a 0,1mm de capa debido al ángulo tan pequeño que tienen las capas superiores del marco (por la extraña forma de la consola del Corsa en esa zona).

![Resultado PLA](/images/posts/crankshaft_resultado.jpg)

Por último, comentar que la primera versión del marco impresa en PLA se derritió una tarde que el coche quedó aparcado al sol.

![Marco derretido](/images/posts/crankshaft_derretido.jpg)

La solución consistió en imprimir las piezas en ABS. Fue mucho más difícil de imprimir, pero ciertamente este material tiene ventajas como poder lijar la pieza (y así hacer desaparecer el estriado del cambio de capa) y por supuesto resistir sin problemas el calor que se acumula al exponer el coche al sol durante horas. El resultado de la segunda versión en ABS lijado.

![Resultado ABS](/images/posts/crankshaft_resultado2.jpg)

Se ofrecen dos versiones del marco, una en una pieza y otra en dos que luego habrá que pegar, ya que es una pieza ancha que puede no entrar en muchas camas de impresoras 3D (como fue mi caso). La sujección del marco se hará por medio de unos pocos puntos de cinta de doble cara.
