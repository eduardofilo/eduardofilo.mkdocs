---
layout: default
permalink: /retro-emulacion/miyoo-mini.html
---

# Miyoo Mini

![RG351](/images/pages/miyoo_mini/miyoo-mini.jpg)

## Enlaces

#### Sistema

* [Firmware](https://lemiyoo.cn/upgrade/)

#### Hardware

* [Extracción UART](https://steward-fu.github.io/website/handheld/miyoo-mini/uart.htm)
* [Teardown](https://steward-fu.github.io/website/handheld/miyoo-mini/teardown_new.htm)
* Para imprimir:
    * Gatillos más accesibles: [V1](https://www.thingiverse.com/thing:5398496), [V2](https://www.thingiverse.com/thing:5422756)
* [Repuestos componentes](https://es.aliexpress.com/item/1005003782013191.html)

## Cheatsheets

#### Directorios/Ficheros interesantes OnionOS

Con el sistema arrancado, la raíz de la tarjeta SD se monta en `/mnt/SDCARD`.

|Directorio|Contenido|
|:---------|:--------|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/playActivity.db`|Base de datos de Play Activity. Para resetear las estadísticas se puede simplemente borrar el fichero|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/PlayActivityBackup/`|Directorio que contiene backups del fichero `playActivity.db` anterior. Aparentemente no se purga este directorio, por lo que habrá que hacerlo a mano de vez en cuando.|
