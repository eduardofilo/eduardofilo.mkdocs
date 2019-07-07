---
layout: default
permalink: /sistemas/odroid.html
---

# ODROID

## Enlaces

### Varios

* [ODROID Magazine](http://magazine.odroid.com/)
* [ODROID Wiki](http://odroid.com/dokuwiki/doku.php?id=en:odroid-c1)
* [ODROID.in](http://odroid.in/): Imágenes de distintos sistemas.

### Hardware

* [2.5 mm x 0.8 mm USB Charger Universal Cable Main Power Supply](http://www.amazon.co.uk/Charger-Universal-Supply-Android-Tablet/dp/B00JPN0SJG)
* [Generic PB20517 - Cargador (2 A, Negro)](http://www.amazon.es/Desconocido-PB20517-Generic-Cargador-Negro/dp/B00ET2VWGQ/ref=sr_1_4?ie=UTF8&qid=1419372446&sr=8-4&keywords=cargador+tablet+2%2C5)
* [NorthPad Universal 2,5x0,8mm Europa Adaptador AC Cargador 5V 3A](http://www.amazon.es/NorthPad-Universal-Adaptador-Cargador-Android/dp/B00CLC36LU/ref=sr_1_2?ie=UTF8&qid=1419372446&sr=8-2&keywords=cargador+tablet+2%2C5)
* [HDMI Femenino Enchufe A Micro HDMI Masculino Clavija Adaptador Para HDMI Cables](http://www.amazon.es/Femenino-Enchufe-Masculino-Clavija-Adaptador/dp/B00DI8Q6PO/ref=sr_1_3?ie=UTF8&qid=1419372325&sr=8-3&keywords=micro+hdmi)

## Comandos útiles

### Utilidad de configuración

```bash
$ sudo odroid-utility.sh
```

### Flasheo de imagen [Ubuntu oficial](http://odroid.com/dokuwiki/doku.php?id=en:c1_release_linux_ubuntu)

```bash
$ xzcat ubuntu-14.04.1lts-lubuntu-odroid-c1-20141211.img.xz | sudo dd of=/dev/mmcblk0 bs=2M
```

### Backup de la SD (comprimiendo al vuelo)

```bash
$ #Backup:
$ sudo dd if=/dev/mmcblk0 bs=2M | gzip -9 - > odroid_8gb_backup.img.gz
$ #Restauración:
$ gunzip odroid_8gb_backup.img.gz -c | sudo dd of=/dev/mmcblk0 bs=2M
```

### Control de progreso durante flasheo

```bash
$ sudo pkill -USR1 -n -x dd
```
