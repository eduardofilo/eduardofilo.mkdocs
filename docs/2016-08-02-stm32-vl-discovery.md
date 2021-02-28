title: Entorno desarrollo STM32 VL Discovery sobre Linux
summary: Configuración de entorno de desarrollo para STM332 VL Discovery con herramientas libres sobre Linux.
date: 2016-08-02 08:30:00

![PiGRRL-2](/images/posts/stm32.png)

ST propone varios entornos de desarrollo para trabajar sobre su placa [STM32 VL Discovery](http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/stm32vldiscovery.html), pero en todos los casos sobre Windows. Vamos a ver aquí cómo montar el toolkit de desarrollo sobre Ubuntu 16.04.

1. Instalación de última versión de [GCC ARM Embedded](https://launchpad.net/gcc-arm-embedded) siguiendo [estas instrucciones](http://gnuarmeclipse.livius.net/blog/toolchain-install/#GNULinux). Básicamente consiste en bajar [este archivo](https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q2-update/+download/gcc-arm-none-eabi-5_4-2016q2-20160622-linux.tar.bz2) y descomprimirlo en /usr/local del siguiente modo:

        $ cd /usr/local
        $ sudo tar xjvf ~/Descargas/gcc-arm-none-eabi-5_4-2016q2-20160622-linux.tar.bz2

2. Introducir en la variable PATH del sistema la ruta del directorio bin del compilador GCC ARM recién instalado incorporando al final del fichero ~/.profile:

        PATH="/usr/local/gcc-arm-none-eabi-5_4-2016q2/bin:$PATH"

3. Descargamos la STM32 Firmware Library de [aquí](https://my.st.com/content/my_st_com/en/products/embedded-software/mcus-embedded-software/stm32-embedded-software/stm32-standard-peripheral-libraries/stsw-stm32054.license%3d1469811720442.html).

4. Descomprimimos y dejamos en la ruta `~/STM32F10x_StdPeriph_Lib_V3.5.0`.

5. Descargamos plantilla para los proyectos de código por ejemplo en `~/git/`:

        $ cd ~/git
        $ git clone git://github.com/geoffreymbrown/STM32-Template.git

6. La compilación del código se haría así:

        $ cd ~/git/STM32-Template/Demo
        $ make

7. Modificamos el fichero `~/git/STM32-Template/Makefile.common` ajustando las variables `TOOLROOT` y `LIBROOT` de la siguiente forma:

        TOOLROOT=/usr/local/gcc-arm-none-eabi-5_4-2016q2/bin
        LIBROOT=~/STM32F10x_StdPeriph_Lib_V3.5.0

8. Instalamos el software que nos permitirá hacer uso del interfaz STLink para programar el MCU:

        $ cd ~/git
        $ git clone git://github.com/texane/stlink.git

9. Instalamos una serie de paquetes necesarios:

        $ sudo apt-get install pkg-config intltool build-essential cmake libusb-1.0 libgtk-3-dev

10. Tal y como se explica en el [README del proyecto](https://github.com/texane/stlink) descargado en el paso 7, el interfaz STLINKv1 que utiliza la STM32VLDISCOVERY, tiene ciertos problemas que para evitar hay que reconfigurar el módulo `usb-storage`. Para ello ejecutar lo siguiente al principio de una sesión en la que se quiera trabajar con él:

        $ sudo modprobe -r usb-storage && sudo modprobe usb-storage quirks=0483:3744:i

11. Si se quiere hacer permanente el cambio en su lugar, crear el fichero `/etc/modprobe.d/usb-storage.conf` con el siguiente contenido:

        # stlink/v1 ignore mass storage
        options usb-storage quirks=0483:3744:i

12. Compilamos:

        $ cd ~/git/stlink
        $ ./autogen.sh
        $ ./configure --with-gtk-gui
        $ make
        $ mkdir build && cd build
        $ cmake -DCMAKE_BUILD_TYPE=Debug ..
        $ make

13. Conectar la placa por USB al ordenador.

14. Arrancamos gdbserver:

        $ cd ~/git/stlink/build
        $ sudo ./st-util -1

15. Conectamos con él desde el directorio donde esté el binario que queremos depurar o ejecutar:

        $ cd ~/git/STM32-Template/Demo
        $ arm-none-eabi-gdb Demo.elf
        (gdb) target extended-remote localhost:4242
        (gdb) load
        (gdb) quit

<iframe width="854" height="480" src="https://www.youtube.com/embed/P1yi9i1A8K4" frameborder="0" allowfullscreen></iframe>
