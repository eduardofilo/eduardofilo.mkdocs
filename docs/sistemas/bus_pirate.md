---
layout: default
permalink: /sistemas/bus_pirate.html
---

# Bus Pirate

## Referencia
![SQL Joins](/images/pages/bpv3_csv2.png)

```
General                                 Protocol interaction
---------------------------------------------------------------------------
?       This help                       (0)     List current macros
=X/|X   Converts X/reverse X            (x)     Macro x
~       Selftest                        [       Start
#       Reset                           ]       Stop
$       Jump to bootloader              {       Start with read
&/%     Delay 1 us/ms                   }       Stop
a/A/@   AUXPIN (low/HI/READ)            "abc"   Send string
b       Set baudrate                    123
c/C     AUX assignment (aux/CS)         0x123
d/D     Measure ADC (once/CONT.)        0b110   Send value
f       Measure frequency               r       Read
g/S     Generate PWM/Servo              /       CLK hi
h       Commandhistory                  \       CLK lo
i       Versioninfo/statusinfo          ^       CLK tick
l/L     Bitorder (msb/LSB)              -       DAT hi
m       Change mode                     _       DAT lo
o       Set output type                 .       DAT read
p/P     Pullup resistors (off/ON)       !       Bit read
s       Script engine                   :       Repeat e.g. r:10
v       Show volts/states               .       Bits to read/write e.g. 0x55.2
w/W     PSU (off/ON)            <x>/<x= >/<0>   Usermacro x/assign x/list all
```

## Enlaces

* [Bus Pirate - Documentación oficial](http://dangerousprototypes.com/docs/Bus_Pirate/es)
* [BusPirate oscilloscope python script](http://hwmayer.blogspot.com.es/2010/09/buspirate-oscilloscope-python-script.html)

## Conexión

```bash
$ screen /dev/buspirate 115200 8N1
```

## Adaptador USB-UART (modo bridge)

Bus Pirate se puede utilizar como un adaptador USB-UART configurándolo en modo UART y activar el macro de modo transparente. Para ello seguir la siguiente secuencia:

```
HiZ>m3
Set serial port speed: (bps)
 1. 300
 2. 1200
 3. 2400
 4. 4800
 5. 9600
 6. 19200
 7. 38400
 8. 57600
 9. 115200
10. BRG raw value

(1)>5
Data bits and parity:
 1. 8, NONE *default
 2. 8, EVEN
 3. 8, ODD
 4. 9, NONE
(1)>1
Stop bits:
 1. 1 *default
 2. 2
(1)>1
Receive polarity:
 1. Idle 1 *default
 2. Idle 0
(1)>1
Select output type:
 1. Open drain (H=Hi-Z, L=GND)
 2. Normal (H=3.3V, L=GND)

(1)>2
Ready
UART>(0)
 0.Macro menu
 1.Transparent bridge
 2. Live monitor
 3.Bridge with flow control
UART>(1)
UART bridge
Reset to exit
Are you sure? y
```

## Adaptador USB-UART (modo debug)

Cuando utilizamos el modo UART en modo debug, tal y como se describe [aquí](http://dangerousprototypes.com/blog/bus-pirate-manual/bus-pirate-uart-guide/), sólo tenemos un buffer de 4 bytes, por lo que es fácil obtener un overrun del mismo. En ese caso, al leer (comando `r`) se nos mostrará el error:

    READ: 0x40 *Bytes dropped*<<<bytes dropped error

En esas situaciones usar el modo transparente o usar el comando 'start' (`[`).
