title: 2020-06-03 RG350 Raspi Imagen
summary: Procedimiento para generar una imagen de tarjeta SD flasheable para RG350, Raspberry Pi y otras.
date: 2020-06-03 17:15:00

![microSD logo](/images/posts/rg350_raspi_image/microsd.png)

Muchas de las placas [Linux Embedded](https://es.wikipedia.org/wiki/Linux_embebido), como la RG350 o la Raspberry Pi, contienen el sistema operativo en una microSD con una distribución de particiones y archivos determinada. Una vez que tenemos un sistema configurado a nuestro gusto nos puede interesar hacer una imagen de la misma por si se corrompe o estropea la tarjeta que estamos utilizando o por si queremos distribuir el sistema a otras personas.

En este artículo se comenta el procedimiento para obtener un dump o imagen de una tarjeta SD, consistente en producir un fichero con el contenido y estructura de una tarjeta dada, es decir el proceso opuesto al flasheo.

## Teoría

En teoría para hacer la imagen tan sólo necesitaríamos una herramienta para hacer el dump. En la práctica hay varios temas que merece la pena considerar antes de utilizar una de estas herramientas. Vamos a comentarlas a continuación. Si no te interesan estos aspectos puedes saltar directamente al apartado [Práctica](#practica).

#### Tamaño de la tarjeta

Es obvio que si hacemos una imagen de una tarjeta de 32GB, luego no tendremos problemas flasheando por ejemplo en tarjetas de 64GB y será imposible flashearla en tarjetas de 16GB. Lo que no resulta tan obvio es que esa imagen de 32GB es posible que no entre en muchas otras tarjetas de 32GB. ¿Por qué? Pues porque no hay dos tarjetas iguales. Por algún motivo que desconozco, los fabricantes producen tarjetas con distintos tamaños.

Podemos consultar los detalles de la capacidad de una tarjeta por medio del comando `fdisk --list` (en Linux, luego veremos un programa equivalente en Windows). La primera linea de toda la información que devuelve este comando nos da todos los detalles. Por ejemplo este es el resultado de ejecutar este comando en tres tarjetas de 16GB de distintos fabricantes:

|Fabricante|Detalles|Capacidad en MB|
|:---------|:-------|:--------------|
|Energizer|14,47 GiB, 15523119104 bytes, 30318592 sectores|14804|
|Toshiba|14,5 GiB, 15552479232 bytes, 30375936 sectores|14832|
|Samsung PRO|14,93 GiB, 16003891200 bytes, 31257600 sectores|15262,5|

A la vista de esto se entiende que si hacemos una imagen de la tarjeta Toshiba por ejemplo, se podrá flashear sin modificar en la Samsung PRO pero no en la Energizer.

El truco para crear una imagen de por ejemplo 16GB que luego vaya a poderse flashear sin problemas en todas las tarjetas de 16GB del mercado consiste en encoger la última partición de la tarjeta de manera que dejemos un espacio de seguridad sin utilizar al final de la misma. Por ejemplo en el caso de la Toshiba que ya hemos determinado que es bastante pequeña, vamos a dejar los 200MB finales. En caso de trabajar con la Samsung sería mejor elevar esa cifra hasta los 500MB.

#### Dump parcial

Más tarde a la hora de realizar el dump o generación del archivo de imagen, tendremos que indicar al programa de turno que lea sólo el espacio ocupado por las particiones. De esta manera el fichero de imagen no cubrirá esos MB de margen que hemos dejado en el paso anterior, y a la hora de escribir en tarjetas especialmente pequeñas no obtendremos el típico error de que se ha alcanzado el límite del dispositivo. En realidad lo verdaderamente importante es haber dejado el espacio sin utilizar al final de la tarjeta. Si luego hacemos el dump de toda la tarjeta, aunque obtengamos el error mencionado anteriormente, el flasheo será correcto, ya que se dará fuera del espacio utilizado por las particiones. Es algo parecido a dejar un margen grande en los documentos de texto que escribimos. Así si luego imprimimos estos documento en hojas ligeramente más pequeñas (por haber recortado los bordes por ejemplo) el contenido del documento se presentará íntegro aunque la impresora pueda detectar que la hoja es más pequeña de lo esperado e incluso pueda mostrar un error por ello.

Siguiendo con el ejemplo de la tarjeta de 16GB anterior vamos a ver cómo hacer las cuentas de la cantidad de tarjeta que tenemos que leer durante el dump para que todas las particiones entren en el mismo, dejando fuera el espacio final sin utilizar que hemos reservado.

En Linux consultamos la información de la tarjeta y las particiones que contiene mediante `fdisk`:

```
$ sudo fdisk -l /dev/mmcblk0
Disco /dev/mmcblk0: 14,5 GiB, 15552479232 bytes, 30375936 sectores
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 512 bytes
Tamaño de E/S (mínimo/óptimo): 512 bytes / 512 bytes
Tipo de etiqueta de disco: dos
Identificador del disco: 0x8e7b7353

Dispositivo    Inicio Comienzo    Final Sectores Tamaño Id Tipo
/dev/mmcblk0p1              32   819199   819168   400M  b W95 FAT32
/dev/mmcblk0p2          819200 29966335 29147136  13,9G 83 Linux
```

Los datos que nos interesan son el sector de comienzo y el número de sectores de la segunda partición, en este caso 819200 y 29147136 respectivamente.

En Windows obtendremos esta misma información con DiskGenius seleccionando la última partición de la tarjeta:

![DiskGenius Partition info](/images/posts/rg350_raspi_image/diskgenius_fdisk.png)

En este caso los datos que nos interesan son los valores `Total Sectors` y `Starting Sector`. Como vemos coinciden con los valores 29147136 y 819200 que habíamos localizado en Linux.

Una vez que tenemos estos valores, el número de sectores a copiar en el dump será la suma de los mismos, es decir 819200 + 29147136 = 29966336 sectores. En la información que ofrecía el comando `fdisk` de Linux, vemos que cada sector ocupa 512 bytes. Por tanto el dump tiene que hacerse de 29966336 * 512 = 15342764032 bytes = 14983168 KB = 14632 MB.

Así pues, el dump que haremos en este caso será de **29966336 sectores** o lo que es lo mismo de **14632 MB**.

#### Información residual en espacio libre

Muchos ya sabréis que cuando se elimina un fichero en un sistema de archivos, normalmente sólo se da de baja de las tablas de directorios, pero el contenido del mismo se mantiene en su lugar. Esto se hace por eficacia de los sistemas de archivo (dedicarse a escribir ceros en donde antes había un fichero que acabamos de borrar lleva tiempo y consumo de ciclos de escritura en dispositivos flash). También permite recuperar información borrada por error. Pero cuando estamos pensando en hacer una imagen, toda esa información que en teoría ya no debería estar ahí es un problema. Primero porque hará que la imagen se comprima peor y segundo porque estaremos incluyendo datos que a lo mejor no nos interesa publicar (por eso los hemos borrado seguramente). Así pues será muy conveniente borrar efectivamente todo el espacio de las particiones que dejemos libre.

## Práctica

Una vez explicadas algunas de las cosas que vamos a hacer a partir de ahora, vamos a mostrar el proceso paso a paso en Linux y Windows.

#### Linux

1. Reducimos con `gparted` el tamaño de la última partición para dejar espacio libre al final de la tarjeta. Según los cálculos explicados en la [teoría](#tamano-de-la-tarjeta) dejaríamos 200MB libres en la tarjeta.

	![Gparted](/images/posts/rg350_raspi_image/gparted.png)

2. Montamos la tarjeta en nuestro sistema y averiguamos los directorios donde se anclan las particiones (en sistemas como los de la RG350 y Raspberry Pi serán dos casi siempre), por ejemplo en mi máquina (filtro la salida del comando `df` por mmcblk0 porque es el nombre de dispositivo que adopta siempre el lector de tarjetas de mi portátil, pero puede cambiar en otras máquinas; retirar el `grep` si se desconoce):

    ```
    $ df -h | grep mmcblk0
    /dev/mmcblk0p1             400M   179M  221M  45% /media/edumoreno/2738-756D
    /dev/mmcblk0p2              14G    13G  1,3G  91% /media/edumoreno/6684e595-e23b-4e2f-8eb9-65f1286798cd
    ```

3. Escribimos ceros en el espacio no utilizado de la tarjeta. Nos situamos en un directorio cualquiera de esas dos particiones (por ejemplo el raíz) y ejecutamos los siguientes comandos (hay que hacerlo para cada partición):

    ```
    $ cd /media/edumoreno/2738-756D
    $ sudo dd if=/dev/zero of=zero.txt && sudo sync
    $ sudo rm zero.txt && sudo sync
    $ cd /media/edumoreno/6684e595-e23b-4e2f-8eb9-65f1286798cd
    $ sudo dd if=/dev/zero of=zero.txt && sudo sync
    $ sudo rm zero.txt && sudo sync
    ```

4. Desmontamos las particiones para que no se puedan modificar durante el dump:

    ```
    $ sudo umount /dev/mmcblk0p*
    ```

5. Finalmente realizamos el dump. Vamos a hacer el dump en bloques de 2MB y dado que según las cuentas hechas en la [teoría](#dump-parcial) sólo queremos copiar 14632 MB, el dump será de 14632 / 2 = 7316 bloques:

    ```
    $ sudo dd if=/dev/mmcblk0 of=imagen.img bs=2M count=7316
    ```

El comando anterior puede tardar bastante. Suele ser mejor utilizar el comando `dcfldd` en lugar del `dd`, si lo tenemos instalado en nuestro sistema, ya que hace lo mismo que `dd` ofreciendo información del progreso del dump. Al finalizar encontraremos el fichero `imagen.img` con nuestro dump de la tarjeta con el tamaño prometido:

```
$ ls -l --block-size=M
total 14632M
-rwxrwxrwx 1 edumoreno edumoreno 14632M jun  4 00:44 imagen.img
```

Suele ser conveniente [comprimir](#compresion-y-troceo-de-la-imagen) el dump (ya que [como sabemos](#informacion-residual-en-espacio-libre) contendrá mucho espacio vacío que se comprimirá bien). Además la mayoría de las aplicaciones de flasheo aceptan imagenes comprimidas directamente.

#### Windows

En el caso de Windows todos los pasos los podemos realizar con la excelente utilidad [DiskGenius](https://www.diskgenius.com/) si contamos con la versión de pago. Si sólo tenemos la versión Free, el paso final lo realizaremos con [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/).

1. Reducimos con `DiskGenius` el tamaño de la última partición para dejar espacio libre al final de la tarjeta. Según los cálculos explicados en la [teoría](#tamano-de-la-tarjeta) dejaríamos 200MB libres en la tarjeta.

	![DiskGenius](/images/posts/rg350_raspi_image/diskgenius.png)

2. Escribimos ceros en el espacio no utilizado de la tarjeta. Para ello en DiskGenius seleccionamos el menú `Tools > Erase Free Space`. Aparece una ventana mostrándonos todas las particiones de los discos detectados en el sistema. Seleccionamos en primer lugar la primera partición:

	![DiskGenius Erase Free Space 1](/images/posts/rg350_raspi_image/diskgenius_erase_free_space1.png)

3. Al pulsar OK aparece otra ventana que nos permite seleccionar el valor que se escribirá en el espacio no utilizado. Dejamos el valor `00` que nos ofrece y pulsamos `OK`:

	![DiskGenius Erase Free Space 2](/images/posts/rg350_raspi_image/diskgenius_erase_free_space2.png)

4. Se nos informa del progreso hasta que el proceso termina y podemos cerrar pulsando `Complete`:

	![DiskGenius Erase Free Space 3](/images/posts/rg350_raspi_image/diskgenius_erase_free_space3.png)

5. Repetimos el proceso para borrar el espacio no utilizado de la segunda partición. Esta vez tardará más tiempo:

	![DiskGenius Erase Free Space 4](/images/posts/rg350_raspi_image/diskgenius_erase_free_space4.png)

6. Para hacer el dump final abandonamos DiskGenius porque la función que necesitamos para ello (`Tools > Copy Sectors`) sólo está disponible en la versión de pago y pasamos a utilizar Win32DiskImager. Abrimos la utilidad y la configuramos indicando en `Image File` el destino y nombre del fichero de imagen, en `Device` seleccionamos la letra de la unidad donde se monta la partición FAT de la tarjeta y finalmente marcamos la opción `Read Only Allocated Partitions` para que el dump no incluya el espacio libre que hemos dejado al final en el paso 1.

	![Win32DiskImager](/images/posts/rg350_raspi_image/win32diskimager.png)

11. Finalmente pulsamos `Read` y esperamos a que el proceso termine:

	![Win32DiskImager 1](/images/posts/rg350_raspi_image/win32diskimager1.png)

## Compresión y troceo de la imagen

Como vemos la imagen de una tarjeta SD va a ser siempre un fichero enorme. Si queremos compartirla lo habitual será comprimirla y trocearla con un compresor. Vamos a ver cómo hacerlo en Linux y Windows.

#### Linux

Como siempre echamos mano de la linea de comando. Vamos a mostrar cómo hacerlo en un par de formatos:

* 7z:

	```
	$ cat imagen.img | 7z -si -v1400m a imagen.img.7z
	```

* Rar:

	```
	$ cat imagen.img | rar a -m5 -simagen.img -v1400000k imagen.img.rar
	```

#### Windows

* 7z: Naturalmente para que esto funcione debemos tener instalado [7-Zip](https://www.7-zip.org/). Pulsamos con el botón derecho del ratón sobre el fichero de imagen y seleccionamos `7-Zip > Añadir al archivo...` en el menu contextual. Aparece una ventana en la que lo único que tenemos que cambiar es introducir el número de MBs que queremos tengan los trozos. Por ejemplo 1400MB se indica en 7-Zip con 1400M:

	![7-Zip](/images/posts/rg350_raspi_image/7zip.png)

* WinRAR: Igualmente necesitaremos tener instalado [WinRAR](https://www.winrar.es/descargas). Pulsamos con el botón derecho del ratón sobre el fichero de imagen y seleccionamos `Añadir al archivo...` en el menu contextual que tiene al lado el icono de WinRAR. Aparece una ventana en la que lo único que tenemos que cambiar es introducir el número de MBs que queremos tengan los trozos. Por ejemplo 1400MB:

	![WinRAR](/images/posts/rg350_raspi_image/winrar.png)
