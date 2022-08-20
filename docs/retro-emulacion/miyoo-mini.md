# Miyoo Mini

![RG351](/images/pages/miyoo_mini/miyoo-mini.jpg)

## Enlaces

#### Emuladores, Ports y Aplicaciones

* [Ports de steward-fu](https://github.com/steward-fu/miyoo-mini/releases/tag/stock)

#### Sistema

* [Firmware](https://lemiyoo.cn/upgrade/)
* Toolchain:
    * [MiyooMini](https://github.com/MiyooMini/union-toolchain)
    * [Shauniman](https://github.com/shauninman/union-miyoomini-toolchain)
    * [OnionUI](https://github.com/OnionUI/dev-miyoomini-toolchain)
* [Onion CFW](https://github.com/OnionUI/Onion)
* [MiniUI CFW](https://github.com/shauninman/MiniUI)

#### Hardware

* Extracción UART:
    * [steward-fu](https://steward-fu.github.io/website/handheld/miyoo-mini/uart.htm)
    * [eduardofilo](/2022-08-08_mmiyoo_uart.html)
* [Teardown](https://steward-fu.github.io/website/handheld/miyoo-mini/teardown_new.htm)
* Para imprimir:
    * Gatillos más accesibles: [V1](https://www.thingiverse.com/thing:5398496), [V2](https://www.thingiverse.com/thing:5422756)
* [Repuestos componentes](https://es.aliexpress.com/item/1005003782013191.html)

## Montaje de rootfs del firmware

1. Descargar el fichero que se utiliza para actualizar el firmware de la consola del [sitio oficial](https://lemiyoo.cn/upgrade/).
2. Localizar dentro del ZIP el fichero `.img`. En el caso de la actualización de 2022-04-19 el fichero se encuentra en el directorio `The firmware0419` y se llama `miyoo283_fw.img`.
3. Abrir el fichero con un editor hexadecimal para leer el inicio del mismo que contiene información en forma de texto con los bloques que hay dentro de la imagen y dónde se flashean en la NAND. En concreto nos interesa la sección que describe la partición `rootfs` que contiene la siguiente información:

    ```
    # File Partition: rootfs
    mxp r.info rootfs
    sf probe 0
    sf erase ${sf_part_start} ${sf_part_size}
    fatload mmc 0 0x21000000 $(SdUpgradeImage) 0x1ae000 0x22b000
    sf write 0x21000000 ${sf_part_start} 0x1AE000
    ```

4. Según la [documentación](https://u-boot.readthedocs.io/en/v2022.04/usage/cmd/fatload.html) del comando `fatload` de U-boot, los dos últimos parámetros en hexadecimal son el tamaño y la posición de la partición rootfs dentro del fichero `.img`.
5. Crear un directorio (por ejemplo `mnt`) y ejecutar el siguiente comando para montar el rootfs del firmware en él:

    ```
    sudo mount -o loop,sizelimit=0x1ae000,offset=0x22b000,ro,noexec miyoo283_fw.img mnt
    ```

Utilizando el mismo método se pueden montar también las particiones `miservice` y `customer`:

```
sudo mount -o loop,sizelimit=0x32f000,offset=0x3d9000,ro,noexec miyoo283_fw.img mnt2
sudo mount -o loop,sizelimit=0x6c5000,offset=0x708000,ro,noexec miyoo283_fw.img mnt3
```

## Cheatsheets

#### Directorios/Ficheros interesantes del firmware

|Directorio|Contenido|
|:---------|:--------|
|`/mnt/SDCARD`|Punto de montaje de la SD|
|`/customer/main`|Script principal de arranque del frontend. Es el que invoca `.tmp_update/updater` en caso de existir que es el punto de arranque de los UIs como Onion o MiniUI|
|`/sys/devices/gpiochip0/gpio/gpio59/value`|Flag indicador de si la máquina se está cargando|
|`/sys/class/pwm/pwmchip0/pwm0/duty_cycle`|Brillo de pantalla (de 0 a 100)|

#### Directorios/Ficheros interesantes OnionUI

|Directorio|Contenido|
|:---------|:--------|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/playActivity.db`|Base de datos de Play Activity. Para resetear las estadísticas se puede simplemente borrar el fichero|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/PlayActivityBackup/`|Directorio que contiene backups del fichero `playActivity.db` anterior. Aparentemente no se purga este directorio, por lo que habrá que hacerlo a mano de vez en cuando.|
|`/mnt/SDCARD/Roms/recentlist.json`|Lista `Recent`|
|`/mnt/SDCARD/.tmp_update/romScreens/`|Screenshots|
|`/mnt/SDCARD/.tmp_update/.disableMenu`|Desactiva el Game Switcher asociado a la tecla Menu|

#### GPIOs

```
/ # cat /sys/kernel/debug/gpio
gpiochip0: GPIOs 0-90, gpio:
 gpio-1   (                    |GPIO Key Up         ) in  hi
 gpio-5   (                    |GPIO Key Right      ) in  hi
 gpio-6   (                    |GPIO Key B          ) in  hi
 gpio-7   (                    |GPIO Key Y          ) in  hi
 gpio-8   (                    |GPIO Key A          ) in  hi
 gpio-9   (                    |GPIO Key X          ) in  hi
 gpio-10  (                    |GPIO Key START      ) in  hi
 gpio-11  (                    |GPIO Key SELECT     ) in  hi
 gpio-12  (                    |GPIO Key MENU       ) in  hi
 gpio-13  (                    |GPIO Key L          ) in  hi
 gpio-14  (                    |GPIO Key L2         ) in  hi
 gpio-47  (                    |GPIO Key R2         ) in  hi
 gpio-59  (                    |sysfs               ) in  lo
 gpio-69  (                    |GPIO Key Down       ) in  hi
 gpio-70  (                    |GPIO Key Left       ) in  hi
 gpio-72  (                    |                    ) out lo
 gpio-86  (                    |GPIO Key POWER      ) in  lo
 gpio-90  (                    |GPIO Key R          ) in  hi
```

#### Teclas

|Tecla|GPIO|Valor SDL|Descriptor SDL|
|:----|:---|:--------|:-------------|
|Arriba|1|273|SDLK_UP|
|Abajo|69|274|SDLK_DOWN|
|Izquierda|70|276|SDLK_LEFT|
|Derecha|5|275|SDLK_RIGHT|
|Menu|12|27|SDLK_ESCAPE|
|A|8|32|SDLK_SPACE|
|B|6|306|SDLK_LCTRL|
|X|9|304|SDLK_LSHIFT|
|Y|7|308|SDLK_LALT|
|Select|11|305|SDLK_RCTRL|
|Start|10|13|SDLK_RETURN|
|L1|13|101|SDLK_e|
|L2|14|9|SDLK_TAB|
|R1|90|116|SDLK_t|
|R2|47|8|SDLK_BACKSPACE|