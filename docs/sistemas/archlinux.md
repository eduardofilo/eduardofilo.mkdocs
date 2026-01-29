---
layout: default
permalink: /sistemas/archlinux.html
---

# Arch Linux

## Enlaces

* [Chaotic-AUR](https://aur.chaotic.cx/): Compilación automática de paquetes AUR.

## Comandos útiles

* `sudo pacman -Syy`: Actualizar la base de datos de paquetes. Equivalente en Debian a `apt update`.
* `sudo pacman -Syu`: Actualizar el sistema. Equivalente en Debian a `apt upgrade`.
* `sudo pacman -S <paquete>`: Instalar un paquete. Equivalente en Debian a `apt install`.
* `sudo pacman -R <paquete>`: Desinstalar un paquete dejando sus dependencia. Equivalente en Debian a `apt remove`.
* `sudo pacman -Rs <paquete>`: Desinstalar un paquete y sus dependencias dejando las que son usadas por otros paquetes.
* `sudo pacman -Rns <paquete>`: Desinstalar un paquete, sus dependencias y archivos de configuración. Equivalente en Debian a `apt purge`.
* `pacman -Qdt`: Listar paquetes huérfanos. Equivalente en Debian a `apt autoremove`.
* `sudo pacman -Rns $(pacman -Qdtq)`: Eliminar paquetes huérfanos. Equivalente en Debian a `apt autoremove`.
* `pacman -Q`: Listar todos los paquetes instalados.
* `pacman -Q <paquete>`: Comprobar si un paquete está instalado. Equivalente en Debian a `dpkg -l | grep <paquete>`.
* `pacman -Ql <paquete>`: Listar los archivos de un paquete. Equivalente en Debian a `dpkg -L <paquete>`.
* `pacman -Qo <archivo>`: Comprobar a qué paquete pertenece un archivo. Equivalente en Debian a `dpkg -S <archivo>`.
* `pacman -Ss <paquete>`: Buscar un paquete. Equivalente en Debian a `apt search`.
* `pacman -Qm`: Listar paquetes instalados desde AUR. Equivalente en Debian a `apt list --installed | grep -v /`.
* `yay -Syu`: Actualizar el sistema, incluyendo paquetes de AUR. Equivalente en Debian a `apt upgrade`.
* `yay -S <paquete>`: Instalar un paquete desde AUR. Equivalente en Debian a `apt install`.
* `sudo pacman -R <paquete>`: Desinstalar un paquete de AUR dejando sus dependencia. Equivalente en Debian a `apt remove`.
* `sudo pacman -Rs <paquete>`: Desinstalar un paquete de AUR y sus dependencias.
* `yay -Rns <paquete>`: Desinstalar un paquete de AUR, sus dependencias y archivos de configuración. Equivalente en Debian a `apt purge`.

## Paquetes interesantes

* `pamac-aur` (AUR): Interfaz gráfica para pacman/yay.