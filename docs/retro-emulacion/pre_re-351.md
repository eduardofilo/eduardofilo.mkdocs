Se pueden guardar configuraciones individuales de juegos. Para ello crear un .opt desde el menú `save game overrides`


BOB FAT edition
https://telegra.ph/BOB-FAT32edition-10-30




7z e -so "BOB 3.7 Fix_FAT32_RG351P.7z" | sudo dd of=/dev/mmcblk0 bs=2M status=progress conv=fsync

/dev/mmcblk0p1          524008    487928     36080  93% /flash
/dev/mmcblk0p2         1376342    474267    897979  35% /storage
/dev/mmcblk0p3        13648848  11761448   1887400  86% /var/media/ROMS

RG351P:~ # ls -l roms
lrwxrwxrwx    1 root     root            15 Nov  8 11:07 roms -> /var/media/ROMS
