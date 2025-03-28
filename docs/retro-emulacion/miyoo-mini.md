# Miyoo Mini

![Miyoo Mini](../images/pages/miyoo_mini/miyoo-mini.jpg)

## Enlaces

#### Emuladores, Ports y Aplicaciones

* [Ports de steward-fu](https://github.com/steward-fu/miyoo-mini/releases/tag/stock)
* [Ports y compilaciones de Eggs](https://www.dropbox.com/sh/hqcsr1h1d7f8nr3/AABtSOygIX_e4mio3rkLetWTa)

#### Sistema

* Firmware:
    * [20220419 para Mini v1 y v2](https://drive.google.com/drive/folders/1VtfcBCoIcpMIBY2FIyAtjV-Dg02JUvhG)
    * [Community Firmware para Mini v3](https://www.reddit.com/r/MiyooMini/comments/104qbak/community_firmware_patch_for_new_devices/)
    * [20230326 para Mini+](https://www.sugarsync.com/pf/D4978471_09235444_837617)
    * [Guía de desbriqueo](https://cdn.discordapp.com/attachments/931367023588569180/967635766228430878/MiyooMiniUnbrickGuide.pdf)
* Toolchain:
    * [MiyooMini](https://github.com/MiyooMini/union-toolchain)
    * [Shauniman](https://github.com/shauninman/union-miyoomini-toolchain)
    * [OnionUI](https://github.com/OnionUI/dev-miyoomini-toolchain)
* Frontends:
    * [Koriki](https://github.com/Rparadise-Team/Koriki)
    * [Onion](https://github.com/OnionUI/Onion)
    * [MiniUI](https://github.com/shauninman/MiniUI)

#### Hardware

* [Tienda oficial en Aliexpress](https://miyoo.es.aliexpress.com/store/912663639)
* Extracción UART:
    * [steward-fu](https://steward-fu.github.io/website/handheld/miyoo-mini/uart.htm)
    * [eduardofilo](../2022-08-08_mmiyoo_uart.md)
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
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_available_governors`|Governors aceptados por el procesador (`userspace`, `powersave`, `ondemand`, `performance`)|
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_governor`|Governor actual|
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_available_frequencies`|Frecuencias aceptadas por el procesador (`400000`, `600000`, `800000`, `1000000`, `1100000`, `1200000`)|
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq`|Mínima frecuencia del procesador|
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq`|Máxima frecuencia del procesador|
|`/sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq`|Frecuencia actual del procesador|
|`/appconfigs/system.json`|Ajustes generales del sistema (corresponde al menú Settings)|

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

#### Framebuffer

```
/ # fbset

mode "640x480-100"
        # D: 45.455 MHz, H: 54.633 kHz, V: 100.060 Hz
        geometry 640 480 640 1440 32
        timings 22000 64 64 32 32 64 2
        accel false
        rgba 8/16,8/8,8/0,8/24
endmode
```

El frambuffer (`/dev/fb0`) contiene 3 imágenes (640x1440) y está rotado 180º. Cada pixel ocupa 4 bytes codificados en el siguiente orden: `BBGGRRAA` donde `AA` (alpha) vale siempre `FF`.
