title: 2019-04-20 Composite mod en consola Pong
summary: Composite mod en vieja consola Pong basada en chip AY-3-8500.
date: 2019-04-20 16:00:00

Uno de los mejores recuerdos de la niñez fue recibir esta pequeña consola como regalo de mi abuela traída de un viaje a Canarias a finales de los 70. Nunca dejó de funcionar del todo, pero acumuló desperfectos como los lógicos problemas en los potenciómetros que contienen los mandos y sobre todo la incomodidad de tener únicamente una salida de RF o antena para conectar al televisor. La unidad que tengo, por lo que he podido averiguar, fue un modelo que apareció bajo diversas denominaciones. La mía presenta la marca REGINA y según la caja es el modelo [T-338](http://www.old-computers.com/museum/computer.asp?st=1&c=685).

![Regina Pong](/images/posts/regina_pong.jpg)

Investigando la modificación para conseguir una salida de vídeo compuesto encontré que la consola está basada en el chip [AY-3-8500](https://en.wikipedia.org/wiki/AY-3-8500) de General Instruments:

![AY-3-8500](/images/posts/regina_pong_ay-3-8500.jpg)

Este chip tiene una historia interesante. Fue todo un éxito en la época y es prácticamente seguro encontrar uno de estos chips, sus clones o alguna de sus evoluciones en cualquier consola de juegos tipo Pong de finales de los 70. El fabricante produjo tantas unidades que, aunque no se fabrica desde entonces, aún hoy es posible encontrarlo nuevo. He conseguido un par para montar alguna unidad desde cero dado que el esquemático es extremadamente sencillo y aparece en la [documentación del integrado](/files/posts/GI-Games-reference-circuits-1978.pdf).

![AY-3-8500 pinout](/images/posts/regina_pong_ay-3-8500_pinout.jpg)

![Pong esquemático](/images/posts/regina_pong_esquematico.jpg)

La señal de vídeo en el patillaje del chip aparece descompuesta en los siguientes 5 pines:

* 6: Ball output
* 9: Right player output
* 10: Left player output
* 16: Sync output
* 24: Score and field output

Esto es así porque existía la opción de incorporar un coprocesador de video que permitía colorear los distintos componentes de la salida (los jugadores, la bola y el resto del campo). El esquemático anterior corresponde a la versión sin este coprocesador y por tanto se limita a sumar las cuatro salidas (sin contar la señal de sync) con una puerta lógica OR de cuatro entradas ([4072](https://upload.wikimedia.org/wikipedia/commons/f/f8/4072_Pinout.svg)). La placa de mi unidad sin embargo difiere del esquemático oficial. Observo que no existe el integrado 4072 con las puertas OR de cuatro entradas:

![Regina placa 1](/images/posts/regina_pong_placa1.jpg)

![Regina placa 2](/images/posts/regina_pong_placa2.jpg)

En su lugar se utilizan los cuatro diodos que marco en la segunda foto. Realmente los diodos son equivalentes a la puerta OR. Una vez localizadas las señales implicadas, era cuestión de encontrar el circuito que las llevara hasta una señal de vídeo compuesto estándar. Hay poco más que hacer que sumarlas y normalizarlas hasta los niveles que se esperan en una señal de este tipo. Al haber tantas consolas en el mercado es fácil encontrar varias versiones del circuito necesario realizados por otros aficionados. Pongo algunos enlaces a continuación:

* [Breathing New (Composite) Life Into a Binatone Pong Console](https://mrpjevans.com/binatone-composite-mod/)
* [Binatone TV Master MK 4 Composite Video Mod](https://www.petervis.com/gallery/Toys_and_Games/binatone-tv-master-mk-4-composite-video-mod/binatone-tv-master-mk-4-composite-video-mod.html)
* [AV modding a pong unit...even possible?](http://atariage.com/forums/topic/194029-av-modding-a-pong-uniteven-possible/#entry2469505)
* [Hacking Composite Video into a 1977 Pong Console](https://www.youtube.com/watch?v=7uTEthm7jqg)

Casi todos los artículos leídos hacen referencia al mismo esquema de una página que ya no existe, pero que afortunadamente todo el mundo ha reproducido en sus sitios, cosa que yo hago aquí también:

![Esquemático mod](/images/posts/regina_pong_esquematico_mod.gif)

Así pues, para realizar este circuito necesitaremos los siguientes componentes:

* 1x [9V – 5V Regulador de tensión 7805](https://www.aliexpress.com/item/10pcs-lot-L7805CV-L7805-7805-LM7805-KA7805-Voltage-Regulator-5V-TO-220-In-Stock/32892570189.html)
* 2x [Resistencia 75Ω](https://www.aliexpress.com/item/100pcs-1-4W-5-Carbon-Film-Resistor-68-75-82-91-100-ohm/32834081570.html)
* 1x [Resistencia 750Ω](https://www.aliexpress.com/item/100pcs-1-4W-5-Carbon-Film-Resistor-510-560-620-680-750-ohm/32834956196.html)
* 1x [Transistor 2N3904](https://www.aliexpress.com/item/100PCS-2N3904-TO-92-TO92-NPN-General-Purpose-Transistor-New-original/32843804468.html)
* 1x [Diodo 1N914](https://www.aliexpress.com/item/100Pcs-1N914-DO-35-High-Conductance-Fast-Diode/32224572752.html)
* 1x [Condensador electrolítico 100μF / 16V](https://www.aliexpress.com/item/20-10-5pcs-aluminum-electrolytic-capacitor-6-3V-10V-16V-25V-35V-10UF-100UF-1000UF-22UF/32964973366.html)
* 1x [Conector RCA](https://www.aliexpress.com/item/10pcs-Red-10pcs-Black-RCA-Panel-Mount-Connector-RCA-Female-Socket-RCA-Panel-Mount-Audio-Socket/32840529402.html)

Utilizaremos una porción de stripboard para montarlo. Lo que sigue es la simulación del circuito con Fritzing:

![Circuito mod Fritzing](/images/posts/regina_pong_composite_mod_bb.png)

Realmente a la hora de soldar se puede compactar más, pero he ahuecado los componentes para que no se solapen en la visualización. Podemos comprobar en la vista esquemática de Fritzing que el circuito es correcto:

![Esquemático mod Fritzing](/images/posts/regina_pong_composite_mod_esquematico.png)

Adjunto el [fichero Fritzing](/files/posts/regina_pong_composite_mod.fzz) por si ayuda con el montaje.

Éste es el resultado en la realidad:

![Circuito mod](/images/posts/regina_pong_mod_circuito1.jpg)

Lo siguiente es localizar sobre la placa de mi consola los puntos de entrada al circuito. Estudiando un poco las pistas llego a la conclusión de que en mi caso son los siguientes:

![Puntos soldadura mod](/images/posts/regina_pong_points1.jpg)
![Puntos soldadura mod](/images/posts/regina_pong_points2.jpg)

El punto 2 es donde se reunen las cuatro señales y se suman con los diodos como comentábamos antes. Ya sólo queda alojar el pequeño circuito en el interior de la caja. Encuentro hueco en la parte inferior y sujeto la pequeña placa con cola caliente:

![Placa pegada](/images/posts/regina_pong_placa_pegada.jpg)

Para la salida retiro los espadines que sujetaban el viejo cable de antena que salía por la parte superior, para hacer hueco a un conector RCA que sujeto agrandando el agujero del cable RF:

![Placa pegada](/images/posts/regina_pong_conector_RCA.jpg)

Ya sólo queda hacer las conexiones entre todas las piezas y cerrar el conjunto:

![Placa pegada](/images/posts/regina_pong_final.jpg)

Además de los componentes para el circuito de modificación, adquirí también [potenciómetros de 1MΩ](https://www.aliexpress.com/item/10PCS-WH148-Potentiometer-Kit-Single-Joint-B1K-2K-5K-10K-20K-50K-100K-250K-500K-1M/32908524525.html) para sustituir los que llevan los mandos. El resultado:

<iframe width="853" height="480" src="https://www.youtube.com/embed/OedojdkP4_E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Al conocer el proyecto un amigo me ha pasado su consola de aquella época para realizar una modificación equivalente. Abriéndola encuentro que efectivamente está basada en el mismo integrado, aunque ésta parece montada con mejores componentes y sí incluye el integrado con las puertas OR para el sumado de las salidas de vídeo del chip:

![Teletenis](/images/posts/regina_pong_teletenis_jorge.jpg)
