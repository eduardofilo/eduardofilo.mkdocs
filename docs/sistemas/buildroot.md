---
layout: default
permalink: /sistemas/buildroot.html
---

# Buildroot

## Enlaces

* Mastering Embedded Linux: [1](https://www.thirtythreeforty.net/posts/2019/08/mastering-embedded-linux-part-1-concepts/). [2](https://www.thirtythreeforty.net/posts/2019/12/mastering-embedded-linux-part-2-hardware/), [3](https://www.thirtythreeforty.net/posts/2020/01/mastering-embedded-linux-part-3-buildroot/), [4](https://www.thirtythreeforty.net/posts/2020/03/mastering-embedded-linux-part-4-adding-features/#commento-login-box-container) y [5](https://www.thirtythreeforty.net/posts/2020/05/mastering-embedded-linux-part-5-platform-daemons/)

## Comandos interesantes

* `make savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs`.
* `make BR2_DEFCONFIG=configs/raspi_defconfig savedefconfig` Graba la configuración actual (`.config`) en el directorio `configs` forzando el nombre del fichero.
* `make <package>-dirclean` Borra el directorio `output/build/<package>` forzando a compilar el paquete en próximas invocaciones de `make`. No borra los ficheros copiados al rootfs en `output/target`.
