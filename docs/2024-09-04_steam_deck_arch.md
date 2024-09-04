title: Instalación Arch Linux en Steam Deck
summary: Procedimiento completo para instalar Arch Linux junto a SteamOS con dual boot en Steam Deck.
date: 2024-09-04 15:30:00

![Steam Deck con Arch Linux](/images/posts/2024-09-04_steam_deck_arch/steam_deck_logo.png)

En julio de 2024 durante unas semanas, el modelo de 512GB de la Steam Deck LCD pudo adquirirse por debajo de los 400€. Un precio muy atractivo para una [máquina muy decente](https://www.steamdeck.com/es/tech/deck) con procesador AMD de arquitectura x86 (AMD64), 16GB de RAM, disco SSD tipo NVMe de la capacidad mencionada antes, pantalla táctil y controles de juego integrados. Es decir un PC consolizado, pero un PC al fin y al cabo. Pero sobre todo lo que hace para mi especialmente atractiva la máquina es su soporte Linux completo, lo que la convierte en una plataforma ideal para cacharrear con distribuciones Linux o utilizarlo como PC portátil secundario. Todo esto naturalmente además de su uso convencional para jugar y [emular](https://www.emudeck.com/) videojuegos.

SteamOS, el sistema operativo que trae de serie, está basado en Arch Linux, y en su modo escritorio, puede utilizarse prácticamente como un Arch Linux normal. La principal restricción es que está construido en modo inmutable y a pesar de que este tipo de configuración de sistema tiene sus virtudes y se entiende perfectamente que Valve lo haya escogido para su máquina, todavía prefiero un sistema normal (mutable), por lo que me decidí por instalar un Arch normal y aprender a instalar de paso esta distribución. Según el [wiki de Arch](https://wiki.archlinux.org/title/Steam_Deck), el hardware del modelo LCD de la Steam Deck está soportado al 100% en Arch.

Lo que sigue es el procedimiento completo que he utilizado.

## Teclado/ratón

Aunque gran parte de las operaciones pueden hacerse utilizando la pantalla táctil y los trackpads de la Steam Deck, es muy recomendable conectar un teclado y ratón a la consola para facilitar la instalación, sobre todo durante la sesión de terminal con la que instalaremos el sistema base. La Steam Deck sólo posee un puerto USB-C, por lo que lo más práctico es utilizar un dock. También puede ser suficiente (sobre todo si ejecutamos los sistemas live desde una microSD) con un dongle de teclado/ratón inalámbricos conectados con un adaptador USB<->USB-C.

En mi caso utilicé un dock [DA310z](https://www.dell.com/es-es/shop/adaptador-multipuerto-usb-c-de-dell-7-en-1-da310/apd/470-aeup/conexi%C3%B3n-wifi-y-redes) de Dell.

## Reparticionado del disco

El disco SSD de la Steam Deck que adquirí es de 512GB y de tipo NVMe. Es el tamaño mínimo si queremos instalar otro sistema junto a SteamOS.

Antes de empezar con la instalación debemos hacer hueco para la misma encogiendo la partición principal (la número 8). Para ello podemos utilizar prácticamente cualquier distribución live Linux que arranquemos desde una unidad extraíble (USB o microSD) ya que todas ellas llevan algún programa para gestionar particiones. En mi caso utilicé una ISO del programa `gparted`.

El procedimiento completo puede verse a continuación:

1. Descargar la [ISO de gparted](https://gparted.org/download.php). En concreto en mi caso utilicé [ésta versión](https://downloads.sourceforge.net/gparted/gparted-live-1.6.0-3-amd64.iso).
2. Instalar la ISO en un pendrive o mejor aún en una microSD (ya que la Steam Deck posee una ranura para éstas). Puede utilizarse un programa como [Balena Etcher](https://www.balena.io/etcher/) o el comando `dd` de Linux si se [sabe manejar](/sistemas/raspi.html#backup-de-la-sd-comprimiendo-al-vuelo).
3. Arrancar la Steam Deck con el pendrive o la microSD insertada manteniendo pulsado el botón de bajar el volumen hasta que se escuchen los tonos de encendido. Esto hace que la consola arranque en el menú `Boot Manager`.
4. Seleccionar la opción de arrancar desde el dispositivo extraíble que aparecerá en el menú como `EFI USB Device (USB)` o `EFI SD/MMC Card (XX XXXX XXXX)` según si utilizamos un pendrive o una microSD respectivamente.
5. Aparece una pantalla de configuración  en la que hacemos las siguientes selecciones:

    * Policy for handling keymaps => Don't touch keymap
    * Which language do you prefer? => 25
    * Which mode do you prefer? => 0

6. Tras aceptar la última opción anterior, arrancará el programa `gparted` en modo gráfico (con la pantalla girada, eso sí). Haremos cambios hasta dejar las particiones como se ve en la foto. Básicamente lo que haremos será encoger la partición #8 unos 100GB, crear la #9 de 4GB para swap y la #10 con el espacio restante para el sistema raíz de Arch:

    ![Particiones de la Steam Deck](/images/posts/2024-09-04_steam_deck_arch/steam-deck-partitions.png)

Destacar a la vista de las particiones que utiliza SteamOS que hace uso de un [sistema de particiones A/B](https://blog.davidbyrne.dev/2018/08/16/linux-ab-partitions), habitual en Android, por el cual la mayoría de las particiones del sistema (excepto la de usuario) están duplicadas. Dicho sistema está pensado para facilitar las actualizaciones, o más bien para volver atrás en caso de problemas durante las mismas.

## Instalación base

Para el proceso de instalación del sistema base me decanté por el camino convencional siguiendo las instrucciones de la [guía de instalación](https://wiki.archlinux.org/title/Installation_guide) en el wiki de Arch. Dicha instalación utiliza una ISO de un sistema Arch que podremos arrancar desde una unidad extraíble (USB o microSD) con el que instalaremos los paquetes básicos para tener un sistema arrancable y muy básico.

Antes de comenzar, comentar que por las características tan dinámicas de la distribución Arch Linux, es muy posible que esta guía quede desactualizada en poco tiempo. Por lo que recomiendo consultar la [guía oficial](https://wiki.archlinux.org/title/Installation_guide) en caso de encontrar que algo no sale como se supone.

A continuación vemos paso a paso el proceso de instalación:

1. Descargar la [ISO de Arch Linux](https://archlinux.org/download/). En concreto en mi caso utilicé [ésta versión](https://es.mirrors.cicku.me/archlinux/iso/2024.08.01/archlinux-2024.08.01-x86_64.iso).
2. Instalar la ISO en un pendrive o mejor aún en una microSD para utilizar la ranura que posee la Steam Deck. Puede utilizarse un programa como [Balena Etcher](https://www.balena.io/etcher/) o el comando `dd` de Linux si se [sabe manejar](/sistemas/raspi.html#backup-de-la-sd-comprimiendo-al-vuelo).
3. Arrancar la Steam Deck con el pendrive o la microSD insertada manteniendo pulsado el botón de bajar el volumen hasta que se escuchen los tonos de encendido. Esto hace que la consola arranque en el menú `Boot Manager`.
4. Seleccionar la opción de arrancar desde el dispositivo extraíble que aparecerá en el menú como `EFI USB Device (USB)` o `EFI SD/MMC Card (XX XXXX XXXX)` según si utilizamos un pendrive o una microSD respectivamente.
5. Una vez que termine de arrancar el sistema live de instalación de Arch, ejecutar los siguiente comandos en orden (en la sesión con `iwctl` sustituiremos `<SSID>` por el nuestro e introduciremos la contraseña cuando se nos pida; también sustituiremos el identificador de usuario `<USER>` por el que queramos utilizar):

    ```bash
    # loadkeys es
    # iwctl
    [iwd]# station wlan0 scan
    [iwd]# station wlan0 get-networks
    [iwd]# station wlan0 connect <SSID>
    [iwd]# exit
    # mkfs.ext4 /dev/nvme0n1p10
    # mkswap /dev/nvme0n1p9
    # mount /dev/nvme0n1p10 /mnt
    # mount --mkdir /dev/nvme0n1p1 /mnt/boot/efi
    # swapon /dev/nvme0n1p9
    # pacstrap -K /mnt base base-devel linux linux-firmware sudo vi ntfs-3g networkmanager amd-ucode grub efibootmgr git cmake qt5-wayland
    # genfstab -U /mnt >> /mnt/etc/fstab
    # arch-chroot /mnt
    # ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime
    # hwclock --systohc
    # vi /etc/locale.gen    # descomentar 'en_US.UTF-8 UTF-8' y 'es_ES.UTF-8 UTF-8'
    # locale-gen
    # echo "LANG=es_ES.UTF-8" > /etc/locale.conf
    # echo "KEYMAP=es" > /etc/vconsole.conf
    # echo "deck" > /etc/hostname
    # echo -e "\n127.0.0.1    localhost\n::1    localhost\n127.0.1.1    deck" >> /etc/hosts
    # passwd
    # grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Arch
    # grub-mkconfig -o /boot/grub/grub.cfg
    # systemctl enable NetworkManager
    # useradd -m -G wheel <USER>
    # passwd <USER>
    # chmod u+w /etc/sudoers
    # vi /etc/sudoers       # Descomentar '%wheel ALL=(ALL) ALL'
    # chmod u-w /etc/sudoers
    # pacman -Syy
    # pacman -S xorg-server xf86-video-amdgpu maliit-keyboard qt5-wayland
    # su - <USER>
    ```

El password que elegiremos cuando ejecutemos el comando `passwd <USER>` debe ser numérico si queremos utilizar Plasma Mobile, ya que la pantalla de desbloqueo sólo nos permite introducir un PIN.

## Instalación entorno gráfico

Continuamos donde nos habíamos quedado, es decir en la sesión chroot desde el sistema live de instalación de Arch Linux. Lo haremos ya con el usuario normal (no root) por lo que a partir de ahora haremos uso con frecuencia de `sudo`.

Ahora vamos a instalar los entornos gráficos. Lo digo en plural porque vamos a instalar dos, Plasma y Plasma Mobile. Hago esto porque dependiendo de si vamos a utilizar la Steam Deck con Arch en modo escritorio (con teclado/ratón y posiblemente pantalla) o portátil (sin teclado/ratón), nos convendrá más un sistema u otro, dado que Plasma Mobile presenta un interfaz diseñado para ser manejado con una pantalla táctil (estilo tablet).

En realidad no es necesario instalar los dos escritorios, por eso se han separado sus pasos de instalación. Podemos instalar uno, el otro o ambos.

#### Plasma

```bash
$ sudo pacman -S plasma-meta
```

Durante la instalación del paquete anterior se nos harán una serie de preguntas. A la tercera pregunta responder `2) noto-fonts`. En el resto ofrecer la respuesta predeterminada (pulsando retorno).

#### Plasma Mobile

Plasma Mobile no se encuentra todavía en los repositorios oficiales. Tenemos que utilizar [AUR](https://aur.archlinux.org/):

1. Empezamos instalando algunas dependencias:

    ```bash
    $ sudo pacman -S plasma-workspace kcontacts kirigami2 kpeople libphonenumber
    ```

2. Instalamos los paquetes de AUR `plasma-nano`, `plasma-settings` y `plasma-mobile` en este orden:

    ```bash
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-nano.git
    $ cd plasma-nano
    $ makepkg -si
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-settings.git
    $ cd plasma-settings
    $ makepkg -si
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-mobile.git
    $ cd plasma-mobile
    $ makepkg -si
    ```

#### Fin de instalación entorno gráfico

1. Instalamos el gestor de sesiones SDDM y Konsole que nos hará falta para terminar la instalación desde el modo gráfico:

    ```bash
    $ sudo pacman -S sddm konsole
    $ sudo systemctl enable sddm
    $ exit
    ```

2. Cerramos la sesión chroot, desmontamos las particiones y reiniciamos el sistema:

    ```bash
    # exit
    # umount -R /mnt
    # reboot
    ```

## Configuración básica

Tras reiniciar deberíamos ver el gestor de sesiones SDDM, inicialmente con la pantalla girada y sin posibilidad de utilizar el teclado en pantalla, por lo que todavía continuaremos utilizando el teclado y ratón externos.

Una vez que hayamos iniciado sesión en Plasma (o Plasma Mobile), abrimos la aplicación Konsole y ejecutamos los siguientes comandos para instalar el paquete de aplicaciones básico de KDE y el navegador Firefox:

```bash
$ sudo pacman -S firefox kde-applications-meta
```

Finalmente hacemos las dos siguientes configuraciones para ajustar la resolución de pantalla (que inicialmente escala las cosas para que se vean más grandes) y la distribución de teclado:

* Configurar la escala de la pantalla a 100% en `Preferencias > Preferencias del sistema > Pantalla y monitor > Escalar`.
* Añadir la distribución de teclado español en `Preferencias > Preferencias del sistema > Teclado > Distribuciones > Configurar distribuciones > Añadir (Español)`.

## Configuración de SDDM

Finalmente vamos a mejorar la configuración del gestor de sesiones SDDM para que permita el teclado en pantalla, tenga mejor aspecto y muestre la pantalla en la orientación correcta:

1. Crear fichero `/etc/sddm.conf.d/10-wayland.conf` con el siguiente contenido:

    ```ini
    [General]
    DisplayServer=wayland
    GreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell

    [Wayland]
    CompositorCommand=kwin_wayland --drm --no-lockscreen --no-global-shortcuts --locale1 --inputmethod maliit-keyboard
    ```

2. Abrir `Preferencias > Pantalla de inicio de sesión (SDDM)`, seleccionar Brisa como theme y pulsar el botón `Aplicar las preferencias de Plasma...` arriba a la derecha.

## Instalación gestor dualboot

El sistema Arch ya está listo y podemos arrancarlo encendiendo la consola en modo Boot Manager (manteniendo pulsada la tecla de bajar volumen) y seleccionando la opción `Arch`. Pero para facilitar el arranque de SteamOS, vamos a instalar un gestor de arranque dualboot llamado [rEFInd](https://github.com/jlobue10/SteamDeck_rEFInd).

1. Arrancar SteamOS (con Volume- + Power).
2. Desde una terminal en modo escritorio ejecutar:

    ```bash
    cd $HOME && rm -rf $HOME/SteamDeck_rEFInd/ && git clone https://github.com/jlobue10/SteamDeck_rEFInd && cd SteamDeck_rEFInd && chmod +x install-GUI.sh && ./install-GUI.sh
    ```

3. Descargar o crear un icono de Arch Linux de 128x128px.
4. Abrir el lanzador del escritorio que encontraremos en el escritorio.
5. Configurar de la siguiente forma (seleccionar en el campo `Boot Option #2 Icon` el icono descargado o creado anteriormente):

    ![Configuración de rEFInd](/images/posts/2024-09-04_steam_deck_arch/rEFInd_conf.png)

6. Pulsar botón `Create Config`.
7. Editar el fichero que encontraremos en `~/.local/SteamDeck_rEFInd/GUI/refind.conf` y modificar la última entrada de la siguiente forma:

    ```conf
    menuentry "Arch" {
        icon /EFI/refind/os_icon2.png
        loader /EFI/Arch/grubx64.efi
        graphics on
    }
    ```

8. Pulsar el botón `Install rEFInd`.
9. Pulsar el botón `Install Config`

La ruta `/EFI/Arch/grubx64.efi` del paso 6 puede cambiar si en el comando `grub-install` ejecutado durante la [instalación del sistema base](#instalacion-base) se eligió otro identificador que no fuera `Arch`. En ese caso habría que adaptar la ruta.

## Conclusión

Y esto sería todo. Ahora tenemos un sistema Arch Linux en nuestra Steam Deck con un gestor de arranque dualboot que nos permite arrancar también SteamOS. A partir de aquí tendremos una máquina con una naturaleza doble, una (SteamOS) para jugar y otra (Arch) para ser utilizada como un PC (Plasma) o tabletPC (Plasma Mobile).

Para elegir el entorno gráfico Plasma normal o el Plasma Mobile, utilizaremos el menú desplegable que aparece abajo a la izquierda en el gestor de inicios de sesión SDDM.

Algunos enlaces de interés consultados durante la elaboración de esta guía:

* [The Arch Linux Handbook – Learn Arch Linux for Beginners](https://www.freecodecamp.org/news/how-to-install-arch-linux/)
* [Instalando Arch Linux con KDE en Steam Deck](https://asgardius.company/?p=1783)