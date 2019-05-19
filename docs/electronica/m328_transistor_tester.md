---
layout: default
permalink: /electronica/m328_transistor_tester.html
---

# M328 Transistor Tester

<iframe width="853" height="480" src="https://www.youtube.com/embed/Oda9WaySOvM?list=PLo19xZgW7bjWW9PQaocDAEdNzO0hC4pOB" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Enlaces

* [2016 DIY KITS ATMEAG328P M328 Transistor Tester LCR Diode Capacitance ESR meter PWM Square wave Signal Generator with case](https://es.aliexpress.com/item/2016-DIY-KITS-ATMEAG328P-M328-Transistor-Tester-LCR-Diode-Capacitance-ESR-meter-PWM-Square-wave-Signal/32808555770.html): ~12€
* [M328 Transistor Tester manual](/images/pages/ttester.pdf)

## Enumeración funciones

Firmware 1.12k

* **Transistor**: Medidor de transistores.
* **Frecuency**: Medidor de frecuencias. Conectar las puntas en la entrada PWM (superior).
* **f-Generator**: Generador de frecuencias. Conectar las puntas en la salida PWM (inferior).
* **10-bit PWM**: Generador de señal PWM. Conectar las puntas en la salida PWM (inferior).
* **C+ESR@TP1:3**: Capacímetro con posibilidad de medir en placa ya que genera tensiones de ~300mV. Conectar un par de puntas en las entradas 1 y 3.
* **Medidor de inductancias**:
* **Capacímetro**: No sirve para medir en placa ya que genera tensiones de 5V. Descargar los condensadores antes de aplicarlos al medidor.
* **DS18B20**:
* **C(uF)-correction**: Calibración del capacímetro.
* **IR_Decoder**: Implementa un par de protocolos de transmisión de datos por infrarrojos. Hay que conectar un receptor IR en las entradas 1, 2 y 3.
* **IR_Encoder**: Implementa un par de protocolos de transmisión de datos por infrarrojos. Hay que conectar un LED emisor de IR en la salida PWM (inferior).
* **DHT11**:
* **Selftest**: Calibración del tester.
* **Voltage**: Voltímetro. Conectar las puntas en la entrada de voltímetro (inferior).
* **FrontColor**: Color RGB de los caracteres.
* **BackColor**: Color RGB del fondo.
* **Show data**: Muestra los datos de calibración y el juego de gráficos y caracteres.
* **Switch off**: Apagado.
