title: 2019-07-07 Compilación OpenAuto para solucionar touch screen
summary: Compilación de OpenAuto.
date: 2019-07-07 21:45:00

Tras una reciente actualización de los Google Play Services de Android, ha dejado de funcionar el touch screen en [Crankshaft](/2018-10-19-crankshaft.html). Parece ser que el problema tiene que ver con el uso de la librería [Protocol Buffers](https://developers.google.com/protocol-buffers/), que ha pasado a ser más estricto en esta última versión de los Play Services y parece que no se había implementado de forma rigurosa en OpenAuto.

En [este hilo](https://github.com/opencardev/crankshaft/issues/352) de los foros de Crankshaft se habla sobre el tema.

La solución pasa por compilar un fork de OpenAuto que uno de los usuarios ha preparado. A continuación se describe el paso a paso para hacer la compilación. El punto de partida es una instalación de la [última versión de Crankshaft](https://github.com/opencardev/crankshaft/releases) en el momento de escribir esto (la `NG Alpha-5 2019-06-08`).

1. Activamos modo DEV (necesario por lo menos para que el sistema se monte en modo lectura/escritura) montando la SD en el ordenador y cambiando el parámetro `DEV_MODE` a 1 (`DEV_MODE=1`) en el fichero `/boot/crankshaft/crankshaft_env.sh`. ([fuente](https://github.com/opencardev/crankshaft/wiki/Dev-Mode-and-Debug-Mode))
2. Monto la microSD, arranco, averiguo la IP (con Fing por ejemplo) y conecto por SSH (user: pi; pwd: raspberry).
3. Actualizo la librería de paquetes e instalo algunos necesarios:

    ```bash
    $ sudo apt-get update
    $ sudo apt-get install -y libboost-all-dev libusb-1.0.0-dev libssl-dev cmake libprotobuf-dev protobuf-c-compiler protobuf-compiler
    $ sudo apt-get install -y libqt5multimedia5 libqt5multimedia5-plugins libqt5multimediawidgets5 qtmultimedia5-dev libqt5bluetooth5 libqt5bluetooth5-bin qtconnectivity5-dev pulseaudio librtaudio-dev librtaudio5a
    ```

4. Bajo el fork de [aasdk](https://github.com/abraha2d/aasdk) de [abraha2d](https://github.com/abraha2d) y compilo:

    ```bash
    $ cd ~
    $ wget --no-check-certificate https://github.com/abraha2d/aasdk/archive/development.zip
    $ unzip development.zip
    $ mv aasdk-development/ aasdk
    $ mkdir aasdk_build
    $ cd aasdk_build
    $ cmake -DCMAKE_BUILD_TYPE=Release ../aasdk
    $ make
    ```

5. Instalo algunos paquetes necesarios para compilar `ilclient`:

    ```bash
    $ sudo apt-get install -y libraspberrypi-doc libraspberrypi-dev
    $ cd /opt/vc/src/hello_pi/libs/ilclient
    $ make
    ```

6. Bajo el fork de [openauto](https://github.com/abraha2d/openauto) de [abraha2d](https://github.com/abraha2d) y compilo:

    ```bash
    $ cd ~
    $ wget --no-check-certificate https://github.com/abraha2d/openauto/archive/crankshaft-ng.zip
    $ unzip crankshaft-ng.zip
    $ mv openauto-crankshaft-ng/ openauto
    $ mkdir openauto_build
    $ cd openauto_build
    $ sudo apt-get install libtag1-dev libblkid-dev
    $ cmake -DCMAKE_BUILD_TYPE=Release -DRPI3_BUILD=TRUE -DAASDK_INCLUDE_DIRS="/home/pi/aasdk/include" -DAASDK_LIBRARIES="/home/pi/aasdk/lib/libaasdk.so" -DAASDK_PROTO_INCLUDE_DIRS="/home/pi/aasdk_build" -DAASDK_PROTO_LIBRARIES="/home/pi/aasdk/lib/libaasdk_proto.so" ../openauto
    $ make
    ```

7. Sustituyo el binario compilado por el de la distribución Crankshaft:

    ```bash
    $ sudo cp /home/pi/openauto/bin/autoapp /usr/local/bin/autoapp
    ```

8. Desactivamos el DEV mode del paso 1 y arrancamos normalmente.
