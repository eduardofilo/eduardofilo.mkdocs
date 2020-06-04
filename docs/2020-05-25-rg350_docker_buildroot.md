title: 2020-05-25 RG350 Docker Buildroot
summary: Compilación de Buildroot con toolchain de RG350 en un contenedor Docker.
date: 2020-05-25 17:00:00

![Buildroot logo](/images/posts/buildroot/logo.png)

La distribución del sistema operativo OpenDingux de la RG350 está basado en [Buildroot](https://buildroot.org/). Para compilarlo se recomienda utilizar una instalación Debian Stretch o Buster (según la versión de Buildroot en que esté basado). Si no es el sistema que tenemos en nuestra máquina (bien por usar Windows o Mac o por tener otra distribución Linux), y no queremos o podemos instalar una pesada máquina virtual para disponer del entorno adecuado, existe la posibilidad de encapsularlo en un contenedor Docker.

El procedimiento que se muestra a continuación está hecho sobre un Linux Ubuntu 20.04, pero no debería ser complicado de adaptar para poder realizarse sobre Windows o Mac.

## Elección de distribución Buildroot

Existen varias distribuciones Buildroot para RG350. A continuación se listan algunas:

|Distribución|Versión Buildroot|Entorno de compilación|Observaciones|
|:-----------|:----------------|:-------------|:------------|
|[GCW0](https://github.com/gcwnow/buildroot)| | |Éste realmente no es para la RG350 sino para la GCWZero, pero se incluye por ser el origen del resto|
|[OpenDingux](https://github.com/OpenDingux/buildroot)| | |Tampoco tiene una configuración específica para la RG350|
|[Tonyjih](https://github.com/tonyjih/RG350_buildroot)|2014.08|Debian Stretch; Docker [eduardofilo/rg350_buildroot](https://hub.docker.com/r/eduardofilo/rg350_buildroot)|Buildroot en el que se bajan muchos|
|[Ninoh-FOX](https://github.com/Ninoh-FOX/toolchain)| |Debian Stretch|ROGUE CFW|
|[gokr](https://github.com/gokr/RG350_buildroot)| | | |
|[soarquin](https://github.com/soarqin/RG350_buildroot)| |CentOS 7; Docker [soarqin/rg350_toolchain](https://hub.docker.com/r/soarqin/rg350_toolchain)| |
|[od-contrib](https://github.com/od-contrib/buildroot-rg350-old-kernel)|2020.05|Debian Buster; Docker [eduardofilo/rg350_buster_buildroot](https://hub.docker.com/r/eduardofilo/rg350_buster_buildroot)|Basado en un Buildroot moderno|
|[glebm](https://github.com/glebm/od-buildroot)| | | |

Vamos a empezar bajando una de estas distribuciones Buildroot de RG350 a un directorio de nuestra máquina (la que actuará de host para Docker). Es habitual utilizar un directorio `git` en el home del usuario donde descargar los repositorios y nosotros seguiremos esta costumbre. Más adelante, al arrancar el contenedor, indicaremos ese directorio como volumen para conectar el sistema de archivos de nuestra máquina (host) con el contenedor. Así conseguimos que nuestra máquina (host) sólo sirva de almacén de las fuentes y los binarios resultantes, utilizando Docker para encapsular las dependencias que tiene la versión de Buildroot que vamos a utilizar que son muy numerosas y con frecuencia no coinciden con lo que nuestro sistema tiene instalado.

Por ejemplo vamos a utilizar la distribución de [Tonyjih](https://github.com/tonyjih/RG350_buildroot). Bajamos pues el repositorio en nuestra máquina. Con los siguientes comandos quedará en `~/git/RG350_buildroot`:

```
$ cd ~/git
$ git clone https://github.com/tonyjih/RG350_buildroot.git
```

## Procedimiento para crear el contenedor

Veíamos en la tabla anterior que podemos compilar la distribución que hemos elegido para ilustrar el artículo (la de [Tonyjih](https://github.com/tonyjih/RG350_buildroot)) con la imagen Docker [eduardofilo/rg350_buildroot](https://hub.docker.com/r/eduardofilo/rg350_buildroot). A continuación vamos a ver los pasos para descargar y ejecutar esta imagen. Los primeros pasos son una receta rápida para instalar Docker en nuestro sistema si no contáramos ya con él, pero es mejor seguir una de las muchas guías que se pueden encontrar (por ejemplo para [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)).

1. Instalar Docker en máquina host:

    ```
    $ sudo apt install docker.io
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER
    $ sudo systemctl enable docker
    $ sudo systemctl start docker
    ```

2. Arrancar contenedor pasando el directorio `~/git` como volumen:

    ```
    $ docker run -it -v ~/git:/root/git --name RG350_buildroot eduardofilo/rg350_buildroot
    ```

Si en lugar de utilizar la versión compilada de la imagen subida al [Docker Hub](https://hub.docker.com/r/eduardofilo/rg350_buildroot) queremos construirla en local (por si quisiéramos hacer alguna modificación en el Dockerfile), intercalaríamos los siguientes comandos entre los pasos 1 y 2 anteriores:

```
$ cd ~/git
$ git clone https://github.com/eduardofilo/RG350_buildroot_docker.git
$ cd ~/git/RG350_buildroot_docker
$ docker build -t eduardofilo/rg350_buildroot .
```

Tras ejecutar el paso 2 debería quedar un prompt ejecutándose desde el entorno Debian dentro del contenedor. Como hemos conectado el directorio `/root/git` del contenedor con el directorio `~/git` de nuestra máquina, cualquier cosa que queramos modificar o recoger al final de la compilación, la podremos localizar desde un explorador de archivos de nuestra máquina. Si en algún momento perdiéramos de vista la terminal ejecutándose en el entorno del contenedor, podremos recuperarla ejecutando:

```
$ docker exec -it RG350_buildroot /bin/bash
```

Si el comando anterior devuelve un error indicando que el contenedor está parado, podemos arrancarlo antes ejecutando la orden:

```
$ docker start RG350_buildroot
```

## Operación general de Buildroot

Una vez que tenemos en marcha y el contenedor y nos hemos conectado con él, ya podemos empezar a trabajar con Buildroot. Esta distribución tiene su propia estructura y formas de operación. Vamos a empezar describiendo por encima el entorno y algunas operaciones habituales o interesantes.

Buildroot se puede describir de forma resumida como un toolchain de compilación cruzada unido a un gran número de paquetes (siendo uno de ellos el kernel Linux) que en conjunto pueden constituir un sistema Linux completo, habitualmente para un sistema embebido. La lista de paquetes que contiene Buildroot podemos encontrarla en el directorio [package](https://github.com/tonyjih/RG350_buildroot/tree/opendingux-2014.08/package).

Luego, existen una serie de configuraciones predefinidas para placas conocidas. Las podemos encontrar en el directorio [configs](https://github.com/tonyjih/RG350_buildroot/tree/opendingux-2014.08/configs). Una de las primeras cosas que haremos más adelante es cargar la configuración para RG350 (fichero [rg350_defconfig](https://github.com/tonyjih/RG350_buildroot/blob/opendingux-2014.08/configs/rg350_defconfig)). Esta configuración se basa en la estructura oficial de Buildroot que es genérica para sistemas embebidos Linux. Si en nuestro sistema deseamos alguna característica especial o parche sobre los paquetes estándar que Buildroot ofrece, tenemos otro mecanismo, los ficheros que encontraremos en el directorio `board/<fabricante>/<placa>`. En el caso de RG350 el nombre del fabricante elegido es `opendingux` y el nombre de la placa `gcw0`. Así pues en el directorio [`board/opendingux/gcw0`](https://github.com/tonyjih/RG350_buildroot/tree/opendingux-2014.08/board/opendingux/gcw0) podemos encontrar por ejemplo los scripts para generar una imagen válida para la consola.

!!! Note "Nota"
    A partir de este punto veremos que las líneas de terminal están precedidas por `#` y no por `$` como antes porque se refieren al terminal dentro del contenedor Docker, que se ejecuta con el usuario root del mismo.

Antes de empezar cargamos la configuración para RG350 de las [múltiples que trae Buildroot de serie](https://github.com/tonyjih/RG350_buildroot/tree/opendingux-2014.08/configs):

```
# cd ~/git/RG350_buildroot
# make rg350_defconfig BR2_EXTERNAL=board/opendingux
```

Si ahora queremos repasar o cambiar algo de esta configuración lo haremos por medio de una herramienta similar a la que se utiliza para configurar un kernel Linux antes de compilarlo. Para ello utilizaremos uno de los dos comandos `make` siguientes (sólo uno):

```
# cd ~/git/RG350_buildroot
# make menuconfig
# make nconfig
```

Antes de empezar a compilar cosas vamos a definir la siguiente variable de entorno que permitirá la compilación en paralelo:

```
# export BR2_JLEVEL=0
```

A continuación describimos algunas operaciones que podemos realizar:

|Comando|Efecto|
|:------|:-----|
|`make clean`|Borra todos los ficheros generados en la compilación|
|`make toolchain`|Genera el toolchain de compilación cruzada. El resultado queda en el directorio `~/git/RG350_buildroot/output/host/usr/bin`; tarda 1h50m en un Intel i3-4005U y genera unos 3GBs de archivos|
|`make <paquete>`|Compila el paquete (de la [lista de paquetes de la distribución](https://github.com/tonyjih/RG350_buildroot/tree/opendingux-2014.08/package))|
|`make <paquete>-rebuild`|Fuerza la recompilación del paquete|
|`make <paquete>-reconfigure`|Fuerza la reconfiguración del paquete|
|`make <paquete>-graph-depends`|Genera un gráfico del árbol de dependencias del paquete|
|`make all`|Compila la distribución completa|

## Operación particular de la distribución Buildroot para RG350

Una vez que tenemos preparado el entorno podremos realizar las tareas y compilaciones previstas en el mismo. Por ejemplo en el entorno preparado por [Tonyjih](https://github.com/tonyjih/RG350_buildroot) vemos que podemos realizar las siguientes operaciones:

* Si se quiere que la imagen incluya emuladores y aplicaciones, ejecutar antes lo siguiente (sólo es necesario hacerlo una vez):

    ```
    # cd ~/git/RG350_buildroot
    # board/opendingux/gcw0/download_local_pack.sh
    ```

* Compilación de imagen para flashear en SD (el fichero con la imagen resultante queda en `~/git/RG350_buildroot/output/images/od-imager/images/sd_image.bin`; tarda 6h en un Intel i3-4005U y genera unos 9GBs de archivos):

    ```
    # cd ~/git/RG350_buildroot
    # board/opendingux/gcw0/make_initial_image.sh
    ```

* Generación de un OPK update para ejecutarse directamente sobre el sistema anterior (el fichero con el OPK resultante queda en `~/git/RG350_buildroot/output/images/rg350-update-<fecha>.opk`):

    ```
    # cd ~/git/RG350_buildroot
    # board/opendingux/gcw0/make_upgrade.sh
    ```

Hay un problema con el script `make_initial_image.sh` y es que internamente ejecuta `make rg350_defconfig BR2_EXTERNAL=board/opendingux` lo que hace que si hemos hecho `make menuconfig` se pierdan los cambios realizados ya que se vuelve a cargar el [`rg350_defconfig` que hay en `config`](https://github.com/tonyjih/RG350_buildroot/blob/opendingux-2014.08/configs/rg350_defconfig). Tenemos varias opciones para evitar este problema:

1. Editar manualmente el fichero [rg350_defconfig](https://github.com/tonyjih/RG350_buildroot/blob/opendingux-2014.08/configs/rg350_defconfig).
2. Retirar la llamada a `make rg350_defconfig BR2_EXTERNAL=board/opendingux` dentro del script [`make_initial_image.sh`](https://github.com/tonyjih/RG350_buildroot/blob/opendingux-2014.08/board/opendingux/gcw0/make_initial_image.sh).
3. Ejecutar `make BR2_DEFCONFIG=configs/rg350_defconfig savedefconfig` tras el `make menuconfig` para regenerar el fichero `configs/rg350_defconfig` con la nueva configuración.

## Compilación de distribución [od-contrib](https://github.com/od-contrib/buildroot-rg350-old-kernel)

Existe una distribución Buildroot bastante moderna (basada en la versión 2020.05), que por tanto ofrece una versión mucho más actual de los paquetes que constituyen la distribución (no así el Kernel Linux que se mantiene en la versión 3.12). El procedimiento de compilación es muy similar al de la distribución de Tonyjih ilustrada antes. Vamos a mostrar el paso a paso sin dar explicaciones (sirven las mismas que antes) para compilar esta versión:

1. En máquina host:

    ```
    $ cd ~/git
    $ git clone https://github.com/od-contrib/buildroot-rg350-old-kernel.git
    $ docker run -it -v ~/git:/root/git --name RG350_buster_buildroot eduardofilo/rg350_buster_buildroot
    ```

2. En contenedor:

    ```
    # cd ~/git/buildroot-rg350-old-kernel
    # make rg350_defconfig BR2_EXTERNAL=board/opendingux
    # make menuconfig
    # export BR2_JLEVEL=0
    # make toolchain
    # board/opendingux/gcw0/make_initial_image.sh rg350
    ```

El script `make_initial_image.sh` tiene el mismo problema que comentábamos al final del apartado anterior con la distribución Tonyjih. Además falla por tener un patrón de target doble:

```
# cd ~/git/buildroot-rg350-old-kernel
# make rg350_defconfig BR2_EXTERNAL=board/opendingux:opks
Makefile:184: *** multiple target patterns.  Stop.
```

La solución consiste en retirar el `:opks` del final de la llamada anterior que hay en la linea 18 del script [`make_initial_image.sh`](https://github.com/od-contrib/buildroot-rg350-old-kernel/blob/master/board/opendingux/gcw0/make_initial_image.sh).

Tras solucionar esos problemas y ejecutar todo lo anterior, encontraremos la imagen completa compilada en `~/git/buildroot-rg350-old-kernel/output/images/od-imager/images/sd_image.bin`.

!!! Note "Nota"
    A la hora de compilar esta distribución Buildroot, no estaba disponible el paquete `libpng14`. La URL principal de descarga producía timeout en la conexión y las secundarias no existían. La solución fue bajar el paquete por nuestra cuenta, colocarlo en el directorio `~/git/buildroot-rg350-old-kernel/dl/libpng14` y volver a compilar. El paquete se puede encontrar por ejemplo [aquí](https://sourceforge.net/projects/libpng/files/libpng14/1.4.22/libpng-1.4.22.tar.xz/download).

## Comandos para gestionar contenedores

Por último se comentan a continuación a modo de cheatsheet unos pocos comandos útiles para gestionar el contenedor que acabamos de crear:

|Comando|Efecto|
|:--------------|:--------|
|`docker container ls -a`|Listar contenedores. Para averiguar hash por ejemplo.|
|`docker container start <hash>`|Arrancar contenedor.|
|`docker exec -it <hash> /bin/bash`|Obtener prompt bash en contenedor.|
|`docker container stop <hash>`|Detener contenedor.|
|`docker container rm <hash>`|Borrar contenedor.|
