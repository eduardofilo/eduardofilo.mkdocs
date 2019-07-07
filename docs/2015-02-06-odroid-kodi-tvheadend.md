title: 2015-02-06 KODI + Tvheadend
summary: Instalación de Kodi y Tvheadend sobre ODROID C.
date: 2015-02-06 22:33:00

![KODI Logo](/images/posts/kodi-logo.png)

Activamos repositorio multiverse (desde Synaptic) para tener acceso a los firmwares no libres. Actualizamos la base de datos del repositorio e instalamos el paquete `linux-firmware-nonfree`:

```bash
$ sudo apt-get update
$ sudo apt-get install linux-firmware-nonfree
```

Con esto conseguimos instalar el firmware `xc3028-v27.fw` en `/lib/firmware`. Como alternativa dejamos descrito el siguiente [procedimiento](http://www.linuxtv.org/wiki/index.php/Xceive_XC3028/XC2028#How_to_Obtain_the_Firmware):

```bash
$ wget http://www.steventoth.net/linux/xc5000/HVR-12x0-14x0-17x0_1_25_25271_WHQL.zip
$ unzip -j HVR-12x0-14x0-17x0_1_25_25271_WHQL.zip Driver85/hcw85bda.sys
$ wget http://linuxtv.org/hg/v4l-dvb/raw-file/3919b17dc88e/linux/Documentation/video4linux/extract_xc3028.pl
$ perl extract_xc3028.pl
$ sudo cp xc3028-v27.fw /lib/firmware
$ rm extract_xc3028.pl hcw85bda.sys HVR-12x0-14x0-17x0_1_25_25271_WHQL.zip xc3028-v27.fw
```

También se puede localizar aquí el [binario](https://github.com/OpenELEC/dvb-firmware/blob/master/firmware/xc3028-v27.fw)

Parece que mi stick "Pinnacle Systems, Inc. PCTV 330e" necesita un par de ficheros de firmware más que no están incluidos en el paquete `linux-firmware-nonfree`. Se trata de los ficheros `drxd-a2-1.1.fw` y `drxd-b1-1.1.fw` que podemos obtener de [aquí](http://kernellabs.com/firmware/drxd/). Copiamos pues esos dos ficheros a `/lib/firmware`.

Instalamos Tvheadend:

```bash
$ curl http://apt.tvheadend.org/repo.gpg.key | sudo apt-key add -
$ sudo echo "deb http://apt.tvheadend.org/stable wheezy main" >> /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install tvheadend
```

Elegimos username: odroid
Elegimos password: ...
http://localhost:9981

Configuration / DVB Inputs / TV Adapters (seleccionamos Micronas DRXD DVB-T) / General / Adapter configuration / Enabled / Save

Configuration / DVB Inputs / TV Adapters (seleccionamos Micronas DRXD DVB-T) / General / Tools / Add DVB Network by location... / Spain / es_Zaragoza

No funciona el adaptador TDT hasta que actualizo el kernel que había quedado en estado kept back. Los paquetes en esa situación se actualizan con `sudo apt-get dist-upgrade`.
