---
layout: default
permalink: /sistemas/archlinux.html
---

# Arch Linux

## Comandos útiles

* `sudo pacman -Syy`: Actualizar la base de datos de paquetes. Equivalente a `apt update`.
* `sudo pacman -Syu`: Actualizar el sistema. Equivalente a `apt upgrade`.
* `sudo pacman -S <paquete>`: Instalar un paquete. Equivalente a `apt install`.
* `sudo pacman -R <paquete>`: Desinstalar un paquete dejando sus dependencia. Equivalente a `apt remove`.
* `sudo pacman -Rs <paquete>`: Desinstalar un paquete y sus dependencias.
* `sudo pacman -Rns <paquete>`: Desinstalar un paquete, sus dependencias y archivos de configuración. Equivalente a `apt purge`.
* `pacman -Qdt`: Listar paquetes huérfanos. Equivalente a `apt autoremove`.
* `sudo pacman -Rns $(pacman -Qdtq)`: Eliminar paquetes huérfanos. Equivalente a `apt autoremove`.
* `pacman -Q <paquete>`: Comprobar si un paquete está instalado. Equivalente a `dpkg -l | grep <paquete>`.
* `pacman -Ql <paquete>`: Listar los archivos de un paquete. Equivalente a `dpkg -L <paquete>`.
* `pacman -Qo <archivo>`: Comprobar a qué paquete pertenece un archivo. Equivalente a `dpkg -S <archivo>`.
* `pacman -Ss <paquete>`: Buscar un paquete. Equivalente a `apt search`.
* `pacman -Qm`: Listar paquetes instalados desde AUR. Equivalente a `apt list --installed | grep -v /`.
* `sudo yay -Syu`: Actualizar el sistema, incluyendo paquetes de AUR. Equivalente a `apt upgrade`.
* `sudo yay -S <paquete>`: Instalar un paquete desde AUR. Equivalente a `apt install`.
* `sudo pacman -R <paquete>`: Desinstalar un paquete de AUR dejando sus dependencia. Equivalente a `apt remove`.
* `sudo pacman -Rs <paquete>`: Desinstalar un paquete de AUR y sus dependencias.
* `sudo yay -Rns <paquete>`: Desinstalar un paquete de AUR, sus dependencias y archivos de configuración. Equivalente a `apt purge`.
