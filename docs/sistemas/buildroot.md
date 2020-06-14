---
layout: default
permalink: /sistemas/buildroot.html
---

# Buildroot

## Enlaces

* [Manual](https://buildroot.org/downloads/manual/manual.html)
* Mastering Embedded Linux: [1](https://www.thirtythreeforty.net/posts/2019/08/mastering-embedded-linux-part-1-concepts/). [2](https://www.thirtythreeforty.net/posts/2019/12/mastering-embedded-linux-part-2-hardware/), [3](https://www.thirtythreeforty.net/posts/2020/01/mastering-embedded-linux-part-3-buildroot/), [4](https://www.thirtythreeforty.net/posts/2020/03/mastering-embedded-linux-part-4-adding-features/#commento-login-box-container) y [5](https://www.thirtythreeforty.net/posts/2020/05/mastering-embedded-linux-part-5-platform-daemons/)

## Comandos interesantes

* `make rg350_defconfig BR2_EXTERNAL=board/opendingux`: Carga un defconfig como la configuración actual (.config).
* `make menuconfig`: Configuración detallada de toda la distribución Buildroot.
* `make uclibc-menuconfig`: Configuración detallada de uClibc.
* `make savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs`.
* `make BR2_DEFCONFIG=configs/raspi_defconfig savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs` forzando el nombre del fichero.
* `make toolchain`: Compila el toolchain.
* `make`: Compila toda la distribución Buildroot.
* `make <package>`: Compila un paquete.
* `make <package>-rebuild`: Fuerza la recompilación del paquete.
* `make <package>-reconfigure`: Fuerza la reconfiguración del paquete.
* `make <package>-graph-depends`: Genera un gráfico del árbol de dependencias del paquete.
* `make <package>-dirclean`: Borra el directorio `output/build/<package>` forzando a compilar el paquete en próximas invocaciones de `make`. No borra los ficheros copiados al rootfs en `output/target`.
* `make clean`: Borra todo lo compilado anteriormente.

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
