title: 2020-05-25 RG350 Docker Buildroot
summary: Compilación de Buildroot con toolchain de RG350 en un contenedor Docker.
date: 2020-05-25 17:00:00

![Buildroot logo](/images/posts/buildroot/logo.png)

La distribución del sistema operativo OpenDingux de la RG350 está basado en [Buildroot](https://buildroot.org/). Para compilarlo se recomienda utilizar una instalación Debian Stretch. Si no es el sistema que tenemos en nuestra máquina (bien por usar Windows o Mac o por tener otra distribución Linux), y no queremos o podemos instalar toda una máquina virtual para disponer de un entorno Debian Stretch, existe la posibilidad de encapsularlo en un contenedor Docker.

El procedimiento que se muestra a continuación está hecho sobre un Linux Ubuntu 20.04, pero no debería ser complicado adaptarlo para poder realizarse sobre Windows o Mac.

## Procedimiento para crear el contenedor

Nos interesa utilizar Docker únicamente para encapsular las dependencias que tiene la versión de Buildroot que vamos a utilizar. El código del mismo y el resultado de la compilación queremos que se mantenga desde la máquina host (la máquina que aloja el contenedor). Para ello vamos a empezar bajando la distribución Buildroot de la RG350. Existen varias de estas distribuciones. A continuación se muestra un pequeño listado:

* [GCW0](https://github.com/gcwnow/buildroot). Éste realmente no es para la RG350 sino para la GCWZero, pero se incluye por ser el origen del resto.
* [Tonyjih](https://github.com/tonyjih/RG350_buildroot)
* [Ninoh-FOX](https://github.com/Ninoh-FOX/toolchain)
* [gokr](https://github.com/gokr/RG350_buildroot)
* [soarquin](https://github.com/soarqin/RG350_buildroot)

En lo que sigue vamos a utilizar la versión de [Tonyjih](https://github.com/tonyjih/RG350_buildroot). El procedimiento completo se detalla a continuación:

1. Instalar Docker en máquina host:

    ```
    $ sudo apt install docker.io
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER
    $ sudo systemctl enable docker
    $ sudo systemctl start docker
    ```

2. Bajar repositorio en máquina host. Con los siguientes comandos quedará en `~/git/RG350_buildroot`:

    ```
    $ cd ~/git
    $ git clone https://github.com/tonyjih/RG350_buildroot.git
    ```

3. Arrancar contenedor pasando el directorio del repositorio del punto anterior como volumen:

    ```
    $ docker run -it -v ~/git:/root/git --name RG350_buildroot eduardofilo/rg350_buildroot
    ```

Si en lugar de utilizar la versión compilada subida al [Docker Hub](https://hub.docker.com/r/eduardofilo/rg350_buildroot) queremos construirlo en local (por si quisiéramos hacer alguna modificación en el Dockerfile), intercalaríamos los siguientes comandos entre los pasos 2 y 3 anteriores:

```
$ cd ~/git
$ git clone https://github.com/eduardofilo/RG350_buildroot_docker.git
$ cd ~/git/RG350_buildroot_docker
$ docker build -t eduardofilo/rg350_buildroot .
```

Tras ejecutar el paso 3 debería quedar un prompt ejecutándose desde el entorno Debian dentro del contenedor. Como hemos conectado el directorio `/root/git` del contenedor con el directorio `~/git` de nuestra máquina, cualquier cosa que queramos modificar o recoger al final de la compilación, la podremos localizar desde cualquier explorador de archivos de nuestra máquina. Si en algún momento perdiéramos de vista la terminal ejecutándose en el entorno del contenedor, podremos recuperarla ejecutando:

```
$ docker exec -it RG350_buildroot /bin/bash
```

Si el comando anterior devuelve un error indicando que el contenedor está parado, podemos arrancarlo antes ejecutando la orden:

```
$ docker start RG350_buildroot
```

## Operación de Buildroot

Una vez que tenemos preparado el entorno podremos realizar las tareas y compilaciones previstas en el mismo. Por ejemplo en el entorno preparado por [Tonyjih](https://github.com/tonyjih/RG350_buildroot) vemos que podemos realizar las siguientes cosas (las líneas de terminal siguientes están precedidas por `#` y no por `$` como antes porque se refieren al terminal dentro del contenedor, que se ejecuta con el usuario root del mismo):

* **OPCIONAL**. Para personalizar alguna opción de Buildroot, utilizar uno de los dos comandos siguientes (sólo uno):

    ```
    # cd ~/git/RG350_buildroot
    # make menuconfig
    # make nconfig
    ```

* Configurar Buildroot (sólo es necesario la primera vez):

    ```
    # cd ~/git/RG350_buildroot
    # make rg350_defconfig BR2_EXTERNAL=board/opendingux
    ```

* Compilar el toolchain (sólo es necesario una vez; el resultado queda en el directorio `~/git/RG350_buildroot/output/host/usr/bin`; por ejemplo el compilador y linker es `mipsel-gcw0-linux-uclibc-gcc`; tarda 1h50m en un Intel i3-4005U y genera unos 3GBs de archivos):

    ```
    # cd ~/git/RG350_buildroot
    # export BR2_JLEVEL=0
    # make toolchain
    ```

* Compilar una librería o paquete. Por ejemplo para compilar SDL y SDL_Image:

    ```
    # cd ~/git/RG350_buildroot
    # export BR2_JLEVEL=0
    # make sdl sdl_image
    ```


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

## Comandos para gestionar contenedores

Por último se comentan a continuación a modo de cheatsheet unos pocos comandos útiles para gestionar el contenedor que acabamos de crear:

* `docker container ls -a`: Listar contenedores. Para averiguar hash por ejemplo.
* `docker container stop <hash>`: Detener contenedor.
* `docker container rm <hash>`: Borrar contenedor.
