---
layout: default
permalink: /sistemas/buildroot.html
---

# Buildroot

## Enlaces

* [Manual](https://buildroot.org/downloads/manual/manual.html)
* Mastering Embedded Linux: [1](https://www.thirtythreeforty.net/posts/2019/08/mastering-embedded-linux-part-1-concepts/). [2](https://www.thirtythreeforty.net/posts/2019/12/mastering-embedded-linux-part-2-hardware/), [3](https://www.thirtythreeforty.net/posts/2020/01/mastering-embedded-linux-part-3-buildroot/), [4](https://www.thirtythreeforty.net/posts/2020/03/mastering-embedded-linux-part-4-adding-features/#commento-login-box-container) y [5](https://www.thirtythreeforty.net/posts/2020/05/mastering-embedded-linux-part-5-platform-daemons/)

## Comandos interesantes

* `make list-defconfigs`: Muestra una lista de todos los defconfig que hay disponibles en la distribución Buildroot.
* `make rg350_defconfig BR2_EXTERNAL=board/opendingux`: Carga un defconfig como la configuración actual (.config).
* `make menuconfig`: Configuración detallada de toda la distribución Buildroot.
* `make savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs`.
* `make BR2_DEFCONFIG=configs/raspi_defconfig savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs` forzando el nombre del fichero.
* `make busybox-menuconfig`: Configuración detallada de BusyBox. Debe estar activado previamente en `System configuration > Init system`.
* `make uclibc-menuconfig`: Configuración detallada de uClibc. Debe estar seleccionada como librería C en `Toolchain > C library`.
* `make linux-menuconfig`: Configuración detallada del kernel Linux.
* `make linux-savedefconfig`: Graba la configuración hecha del kernel Linux.
* `make barebox-menuconfig`: Configuración detallada del bootloader Barebox. Debe estar seleccionado como bootloader en `Bootloaders`.
* `make barebox-savedefconfig`: Graba la configuración hecha del bootloader Barebox.
* `make uboot-menuconfig`: Configuración detallada del bootloader U-Boot. Debe estar seleccionado como bootloader en `Bootloaders`.
* `make uboot-savedefconfig`: Graba la configuración hecha del bootloader U-Boot.
* `make source`: Descarga todo lo necesario para luego poder hacer una compilación offline.
* `make toolchain`: Compila el toolchain.
* `make`: Compila toda la distribución Buildroot.
* `make V=1`: Compila toda la distribución Buildroot en modo verbose.
* `make help`: Muestra una lista de todos los targets.
* `make <package>`: Compila un paquete.
* `make <package>-rebuild`: Fuerza la recompilación del paquete. No implica la recreación de la imagen ni el root filesystem. Para hacerlo ejecutar `make`.
* `make <package>-reconfigure`: Fuerza la reconfiguración y recompilación del paquete. No implica la recreación de la imagen ni el root filesystem. Para hacerlo ejecutar `make`.
* `make <package>-graph-depends`: Genera un gráfico del árbol de dependencias del paquete.
* `make <package>-dirclean`: Borra el directorio `output/build/<package>` forzando a compilar el paquete en próximas invocaciones de `make`. No borra los ficheros copiados al rootfs en `output/target`. Al forzar la recompilación se sobreescribirán de nuevo, pero si en la nueva compilación algún fichero copiado la primera vez ya no debe ser incluido, permanecerá, por lo que en esos casos conviene borrar `output/target` previamente.
* `make clean`: Borra todo lo compilado anteriormente (incluyendo directorios build, host, staging y target, las imágenes y el toolchain). Para saber cuándo merece la pena hacer un rebuild, consultar el apartado [Understanding when a full rebuild is necessary](https://buildroot.org/downloads/manual/manual.html#full-rebuild).
* `make distclean`: Borra todo lo que no sean fuentes (incluyendo .config). Útil cuando se quiere cambiar de placa.

!!! Warning "Aviso"
    Si `ccache` está activado, `make clean` o `make distclean` no borra la caché de compilación usada por Buildroot. Para borrarla, consultar la sección 8.13.3 de [Using ccache in Buildroot](https://buildroot.org/downloads/manual/manual.html#ccache).

## Stamp files

Cada vez que se compila un package, se generan unos ficheros ocultos que marcan las distintas fases de la compilación en el directorio `output/build/<package>-<version>`. Se pueden borrar para provocar la repetición de esas fases, aunque lo habitual es utilizar los comandos `make <package>-rebuild` o `make <package>-reconfigure` (de hecho estos comandos precisamente lo que hacen es eliminar estos ficheros stamp). Por ejemplo estos son los ficheros generados en la compilación del paquete `sdl_image`:

```
root@04084426cffe:~/git/buildroot-rg350-old-kernel/output/build/sdl2_image-2.0.2# ls -ltra .stamp*
-rw-r--r-- 1 root root 0 Jun  1 18:50 .stamp_downloaded
-rw-r--r-- 1 root root 0 Jun  1 18:50 .stamp_extracted
-rw-r--r-- 1 root root 0 Jun  1 18:50 .stamp_patched
-rw-r--r-- 1 root root 0 Jun  1 18:50 .stamp_configured
-rw-r--r-- 1 root root 0 Jun  1 18:50 .stamp_built
-rw-r--r-- 1 root root 0 Jun  1 18:51 .stamp_staging_installed
-rw-r--r-- 1 root root 0 Jun  1 18:51 .stamp_target_installed
```

## Parámetros importantes del menuconfig

* `Target options`
    * `Target Architecture`
    * `Target Architecture Variant`
    * `Target ABI`
* `Build options`
    * `[*] Enable compiler cache`
    * `($(HOME)/git/.buildroot-ccache) Compiler cache location`
    * `(board/<company>/<model>/patches) global patch directories`
* `Toolchain`
    * `Toolchain type (Buildroot toolchain)`
    * `C library (uClibc-ng)`
        * `Kernel Headers ()`: Seleccionar una versión igual o inferior a la del Kernel seleccionado más adelante (lo mejor es que sean iguales para no desaprovechar características del Kernel que se instalará)
    * `GCC compiler Version ()`
* `System configuration`
    * `(<hostname>) System hostname`: Sólo con `Root FS skeleton (default target skeleton)`
    * `(Welcome to <hostname>) System banner`: Sólo con `Root FS skeleton (default target skeleton)`
    * `/dev management`: [Documentación](https://buildroot.org/downloads/manual/manual.html#_dev_management)
    * `Init system`: [Documentación](https://buildroot.org/downloads/manual/manual.html#_init_system)
    * `(<directorio con los ficheros a sustituir>) Root filesystem overlay directories`
    * `(<script>) Custom scripts to run before creating filesystem images`
* `Kernel`
    * `[*] Linux Kernel`
    * `Kernel version ()`
    * `(<defconfig_name>) Defconfig name`
    * `[ ]   Build a Device Tree Blob (DTB)`: En RG350 no, en Raspi Sí.
* `Target packages`
    * `-*- BusyBox`
* `Filesystem images`
    * `[*] ext2/3/4 root filesystem`
    * `ext2/3/4 variant (ext4)`
* `Bootloaders`: En RG350 y Raspi no seleccionar ninguno.

## Monográficos

#### [Compilación de Buildroot con toolchain de RG350 en un contenedor Docker](/2020-05-25-rg350_docker_buildroot.html)

#### [Ejemplos de compilación de algunas aplicaciones para RG350 por medio del toolchain en Docker](/2020-05-31-rg350_compile.html)
