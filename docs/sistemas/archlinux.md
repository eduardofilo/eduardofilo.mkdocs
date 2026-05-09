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

## Modificación Manual de Paquetes AUR

Este es el procedimiento oficial cuando un paquete falla, quieres aplicar un parche personalizado o necesitas cambiar una opción de compilación antes de instalar.

### 1. Clonar el repositorio del paquete

En lugar de usar un helper (como `yay`), descargamos el código fuente directamente desde los servidores de AUR usando Git.

```bash
git clone https://aur.archlinux.org/nombre-del-paquete.git
cd nombre-del-paquete

```

### 2. Modificar el PKGBUILD o archivos fuente

Aquí es donde editas lo que necesites.

* **Para errores de rutas:** Edita las funciones `build()` o `package()` dentro del archivo `PKGBUILD`.
* **Para cambiar versiones:** Modifica la variable `pkgver`.

!!! Tip
    Si modificas archivos que están listados en el array `source()` (como un parche `.patch` o un script `.sh`), las sumas de verificación (checksums) fallarán. Para arreglarlo automáticamente, ejecuta:

    ```
    updpkgsums
    ```

### 3. Compilar e Instalar

Una vez que el `PKGBUILD` está a tu gusto, usamos el comando `makepkg`.

```bash
makepkg -si

```

**Desglose de flags:**

* `-s` (**s**ync): Instala automáticamente las dependencias necesarias usando `pacman`.
* `-i` (**i**nstall): Instala el paquete generado (`.pkg.tar.zst`) en tu sistema una vez terminada la compilación.

### Resumen de comandos

| Acción | Comando |
| --- | --- |
| **Bajar fuentes** | `git clone [https://aur.archlinux.org/paquete.git](https://aur.archlinux.org/paquete.git)` |
| **Actualizar sumas** | `updpkgsums` |
| **Limpiar y compilar** | `makepkg -f` (el `-f` fuerza a sobrescribir si ya compilaste antes) |
| **Compilar e instalar** | `makepkg -si` |
| **Limpiar basura** | `makepkg -c` (borra los directorios temporales `src/` y `pkg/` tras terminar) |

### ¿Cómo manejar las actualizaciones futuras?

Si modificaste un paquete manualmente, la próxima vez que uses `yay -Syu`, el helper verá que hay una versión nueva en AUR e intentará sobrescribir tu versión modificada. Tienes dos opciones:

1. **Si el error ya se arregló en AUR:** Deja que `yay` lo actualice normalmente.
2. **Si quieres mantener tu modificación:** Puedes añadir el paquete a la línea `IgnorePkg` en `/etc/pacman.conf` para que pacman no lo toque sin tu permiso.