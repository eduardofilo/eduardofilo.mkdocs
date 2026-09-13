---
layout: default
permalink: /sistemas/linux.html
---

# Linux

## Enlaces

* [Colección de Carlos Fenollosa](http://mmb.pcb.ub.es/~carlesfe/#unix)
* [Tricks de Carlos Fenollosa](http://cfenollosa.com/misc/tricks.txt)
* [Bash Cheat Sheet](http://www.johnstowers.co.nz/blog/pages/bash-cheat-sheet.html)
* [Programar en Bash, pequeño manual de referencia](http://www.linuxhispano.net/2010/06/08/bash-manual-referencia-cheat-sheet-mini/)
* [How To Use Linux Screen](http://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/)
* [Bash Conditional Expressions](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)
* [Linux Command Library](https://linuxcommandlibrary.com/)

## Gestión de paquetes

### Equivalencias entre apt/dpkg y pacman

| Acción | Debian/Ubuntu | Arch |
| :--- | :--- | :--- |
| Actualizar la base de datos de paquetes | `apt update` | `sudo pacman -Syy` |
| Actualizar el sistema | `apt upgrade` | `sudo pacman -Syu` |
| Instalar un paquete | `apt install <paquete>` | `sudo pacman -S <paquete>` |
| Desinstalar un paquete dejando sus dependencias | `apt remove <paquete>` | `sudo pacman -R <paquete>` |
| Desinstalar un paquete y sus dependencias dejando las usadas por otros | `apt autoremove` | `sudo pacman -Rs <paquete>` |
| Desinstalar paquete, dependencias y ficheros de configuración | `apt purge` | `sudo pacman -Rns <paquete>` |
| Eliminar paquetes huérfanos | `apt autoremove` | `sudo pacman -Rns $(pacman -Qdtq)` |
| Buscar un paquete | `apt search` / `apt-cache search` | `pacman -Ss <paquete>` |
| Comprobar si un paquete está instalado | `dpkg -l \| grep <paquete>` | `pacman -Q <paquete>` |
| Listar los ficheros de un paquete | `dpkg -L <paquete>` | `pacman -Ql <paquete>` |
| Comprobar a qué paquete pertenece un archivo | `dpkg -S <archivo>` | `pacman -Qo <archivo>` |
| Listar todos los paquetes instalados | `apt list --installed` | `pacman -Q` |
| Listar paquetes instalados fuera de los repositorios | `apt list --installed \| grep -v /` | `pacman -Qm` |

### Comandos apt y dpkg

(Fuentes: [1](https://serverfault.com/questions/96964/list-of-files-installed-from-apt-package/96965#96965), [2](https://www.cyberciti.biz/faq/equivalent-of-rpm-qf-command/))

* Encontrar un paquete por su nombre: `apt-cache search 'cadena'`
* Encontrar un paquete ya instalado que contiene un fichero: `dpkg -S 'fichero'`
* Encontrar un paquete no instalado que contiene un fichero: `apt-file search 'fichero'`
* Localizar el repositorio del que procede un paquete: `apt-cache policy 'paquete'`
* Listar los ficheros que contiene un paquete ya instalado: `dpkg -L paquete`
* Listar los ficheros que contiene un paquete no instalado: `apt-file list paquete` (antes hay que hacer `apt-file update`)
* Listar los ficheros de un fichero .deb: `dpkg -c paquete.deb`
* Purgar los paquetes que quedaron en estado `rc` tras eliminarse (configuración residual): `sudo apt purge ~c`
* Solucionar problemas con paquetes mal instalados: `dpkg --configure -a`

Para usar `apt-file` hay que instalarlo y actualizar su base de datos previamente:

```bash
$ sudo apt-get install apt-file
$ sudo apt-file update
```

## Aplicaciones y servicios interesantes

* [ReText](https://github.com/retext-project/retext): Editor Markdown.
* [Franz](https://meetfranz.com/): [Configuración de icono en GNome](https://gist.github.com/jamiesoncj/756728b3ba7c07d7a90f843400af37bb).
* [App Grid](http://www.appgrid.org/): Repositorio de aplicaciones.
* [OpenWeather Shell Extension](https://itsfoss.com/display-weather-ubuntu/): Información del tiempo meteorológico en la barra de menú.
* [KodExplorer](https://github.com/kalcaddle/KODExplorer)
* [Gitea](https://gitea.io/en-us/)

## Comandos útiles

*  `strace -e file [command]`: runs `command`, printing out any time a file is opened or checked.
*  `strace -e file,network,process [command]`: the same as above, but also printing network process and subcommands run.
*  `strace -e file,process -f [command]`: the -f parameter follows forks -- in case it's not main command but a subshell that you're interested in.
*  `strace -p [PID]`: Connect to pid PID and start tracing.
*  `route -n` / `netstat -nr`: Tabla de rutas del sistema (muestra IPs en lugar de hostnames).
*  `du -h --max-depth=1 .`: Tamaño de un directorio y sus subdirectorios directos.
*  `du -sh */ | sort -h`: Muestra los directorios del directorio actual ordenados por tamaño (en formato humano) indicando su tamaño.
*  `find [directorio] ! -user [usuario] -ls`: Lista los ficheros que NO pertenecen a un usuario.
*  `badblocks -swv /dev/sda`: Bloquear sectores defectuosos (sustituir `/dev/sda` por el dispositivo que corresponda.
*  `sudo badblocks /dev/sda > badblocks.txt; sudo fsck -l badblocks.txt /dev/sda`: Bloqueo de sectores defectuosos del disco duro ([fuente](http://tech.chandrahasa.com/2013/06/09/how-to-check-your-hard-disk-for-bad-blocks-in-ubuntu/)).
*  `mkdosfs -F 32 -v -n "" /dev/sdc1`: Formato de partición en FAT32.
*  `cat fichero.txt | awk '{print $5}'`: Imprime la quinta columna (separando por espacios) de cada linea del fichero.
*  `cat fichero.txt | cut -d' ' -f5`: Imprime la quinta columna (separando por espacios) de cada linea del fichero.
*  `cat fichero.txt | sed -e 's/ /\n/g'`: Sustituye todos los espacios del fichero por retornos de carro.
*  `netstat -ntu|grep :80|wc -l`: número de conexiones al servidor HTTP.
*  `netstat -ntu|grep :21|wc -l`: número de conexiones al servidor FTP.
*  `netstat -tulanp`: Lista los puertos TCP/UDP abiertos (tanto de servidores como de clientes).
*  `netstat -tlnp`: Lista los puertos TCP abiertos de los servicios.
*  `sudo netstat -lp --inet`: Puertos de red abiertos y procesos asociados.
*  `crontab -e`: Añadir un job a cron.
*  `sudo blkid`: Lista los dispositivos de bloques (discos) disponibles en el sistema.
*  `sudo nmap -sP 192.168.1.0/24`: Descubrir todos los equipos presentes en la red `192.168.1.0`.
*  `sudo dd if=/dev/zero of=/dev/mmcblk0`: Formateo de una tarjeta de memoria (en realidad vale para cualquier dispositivo de almacenamiento).
*  `sudo tcpdump -s 0 -i ppp0 -w trafico.pcap`: Captura de tráfico por el interfaz ppp0.
*  `iptables -L -n`: Listar reglas iptables en formato numérico (muestra IPs en lugar de hostnames).
*  `iptables -t nat -L`: Listar reglas iptables de tabla NAT.
*  `wget -q -O - url`: Hace la request de la URL sin emitir trazas (-q = no verbose) y redireccionando la response a la salida estándar (-O -).
*  `cat /etc/resolv.conf`: Muestra el gateway en uso.
*  `nmcli dev show <adaptador_red>`: Muestra los parámetros de la conexión de red (IP, gateway, DNS's, etc.).
*  `ldd <binario>`: Indica las librerías que usa el binario.
*  `exiftool -AllDates='2010:08:08 15:35:33' -overwrite_original photo.jpg`: Actualiza todas las fechas dentro de la metainformación de un JPG.
*  `exiftool -all= photo.jpg`: Borrar toda la metainformación de una foto (por cuestiones de privacidad antes de subirla a un sitio por ejemplo).
*  `mplayer -vo caca MovieName.avi`: Reproduce un vídeo en consola con ascii. Para verlo en blanco y negro sustituir `caca` por `aa`.
*  `sudo traceroute -4T -p 22 192.168.1.203`: Comprobar la traza hasta alcanzar un determinado puerto en una determinada máquina.
*  `dig @8.8.8.8 -t any eduardofilo.es`: Query DNS de los registros de cualquier tipo a través del servidor `8.8.8.8` al dominio `eduardofilo.es`.
* `sudo stat /proc/1/exe`: Nos da pistas de si el sistema funciona sobre SysV, Upstart o Systemd ([fuente](https://unix.stackexchange.com/questions/196166/how-to-find-out-if-a-system-uses-sysv-upstart-or-systemd-initsystem)).
* `stty < /dev/port`: (sustituir `port` por lo que corresponda) Interroga el puerto para encontrar sus parámetros de conexión.
* `zenity`: Para dotar de cuadros de diálogo a los scripts bash. [Documentación](https://help.gnome.org/users/zenity/3.24/)
* `taskset`: Para fijar un proceso a un conjunto de CPUs. Por ejemplo `taskset -c 0-3 <command>` fija el proceso `<command>` a las CPUs 0-3.

## SSH

### Alias SSH

Para asimilar un identificador a una pareja user@host, editar el fichero `~/.ssh/config` y añadir un bloque como el siguiente ([fuente](http://collectiveidea.com/blog/archives/2011/02/04/how-to-ssh-aliases/)):

```
Host example
  HostName example.com
  User exampleuser
```

### Tunel de un puerto remoto por SSH

([Fuente](http://www.revsys.com/writings/quicktips/ssh-tunnel.html)) Para conducir el tráfico hasta un host:puerto remoto canalizándolo por un tunel seguro, se puede utilizar el comando `ssh`. Por ejemplo, vamos a tunelizar una conexión contra el puerto telnet de la máquina remota `telnet.example.com` por medio del usuario `ssh-user` para tenerlo disponible en el puerto 2000 local de nuestra máquina:

```
ssh -f ssh-user@telnet.example.com -L 2000:telnet.example.com:23 -N
```

A partir de ahora podremos conectarnos al telnet conectando con `localhost:2000`.

### Autentificación automática por SSH

Conseguiremos que la autentificación del cliente se haga por medio de una pareja de claves privada/pública en lugar de con identificador de usuario/password. Primero generamos la pareja de claves pública-privada ejecutando en el cliente `ssh-keygen`:

```bash
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is:
xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx user@machine
```

Las claves se almacenan por defecto en `~/.ssh/`, quedando el directorio así:

```bash
$ ls -l
total 12
-rw-------  1 user user  883 2005-08-13 14:16 id_rsa
-rw-r--r--  1 user user  223 2005-08-13 14:16 id_rsa.pub
-rw-r--r--  1 user user 1344 2005-08-04 02:14 known_hosts
```

Los ficheros `id_rsa` e `id_rsa.pub` contienen respectivamente las claves privada y pública. El fichero `known_hosts` contiene la lista de las claves públicas de las máquinas reconocidas.

Ahora se debe copiar la clave pública al servidor, al fichero `~/.ssh/authorized_keys`. Para ello se utiliza el comando ssh-copy-id:

```bash
$ ssh-copy-id -i ~/.ssh/id_rsa.pub user@machine1
$ ssh-copy-id -i ~/.ssh/id_rsa.pub user@machine2
```

`ssh-copy-id` es un script que se conecta a la máquina y copia el archivo (indicado por la opción `-i`) en `~/.ssh/authorized_keys`, y ajusta los permisos a los valores adecuados.

Si no se dispone del programa `ssh-copy-id` se puede realizar una copia manual a la máquina remota del fichero conteniendo la clave pública (por ejemplo usando `scp` o `sftp`) y añadir su contenido al fichero `~/.ssh/authorized_keys`.

Ahora la conexión debería funcionar sin necesidad de introducir la clave. Si no es así es posible que sea un problema de permisos en los ficheros. Los permisos correctos deben ser similares a estos:

```bash
$ chmod go-w ~ ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
```

La conexión SSH se realizará indicando el fichero con la clave privada como argumento de la siguiente forma:

```bash
$ ssh -i ~/.ssh/id_rsa user@machine
```

(Si el nombre del fichero con la clave privada es precisamente el del ejemplo, es decir `id_rsa`, creo que no es necesario indicarlo con la opción `-i`).

### Ejecución remota de aplicaciones XWindow

 1.  Abrir el servidor X (Cygwin)
 2.  Iniciar sesión remota: ssh -X [usuario]@[máquina]
 3.  Ejecutar la aplicación

## Uso básico de `screen`

En [esta cheat sheet](http://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/) se reúnen bastantes comandos útiles. A continuación indico el uso típico:

1. Arrancamos una sesión:

        shell ~$ screen

2. Aparece una splashscreen que cerramos pulsando enter y ya podemos trabajar
3. Lanzamos un comando:

        screenshell_1 ~$ top

4. Para cerrar la sesión screen que acabamos de abrir, tan sólo hay que lanzar el comando `exit` (en este ejemplo, parando previamente el comando `top` que habíamos lanzado). Ahora sin embargo pretendemos dejarla abierta, con el comando `top` en ejecución, para volver a ella más adelante. Es lo que se llama un detach (sirve para recordar la tecla que se pulsa al final de la combinación de teclas). Para ello pulsamos la combinación de teclas:

        "Ctrl-a" "d"

5. Habremos vuelto a nuestro bash inicial. Cuando en cualquier momento queramos recuperar la sesión screen, lo haremos con el comando:

        shell ~$ screen -r

6. Ahora estaremos viendo de nuevo la salida del comando top que habíamos dejado arrancado dentro de la sesión screen. Volvemos a abandonar la sesión sin cerrarla procediendo por tanto como en el paso 4:

        "Ctrl-a" "d"

7. De vuelta al bash inicial, vamos a abrir una segunda sesión screen para ver cómo podemos movernos a una u a otra. Arrancamos la sesión como hicimos con la primera:

        shell ~$ screen

8. Cerramos la splashscreen y ejecutamos algún comando para reconocer la sesión cuando volvamos a ella. Por ejemplo:

        screenshell_2 ~$ ping 8.8.8.8

9. Abandonamos la sesión dejándola abierta:

        "Ctrl-a" "d"

10. De vuelta al bash inicial ahora tenemos dos sesiones screen lanzadas. Ahora el comando `screen -r` no se puede lanzar sin especificar el identificador de la sesión tras la opción `-r`. Obtenemos la lista de sesiones con el siguiente comando:

        shell ~$ screen -list
        There are screens on:
            12629.pts-7.eduardo-HP-Folio-13	(04/04/15 13:55:03)	(Detached)
            12609.pts-7.eduardo-HP-Folio-13	(04/04/15 13:54:51)	(Detached)
        2 Sockets in /var/run/screen/S-edumoreno.

11. Ahora, para recuperar una de ella, por ejemplo la más vieja que contenía lanzado el comando `top` incorporaremos el identificador de la sesión tras la opción `-r` (si la sesión aparece en el listado como Attached, no podremos conectar a no ser que añadamos la opción `-d`):

        shell ~$ screen -r 12609.pts-7.eduardo-HP-Folio-13

12. Como se comentaba en el punto 4, para cerrar las sesiones simplemente saldremos con `exit`, aunque también, y sobre todo en caso de que la sesión se quedara bloqueada con algún comando que no se pudiera cerrar, se puede matar la sesión con la siguiente combinación de teclas:

        "Ctrl-a" "k"

## GRUB

### Configuración de opción predeterminada en GRUB

[Fuente](https://forums.linuxmint.com/viewtopic.php?t=230650)

1. Editar fichero `/etc/default/grub` y modificar el parámetro `GRUB_DEFAULT` dando el valor `saved` en lugar del valor numérico que encontraremos.
2. Ejecutar `sudo update-grub`.
3. Ejecutar `sudo grub-set-default N` siendo N la posición de la entrada del menú de GRUB que queremos que actúe como predeterminada (contando desde 0).

### Problemas con GRUB

[Reinstalar GRUB 2](http://molinuxaula.pbworks.com/w/page/27409912/Reinstalar%20GRUB%202)

### UEFI

* [How to get GRUB to be the default bootloader instead of Windows Boot Manager on a UEFI laptop?](https://askubuntu.com/questions/666631/how-to-get-grub-to-be-the-default-bootloader-instead-of-windows-boot-manager-on/666632#666632)
* [UEFI boot: how does that actually work, then?](https://www.happyassassin.net/posts/2014/01/25/uefi-boot-how-does-that-actually-work-then/)

## Arranque y servicios

### Ficheros implicados en arranque

*  `/etc/rc.local`: This script is executed at the end of each multiuser runlevel.

### Instalación/desinstalación de scripts SysV/Upstart

Los scripts del serivicio deberán tener una cabecera especial que indique cómo deben comportarse en cada nivel de ejecución. Por ejemplo éste es el que tiene MySQL:

```
#!/bin/bash
#
### BEGIN INIT INFO
# Provides:          mysql
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Should-Start:      $network $time
# Should-Stop:       $network $time
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start and stop the mysql database server daemon
# Description:       Controls the main MySQL database server daemon "mysqld"
#                    and its wrapper script "mysqld_safe".
### END INIT INFO
#
```

* Instalar: `sudo update-rc.d SERVICE defaults`
* Desinstalar: `sudo update-rc.d -f SERVICE remove`

### Creación de servicios Systemd

1. Crear un archivo en `/etc/systemd/system/` con el nombre del servicio y la extensión `.service`.
2. Insertar el siguiente contenido:

    ```
    [Unit]
    Description=Nombre del servicio
    Wants=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    ExecStart=/bin/bash /home/usuario/script_arranque.sh
    Restart=on-abort
    User=usuario
    Group=usuario

    [Install]
    WantedBy=multi-user.target
    ```

3. Activar el nuevo servicio:

        $ sudo systemctl enable mi_servicio.service

4. Para no esperar al reinicio, arrancar manualmente el servicio:

        $ sudo systemctl start mi_servicio.service

5. Para comprobar si el servicio se inicia correctamente:

        $ sudo systemctl status mi_servicio.service

### Gestión de servicios Systemd

* `systemctl start SERVICE` - Use it to start a service. Does not persist after reboot
* `systemctl stop SERVICE` - Use it to stop a service. Does not persist after reboot
* `systemctl restart SERVICE` - Use it to restart a service
* `systemctl reload SERVICE` - If the service supports it, it will reload the config files related to it without interrupting any process that is using the service.
* `systemctl status SERVICE` - Shows the status of a service. Tells whether a service is currently running.
* `systemctl enable SERVICE` - Turns the service on, on the next reboot or on the next start event. It persists after reboot.
* `systemctl disable SERVICE` - Turns the service off on the next reboot or on the next stop event. It persists after reboot.
* `systemctl is-enabled SERVICE` - Check if a service is currently configured to start or not on the next reboot.
* `systemctl is-active SERVICE` - Check if a service is currently active.
* `systemctl show SERVICE` - Show all the information about the service.
* `systemctl mask SERVICE` - Completely disable a service by linking it to `/dev/null`; you cannot start the service manually or enable the service.
* `systemctl unmask SERVICE` - Removes the link to `/dev/null` and restores the ability to enable and or manually start the service.

## Kernel y módulos

### Añadir un módulo al kernel

```bash
$ sudo modprobe <modulo>
```

Si se quiere añadir de forma permanente, es decir, de forma automática en el arranque, se incorpora el nombre del módulo al fichero `/etc/modules`.

Cuando el módulo que se carga es un driver de un dispositivo, el kernel envía un evento al subsistema `udev`. La monitorización de estos mensajes se puede hacer teniendo abierto un terminal con el siguiente comando lanzado ([fuente](https://wiki.ubuntu.com/Kernel/Firmware)):

```bash
$ udevadm monitor --property
```

### Listado de módulos

```bash
$ lsmod
```

### Información de un módulo

```bash
$ modinfo <modulo>
```

## Usuarios

### Gestión de usuarios

*  `sudo adduser userName`: Añade usuario creando home.
*  `sudo usermod -a -G groupName userName`: Añade el usuario userName ya existente al grupo groupName ya existente.
*  `sudo userdel -r userName`: Borra el usuario eliminando su home.

### Cambiar ID de usuario

Por ejemplo para sincronizar con los IDs de un sistema de archivos montado por NFS y así no tener problemas de permisos. En el siguiente ejemplo se cambia el ID del usuario edumoreno a 1002:

```bash
sudo usermod -u 1002 edumoreno
```

### Eliminar petición password en sudo

Es necesario reconfigurar el fichero `/etc/sudoers` para que no se solicite el password del usuario a la hora de hacer sudo, dado que necesitamos que se haga sudo desde un proceso que no tendrá interacción con el usuario. Para conseguir esto hay que hacer dos cosas:

1.  Incorporar el usuario que nos interesa al grupo `sudo` del sistema
2.  Situar al final del fichero de configuración `/etc/sudoers` lo siguiente:

```
%sudo ALL=NOPASSWD: ALL
```

Hay que fijarse que la linea anterior normalmente ya aparece en el fichero pero comentada con una almohadilla. Se puede aprovechar la linea quitando el carácter almohadilla del principio, pero hay que tener en cuenta que no es suficiente con eso. Hay que mover la linea al final del fichero ya que las lineas siguientes pueden sobreescribir su efecto.

**Importante**: La edición del fichero `/etc/sudoers` sólo se puede hacer con el comando `visudo`. Este comando hay que lanzarlo con `sudo` a su vez, por lo que se hará de la siguiente forma:

```bash
$ sudo visudo
```

### Migración masiva de usuarios

([Fuente](http://www.esemanal.com.mx/articulos.php?id_sec=5&id_art=4583))

Para los casos en los que sea necesario replicar los usuarios de un servidor Linux a otro o en los que se vaya a migrar a un servidor con más recursos, el siguiente procedimiento puede ser de utilidad.

Los escenarios son varios, desde los servidores que ejecutan algún tipo de base de datos, los que tienen ciertas aplicaciones, los que alojan páginas Web, etcétera. Para fines de la demostración pensaremos que el servidor está dedicado como servidor de archivos, mismos que se almacenan en el home de cada uno de los usuarios.
NOTA: El presente procedimiento da por hecho que se hayan realizado las configuraciones necesarias en el nuevo servidor.

Primero, lo que debe respaldarse es la lista de usuarios con su respectiva contraseña.
El archivo `/etc/passwd` contiene las cuentas de los usuarios en el sistema bajo el siguiente formato de ejemplo:

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/
nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
nitsuga:x:500:500::/home/nitsuga:/bin/bash
nitsuga2:x:501:501::/home/nitsuga2:/bin/bash
nitsuga3:x:502:502::/home/nitsuga3:/bin/bash
```

Como se observa, el segundo campo respectivo al hash de la contraseña no se muestra. La contraseña se encuentra en el archivo `/etc/shadow`

```
root:$1$/7zmwgAa$Jd5ja7nsC4nTm
O3s0.Z1j1:13445:0:99999:7:::
bin:*:13445:0:99999:7:::
daemon:*:13445:0:99999:7:::
adm:*:13445:0:99999:7:::
nitsuga:$1$QwPqN0Vc$dn9OIyE3HQUh5W4Yh/.aQ.:13498:2:1:1:::
nitsuga2:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:13496:2:45:7:::
nitsuga3:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:13496:2:45:7:::
```

Se procederá a unir el usuario con su contraseña utilizando el comando `pwunconv` para “desactivar” el shadow, quedando así las contraseñas en el archivo passwd.

```
root:$1$/7zmwgAa$Jd5ja7nsC4n
TmO3s0.Z1j1:0:0:root:/root:/bin/bash
bin:*:1:1:bin:/bin:/sbin/nologin
daemon:*:2:2:daemon:/sbin:/sbin/
nologin
adm:*:3:4:adm:/var/adm:/sbin/nologin
nitsuga:$1$QwPqN0Vc$dn9OIyE3HQUh5W4Yh/.aQ.:500:500::/home/
nitsuga:/bin/bash
nitsuga2:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:501:501::/home/nitsuga2:/bin/bash
nitsuga3:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:502:502::/home/nitsuga3:/bin/bash
```

#### Depuración de /etc/passwd

Se copiará el archivo `/etc/passwd` a uno de trabajo `/etc/passwd.migracion`. Ahora se editará el archivo y se quitarán todos los usuarios propios del sistema (root, usuarios de demonios, etcétera) dejando sólo los usuarios que van a ser autenticados.

```
nitsuga:$1$QwPqN0Vc$dn9OIyE3HQUh5W4Yh/.aQ.:500:500::/home/nitsuga:/bin/bash
nitsuga2:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:501:501::/home/nitsuga2:/bin/bash
nitsuga3:$1$635CQht0$rFIbilzKqfc1zStqeOwlk/:502:502::/home/nitsuga2:/bin/bash
```

También se copiará el archivo `/etc/group` a `/etc/group.migracion`

```
root:x:0:root
bin:x:1:root,bin,daemon
daemon:x:2:root,bin,daemon
sys:x:3:root,bin,adm
adm:x:4:root,adm,daemon
nitsuga:x:500:
nitsuga2:x:501:
nitsuga3:x:502:
nitsuga8:x:507:
```

Y se editará para dejar sólo los grupos de los usuarios:

```
nitsuga:x:500:
nitsuga2:x:501:
nitsuga3:x:502:
```

Ahora se respaldará el home de los usuarios, suponiendo que se encuentra bajo el directorio/home, se hará lo siguiente desde raíz (/):

```
[root@localhost /]# tar -cpzvf home.tgz home/
```

En el que las banderas:

*  c = crea el archivo
*  p = preserva los permisos
*  z = comprime el archivo .tar generado
*  v = da salida detallada
*  f = especifica el archivo a crear (para este caso home.tgz)

Ahora bien, se realizará la transferencia de los archivos home.tgz, passwd.migracion y group.migracion al nuevo servidor:

```
[root@localhost /]# scp /home.tgz root@nuevoservidor

[root@localhost /]# scp /etc/passwd.migracion root@nuevoservidor

[root@localhost /]# scp /etc/group.migracion root@nuevoservidor
```

Una vez en el nuevo servidor se deberá verificar que no se repitan tanto los UID como los GID entre los dos servidores.
Se realizará:

```
[root@localhost /]# cp –p home.tgz / ; tar –zxvf home.tgz

[root@localhost /]# cp –p passwd.migracion /etc ; pwunconv ; cat passwd.migracion >> passwd; pwconv

[root@localhost /]# cp –p group.migracion /etc ; cat group.migracion >> group
```

## Configuración del sistema

### Ficheros interesantes

|Fichero|Utilidad|
|:------|:-------|
|`/usr/lib/os-release`|Información sobre la distribución|
|`/etc/security/limits.conf`|Configuration file for the pam_limits module. Permite limitar el número de ficheros abiertos por el sistema, el número de procesos, etc.|

### Ficheros definición variables de entorno

Si se necesita definir una variable global se podrá hacer en los ficheros:

* `/etc/environment`
* `/etc/profile`
* `/etc/profile.d`
* `/etc/bashrc` o `/etc/bash.bashrc`

Si es a nivel de usuario se hará en:

* `~/.bashrc`
* `~/.bash_profile`

### Error "error while loading shared libraries: ..."

Runtime error. The linker hasn't found your libraries. Either they are not installed properly or the linker doesn't know where they are (most probably in `/usr/local/lib`). To get your linker to update its list of libraries type:

```bash
$ ldconfig /usr/local/lib
```

or as a temporary measure:

```bash
$ export LD_LIBRARY_PATH="/usr/local/lib"
```

En [este documento](https://codeyarns.com/2014/01/14/how-to-fix-shared-object-file-error/) se dan más detalles.

### Proxy HTTP en consola

Setting up proxy at Firefox do not have effects at console, which means your wget, ssh, apt-get, yum etc do not access through the proxy you set at Firfox browser. To setup http proxy at console, you can do as bellow, assume the proxy IP is 219.93.2.113 and port 3128:

```bash
$ export http_proxy='http://219.93.2.113:3128/'
```

Remember, you have to specified http://, and to know more about export, check out HERE.
To clear your http proxy and use back yours, do this:

```bash
$ export http_proxy=''
```

### Redirección de salidas en bash

Para redirigir ambas salidas de un programa (estandar y error) hacer lo siguiente:

```bash
$ COMANDO>FICHERO_O_DISPOSITIVO 2>&1
```

Para redirigir la salida de error a un fichero o dispositivo:

```bash
$ COMANDO 2>FICHERO_O_DISPOSITIVO
```

En [esta página](https://web.archive.org/web/20170715100659/http://sc.tamu.edu/help/general/unix/redirection.html) se documenta con más detalle este tema.

### Convertir nombres de ficheros de ISO a UTF-8

Al migrar una web, o al copiar un sistema de archivos, te puedes encontrar con nombres de ficheros en otras codificaciones de caracteres. Mediante el siguiente comando transformaríamos los nombres de ficheros desde ISO-8869-1 a UTF-8:

```bash
$ convmv -r -f ISO-8859-1 -t UTF-8  --notest *
```

### Recodificar contenido de ficheros de Windows a UTF-8

```bash
$ recode ISO-8859-15/CR-LF..UTF8 fichero.txt
```

Para todos los ficheros de texto de un directorio:

```bash
$ find . ! -type d -name "*.txt" -exec recode ISO-8859-15/CR-LF..UTF8 {} \;
```

### Obtener hash MD5 de una cadena

```bash
$ echo -n "<cadena>"|md5sum
```

### Localización de ficheros .desktop

* Los del usuario se encuentran en: `~/.local/share/applications`
* Los del sistema en: `/usr/share/applications`

## Permisos

### Ajustes de permisos a ficheros y directorios por separado

```bash
$ #Para los ficheros:
$ find . ! -type d -exec chmod 664 {} \;
$ #Para los directorios:
$ find . -type d -exec chmod 775 {} \;
```

### Bits SUID, SGID y sticky

[Manual de LuCAS](http://lucas.olea.org/Manuales-LuCAS/doc-unixsec/unixsec-html/node56.html)

## Discos, particiones y montaje

### Reparación del sistema de archivos cuando se pone en modo "sólo lectura"

```bash
$ sudo fsck
```

### Recuperación de pendrive o tarjeta de memoria corrupta

Con TestDisk/Photorec.

#### Enlaces

* [TestDisk Paso A Paso](http://www.cgsecurity.org/wiki/TestDisk_Paso_A_Paso)
* [How to Recover Data from Corrupt / formatted USB Flash using Photorec](https://linoxide.com/linux-how-to/recovery-data-corrupt-formatted-usb-flash-using-photorec/)

### Montar imagen de disco o partición

([Fuente](http://www.forensicswiki.org/wiki/Mounting_Disk_Images#To_mount_a_disk_image_on_Linux), [también aquí](http://www.linuxquestions.org/questions/linux-general-1/how-to-mount-img-file-882386/))

1. Averiguar la estructura de las particiones:

    ```bash
    $ fdisk -l Rpi_8gb_wheezy_backup.img
    Disco Rpi_8gb_wheezy_backup.img: 7,5 GiB, 8068792320 bytes, 15759360 sectores
    Unidades: sectores de 1 * 512 = 512 bytes
    Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
    Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
    Tipo de etiqueta de disco: dos
    Identificador del disco: 0x000981cb

    Dispositivo                Inicio Comienzo    Final Sectores Tamaño Id Tipo
    Rpi_8gb_wheezy_backup.img1            8192   122879   114688    56M  c W95 FAT32 (LBA)
    Rpi_8gb_wheezy_backup.img2          122880 15759359 15636480   7,5G 83 Linux
    ```

2. Calcular el offset multiplicando el sector de comienzo de la partición por el tamaño del sector:

    ```
    122880 * 512 = 62914560
    ```

3. Montar:

    ```bash
    $ sudo mount -t ext4 -o loop,offset=62914560,ro,noexec Rpi_8gb_wheezy_backup.img mnt
    ```

### Backup de un FileSystem

Backup:

```bash
$ dd if=/dev/hdx | gzip > /path/to/image.gz
```

Restauración:

```bash
$ gzip -dc /path/to/image.gz | dd of=/dev/hdx
```

### Montar ext4 para usuario

Normalmente al automontar una partición ext4 se respetarán los ID's de los propietarios:grupos de los ficheros. Para montar temporalmente con permisos ajustados para un usuario, utilizar `bindfs` de esta forma:

```bash
# El punto de partida es una partición automontada de esta forma:
# /dev/sdb1                                   306616440      64348   290907216   1% /media/edumoreno/47acea17-841f-42d3-85f2-886543f056db
sudo bindfs -u $(id -u) -g $(id -g) /media/edumoreno/47acea17-841f-42d3-85f2-886543f056db /home/edumoreno/mnt/
```

## Compartir ficheros en red

### Compartir ficheros con Samba

Aparte de instalar y configurar Samba (fichero `/etc/samba/smb.conf`) hay que dar de alta los usuarios UNIX que se usarán a través de Samba y asignarles un password para el acceso por el mismo. Esto se hace con el comando:

```bash
$ sudo smbpasswd -a usuario
```

### Montaje de carpeta compartida samba en /etc/fstab

Crear un fichero `/home/usuario/.smbcredentials` con el siguiente contenido:

```
user=usuario
password=password
```

Añadir la siguiente línea a `/etc/fstab`:

```
192.168.1.100/carpeta_compartida /home/usuario/punto_montaje cifs uid=usuario,gid=usuario,credentials=/home/usuario/.smbcredentials,iocharset=utf8,sec=ntlmv2,file_mode=0664,dir_mode=0775 0 0
```

### Montado de unidades de red con autofs

#### NFS

([Fuente](http://www.instructables.com/id/Reduce-overhead-due-to-network-drive-on-Raspberry-/))

1. Instalar paquetes:

    ```bash
    $ sudo apt-get install autofs nfs-common
    ```

2. Añadir lo siguiente al final del fichero `/etc/auto.master`:

    ```
    /home/usuario/red   /etc/auto.red
    ```

3. Crear fichero `/etc/auto.red` con el siguiente contenido (cambiar rw por ro si se desea acceso de sólo lectura):

    ```
    montaje  -fstype=nfs4,rw 192.168.1.100:/path/directory
    ```

4. Crear enlaces a los directorios montados con autofs:

    ```bash
    $ cd ~
    $ ln -s /home/usuario/red/montaje montaje
    ```

#### SMB/CIFS

([Fuente](https://serverfault.com/questions/219615/mount-cifs-share-with-autofs))

1. Instalar paquetes:

    ```bash
    $ sudo apt-get install autofs smbclient cifs-utils
    ```

2. Añadir lo siguiente al final del fichero `/etc/auto.master`:

    ```
    /home/usuario/red /etc/auto.red --timeout=600
    ```

3. Crear fichero `/etc/auto.red` con el siguiente contenido:

    ```
    montaje  -fstype=cifs,rw,noperm,netbiosname=${HOST},credentials=/home/usuario/.smbcredentials  ://192.168.1.100/carpeta_compartida
    ```

4. Crear fichero `/home/usuario/.smbcredentials` con el siguiente contenido:

    ```
   username=<usuario>
   password=<password>
   ```

5. Proteger el fichero:

    ```bash
    $ chmod 600 /home/usuario/.smbcredentials
    ```

6. Crear enlaces a los directorios montados con autofs:

    ```bash
    $ cd ~
    $ ln -s /home/usuario/red/montaje montaje
    ```

### Mini servidor HTTP

[Web oficial](http://acme.com/software/thttpd/)

```bash
$ wget http://www.acme.com/software/thttpd/thttpd-2.29.tar.gz
$ tar xzvf thttpd-2.29.tar.gz
$ cd thttpd-2.29/
$ ./configure
$ make
$ sudo ./thttpd -d <directorio_root>
```

## Escritorio

### Configuración de gedit

Al menos las últimas versiones de gedit no tienen un panel de ajustes para las opciones predeterminadas. Cada vez que arranca aparecen preajustados 8 espacios como anchura del tabulador y no sustituye por espacios. Puede sacarse una lista de todos los ajustes que se pueden cambiar con el siguiente comando:

```
gsettings list-recursively | grep -i gedit.preferences.editor
```

Los ajustes del tabulador mencionados antes, para pasar a 4 espacios, ejecutar:

```
gsettings set org.gnome.gedit.preferences.editor insert-spaces true
gsettings set org.gnome.gedit.preferences.editor tabs-size 4
```

Otro ajuste interesante es el del wrap mode. Se puede hacer con (puede valer 'none', 'word', 'char', o 'word-char'):

```
gsettings set org.gnome.gedit.preferences.editor wrap-mode 'word'
```

### Recursos gráficos

```
/usr/share/icons
/usr/share/app-install/icons
/usr/share/pixmaps
/usr/share/icons/gnome
/usr/share/icons/hicolor
/usr/share/icons/Human
/usr/share/icons/Humanity        <---
/usr/share/icons/oxygen
/usr/share/icons/default.kde4    <---
```

### Restaurar panel Gnome

([fuente 1](http://www.google.com/url?q=http%3A%2F%2Fsuperuser.com%2Fquestions%2F129320%2Fhow-do-i-restore-the-default-applets-to-gnomes-notification-area&sa=D&sntz=1&usg=AFQjCNGUVYnYCoUfrVCGX5tIHc5UWBNeDw); [fuente 2](http://www.google.com/url?q=http%3A%2F%2Fwww.watchingthenet.com%2Frestore-panels-in-ubuntu-back-to-their-default-settings.html&sa=D&sntz=1&usg=AFQjCNHAEFYUaK7ztqIKEgF563uoWWTHBw))

```bash
$ gconftool --recursive-unset /apps/panel
$ rm -rf ~/.gconf/apps/panel
$ pkill gnome-panel
```

### Organización de menús cuando se mezclan aplicaciones KDE y Gnome

GNU/Linux nos permite tener varios sistemas de escritorio diferentes instalados y funcionando, pero inevitablemente nos encontramos con una mezcla de opciones y programas de cada entorno en los menús principales. Existen aplicaciones precisamente para limpiar automáticamente las entradas del menú que no corresponden a tu sistema de escritorio habitual, y dejarlas apartadas y ordenadas de alguna manera. Con Gnome y KDE instalados a la vez, hay dos programas para aquellos Gnomeros que han querido probar KDE y para los KDEeros que han querido probar Gnome.

*  [Gnome Menu Extended](http://www.gtk-apps.org/content/show.php/Gnome+Menu+Extended+%28Debian+Package%29?content=73515) es el propio menú normal de Gnome, pero incluye una carpeta donde se guardan todas las aplicaciones y opciones de KDE. Se instala fácilmente descargando el paquete para cualquier distribución: Debian (y Ubuntu), Slackware o directamente el código fuente para compilarlo. Una vez instalado, se activa yendo a Preferencias -> Add KDE Menu. Y si quieres recuperar el menú como estaba, también tiene la opción de restaurarlo.
*  [K Menu Gnome](http://www.kde-apps.org/content/show.php/K+Menu+Gnome+%28Debian+Package%29?content=31031&amp;PHPSESSID=39c71268b399effce8c57dbf8ff09e16) es un menú exactamente igual que el KMenu original, pero incluye una carpeta donde residen todas las aplicaciones de Gnome, en sistemas que tienen ambos escritorios instalados. Está disponible para Debian (y Ubuntu), Slackware, Fedora y el código fuente para compilarlo en cualquier sistema.

### Fondo de escritorio con la imagen astronómica del día (APOD)

Programa para descargar y ajustar como fondo de escritorio la imagen astronómica del día de la web [APOD](http://apod.nasa.gov/apod/). Es necesario que se encuentre Python instalado en el sistema.

Instalar el siguiente script en algún lugar:

```python
#!/usr/bin/python

#APOD in the GNOME desktop
#Author: Rodrigo Rivas Costa.
#Mail:  rodrigorivascosta@gmail.com
#Web:   http://rodrigo.dualnot.com/

# This program is in public domain, so do whatever you wish with it,
# although it'd be nice if you keep the above notice.
# Just don't blame me if it blows your computer.

import urllib
import gconf
import os

dir = os.getenv('HOME') + '/.apod'
try:
    os.mkdir(dir)
except:
    pass

try:
    execfile(dir + '/options.py')
except:
    pass

def DoAPOD():
    u = urllib.urlopen('http://apod.nasa.gov/apod/')
    KEY1 = 'href="'
    KEY2 = '"'
    image = None
    for line in u.readlines():
        pos1 = line.find(KEY1)
        if pos1 == -1:
            continue
        pos1 += len(KEY1)
        pos2 = line.find(KEY2, pos1)
        if pos2 == -1:
            continue
        href = line[pos1:pos2]
        hrefl = href.lower()
        if hrefl.endswith('.jpg') or hrefl.endswith('.png'):
            image = href
            break
    u.close()

    if not image:
        return

    image_base = os.path.split(image)[-1]
    image_base_ext = os.path.splitext(image_base)
    image_base = 'apod' + image_base_ext[-1]

    if not (image.startswith('http:') or image.startswith('ftp:')):
        if not image.startswith('/'):
            image = '/apod.nasa.gov/apod/' + image
        image = 'http:/' + image

    img = urllib.urlopen(image)
    d = img.read()
    img.close()

    try:
        os.unlink('apod.jpg')
    except:
        pass
    try:
        os.unlink('apod.png')
    except:
        pass

    name = dir + '/' + image_base
    f = file(name, 'wb')
    f.write(d)
    f.close()

    cli = gconf.client_get_default()
    cli.set_string('/desktop/gnome/background/picture_filename', name)
    cli.set_string('/desktop/gnome/background/picture_options', 'zoom')

if __name__ == '__main__':
    DoAPOD()
```

Por último programar una tarea en cron para ejecutar el script con el usuario al que queramos que se aplique el fondo de escritorio. Por ejemplo introduciendo la siguiente línea en `/etc/crontab` para que se ejecute a las 10 de la mañana:

```
00 10   * * *   edumoreno       /home/edumoreno/.apod/apod
```

En el ejemplo se ha puesto como ejemplo el usuario `edumoreno` así como su home.

## Multimedia

### Redimensionado de imágenes en lote

Por ejemplo a 1080 de alto manteniendo el ratio dentro de un directorio llamado resized:

```bash
$ convert '*.jpg[x1080]' resized/%03d.jpg
```

En ocasiones, si hay varios miles de fotos, se puede llenar la memoria. En este caso hacer la conversión con el siguiente comando, que trata las imágenes una a una:

```bash
a=1
for i in *.jpg; do
  new=$(printf "%04d.jpg" ${a})
  convert ${i}[x1080] resized/${new}
  let a=a+1
done
```

### Crop y resize de imágenes en lote

```bash
a=1
for i in *.jpg; do
  new=$(printf "%04d.jpg" ${a})
  convert ${i} -crop wxh+x+y -resize wsxhs -gravity Center ${new}
  let a=a+1
done
```

donde:

* w: ancho del crop
* h: alto del crop
* x: posición horizontal esquina superior derecha del crop
* y: posición vertical esquina superior derecha del crop
* ws: ancho del reescalado final
* hs: alto del reescalado final

### Conversión de formato de imágenes en lote

```bash
for file in *.jpg; do
  filename=$(basename "$file")
  fileid=${filename%%.*}
  convert ${filename} ${fileid}.png
done
```

### Montaje de gif a partir de imágenes

```bash
convert -delay n -loop 0 *.jpg output.gif
```

donde:

* n: milisegundos entre cada frame.

### Split de vídeos

([Fuente](http://askubuntu.com/questions/35605/splitting-an-mp4-file))

Con el siguiente comando:

```bash
$ ffmpeg -i archivo_original.mp4 -codec copy -ss 00:00:00 -t 00:04:09 archivo_recortado.mp4
```

Donde el valor de la opción -ss es el instante de inicio en hh:mm:ss y el valor de -t es la longitud en hh:mm:ss

Es importante respetar el orden de las opciones, sobre todo poner al principio la opción `-i` que indica el fichero de entrada. De no hacerlo así (se explica [aquí](https://github.com/valekhz/m4b-converter/issues/13)) las opciones de codec no saben localizar bien los codecs del fichero de entrada.

Durante un tiempo en Ubuntu, `ffmpeg` no estuvo disponible. Su sustituto fue `avconv`, compatible la mayoría de las veces. No admitía sin embargo la opción de copiar el codec de audio y vídeo. Había que especificarlo. Una lista de encoders soportados se puede obtener ejecutando:

```bash
$ avconv -encoders
```

Un par de codecs comprobados que suelen dar buen resultados son h264 y aac:

```bash
ffmpeg -i archivo_original.mp4 -acodec aac -vcodec h264 -ss 01:07:38 -t 00:01:14 archivo_recortado.mp4
```

### Crop en video

```bash
$ ffmpeg -i input.mp4 -filter:v "crop=w:h:x:y" output.mp4
```

donde:

* w: ancho final
* h: alto final
* x: coordenada x del punto superior izquierdo del recuadro
* y: coordenada y del punto superior izquierdo del recuadro

### Extraer frame de video

```bash
$ ffmpeg -i input.mp4 -ss 00:01:00 -frames:v 1 frame.png
```

donde el argumento -ss marca el instante del frame en hh:mm:ss

### Montaje de vídeo StopMotion a partir de imágenes

A 10fps por ejemplo ([Fuente](http://www.dototot.com/compile-stop-motion-animation-image-sequence-avconv/)):

```bash
$ ffmpeg -f image2 -r 10 -i %04d.jpg -vf scale=1440:1080 -r:v 10 -c:v libx264 -qp 0 -preset veryslow -an "video.mkv"
```

### Screencast

```bash
$ avconv -f x11grab -r 25 -s 910x550 -i :0.0 -vcodec huffyuv screencast.avi
```

### Compresión batch de vídeos

Instalar el cliente de linea de comando de [Handbrake](http://handbrake.fr/downloads.php).

Dependiendo de la extensión habrá que cambiar el `ls` inicial. Los vídeos de salida son MP4, por lo que si la extensión inicial no es esa, habrá que cambiarla en los ficheros finales.

```bash
$ mkdir comp
$ ls *.mp4 | awk '{print "HandBrakeCLI -Z Normal -i "$0" -o comp/"$0}' | sh
```

### Resampleado de video con HandBrake

([Fuente](http://www.antiscreeners.com/phpBB2/viewtopic.php?p=85974#85974))

On the Video tab use Avg Bitrate and use 2500 to 3000 depending if a big action movie(3000) or if less fast action/movement in the movie(2500). Make sure to click on 2-Pass Encoding and Turbo first pass.

### Convertir un video a formato 3GP (H263+AAC)

* Instalar un [repositorio no oficial](http://medibuntu.org/repository.php) que contiene los codecs:

```bash
$ sudo -E wget --output-document=/etc/apt/sources.list.d/medibuntu.list http://www.medibuntu.org/sources.list.d/$(lsb_release -cs).list && sudo apt-get --quiet update && sudo apt-get --yes --quiet --allow-unauthenticated install medibuntu-keyring && sudo apt-get --quiet update
```

* Instalar el codificador y los codecs:

```bash
$ sudo aptitude install ffmpeg libavcodec-extra-53
```

* Codificar el video:

```bash
$ ffmpeg -i EspacioMudejar.wmv -s qcif -vcodec h263 -acodec libfaac -ac 1 -ar 8000 -r 25 -ab 32 -strict experimental -y EspacioMudejar.3gp
```

Las opciones más importantes son:

*  ar: Frecuencia de audio
*  r: framerate
*  ab: Audio bitrate en kbps

### Convertir APE a WAV

Los ficheros .ape con que se distribuyen algunos CD's se puede convertir a WAV para poder quemarlo a un CD (con un fichero .cue que normalmente acompaña al .ape se puede quemar directamente con el Burn del Mac por ejemplo) instalando el paquete `ffmpeg` y ejecutando el siguiente comando:

```bash
$ ffmpeg -i fichero.ape fichero.wav
```

Hay que acordarse de sustituir dentro del fichero .cue la referencia al fichero original .ape por el nuevo .wav.

### Convertir FLAC a WAV

Los ficheros .flac con que se distribuyen algunos CD's se puede convertir a WAV para poder quemarlo a un CD (con un fichero .cue que normalmente acompaña al .flac se puede quemar directamente con el Burn del Mac por ejemplo) instalando el paquete `flac` y ejecutando el siguiente comando:

```bash
$ flac -d fichero.flac
```

Hay que acordarse de sustituir dentro del fichero .cue la referencia al fichero original .flac por el nuevo .wav.

## Tratamiento de ficheros en lote

### Renombrado de archivos en lote

Por ejemplo una serie de archivos jpg:

```bash
a=1
for i in *.jpg; do
  new=$(printf "%04d.jpg" ${a})
  mv ${i} ${new}
  let a=a+1
done
```

### Renombrado de ficheros de mayúsculas a minúsculas

([Fuente](http://aptgetanarchy.org/node/75))

```bash
#!/bin/sh
for f in *; do
g=`expr "xxx$f" : 'xxx\(.*\)' | tr '[A-Z]' '[a-z]'`
mv "$f" "$g"
done
```

### Quitar los primeros 5 caracteres de los ficheros de un directorio

```bash
for f in *.gba; do
mv "$f" "${f:5:${#f}}"
done
```

### Compresión de ficheros en lote

```bash
for file in *.col; do
  filename=$(basename "${file}")
  fileid=${filename%%.*}
  7z a "${fileid}.7z" "${filename}"
done
```

### Comprimir uno a uno los ficheros de un directorio

Por ejemplo ficheros de extensión `.gba`:

```bash
for f in *.gba; do
file=$(basename "$f" .gba)
zip "${file}.zip" "${file}.gba"
done
```

### Sustitución de cadena en ficheros en lote

```bash
for file in *.cfg; do
  filename=$(basename "${file}")
  fileid=${filename%%.*}
  sed -i 's/ShowFps 1/ShowFps 0/' "${file}"
done
```

### Búqueda de ficheros que contienen una cadena

```bash
#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for file in `find .`
do
fgrep "[cadena a buscar]" $file > /dev/null 2>&1
if [ $? -eq 0 ]; then
echo $file
fi
done
IFS=$SAVEIFS
```

En realidad el script anterior hace lo mismo que el simple comando siguiente:

```bash
$ fgrep -rl "[cadena a buscar]" .
```

## PDFs

Instalar `pdftk`, programa en linea de comando para procesar ficheros PDF. Está para casi todas las plataformas.

```bash
$ sudo aptitude search pdftk
i pdftk - A useful tool for manipulating PDF documents

$ sudo aptitude install pdftk
```

### Concatenar

Concatenar todos los archivos facilmente que tengas en una carpeta:

```bash
$ pdftk carpeta_con_todos_ficheros/*.pdf cat output fichero_concatenado.pdf
```

Fusión de varios ficheros en uno (equivalente a la anterior):

```bash
$ pdftk *.pdf cat output onelargepdfile.pdf
```

### División

División en múltiples ficheros (uno por página):

```bash
$ pdftk largepdfile.pdf burst
```

Tiene muchas mas funcionalidades consultables con –help, pero si quieres, puedes echarle un vistazo a un [articulo de Linux-Magazine “PDF a tope”](https://www.linux-magazine.es/issue/12/PDFTk.pdf).

## Wireshark

### Configurar Wireshark para poder capturar con usuarios no-root

Ejecutar lo siguiente:

```bash
$ sudo dpkg-reconfigure wireshark-common
$ sudo usermod -a -G wireshark <usuario>
```

Reiniciar la sesión.

## Backups

### System + MySQL backup script

```bash
#!/bin/bash
# System + MySQL backup script
# Full backup day - Sun (rest of the day do incremental backup)
# Copyright (c) 2005-2006 nixCraft `<http://www.cyberciti.biz/fb/>`
# This script is licensed under GNU GPL version 2.0 or above
# Automatically generated by http://bash.cyberciti.biz/backup/wizard-ftp-script.php
# ---------------------------------------------------------------------

### System Setup ###
DIRS="/var/spool/sms /var/log/smstools /root"
BACKUP=/tmp/backup.$$
NOW=$(date +"%d-%m-%Y")
INCFILE="/var/tar-inc-backup.dat"
DAY=$(date +"%a")
# echo $DAY >> /root/dates
FULLBACKUP="Sun"

### MySQL Setup ###
MUSER="mysqluser"
MPASS="mysqlpwd"
MHOST="localhost"
MYSQL="$(which mysql)"
MYSQLDUMP="$(which mysqldump)"
GZIP="$(which gzip)"

### FTP server Setup ###
FTPD="//incremental"
FTPU="ftpuser"
FTPP="ftppwd"
FTPS="ftphost"
NCFTP="$(which ncftpput)"

### Other stuff ###
EMAILID="user@domain.com"

### Start Backup for file system ###
[ ! -d $BACKUP ] && mkdir -p $BACKUP || :

### See if we want to make a full backup ###
if [ "$DAY" == "$FULLBACKUP" ]; then
  FTPD="//full"
  FILE="fs-full-$NOW.tar.gz"
  tar -zcvf $BACKUP/$FILE $DIRS
else
  i=$(date +"%Hh%Mm%Ss")
  FILE="fs-i-$NOW-$i.tar.gz"
  tar -g $INCFILE -zcvf $BACKUP/$FILE $DIRS
fi

### Start MySQL Backup ###
# Get all databases name
DBS="$($MYSQL -u $MUSER -h $MHOST -p$MPASS -Bse 'show databases')"
for db in $DBS
do
 FILE=$BACKUP/mysql-$db.$NOW-$(date +"%T").gz
 $MYSQLDUMP -u $MUSER -h $MHOST -p$MPASS $db | $GZIP -9 > $FILE
done

### Dump backup using FTP ###
#Start FTP backup using ncftp
ncftp -u"$FTPU" -p"$FTPP" $FTPS<<EOF
mkdir $FTPD
mkdir $FTPD/$NOW
cd $FTPD/$NOW
lcd $BACKUP
mput *
quit
EOF

### Find out if ftp backup failed or not ###
if [ "$?" == "0" ]; then
 rm -f $BACKUP/*
else
 T=/tmp/backup.fail
 echo "Date: $(date)">$T
 echo "Hostname: $(hostname)" >>$T
 echo "Backup failed" >>$T
 mail  -s "BACKUP FAILED" "$EMAILID" <$T
 rm -f $T
fi
```

## Arch Linux

### Enlaces

* [Chaotic-AUR](https://aur.chaotic.cx/): Compilación automática de paquetes AUR.

### Paquetes interesantes

* `pamac-aur` (AUR): Interfaz gráfica para pacman/yay.

### Comandos yay

* `yay -Syu`: Actualizar el sistema, incluyendo paquetes de AUR. Equivalente en Debian a `apt upgrade`.
* `yay -S <paquete>`: Instalar un paquete desde AUR. Equivalente en Debian a `apt install`.
* `yay -Rns <paquete>`: Desinstalar un paquete de AUR, sus dependencias y archivos de configuración. Equivalente en Debian a `apt purge`.

### Modificación manual de paquetes AUR

Este es el procedimiento oficial cuando un paquete falla, quieres aplicar un parche personalizado o necesitas cambiar una opción de compilación antes de instalar.

#### 1. Clonar el repositorio del paquete

En lugar de usar un helper (como `yay`), descargamos el código fuente directamente desde los servidores de AUR usando Git.

```bash
git clone https://aur.archlinux.org/nombre-del-paquete.git
cd nombre-del-paquete

```

#### 2. Modificar el PKGBUILD o archivos fuente

Aquí es donde editas lo que necesites.

* **Para errores de rutas:** Edita las funciones `build()` o `package()` dentro del archivo `PKGBUILD`.
* **Para cambiar versiones:** Modifica la variable `pkgver`.

!!! Tip
    Si modificas archivos que están listados en el array `source()` (como un parche `.patch` o un script `.sh`), las sumas de verificación (checksums) fallarán. Para arreglarlo automáticamente, ejecuta:

    ```
    updpkgsums
    ```

#### 3. Compilar e Instalar

Una vez que el `PKGBUILD` está a tu gusto, usamos el comando `makepkg`.

```bash
makepkg -si

```

**Desglose de flags:**

* `-s` (**s**ync): Instala automáticamente las dependencias necesarias usando `pacman`.
* `-i` (**i**nstall): Instala el paquete generado (`.pkg.tar.zst`) en tu sistema una vez terminada la compilación.

#### Resumen de comandos

| Acción | Comando |
| :--- | :--- |
| **Bajar fuentes** | `git clone [https://aur.archlinux.org/paquete.git](https://aur.archlinux.org/paquete.git)` |
| **Actualizar sumas** | `updpkgsums` |
| **Limpiar y compilar** | `makepkg -f` (el `-f` fuerza a sobrescribir si ya compilaste antes) |
| **Compilar e instalar** | `makepkg -si` |
| **Limpiar basura** | `makepkg -c` (borra los directorios temporales `src/` y `pkg/` tras terminar) |

#### ¿Cómo manejar las actualizaciones futuras?

Si modificaste un paquete manualmente, la próxima vez que uses `yay -Syu`, el helper verá que hay una versión nueva en AUR e intentará sobrescribir tu versión modificada. Tienes dos opciones:

1. **Si el error ya se arregló en AUR:** Deja que `yay` lo actualice normalmente.
2. **Si quieres mantener tu modificación:** Puedes añadir el paquete a la línea `IgnorePkg` en `/etc/pacman.conf` para que pacman no lo toque sin tu permiso.

## Ubuntu

### Enlaces

* [Solución a warning apt-key is deprecated](https://tecadmin.net/resolved-key-is-stored-in-legacy-trusted-gpg-keyring/)

### Paquetes a instalar en Xubuntu

* `font-viewer`: Visor/instalador de tipos de letra.
* `python3-pip`: PIP instalado desde los repositorios (facilita la instalación de virtualenvwrapper).
* `python-is-python3`: Abre Python3 ejecutando `python`.
* `android-file-transfer`: Para transferir ficheros por MTP (hacia Android o las Oculus Quest).
* `qpdfview`: Visor PDF.
* `thunar-archive-plugin`: Crear archivadores y descomprimir desde Thunar.
* `gvfs gvfs-common gvfs-backends gvfs-fuse thunar-volman`: Soporte MTP para Android.

### Limpieza de paquetes snap

Localizar los paquetes desactivados con:

```
$ snap list --all|fgrep desactivado
```

Y luego borrarlos con:

```
$ snap remove --revision XXX NOMBRE
```

Por ejemplo:

```
edumoreno@eduardo-HP-Folio-13:~$ snap list --all|fgrep desactivado
canonical-livepatch   9.7.3                       105    latest/stable    canonical*  desactivado
chromium              94.0.4606.81                1781   latest/stable    canonical*  desactivado
edumoreno@eduardo-HP-Folio-13:~$ snap remove --revision 105 canonical-livepatch
canonical-livepatch (revisión 105) eliminado
edumoreno@eduardo-HP-Folio-13:~$ snap remove --revision 1781 chromium
chromium (revisión 1781) eliminado
```

### Configuración de idiomas del sistema (locales)

```bash
$ sudo dpkg-reconfigure locales
```

### Configuración de SWAP en disco SSD

Siguiendo [esta página](https://ubunlog.com/swappiness-como-ajustar-el-uso-de-la-memoria-virtual/), añado lo siguiente al fichero `/etc/sysctl.conf` para bajar el 60% que usa Ubuntu por defecto a 10%:

```
vm.swappiness=10
```

### Problema con aplicaciones root en Wayland

Hay que ejecutar el comando:

    xhost si:localuser:root

Se puede automatizar en el arranque añadiendo el comando en las `Aplicaciones al incio` ([fuente](http://ubuntuhandbook.org/index.php/2017/10/ubuntu-17-10-tip-graphical-apps-doesnt-launch-via-root-sudo-gksu/)).

### Poner barras de scroll normales

```bash
gsettings set com.canonical.desktop.interface scrollbar-mode normal
```

### Skype en tray

Instalar los paquetes `sni-qt` y `sni-qt:i386`.

### Workrave en tray

[Fuente](https://sourceforge.net/p/workrave/mailman/message/30722930/)

```bash
gsettings set com.canonical.Unity.Panel systray-whitelist "['all']"
```

### Solucionar el problema con Wireshark (overlay scrollbar)

Cuando se inicia una captura, se cuelga Wireshark, emitiendo una serie infinita de errores de GTK en consola. En [esta página](https://bugs.launchpad.net/ubuntu/+source/overlay-scrollbar/+bug/1248400) comentan varios workarrounds. Por ejemplo editando el fichero `/usr/share/applications/wireshark.desktop` y cambiando la línea de ejecución por:

```
Exec=env LIBOVERLAY_SCROLLBAR=0 wireshark %f
```

### Java

#### Instalar Oracle Java

(Fuentes: [1](http://www.guia-ubuntu.org/index.php?title=Java#Desde_la_web_de_Java) y [2](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html))

Movemos la carpeta creada después de la instalación (llamada `jre1.7.0_05` en este ejemplo) a una ruta más apropiada:

```bash
$ sudo mv jre1.7.0_05 /usr/lib/jvm
```

Establecemos el nuevo Java como una de las "alternativas de java":

```bash
$ sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jre1.7.0_05/bin/java" 1
```

Ahora establecemos la "nueva alternativa" como la real de Java. Este paso hace que la versión de Oracle sea la usada por defecto:

```bash
$ sudo update-alternatives --set java /usr/lib/jvm/jre1.7.0_05/bin/java
```

Para comprobar si tenemos la versión 1.7.0, tecleamos en la terminal:

```bash
$ java -version
java version "1.7.0_05"
Java(TM) SE Runtime Environment (build 1.7.0_05-b05)
Java HotSpot(TM) 64-Bit Server VM (build 23.1-b03, mixed mode)
```

Para ver cómo ha quedado el estado de las alternativas:

```bash
$ update-alternatives --config java
```

Para ver físicamente cómo han quedado las alternativas relativas a `java`:

```bash
$ ls -l /etc/alternatives/java*
```

Si nos interesa borrar alguna de las alternativas (por ejemplo una para `java`):

```bash
$ sudo update-alternatives --remove java /usr/lib/jvm/jdk1.8.0_20/bin/java
```

Hay un PPA para poder instalar el JDK más fácilmente. Se pueden ver las instrucciones [aquí](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html). Desafortunadamente dejó de funcionar a mediados de abril de 2019 por cambios en la política de distribución de Java por parte de Oracle. A partir de ahora instalar manualmente siguiendo [estas instrucciones](https://www.fosstechnix.com/install-oracle-java-8-on-ubuntu-20-04/) o instalar el JDK que se distribuye en forma de [.deb](https://www.oracle.com/java/technologies/javase-jdk15-downloads.html).

#### Problema de los alias (alternatives) de Java6

Los paquetes de Java 6 (1.6) en Ubuntu tienen problemas a la hora de ajustar los alias en /etc/alternatives cuando antes ha estado instalada otra versión (1.5 por ejemplo). Se puede forzar la generación de los alias mediante las siguientes ordenes:

```bash
$ update-java-alternatives --list
$ sudo update-java-alternatives --set [elegir el identificador de la lista que muestra el comando anterior]
```

#### Configuración de Firefox para ejecución de applets Java

([Fuente](http://www.java.com/es/download/help/5000010500.xml#14))

* Vaya al subdirectorio de complementos, situado dentro del directorio de instalación de Mozilla.

```bash
$ cd `<directorio de instalación de Mozilla>`/plugins  # Normalmente /usr/lib/firefox/plugins
```

o

```bash
$ cd `<home del usuario>`/.mozilla/plugins
```

* En el directorio actual, cree un vínculo simbólico al archivo del JRE ns7/libjavaplugin_oji.so. Escriba:

```bash
$ ln -s `<directorio de instalación del JRE>`/plugin/i386/ns7/libjavaplugin_oji.so
```

* Inicie el navegador Mozilla o reinícielo si ya se estaba ejecutando. Tenga en cuenta que, si se está ejecutando algún otro componente de Mozilla (como Messenger, Composer, etc.) deberá también reiniciarlo.
* Vaya a Editar > Preferencias. En la categoría Avanzadas, seleccione Activar Java.

### Problemas históricos

#### Solución problemas wifi en 11.04 y 11.10

[Help with Ubuntu: Fix slow WiFi in Ubuntu 11.04](http://joeslifewithubuntu.blogspot.com/2011/06/how-to-fix-slow-wifi-in-ubuntu-1104.html)

#### Actualización de Intrepid a Jaunty

Tras actualizar de Intrepid a Jaunty se observa un empobrecimiento del rendimiento gráfico en equipos con gráficas integradas Intel 945. En las siguientes páginas explican como hacer downgrade al controlador Intel que había en Intrepid:

*  [https://wiki.ubuntu.com/ReinhardTartler/X/RevertingIntelDriverTo2.4](https://wiki.ubuntu.com/ReinhardTartler/X/RevertingIntelDriverTo2.4)
*  [http://www.astaroth.glufca.com/?p=346](http://www.astaroth.glufca.com/?p=346)

Otro truco que también funcionó sin necesidad de hacer lo anterior fue reconfigurar xorg a la configuración por defecto y luego en la composición de múltiples monitores, situar uno debajo del otro en lugar de uno al lado del otro.

#### Actualización de raring a saucy

Apache cambia de versión de 2.2 a 2.4. [Aquí](http://tfountain.co.uk/blog/2013/10/18/fixing-apache-ubuntu-13-10) encontré solución a los problemas que eso supuso.
