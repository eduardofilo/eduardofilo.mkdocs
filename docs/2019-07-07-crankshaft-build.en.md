title: Compiling OpenAuto to fix the touch screen
summary: Compiling OpenAuto after the touch screen stopped working due to a Google Play Services update.
date: 2019-07-07 21:45:00

After a recent update to Android Google Play Services, the touch screen in [Crankshaft](2018-10-19-crankshaft.md) stopped working. It seems that the problem is related to the use of the [Protocol Buffers](https://developers.google.com/protocol-buffers/) library, which has become stricter in this latest version of Play Services and apparently had not been implemented rigorously in OpenAuto.

[This is the issue](https://github.com/opencardev/crankshaft/issues/352) in Crankshaft where the topic is discussed.

The solution is to compile a fork of OpenAuto that one of the users prepared. Below is the step-by-step process to perform the build. The starting point is an installation of the [latest version of Crankshaft](https://github.com/opencardev/crankshaft/releases) available at the time of writing this (the `NG Alpha-5 2019-06-08`).

1. Enable DEV mode (needed at least so the system is mounted in read/write mode) by mounting the SD card on your computer and changing the `DEV_MODE` parameter to 1 (`DEV_MODE=1`) in the `/boot/crankshaft/crankshaft_env.sh` file. ([source](https://github.com/opencardev/crankshaft/wiki/Dev-Mode-and-Debug-Mode))
2. Mount the microSD, boot the system, find out its IP address (using Fing for example), and connect over SSH (`user: pi`; `pwd: raspberry`).
3. Update the package library and install some required packages:

    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install -y libboost-all-dev libusb-1.0.0-dev cmake libprotobuf-dev protobuf-c-compiler protobuf-compiler librtaudio-dev
    ```

4. Download the `development` branch of [abraha2d](https://github.com/abraha2d)'s [aasdk](https://github.com/abraha2d/aasdk) fork:

    ```bash
    $ cd ~
    $ git clone -b development https://github.com/abraha2d/aasdk.git
    ```

5. (OPTIONAL) At the time of writing this guide I built commit `361380e7d74ddeaf17afd8cd89882001bb62c77e`. If newer commits cause problems, check out the following revision:

    ```bash
    $ cd aasdk
    $ git checkout 361380e7d74ddeaf17afd8cd89882001bb62c77e
    ```

6. Build `aasdk`:

    ```bash
    $ cd ~
    $ mkdir aasdk_build
    $ cd aasdk_build
    $ cmake -DCMAKE_BUILD_TYPE=Release ../aasdk
    $ make
    ```

7. Install some packages required to compile `ilclient`:

    ```bash
    $ sudo apt-get install -y libraspberrypi-doc libraspberrypi-dev
    $ cd /opt/vc/src/hello_pi/libs/ilclient
    $ make
    ```

8. Download the `crankshaft-ng` branch of [abraha2d](https://github.com/abraha2d)'s [openauto](https://github.com/abraha2d/openauto) fork:

    ```bash
    $ cd ~
    $ git clone -b crankshaft-ng https://github.com/abraha2d/openauto.git
    ```

9. (OPTIONAL) At the time of writing this guide I built commit `d56417bfd6b2af9beacb104f8659aea8bff94a72`. If newer commits cause problems, check out the following revision:

    ```bash
    $ cd openauto
    $ git checkout d56417bfd6b2af9beacb104f8659aea8bff94a72
    ```

10. Build `openauto`:

    ```bash
    $ cd ~
    $ mkdir openauto_build
    $ cd openauto_build
    $ sudo apt-get install -y libtag1-dev libblkid-dev
    $ cmake -DCMAKE_BUILD_TYPE=Release -DRPI3_BUILD=TRUE -DAASDK_INCLUDE_DIRS="/home/pi/aasdk/include" -DAASDK_LIBRARIES="/home/pi/aasdk/lib/libaasdk.so" -DAASDK_PROTO_INCLUDE_DIRS="/home/pi/aasdk_build" -DAASDK_PROTO_LIBRARIES="/home/pi/aasdk/lib/libaasdk_proto.so" ../openauto
    $ make
    ```

11. Replace the Crankshaft distribution binary with the compiled one:

    ```bash
    $ sudo cp /home/pi/openauto/bin/autoapp /usr/local/bin/autoapp
    ```

12. Disable the DEV mode from step 1 and boot normally.
