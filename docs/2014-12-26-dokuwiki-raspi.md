title: Dokuwiki en Raspberry Pi manteniendo los ficheros en NAS
summary: Instalación de Dokuwiki sobre Raspberry Pi con ficheros alojados en NAS.
date: 2014-12-26 12:00:00

![Dokuwiki Logo](images/posts/dokuwiki-logo.png)

Tengo desde hace años un [Dokuwiki][dokuwiki] corriendo en el NAS, pero [el que utilizo][duo] tiene un procesador muy poco potente y funcionaba muy lento. Sin embargo me gustaba que estuviera en el NAS por ser el sitio más seguro para tener la importante información que en el [Dokuwiki][dokuwiki] mantengo. La forma de tener la información asegurada y disponible permanentemente es combinar el almacenamiento en el NAS con la ejecución de los procesos en una de las Raspberry Pi que tengo en marcha permanentemente. Describo a continuación cómo ha sido el proceso en mi caso.

Antes de empezar, un comentario. Voy a utilizar el paquete `dokuwiki` de la distribución porque de [Dokuwiki][dokuwiki] salen continuas ediciones y parches. De esta forma la actualización se hará con un simple `apt-get upgrade`. [Dokuwiki][dokuwiki], en su versión empaquetada para [Raspbian][raspbian], puede correr sobre Apache o sobre [Lighttpd][lighty]. Si instalo directamente `dokuwiki`, el paquete prioriza la dependencia con Apache, pero prefiero utilizar [Lighttpd][lighty] en la Raspberry. Así pues la instalación la hago por etapas para forzar la dependencia con [Lighttpd][lighty]. En otro caso hubiera sido tan sencillo como hacer `apt-get install dokuwiki`.

1. Instalo [Lighttpd][lighty]:

        sudo apt-get install lighttpd

2. Instalo PHP:

        sudo apt-get install php5-common php5-cgi php5

3. Activo el módulo PHP en [Lighttpd][lighty] y recargo la configuración de este último:

        sudo lighty-enable-mod fastcgi-php
        sudo service lighttpd force-reload

4. Ahora sí instalo [Dokuwiki][dokuwiki]:

        sudo apt-get install dokuwiki

5. Durante la instalación del paquete aparece un diálogo de configuración en el que, aparte de solicitar el password del usuario `admin` para [Dokuwiki][dokuwiki], pregunta sobre qué servidores HTTP de los dos soportados, queremos que se haga una configuración automática. De nuevo prioriza Apache, es decir, este servidor sale preseleccionado y [Lighttpd][lighty] desactivado. Invierto la situación.
6. Doy de alta un recurso compartido en el NAS. No muestro el proceso de esto puesto que es muy distinto en cada NAS. Comparto el recurso por medio del protocolo NFS.
7. La instalación predeterminada de [Dokuwiki][dokuwiki] en Raspbian mantiene los ficheros en el directorio `/var/lib/dokuwiki/data`, así que será esto lo que habrá que mantener en el NAS. Me fijo en los permisos de los ficheros de este directorio, puesto que tendremos que respetarlos para que [Dokuwiki][dokuwiki] pueda trabajar. Veo esto:

        edumoreno@raspi-git /var/lib/dokuwiki/data $ ls -l
        total 208
        drwx------  2 www-data root 16384 dic 26 11:58 attic
        drwx------ 11 www-data root 16384 dic 26 11:39 cache
        -rw-r--r--  1 www-data root  7180 dic 26 11:39 deleted.files
        -rw-r--r--  1 www-data root     0 dic 26 11:38 _dummy
        drwx------  2 www-data root 16384 dic 26 11:58 index
        drwx------  2 www-data root 16384 dic 26 11:58 locks
        drwx------  3 www-data root 16384 dic 26 11:39 media
        drwxr-xr-x  2 www-data root 16384 dic 26 11:39 media_attic
        drwxr-xr-x  2 www-data root 16384 dic 26 11:39 media_meta
        drwx------  2 www-data root 16384 dic 26 11:58 meta
        drwx------  4 www-data root 16384 dic 26 11:42 pages
        -rw-r--r--  1 www-data root  7917 dic 26 11:39 security.png
        -rw-r--r--  1 www-data root 12093 dic 26 11:39 security.xcf
        drwx------  2 www-data root 16384 dic 26 11:39 tmp

8. Antes de hacer el montaje del directorio remoto del NAS hacia la Raspberry, transfiero al primero todos los ficheros que ha dejado la instalación en Raspberry. En mi caso, como tengo habilitado el acceso SSH en el NAS, lo hago así (desde la Raspberry):

        scp -r /var/lib/dokuwiki/data/* 192.168.1.200:/c/dokuwiki

9. Ahora configuro en Raspberry el montaje del recurso compartido en el NAS, lo que hago insertando la siguiente línea en el fichero `/etc/fstab`:

        192.168.1.200:/c/dokuwiki /var/lib/dokuwiki/data nfs rw 0 0

10. Como veo que los permisos están muy orientados al acceso por usuario, y no por grupo, averiguo el UID del usuario `www-data` para ajustar ese valor en los ficheros en el NAS. Lo hago ejecutando sobre Raspberry:

        edumoreno@raspi-git ~ $ id www-data
        uid=33(www-data) gid=33(www-data) grupos=33(www-data)

11. Ahora inicio sesión por SSH en el NAS, me voy al directorio que voy a montar en la Raspberry y ajusto el UID de los ficheros que he copiado en el paso 7:

        chown -R 33 /c/dokuwiki/*

12. Finalmente vuelvo a Raspberry Pi y monto el nuevo directorio:

        sudo mount -a

A partir de entonces, el directorio `/var/lib/dokuwiki/data` de la Raspberry se encuentra en realidad en el NAS y por tanto, toda la actividad de Dokuwiki se registrará donde más conviene. Ya puedo acceder a [Dokuwiki][dokuwiki] en: http://192.168.1.204/dokuwiki

[dokuwiki]: https://www.dokuwiki.org/dokuwiki
[duo]:      http://support.netgear.com/product/RND2000v1%2b%2428ReadyNAS%2bDuo%2bv1%2429
[raspbian]: http://www.raspbian.org/
[lighty]:   http://www.lighttpd.net/
