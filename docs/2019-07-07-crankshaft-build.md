title: 2019-07-07 Compilación OpenAuto para solucionar touch screen
summary: Compilación de OpenAuto.
date: 2019-07-07 21:45:00

Tras una reciente actualización de los Google Play Services de Android, ha dejado de funcionar el touch screen en [Crankshaft](/2018-10-19-crankshaft.html). Parece ser que el problema tiene que ver con el uso de la librería [Protocol Buffers](https://developers.google.com/protocol-buffers/), que ha pasado a ser más estricto en esta última versión de los Play Services y parece que no se había implementado de forma rigurosa en OpenAuto.

[Esta es la issue](https://github.com/opencardev/crankshaft/issues/352) de Crankshaft donde se trata el tema.

La solución pasa por compilar un fork de OpenAuto que uno de los usuarios ha preparado. A continuación se describe el paso a paso para hacer la compilación. El punto de partida es una instalación de la [última versión de Crankshaft](https://github.com/opencardev/crankshaft/releases) en el momento de escribir esto (la `NG Alpha-5 2019-06-08`).

1. Activamos modo DEV (necesario por lo menos para que el sistema se monte en modo lectura/escritura) montando la SD en el ordenador y cambiando el parámetro `DEV_MODE` a 1 (`DEV_MODE=1`) en el fichero `/boot/crankshaft/crankshaft_env.sh`. ([fuente](https://github.com/opencardev/crankshaft/wiki/Dev-Mode-and-Debug-Mode))
2. Montamos la microSD, arrancamos, averiguamos la IP (con Fing por ejemplo) y conectamos por SSH (user: pi; pwd: raspberry).
3. Actualizamos la librería de paquetes e instalamos algunos necesarios:

    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install -y libboost-all-dev libusb-1.0.0-dev cmake libprotobuf-dev protobuf-c-compiler protobuf-compiler librtaudio-dev
    ```

4. Bajamos el branch `development`del fork de [aasdk](https://github.com/abraha2d/aasdk) de [abraha2d](https://github.com/abraha2d):

    ```bash
    $ cd ~
    $ git clone -b development https://github.com/abraha2d/aasdk.git
    ```

5. (OPCIONAL) En el momento de escribir esta guía compilé el commit `361380e7d74ddeaf17afd8cd89882001bb62c77e`. Si nuevos commits provocan problemas, hacer el siguiente checkout:

    ```bash
    $ cd aasdk
    $ git checkout 361380e7d74ddeaf17afd8cd89882001bb62c77e
    ```

6. Compilamos aasdk:

    ```bash
    $ cd ~
    $ mkdir aasdk_build
    $ cd aasdk_build
    $ cmake -DCMAKE_BUILD_TYPE=Release ../aasdk
    $ make
    ```

7. Instalamos algunos paquetes necesarios para compilar `ilclient`:

    ```bash
    $ sudo apt-get install -y libraspberrypi-doc libraspberrypi-dev
    $ cd /opt/vc/src/hello_pi/libs/ilclient
    $ make
    ```

8. Bajamos el branch `crankshaft-ng` del fork de [openauto](https://github.com/abraha2d/openauto) de [abraha2d](https://github.com/abraha2d):

    ```bash
    $ cd ~
    $ git clone -b crankshaft-ng https://github.com/abraha2d/openauto.git
    ```

9. (OPCIONAL) En el momento de escribir esta guía compilé el commit `d56417bfd6b2af9beacb104f8659aea8bff94a72`. Si nuevos commits provocan problemas, hacer el siguiente checkout:

    ```bash
    $ cd openauto
    $ git checkout d56417bfd6b2af9beacb104f8659aea8bff94a72
    ```

10. Compilamos openauto:

    ```bash
    $ cd ~
    $ mkdir openauto_build
    $ cd openauto_build
    $ sudo apt-get install -y libtag1-dev libblkid-dev
    $ cmake -DCMAKE_BUILD_TYPE=Release -DRPI3_BUILD=TRUE -DAASDK_INCLUDE_DIRS="/home/pi/aasdk/include" -DAASDK_LIBRARIES="/home/pi/aasdk/lib/libaasdk.so" -DAASDK_PROTO_INCLUDE_DIRS="/home/pi/aasdk_build" -DAASDK_PROTO_LIBRARIES="/home/pi/aasdk/lib/libaasdk_proto.so" ../openauto
    $ make
    ```

11. Sustituimos el binario compilado por el de la distribución Crankshaft:

    ```bash
    $ sudo cp /home/pi/openauto/bin/autoapp /usr/local/bin/autoapp
    ```

12. Desactivamos el DEV mode del paso 1 y arrancamos normalmente.
