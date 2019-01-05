---
layout: default
permalink: /sistemas/unix.html
---

# UNIX

## Cheat sheets

*  [Colección de Carlos Fenollosa](http://mmb.pcb.ub.es/~carlesfe/#unix)
*  [Tricks de Carlos Fenollosa](http://cfenollosa.com/misc/tricks.txt)
*  [Bash Cheat Sheet](http://www.johnstowers.co.nz/blog/pages/bash-cheat-sheet.html)
*  [Programar en Bash, pequeño manual de referencia](http://www.linuxhispano.net/2010/06/08/bash-manual-referencia-cheat-sheet-mini/)
*  [How To Use Linux Screen](http://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/)

## Comandos útiles

*  `strace -e file [command]`: runs `command`, printing out any time a file is opened or checked.
*  `strace -e file,network,process [command]`: the same as above, but also printing network process and subcommands run.
*  `strace -e file,process -f [command]`: the -f parameter follows forks -- in case it's not main command but a subshell that you're interested in.
*  `strace -p [PID]`: Connect to pid PID and start tracing.
*  `route -n`: Tabla de rutas del sistema.
*  `du -h --max-depth=1 .`: Tamaño de un directorio y sus subdirectorios directos.
*  `find [directorio] ! -user [usuario] -ls`: Lista los ficheros que NO pertenecen a un usuario.
*  `badblocks -swv /dev/sda`: Bloquear sectores defectuosos (sustituir `/dev/sda` por el dispositivo que corresponda.
*  `dpkg --configure -a`: Soluciona problemas con paquetes mal instalados.
*  `mkdosfs -F 32 -v -n "" /dev/sdc1`: Formato de partición en FAT32.
*  `du -sh */ | sort -h`: Muestra los directorios del directorio actual ordenados por tamaño (en formato humano) indicando su tamaño.
*  `cat fichero.txt | awk '{print $5}'`: Imprime la quinta columna (separando por espacios) de cada linea del fichero.
*  `cat fichero.txt | cut -d' ' -f5`: Imprime la quinta columna (separando por espacios) de cada linea del fichero.
*  `cat fichero.txt | sed -e 's/ /\n/g'`: Sustituye todos los espacios del fichero por retornos de carro.
*  `netstat -nr`: Tabla de rutas del sistema.
*  `netstat -ntu|grep :80|wc -l`: número de conexiones al servidor HTTP.
*  `netstat -ntu|grep :21|wc -l`: número de conexiones al servidor FTP.
*  `netstat -tulanp`: Lista los puertos TCP/UDP abiertos (tanto de servidores como de clientes).
*  `netstat -tlnp`: Lista los puertos TCP abiertos de los servicios.
*  `crontab -e`: Añadir un job a cron.
*  `sudo badblocks /dev/sda > badblocks.txt; sudo fsck -l badblocks.txt /dev/sda`: Bloqueo de sectores defectuosos del disco duro ([fuente](http://tech.chandrahasa.com/2013/06/09/how-to-check-your-hard-disk-for-bad-blocks-in-ubuntu/)).
*  `sudo blkid`: Lista los dispositivos de bloques (discos) disponibles en el sistema.
*  `sudo nmap -sP 192.168.1.0/24`: Descubrir todos los equipos presentes en la red `192.168.1.0`.
*  `sudo netstat -lp --inet`: Puertos de red abiertos y procesos asociados.
*  `sudo usermod -a -G groupName userName`: Añade el usuario userName ya existente al grupo groupName.
*  `sudo dd if=/dev/zero of=/dev/mmcblk0`: Formateo de una tarjeta de memoria (en realidad vale para cualquier dispositivo de almacenamiento).
*  `sudo tcpdump -s 0 -i ppp0 -w trafico.pcap`: Captura de tráfico por el interfaz ppp0.
*  `iptables -L -n`: Listar reglas iptables.
*  `wget -q -O - url`: Hace la request de la URL sin emitir trazas (-q = no verbose) y redireccionando la response a la salida estándar (-O -).
*  `route -n`: Muestra la tabla de rutas con IP's en lugar de con nombres.
*  `cat /etc/resolv.conf`: Muestra el gateway en uso.
*  `ldd <binario>`: Indica las librerías que usa el binario.
*  `exiftool -AllDates='2010:08:08 15:35:33' -overwrite_original photo.jpg`: Actualiza todas las fechas dentro de la metainformación de un JPG.
*  `exiftool -all= photo.jpg`: Borrar toda la metainformación de una foto (por cuestiones de privacidad antes de subirla a un sitio por ejemplo).
*  `mplayer -vo caca MovieName.avi`: Reproduce un vídeo en consola con ascii. Para verlo en blanco y negro sustituir `caca` por `aa`.
*  `sudo traceroute -4T -p 22 192.168.1.203`: Comprobar la traza hasta alcanzar un determinado puerto en una determinada máquina.
*  `dig @8.8.8.8 -t any eduardofilo.es`: Query DNS de los registros de cualquier tipo a través del servidor `8.8.8.8` al dominio `eduardofilo.es`.

## Alias SSH

Para asimilar un identificador a una pareja user@host, editar el fichero `~/.ssh/config` y añadir un bloque como el siguiente ([fuente](http://collectiveidea.com/blog/archives/2011/02/04/how-to-ssh-aliases/)):

```
Host example
  HostName example.com
  User exampleuser
```

## Tunel de un puerto remoto por SSH

([Fuente](http://www.revsys.com/writings/quicktips/ssh-tunnel.html)) Para conducir el tráfico hasta un host:puerto remoto canalizándolo por un tunel seguro, se puede utilizar el comando `ssh`. Por ejemplo, vamos a tunelizar una conexión contra el puerto telnet de la máquina remota `telnet.example.com` por medio del usuario `ssh-user` para tenerlo disponible en el puerto 2000 local de nuestra máquina:

```
ssh -f ssh-user@telnet.example.com -L 2000:telnet.example.com:23 -N
```

A partir de ahora podremos conectarnos al telnet conectando con `localhost:2000`.

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

11. Ahora, para recuperar una de ella, por ejemplo la más vieja que contenía lanzado el comando `top` incorporaremos el identificador de la sesión tras la opción `-r`:

        shell ~$ screen -r 12609.pts-7.eduardo-HP-Folio-13

12. Como se comentaba en el punto 4, para cerrar las sesiones simplemente saldremos con `exit`, aunque también, y sobre todo en caso de que la sesión se quedara bloqueada con algún comando que no se pudiera cerrar, se puede matar la sesión con la siguiente combinación de teclas:

        "Ctrl-a" "k"

## Búqueda de ficheros que contienen una cadena

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

## Ajustes de permisos a ficheros y directorios por separado

```bash
$ #Para los ficheros:
$ find . ! -type d -exec chmod 664 {} \;
$ #Para los directorios:
$ find . -type d -exec chmod 775 {} \;
```

## Renombrado de ficheros de mayúsculas a minúsculas

([Fuente](http://aptgetanarchy.org/node/75))

```bash
#!/bin/sh
for f in *; do
g=`expr "xxx$f" : 'xxx\(.*\)' | tr '[A-Z]' '[a-z]'`
mv "$f" "$g"
done
```

## Redirección de salidas

Para redirigir ambas salidas de un programa (estandar y error) hacer lo siguiente:

```bash
$ COMANDO > FICHERO_O_DISPOSITIVO 2>&1
```

En [esta página](http://sc.tamu.edu/help/general/unix/redirection.html) se documenta con más detalle este tema.

## Ejecución remota de aplicaciones XWindow

 1.  Abrir el servidor X (Cygwin)
 2.  Iniciar sesión remota: ssh -X [usuario]@[máquina]
 3.  Ejecutar la aplicación

## MySQL

*  Acceso: mysql -u root -p
*  Listar bases de datos: show databases;
*  Abrir una base de datos: use [NombreBBDD];
*  Listar tablas: show tables


## Ficheros de configuración importantes

*  `/etc/security/limits.conf`: Configuration file for the pam_limits module. Permite limitar el número de ficheros abiertos por el sistema, el número de procesos, etc.

## Solución al problema de los alias (alternatives) de Java6 en Ubuntu

Los paquetes de Java 6 (1.6) en Ubuntu tienen problemas a la hora de ajustar los alias en /etc/alternatives cuando antes ha estado instalada otra versión (1.5 por ejemplo). Se puede forzar la generación de los alias mediante las siguientes ordenes:

```bash
$ update-java-alternatives --list
$ sudo update-java-alternatives --set [elegir el identificador de la lista que muestra el comando anterior]
```

## Bits SUID, SGID y sticky

[Manual de LuCAS](http://lucas.olea.org/Manuales-LuCAS/doc-unixsec/unixsec-html/node56.html)

## Autentificación automática por SSH

Conseguiremos que la autentificación del cliente se haga por medio de una pareja de claves privada/pública en lugar de con identificador de usuario/password. Primero generamos la pareja de claves pública-privada ejecutando en el cliente `ssh-keygen`:

```bash
$ ssh-keygen  -t rsa
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

## Configuración de Firefox para ejecución de applets Java

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

## Organización de menús cuando se mezclan aplicaciones KDE y Gnome

GNU/Linux nos permite tener varios sistemas de escritorio diferentes instalados y funcionando, pero inevitablemente nos encontramos con una mezcla de opciones y programas de cada entorno en los menús principales. Existen aplicaciones precisamente para limpiar automáticamente las entradas del menú que no corresponden a tu sistema de escritorio habitual, y dejarlas apartadas y ordenadas de alguna manera. Con Gnome y KDE instalados a la vez, hay dos programas para aquellos Gnomeros que han querido probar KDE y para los KDEeros que han querido probar Gnome.

*  [Gnome Menu Extended](http://www.gtk-apps.org/content/show.php/Gnome+Menu+Extended+%28Debian+Package%29?content=73515) es el propio menú normal de Gnome, pero incluye una carpeta donde se guardan todas las aplicaciones y opciones de KDE. Se instala fácilmente descargando el paquete para cualquier distribución: Debian (y Ubuntu), Slackware o directamente el código fuente para compilarlo. Una vez instalado, se activa yendo a Preferencias -> Add KDE Menu. Y si quieres recuperar el menú como estaba, también tiene la opción de restaurarlo.
*  [K Menu Gnome](http://www.kde-apps.org/content/show.php/K+Menu+Gnome+%28Debian+Package%29?content=31031&amp;PHPSESSID=39c71268b399effce8c57dbf8ff09e16) es un menú exactamente igual que el KMenu original, pero incluye una carpeta donde residen todas las aplicaciones de Gnome, en sistemas que tienen ambos escritorios instalados. Está disponible para Debian (y Ubuntu), Slackware, Fedora y el código fuente para compilarlo en cualquier sistema.

## Error "error while loading shared libraries: ..."

Runtime error. The linker hasn't found your libraries. Either they are not installed properly or the linker doesn't know where they are (most probably in `/usr/local/lib`). To get your linker to update its list of libraries type:

```bash
$ ldconfig /usr/local/lib
```

or as a temporary measure:

```bash
$ export LD_LIBRARY_PATH="/usr/local/lib"
```

## Compartir ficheros con Samba

Aparte de instalar y configurar Samba (fichero `/etc/samba/smb.conf`) hay que dar de alta los usuarios UNIX que se usarán a través de Samba y asignarles un password para el acceso por el mismo. Esto se hace con el comando:

```bash
$ sudo smbpasswd -a usuario
```

## Migración masiva de usuarios

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

### Depuración de /etc/passwd

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

## Eliminar petición password en sudo

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

## Proxy HTTP en consola

Setting up proxy at Firefox do not have effects at console, which means your wget, ssh, apt-get, yum etc do not access through the proxy you set at Firfox browser. To setup http proxy at console, you can do as bellow, assume the proxy IP is 219.93.2.113 and port 3128:

```bash
$ export http_proxy='http://219.93.2.113:3128/'
```

Remember, you have to specified http://, and to know more about export, check out HERE.
To clear your http proxy and use back yours, do this:

```bash
$ export http_proxy=''
```

## Convertir nombres de ficheros de ISO a UTF-8

Al migrar una web, o al copiar un sistema de archivos, te puedes encontrar con nombres de ficheros en otras codificaciones de caracteres. Mediante el siguiente comando transformaríamos los nombres de ficheros desde ISO-8869-1 a UTF-8:

```bash
$ convmv -r -f ISO-8859-1 -t UTF-8  --notest *
```

## Backup de un FileSystem

Backup:

```bash
$ dd if=/dev/hdx | gzip > /path/to/image.gz
```

Restauración:

```bash
$ gzip -dc /path/to/image.gz | dd of=/dev/hdx
```

## Montar un fichero .img

([Fuente](http://www.linuxquestions.org/questions/linux-general-1/how-to-mount-img-file-882386/)). Primero hay que averiguar el offset de la partición que queremos montar:

```
fdisk -l /ruta/fichero.img
```

Esto nos mostrará el tamaño del bloque y el bloque de comienzo de la partición. Por ejemplo:

```
edumoreno@eduardo-HP-Folio-13:~/Descargas$ fdisk -l RetroPie.img
Disk RetroPie.img: 3,7 GiB, 3965190144 bytes, 7744512 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xb847d94e

Disposit.     Inicio  Start   Final Sectores  Size Id Tipo
RetroPie.img1 *        8192  124927   116736   57M  e W95 FAT16 (LBA)
RetroPie.img2        124928 7744511  7619584  3,6G 83 Linux
```

El offset se calculará multiplicando el bloque de comienzo por el tamaño de bloque. En el ejemplo, para la segunda partición:

offset = 124928 * 512 = 63963136

Por tanto el comando para montar será:

```
sudo mount -o loop,offset=63963136 RetroPie.img /mnt/tmp
```

## Manipulación de PDFs

División en múltiples ficheros (uno por página):

```bash
$ pdftk largepdfile.pdf burst
```

Fusión de varios ficheros en uno:

```bash
$ pdftk *.pdf cat output onelargepdfile.pdf
```

## Obtener hash MD5 de una cadena

```bash
$ echo -n "<cadena>"|md5sum
```

## System + MySQL backup script

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

## Recuperación de pendrive o tarjeta de memoria corrupta

Con TestDisk/Photorec.

### Enlaces

* [TestDisk Paso A Paso](http://www.cgsecurity.org/wiki/TestDisk_Paso_A_Paso)
* [How to Recover Data from Corrupt / formatted USB Flash using Photorec](https://linoxide.com/linux-how-to/recovery-data-corrupt-formatted-usb-flash-using-photorec/)
