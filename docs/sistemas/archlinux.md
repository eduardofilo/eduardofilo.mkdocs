---
layout: default
permalink: /sistemas/archlinux.html
---

# Arch Linux

## Comandos útiles

* `pacman -Syy`: Actualizar la base de datos de paquetes. Equivalente a `apt update`.
* `pacman -Syu`: Actualizar el sistema. Equivalente a `apt upgrade`.
* `pacman -S <paquete>`: Instalar un paquete. Equivalente a `apt install`.
* `pacman -R <paquete>`: Desinstalar un paquete. Equivalente a `apt remove`.
* `pacman -Q <paquete>`: Comprobar si un paquete está instalado. Equivalente a `dpkg -l | grep <paquete>`.
* `pacman -Ql <paquete>`: Listar los archivos de un paquete. Equivalente a `dpkg -L <paquete>`.
* `pacman -Qo <archivo>`: Comprobar a qué paquete pertenece un archivo. Equivalente a `dpkg -S <archivo>`.
* `pacman -Ss <paquete>`: Buscar un paquete. Equivalente a `apt search`.
* `pacman -Qdt`: Listar paquetes huérfanos. Equivalente a `apt autoremove`.
* `pacman -Rns $(pacman -Qdtq)`: Eliminar paquetes huérfanos. Equivalente a `apt autoremove`.
* `pacman -Qm`: Listar paquetes instalados desde AUR. Equivalente a `apt list --installed | grep -v /`.
