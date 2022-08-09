---
layout: default
permalink: /retro-emulacion/miyoo-mini.html
---

# Miyoo Mini

![RG351](/images/pages/miyoo_mini/miyoo-mini.jpg)

## Enlaces

#### Emuladores, Ports y Aplicaciones

* [Ports de steward-fu](https://github.com/steward-fu/miyoo-mini/releases/tag/stock)

#### Sistema

* [Firmware](https://lemiyoo.cn/upgrade/)
* Toolchain:
    * [Shauniman](https://github.com/shauninman/union-miyoomini-toolchain)
    * [OnionUI](https://github.com/OnionUI/dev-miyoomini-toolchain)
* [Onion CFW](https://github.com/OnionUI/Onion)
* [MiniUI CFW](https://github.com/shauninman/MiniUI)

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
|`/mnt/SDCARD/Roms/recentlist.json`|Lista `Recent`|
|`/mnt/SDCARD/.tmp_update/romScreens/`|Screenshots|
|`/mnt/SDCARD/.tmp_update/.disableMenu`|Desactiva el Game Switcher asociado a la tecla Menu|
