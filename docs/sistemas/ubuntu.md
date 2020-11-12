---
layout: default
permalink: /sistemas/ubuntu.html
---

# Ubuntu

## Aplicaciones interesantes

* [ReText](https://github.com/retext-project/retext): Editor Markdown.
* [Franz](https://meetfranz.com/): [Configuración de icono en GNome](https://gist.github.com/jamiesoncj/756728b3ba7c07d7a90f843400af37bb).
* [App Grid](http://www.appgrid.org/): Repositorio de aplicaciones.
* [OpenWeather Shell Extension](https://itsfoss.com/display-weather-ubuntu/): Información del tiempo meteorológico en la barra de menú.

## Servicios interesantes

* [KodExplorer](https://github.com/kalcaddle/KODExplorer)
* [Gitea](https://gitea.io/en-us/)

## Problema con aplicaciones root en Wayland

Hay que ejecutar el comando:

    xhost si:localuser:root

Se puede automatizar en el arranque añadiendo el comando en las `Aplicaciones al incio` ([fuente](http://ubuntuhandbook.org/index.php/2017/10/ubuntu-17-10-tip-graphical-apps-doesnt-launch-via-root-sudo-gksu/)).

## Configuración de opción predeterminada en GRUB

[Fuente](https://forums.linuxmint.com/viewtopic.php?t=230650)

1. Editar fichero `/etc/default/grub` y modificar el parámetro `GRUB_DEFAULT` dando el valor `saved` en lugar del valor numérico que encontraremos.
2. Ejecutar `sudo update-grub`.
3. Ejecutar `sudo grub-set-default N` siendo N la posición de la entrada del menú de GRUB que queremos que actúe como predeterminada (contando desde 0).

## Problemas con GRUB

[Reinstalar GRUB 2](http://molinuxaula.pbworks.com/w/page/27409912/Reinstalar%20GRUB%202)

## Solución problemas wifi en 11.04 y 11.10

[Help with Ubuntu: Fix slow WiFi in Ubuntu 11.04](http://joeslifewithubuntu.blogspot.com/2011/06/how-to-fix-slow-wifi-in-ubuntu-1104.html)

## Solución problema Wireshark en trusty y utopic

[liboverlay-scrollbar hangs Wireshark](https://bugs.launchpad.net/ubuntu/+source/overlay-scrollbar/+bug/1248400)

## Actualización de Intrepid a Jaunty

Tras actualizar de Intrepid a Jaunty se observa un empobrecimiento del rendimiento gráfico en equipos con gráficas integradas Intel 945. En las siguientes páginas explican como hacer downgrade al controlador Intel que había en Intrepid:

*  [https://wiki.ubuntu.com/ReinhardTartler/X/RevertingIntelDriverTo2.4](https://wiki.ubuntu.com/ReinhardTartler/X/RevertingIntelDriverTo2.4)
*  [http://www.astaroth.glufca.com/?p=346](http://www.astaroth.glufca.com/?p=346)

Otro truco que también funcionó sin necesidad de hacer lo anterior fue reconfigurar xorg a la configuración por defecto y luego en la composición de múltiples monitores, situar uno debajo del otro en lugar de uno al lado del otro.

## Actualización de raring a saucy

Apache cambia de versión de 2.2 a 2.4. [Aquí](http://tfountain.co.uk/blog/2013/10/18/fixing-apache-ubuntu-13-10) encontré solución a los problemas que eso supuso.

## Recursos gráficos

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

## Convertir un video a formato 3GP (H263+AAC)

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

## Convertir APE a WAV

Los ficheros .ape con que se distribuyen algunos CD's se puede convertir a WAV para poder quemarlo a un CD (con un fichero .cue que normalmente acompaña al .ape se puede quemar directamente con el Burn del Mac por ejemplo) instalando el paquete `ffmpeg` y ejecutando el siguiente comando:

```bash
$ ffmpeg -i fichero.ape fichero.wav
```

Hay que acordarse de sustituir dentro del fichero .cue la referencia al fichero original .ape por el nuevo .wav.

## Convertir FLAC a WAV

Los ficheros .flac con que se distribuyen algunos CD's se puede convertir a WAV para poder quemarlo a un CD (con un fichero .cue que normalmente acompaña al .flac se puede quemar directamente con el Burn del Mac por ejemplo) instalando el paquete `flac` y ejecutando el siguiente comando:

```bash
$ flac -d fichero.flac
```

Hay que acordarse de sustituir dentro del fichero .cue la referencia al fichero original .flac por el nuevo .wav.

## Restaurar panel Gnome

([fuente 1](http://www.google.com/url?q=http%3A%2F%2Fsuperuser.com%2Fquestions%2F129320%2Fhow-do-i-restore-the-default-applets-to-gnomes-notification-area&sa=D&sntz=1&usg=AFQjCNGUVYnYCoUfrVCGX5tIHc5UWBNeDw); [fuente 2](http://www.google.com/url?q=http%3A%2F%2Fwww.watchingthenet.com%2Frestore-panels-in-ubuntu-back-to-their-default-settings.html&sa=D&sntz=1&usg=AFQjCNHAEFYUaK7ztqIKEgF563uoWWTHBw))

```bash
$ gconftool --recursive-unset /apps/panel
$ rm -rf ~/.gconf/apps/panel
$ pkill gnome-panel
```

## Concatenar PDF's

Con `pdftk` programa en linea de comando para procesar ficheros PDF. Está para casi todas las plataformas.

```bash
$ sudo aptitude search pdftk
i pdftk - A useful tool for manipulating PDF documents

$ sudo aptitude install pdftk
```

Concatenar todos los archivos facilmente que tengas en una carpeta:

```bash
$ pdftk carpeta_con_todos_ficheros/*.pdf cat output fichero_concatenado.pdf
```

Tiene muchas mas funcionalidades consultables con –help, pero si quieres, puedes echarle un vistazo a un [articulo de Linux-Magazine “PDF a tope”](https://www.linux-magazine.es/issue/12/PDFTk.pdf).

## APOD

Programa para descargar y ajustar como fondo de escritorio la imagen astronómica del día de la web [APOD](http://apod.nasa.gov/apod/). Es necesario que se encuentre Python instalado en el sistema.

Instalar el siguiente script en algún lugar:

```bash
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

## Instalar Oracle Java

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

## Reparación del sistema de archivos cuando se pone en modo "sólo lectura"

```bash
$ sudo fsck
```

## Descarga de un vídeo incrustado en un reproductor Flash

[Fuente](http://www.youtube.com/watch?v=8PuUnQCS7DQ)

Hacer captura Wireshark. Filtrar los paquetes RTMP con el filtro: "rtmpt". Localizar en los paquetes RTMP los comandos Handshake o Invoke la base de la url, lo que está en una propiedad llamada "tcUrl". Por ejemplo en un vídeo de Antena3 de F1 esta propiedad valía:

```
rtmp://antena3tvfs.fplive.net/antena3mediateca
```

Luego localizar el fichero en concreto. Suele estar en otro paquete y está relacionado con el comando "play". En el caso del ejemplo anterior salía:

```
mp4:mp_series1/f1cms/gestorf1/videos/517/VIDEOS_20130512_1315517.mp4
```

Unir las dos piezas para construir la URL completa:

```
rtmp://antena3tvfs.fplive.net/antena3mediateca/mp_series1/f1cms/gestorf1/videos/517/VIDEOS_20130512_1315517.mp4
```

Descargar el stream con el comando "rtmpdump":

```bash
$ rtmpdump -r "rtmp://antena3tvfs.fplive.net/antena3mediateca/mp_series1/f1cms/gestorf1/videos/517/VIDEOS_20130512_1315517.mp4" -o archivo.mp4
```

En ocasiones se produce el error siguiente:

```
WARNING: Received FLV packet before play()! Ignoring.
```

En estos casos utilizar el siguiente comando que separa las dos porciones de la URL:

```bash
$ rtmpdump -r "rtmp://alacarta.aragontelevision.es/vod" -y "mp4:/_archivos/videos/web/15288/15288.mp4" -o archivo.flv
```

Para vídeos de emisiones en vivo hay que añadir la opción `-v`. Por ejemplo, en una emisión de AragónTV, en la captura Wireshark se localizaron los siguientes elementos:

*  Paquete Handshake S2 => tcUrl = rtmp://aragontvlivefs.fplive.net/aragontvlive-live
*  Paquete play => valor = stream_normal_abt

Así pues la URL final será: `rtmp://aragontvlivefs.fplive.net/aragontvlive-live/stream_normal_abt` y el comando de descarga:

```bash
$ rtmpdump -v -r "rtmp://aragontvlivefs.fplive.net/aragontvlive-live/stream_normal_abt" -o archivo.mp4
```

Para descargar vídeos desde YouTube, last.fm, Google video, Dailymotion y Vimeo se puede utilizar el comando `clive`. [Aquí](http://www.emezeta.com/articulos/10-comandos-interesantes-para-linux) comentan cómo se usa.

## Descarga vídeo de A3Player

### Enlaces

*  [Cómo descargar vídeos en formato M3U8 (o HLS)](http://blog.tvalacarta.info/2012/10/25/como-descargar-videos-en-formato-m3u8-o-hls/)
*  [http live streaming player](https://gitorious.org/hls-player#more)

Las carreras de Formula1 últimamente son emitidas en el formato HLS. Para descargar una carrera empezar haciendo una captura con Wireshark desde el momento en que se le da al Play hasta que se empieza a ver parte del vídeo (esperando que terminen los anuncios). Luego filtrar en Wireshark con la siguiente expresión:

```
http.request.uri contains "playlist.m3u8"
```

Localizar la URL de descarga del fichero playlist.m3u8. Por ejemplo podría ser:

```
http://geodeswowa3player.antena3.com/vcg/_definst_/mp4:assets3/2013/10/26/E6941C5D-2A9F-414B-B3FF-01FAC33073C4/sigra.mp4/playlist.m3u8?pulse=assets3%2F2013%2F10%2F26%2FE6941C5D-2A9F-414B-B3FF-01FAC33073C4%2F%7C1382835190%7Cb23df1201096fc1cc490427e05307f70
```

## Compresión batch de vídeos

Instalar el cliente de linea de comando de [Handbrake](http://handbrake.fr/downloads.php).

Dependiendo de la extensión habrá que cambiar el `ls` inicial. Los vídeos de salida son MP4, por lo que si la extensión inicial no es esa, habrá que cambiarla en los ficheros finales.

```bash
$ mkdir comp
$ ls *.mp4 | awk '{print "HandBrakeCLI -Z Normal -i "$0" -o comp/"$0}' | sh
```

## Resampleado de video con HandBrake

([Fuente](http://www.antiscreeners.com/phpBB2/viewtopic.php?p=85974#85974))

On the Video tab use Avg Bitrate and use 2500 to 3000 depending if a big action movie(3000) or if less fast action/movement in the movie(2500). Make sure to click on 2-Pass Encoding and Turbo first pass.

## Split de vídeos

([Fuente](http://askubuntu.com/questions/35605/splitting-an-mp4-file))

Con el siguiente comando:

```bash
$ ffmpeg -acodec copy -vcodec copy -ss 00:00:00 -t 00:04:09 -i archivo_original.mp4 archivo_recortado.mp4
```

Donde el valor de la opción -ss es el instante de inicio en hh:mm:ss y el valor de -t es la longitud en hh:mm:ss

Durante un tiempo en Ubuntu, `ffmpeg` no estuvo disponible. Su sustituto fue `avconv`, compatible la mayoría de las veces. No admitía sin embargo la opción de copiar el codec de audio y vídeo. Había que especificarlo. Una lista de encoders soportados se puede obtener ejecutando:

```bash
$ avconv -encoders
```

Un par de codecs comprobados que suelen dar buen resultados son h264 y aac:

```bash
ffmpeg -acodec aac -vcodec h264 -ss 01:07:38 -t 00:01:14 -i archivo_original.mp4 archivo_recortado.mp4
```

## Crop en video

```bash
$ ffmpeg -i input.mp4 -filter:v "crop=w:h:x:y" output.mp4
```

donde:

* w: ancho final
* h: alto final
* x: coordenada x del punto superior izquierdo del recuadro
* y: coordenada y del punto superior izquierdo del recuadro

## Extraer frame de video

```bash
$ ffmpeg -ss 00:01:00 -i input.mp4 -frames:v 1 frame.png
```

donde el argumento -ss marca el instante del frame en hh:mm:ss

## Redimensionado de imágenes en lote

Ajustar a 200 px de ancho manteniendo el ratio:

```bash
$ convert '*.jpg[200x]' resized%03d.png
```

Ajustar a 200 px de alto manteniendo el ratio:

```bash
$ convert '*.jpg[x200]' resized%03d.png
```

## Redimensionado de imágenes en lote

Por ejemplo a 1080 de alto dentro de un directorio llamado resized:

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

## Crop y resize de imágenes en lote

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

## Conversión de formato en lote

```bash
for file in *.jpg; do
  filename=$(basename "$file")
  fileid=${filename%%.*}
  convert ${filename} ${fileid}.png
done
```

## Renombrado de archivos en lote

Por ejemplo una serie de archivos jpg:

```bash
a=1
for i in *.jpg; do
  new=$(printf "%04d.jpg" ${a})
  mv ${i} ${new}
  let a=a+1
done
```

## Montaje de vídeo StopMotion a partir de imágenes

A 10fps por ejemplo ([Fuente](http://www.dototot.com/compile-stop-motion-animation-image-sequence-avconv/)):

```bash
$ ffmpeg -f image2 -r 10 -i %04d.jpg -vf scale=1440:1080 -r:v 10 -c:v libx264 -qp 0 -preset veryslow -an "video.mkv"
```

## Montaje de gif a partir de imágenes

```bash
convert -delay n -loop 0 *.jpg output.gif
```

donde:

* n: milisegundos entre cada frame.

## Configurar Wireshark para poder capturar con usuarios no-root

Ejecutar lo siguiente:

```bash
$ sudo dpkg-reconfigure wireshark-common
$ sudo usermod -a -G wireshark <usuario>
```

Reiniciar la sesión.

## Solucionar el problema con Wireshark en las últimas versiones de Ubuntu

Cuando se inicia una captura, se cuelga Wireshark, emitiendo una serie infinita de errores de GTK en consola. En [esta página](https://bugs.launchpad.net/ubuntu/+source/overlay-scrollbar/+bug/1248400) comentan varios workarrounds. Por ejemplo editando el fichero `/usr/share/applications/wireshark.desktop` y cambiando la línea de ejecución por:

        Exec=env LIBOVERLAY_SCROLLBAR=0 wireshark %f

## Ficheros implicados en arranque

*  `/etc/rc.local`: This script is executed at the end of each multiuser runlevel.

## Montar imagen de disco o partición

([Fuente](http://www.forensicswiki.org/wiki/Mounting_Disk_Images#To_mount_a_disk_image_on_Linux))

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

    122880 * 512 = 62914560

3. Montar:

    ```bash
    $ sudo mount -t ext4 -o loop,offset=62914560,ro,noexec Rpi_8gb_wheezy_backup.img mnt
    ```

## Screencast

```bash
$ avconv -f x11grab -r 25 -s 910x550 -i :0.0 -vcodec huffyuv screencast.avi
```

## Gestión de módulos

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

## Ficheros definición variables de entorno

Si se necesita definir una variable global se podrá hacer en los ficheros:

* `/etc/environment`
* `/etc/profile`
* `/etc/profile.d`
* `/etc/bashrc` o `/etc/bash.bashrc`

Si es a nivel de usuario se hará en:

* `~/.bashrc`
* `~/.bash_profile`

## Poner barras de scroll normales

```bash
gsettings set com.canonical.desktop.interface scrollbar-mode normal
```

## Skype en tray

Instalar los paquetes `sni-qt` y `sni-qt:i386`.

## Workrave en tray

[Fuente](https://sourceforge.net/p/workrave/mailman/message/30722930/)

```bash
gsettings set com.canonical.Unity.Panel systray-whitelist "['all']"
```

## Localización de ficheros .desktop

* Los del usuario se encuentran en: `~/.local/share/applications`
* Los del sistema en: `/usr/share/applications`

## Configuración de gedit

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

## Localizar paquete que contiene un fichero

([Fuente](https://www.cyberciti.biz/faq/equivalent-of-rpm-qf-command/))

1. Instalar `apt-file`:

    ```bash
    $ sudo apt-get install apt-file
    ```

2. Actualizar su base de datos:

    ```bash
    $ sudo apt-file update
    ```

3. Hacer la búsqueda:

    ```bash
    $ apt-file search <fichero_con_ruta>
    ```

## Configuración de idiomas del sistema (locales)

```bash
$ sudo dpkg-reconfigure locales
```

## Configuración de SWAP en disco SSD

Siguiendo [esta página], añado lo siguiente al fichero `/etc/sysctl.conf` para bajar el 60% que usa Ubuntu por defecto a 10%:

```
vm.swappiness=10
```
