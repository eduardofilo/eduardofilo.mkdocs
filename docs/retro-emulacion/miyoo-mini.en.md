# Miyoo Mini

![RG351](/images/pages/miyoo_mini/miyoo-mini.jpg)

## Links

#### Emulators, Ports and Applications

* [Ports by steward-fu](https://github.com/steward-fu/miyoo-mini/releases/tag/stock)

#### System

* [Firmware](https://lemiyoo.cn/upgrade/)
* Toolchain:
    * [MiyooMini](https://github.com/MiyooMini/union-toolchain)
    * [Shauniman](https://github.com/shauninman/union-miyoomini-toolchain)
    * [OnionUI](https://github.com/OnionUI/dev-miyoomini-toolchain)
* [Onion CFW](https://github.com/OnionUI/Onion)
* [MiniUI CFW](https://github.com/shauninman/MiniUI)

#### Hardware

* UART mod:
    * [steward-fu](https://steward-fu.github.io/website/handheld/miyoo-mini/uart.htm)
    * [eduardofilo](/en/2022-08-08_mmiyoo_uart.html)
* [Teardown](https://steward-fu.github.io/website/handheld/miyoo-mini/teardown_new.htm)
* 3D Print:
    * More accessible triggers: [V1](https://www.thingiverse.com/thing:5398496), [V2](https://www.thingiverse.com/thing:5422756)
* [Spare parts](https://es.aliexpress.com/item/1005003782013191.html)

## Firmware's rootfs mounting

1. Download the file used to update the console firmware from [official site](https://lemiyoo.cn/upgrade/).
2. Locate inside the ZIP the `.img` file. In the case of the 2022-04-19 update the file is located in `The firmware0419` directory and is named `myoo283_fw.img`.
3. Open the file with an hex editor to read the beginning of it which contains information in text form with the blocks inside the image and where they are flashed on the NAND. In particular we are interested in the section describing the `rootfs` partition which contains the following information:

    ```
    # File Partition: rootfs
    mxp r.info rootfs
    sf probe 0
    sf erase ${sf_part_start} ${sf_part_size}
    fatload mmc 0 0x21000000 $(SdUpgradeImage) 0x1ae000 0x22b000
    sf write 0x21000000 ${sf_part_start} 0x1AE000
    ```

4. According to the U-boot `fatload` command [documentation](https://u-boot.readthedocs.io/en/v2022.04/usage/cmd/fatload.html), the last two parameters in hexadecimal are the size and the position of the rootfs partition inside the `.img` file.
5. Create a directory (for example `mnt`) and run the following command to mount the firmware rootfs in it:

    ```
    sudo mount -o loop,sizelimit=0x1ae000,offset=0x22b000,ro,noexec miyoo283_fw.img mnt
    ```

Using the same method you can also mount the `miservice` and `customer` partitions:

```
sudo mount -o loop,sizelimit=0x32f000,offset=0x3d9000,ro,noexec miyoo283_fw.img mnt2
sudo mount -o loop,sizelimit=0x6c5000,offset=0x708000,ro,noexec miyoo283_fw.img mnt3
```

## Cheatsheets

#### Interesting firmware directories/files

|Directory|Content|
|:---------|:--------|
|`/mnt/SDCARD`|SD mounting point|
|`/customer/main`|Main frontend startup script. It is the one that invokes `.tmp_update/updater` in case it exists which is the starting point of UIs like Onion or MiniUI|
|`/sys/devices/gpiochip0/gpio/gpio59/value`|Flag indicating if the machine is being charged|
|`/sys/class/pwm/pwmchip0/pwm0/duty_cycle`|Screen brightness (from 0 to 100)|

#### Interesting OnionUI directories/files

|Directory|Content|
|:---------|:--------|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/playActivity.db`|Play Activity database. To reset the statistics, you can simply delete the file|
|`/mnt/SDCARD/Saves/CurrentProfile/saves/PlayActivityBackup/`|Directory containing backups of the previous `playActivity.db` file. Apparently this directory is not purged, so you will have to do it by hand from time to time.|
|`/mnt/SDCARD/Roms/recentlist.json`|`Recent` list|
|`/mnt/SDCARD/.tmp_update/romScreens/`|Screenshots|
|`/mnt/SDCARD/.tmp_update/.disableMenu`|Disables the Game Switcher associated with the Menu key|

#### Key GPIOs

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

#### Keys

|Key|GPIO|SDL value|SDL descriptor|
|:----|:---|:--------|:-------------|
|Up|1|273|SDLK_UP|
|Down|69|274|SDLK_DOWN|
|Left|70|276|SDLK_LEFT|
|Right|5|275|SDLK_RIGHT|
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