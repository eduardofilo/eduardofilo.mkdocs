title: Installing Arch Linux on Steam Deck
summary: A complete guide to installing Arch Linux alongside SteamOS with dual boot on the Steam Deck.
date: 2024-09-04 15:30:00

![Steam Deck with Arch Linux](/images/posts/2024-09-04_steam_deck_arch/steam_deck_logo.png)

In July 2024, the 512GB LCD model of the Steam Deck was available for under €400 for a few weeks. This price was very appealing for a [decent machine](https://www.steamdeck.com/es/tech/deck) with an AMD processor based on x86 (AMD64) architecture, 16GB of RAM, an NVMe SSD of the mentioned capacity, a touchscreen, and integrated gaming controls. Essentially, it's a handheld PC, but still a PC. What makes this machine especially attractive to me is its full Linux support, making it an ideal platform for tinkering with Linux distributions or using it as a secondary portable PC. Of course, this is in addition to its conventional use for gaming and [emulating](https://www.emudeck.com/) video games.

SteamOS, the default operating system, is based on Arch Linux, and in desktop mode, it can be used almost like a regular Arch Linux system. The main restriction is that it's built in immutable mode. While this type of system configuration has its virtues and it's understandable why Valve chose it for their machine, I still prefer a normal (mutable) system. So, I decided to install a regular Arch Linux and learn how to install this distribution. According to the [Arch wiki](https://wiki.archlinux.org/title/Steam_Deck), the hardware of the Steam Deck LCD model is 100% supported by Arch.

The following is the complete procedure I used.

<!-- more -->

## Keyboard/Mouse

Although most operations can be performed using the Steam Deck's touchscreen and trackpads, it's highly recommended to connect a keyboard and mouse to the console to facilitate the installation, especially during the terminal session where we'll install the base system. The Steam Deck only has one USB-C port, so the most practical solution is to use a dock. It may also suffice (especially if we run live systems from a microSD) to use a wireless keyboard/mouse dongle connected with a USB<->USB-C adapter, though in that case, it's advisable to ensure the Steam Deck is fully charged.

In my case, I used a Dell [DA310z](https://www.dell.com/es-es/shop/adaptador-multipuerto-usb-c-de-dell-7-en-1-da310/apd/470-aeup/conexi%C3%B3n-wifi-y-redes) dock.

## Disk repartitioning

The Steam Deck's SSD I purchased is 512GB and of the NVMe type. This is the minimum size if we want to install another system alongside SteamOS.

Before starting the installation, we need to make space by shrinking the main partition (number 8). For this, we can use almost any live Linux distribution that we boot from a removable drive (USB or microSD) since all of them come with some partition management program. I used a `gparted` ISO.

The complete procedure can be seen below:

1. Download the [gparted ISO](https://gparted.org/download.php). Specifically, I used [this version](https://downloads.sourceforge.net/gparted/gparted-live-1.6.0-3-amd64.iso).
2. Install the ISO on a USB drive or, even better, on a microSD (since the Steam Deck has a slot for these). You can use a program like [Balena Etcher](https://www.balena.io/etcher/) or the `dd` command in Linux if you [know how to use it](/sistemas/raspi.html#backup-de-la-sd-comprimiendo-al-vuelo).
3. Boot the Steam Deck with the USB drive or microSD inserted by holding down the volume- button until you hear the power-up tones. This causes the console to boot into the `Boot Manager` menu.
4. Select the option to boot from the removable device, which will appear in the menu as `EFI USB Device (USB)` or `EFI SD/MMC Card (XX XXXX XXXX)` depending on whether you used a USB drive or a microSD respectively.
5. A configuration screen appears where we make the following selections:

    * Policy for handling keymaps => Don't touch keymap
    * Which language do you prefer? => 25
    * Which mode do you prefer? => 0

6. After accepting the last option, the `gparted` program will start in graphical mode (with the screen rotated, though). We will make changes until the partitions look like the screenshot. Essentially, we'll shrink partition #8 by about 100GB, create #9 with 4GB for swap, and #10 with the remaining space for the Arch root system:

    ![Steam Deck Partitions](/images/posts/2024-09-04_steam_deck_arch/steam-deck-partitions.png)

Note, when looking at the partitions used by SteamOS, that it uses an [A/B partition system](https://blog.davidbyrne.dev/2018/08/16/linux-ab-partitions), common in Android, where most of the system partitions (except the user space one) are duplicated. This system is designed to facilitate updates, or rather to roll back in case of problems during them.

## Base installation

For the base system installation, I opted for the conventional method following the instructions in the [installation guide](https://wiki.archlinux.org/title/Installation_guide) on the Arch wiki. This installation uses an Arch system ISO that we can boot from a removable drive (USB or microSD) to install the basic packages needed for a bootable and very basic system.

Before starting, note that due to the dynamic nature of the Arch Linux distribution, it's very likely that this guide will become outdated soon. Therefore, I recommend checking the [official guide](https://wiki.archlinux.org/title/Installation_guide) if something doesn't go as expected.

Below is the step-by-step installation process:

1. Download the [Arch Linux ISO](https://archlinux.org/download/). Specifically, I used [this version](https://es.mirrors.cicku.me/archlinux/iso/2024.08.01/archlinux-2024.08.01-x86_64.iso).
2. Install the ISO on a USB drive or, even better, on a microSD to use the slot on the Steam Deck. You can use a program like [Balena Etcher](https://www.balena.io/etcher/) or the `dd` command in Linux if you [know how to use it](/sistemas/raspi.html#backup-de-la-sd-comprimiendo-al-vuelo).
3. Boot the Steam Deck with the USB drive or microSD inserted by holding down the volume- button until you hear the power-up tones. This causes the console to boot into the `Boot Manager` menu.
4. Select the option to boot from the removable device, which will appear in the menu as `EFI USB Device (USB)` or `EFI SD/MMC Card (XX XXXX XXXX)` depending on whether you used a USB drive or a microSD respectively.
5. Once the Arch live installation system finishes booting, run the following commands in order (in the `iwctl` session, replace `<SSID>` with your own and enter the password when prompted; also replace the user identifier `<USER>` with the one you want to use):

    ```bash
    # loadkeys en
    # iwctl
    [iwd]# station wlan0 scan
    [iwd]# station wlan0 get-networks
    [iwd]# station wlan0 connect <SSID>
    [iwd]# exit
    # mkfs.ext4 /dev/nvme0n1p10
    # mkswap /dev/nvme0n1p9
    # mount /dev/nvme0n1p10 /mnt
    # mount --mkdir /dev/nvme0n1p1 /mnt/boot/efi
    # swapon /dev/nvme0n1p9
    # pacstrap -K /mnt base base-devel linux linux-firmware sudo vi ntfs-3g networkmanager amd-ucode grub efibootmgr git cmake qt5-wayland
    # genfstab -U /mnt >> /mnt/etc/fstab
    # arch-chroot /mnt
    # ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime
    # hwclock --systohc
    # vi /etc/locale.gen    # uncomment 'en_US.UTF-8 UTF-8'
    # locale-gen
    # echo "LANG=en_US.UTF-8" > /etc/locale.conf
    # echo "KEYMAP=en" > /etc/vconsole.conf
    # echo "deck" > /etc/hostname
    # echo -e "\n127.0.0.1    localhost\n::1    localhost\n127.0.1.1    deck" >> /etc/hosts
    # passwd
    # grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Arch
    # grub-mkconfig -o /boot/grub/grub.cfg
    # systemctl enable NetworkManager
    # useradd -m -G wheel <USER>
    # passwd <USER>
    # chmod u+w /etc/sudoers
    # vi /etc/sudoers       # Uncomment '%wheel ALL=(ALL) ALL'
    # chmod u-w /etc/sudoers
    # pacman -Syy
    # pacman -S xorg-server xf86-video-amdgpu maliit-keyboard qt5-wayland
    # su - <USER>
    ```

The password you choose when running the `passwd <USER>` command should be numeric if you want to use Plasma Mobile, as the unlock screen only allows you to enter a PIN.

## Graphical environment installation

Continuing from where we left off, that is, in the chroot session from the Arch Linux live installation system. We will now do this as a normal user (not root), so from now on, we will frequently use `sudo`.

Now we are going to install the graphical environments. I say this in plural because we will install two: Plasma and Plasma Mobile. I do this because, depending on whether we will use the Steam Deck with Arch in desktop mode (with keyboard/mouse and possibly a screen) or portable mode (without keyboard/mouse), one system or the other will be more convenient, as Plasma Mobile has an interface designed to be operated with a touchscreen (tablet-style).

Really, it's not necessary to install both desktops, so their installation steps are separated. You can install one, the other, or both.

#### Plasma

```bash
$ sudo pacman -S plasma-meta
```

During the installation of the above package, you will be asked several questions. On the third question, answer `2) noto-fonts`. For the rest, provide the default answer (by pressing enter).

#### Plasma Mobile

Plasma Mobile is not yet available in the official repositories. We have to use [AUR](https://aur.archlinux.org/):

1. Start by installing some dependencies:

    ```bash
    $ sudo pacman -S plasma-workspace kcontacts kirigami2 kpeople libphonenumber
    ```

2. Install the AUR packages `plasma-nano`, `plasma-settings`, and `plasma-mobile` in this order:

    ```bash
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-nano.git
    $ cd plasma-nano
    $ makepkg -si
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-settings.git
    $ cd plasma-settings
    $ makepkg -si
    $ cd ~
    $ git clone https://aur.archlinux.org/plasma-mobile.git
    $ cd plasma-mobile
    $ makepkg -si
    ```

#### End of graphical environment installation

1. Install the SDDM session manager and Konsole, which we'll need to finish the installation from the graphical mode:

    ```bash
    $ sudo pacman -S sddm konsole
    $ sudo systemctl enable sddm
    $ exit
    ```

2. Close the chroot session, unmount the partitions, and reboot the system:

    ```bash
    # exit
    # umount -R /mnt
    # reboot
    ```

## Basic configuration

After rebooting, you should see the SDDM session manager, initially with the screen rotated and without the ability to use the on-screen keyboard, so we'll still be using the external keyboard and mouse.

Once we have logged into Plasma or Plasma Mobile, the first thing we need to do is configure the internet connection. To do this, click on the corresponding icon in the system tray at the bottom right in Plasma or at the top right in Plasma Mobile.

Once connected, open the Konsole application and run the following commands to install the basic KDE application package, Firefox browser and the SSH server:

```bash
$ sudo pacman -S firefox kde-applications-meta openssh
$ sudo systemctl start sshd
$ sudo systemctl enable sshd
```

Finally, make the following two configurations to adjust the screen resolution (which initially scales things to appear larger) and the keyboard layout:

* Set the screen scale to 100% in `Preferences > System Settings > Display and Monitor > Scale`.
* Add the English keyboard layout in `Preferences > System Settings > Keyboard > Layouts > Configure Layouts > Add (English)`.

## SDDM configuration

Finally, we'll improve the SDDM session manager configuration to enable the on-screen keyboard, enhance the appearance, and display the screen in the correct orientation:

1. Create the file `/etc/sddm.conf.d/10-wayland.conf` with the following content:

    ```ini
    [General]
    DisplayServer=wayland
    GreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell

    [Wayland]
    CompositorCommand=kwin_wayland --drm --no-lockscreen --no-global-shortcuts --locale1 --inputmethod maliit-keyboard
    ```

2. Open `Preferences > Login Screen (SDDM)`, select Breeze as the theme, and click the `Apply Plasma settings...` button in the top right corner.

## Sound configuration

As [the Arch wiki mentions](https://wiki.archlinux.org/title/Steam_Deck#Audio), the default volume on the Steam Deck is very low. To fix this, you need to install the `alsa-utils` package and run the `alsamixer` command to adjust the volume of some of the channels.

```bash
$ sudo pacman -S alsa-utils
$ alsamixer
```

To access them, once in `alsamixer`, press `F6` to select the `acp5x` audio device, as by default the selected device is 0, which is associated with the HDMI output of the graphics chip:

![alsamixer](/images/posts/2024-09-04_steam_deck_arch/alsamixer-select-device.png)

Once the correct device is selected, you will see all its channels, which are quite numerous. Locate the ones [mentioned in the wiki](https://wiki.archlinux.org/title/Steam_Deck#Audio) and adjust them to the following values:

| Channel            | Value |
|:-------------------|------:|
| Analog PCM         |   85% |
| Digital            |   86% |
| Digital PCM        |   85% |
| Left Analog PCM    |   85% |
| Left Digital PCM   |   85% |
| Right Analog PCM   |   85% |
| Right Digital PCM  |   85% |

## Dual Boot manager installation

The Arch system is now ready and can be booted by starting the console in Boot Manager mode (holding down the volume- key) and selecting the `Arch` option. But to make it easier to boot SteamOS, we'll install a dual boot manager called [rEFInd](https://github.com/jlobue10/SteamDeck_rEFInd).

1. Boot SteamOS (with Volume- + Power).
2. From a terminal in desktop mode, run:

    ```bash
    cd $HOME && rm -rf $HOME/SteamDeck_rEFInd/ && git clone https://github.com/jlobue10/SteamDeck_rEFInd && cd SteamDeck_rEFInd && chmod +x install-GUI.sh && ./install-GUI.sh
    ```

3. Download or create an Arch Linux icon of 128x128px.
4. Open the desktop launcher found on the desktop.
5. Configure it as follows (select the icon downloaded or created earlier in the `Boot Option #2 Icon` field):

    ![rEFInd Configuration](/images/posts/2024-09-04_steam_deck_arch/rEFInd_conf.png)

6. Click the `Create Config` button.
7. Edit the file found at `~/.local/SteamDeck_rEFInd/GUI/refind.conf` and modify the last entry as follows:

    ```conf
    menuentry "Arch" {
        icon /EFI/refind/os_icon2.png
        loader /EFI/Arch/grubx64.efi
        graphics on
    }
    ```

8. Click the `Install rEFInd` button.
9. Click the `Install Config` button.

The path `/EFI/Arch/grubx64.efi` in step 6 may change if you chose a different identifier than `Arch` during the `grub-install` command executed during the [base system installation](#base-installation). In that case, you'll need to adapt the path.

## Conclusion

And that's it. Now we have an Arch Linux system on our Steam Deck with a dual boot manager that allows us to boot into SteamOS as well. From here, we have a machine with a dual nature, one (SteamOS) for gaming and another (Arch) to be used as a PC (Plasma) or tablet PC (Plasma Mobile).

To choose between the normal Plasma or Plasma Mobile graphical environment, use the dropdown menu that appears at the bottom left in the SDDM login manager.

<iframe width="688" height="387" src="https://www.youtube.com/embed/hColcI3rv38" title="Arch Linux on Steam Deck" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Some interesting links consulted during the creation of this guide:

* [The Arch Linux Handbook – Learn Arch Linux for Beginners](https://www.freecodecamp.org/news/how-to-install-arch-linux/)
* [Instalando Arch Linux con KDE en Steam Deck](https://asgardius.company/?p=1783)
* [Steam Deck - ArchWiki](https://wiki.archlinux.org/title/Steam_Deck)