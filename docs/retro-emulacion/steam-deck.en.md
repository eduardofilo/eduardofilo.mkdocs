---
layout: default
permalink: /retro-emulacion/steam-deck.html
---

# Steam Deck

![Steam Deck](../images/pages/steam_deck/steam_deck.png)

## Links

* [Steam Deck Recovery Instructions](https://help.steampowered.com/en/faqs/view/1b71-edf2-eb6d-2bb3)
* [Proton DB](https://www.protondb.com/): Lists Steam Deck compatible games and offers solutions for those that are not.
* [NonSteamLaunchers](https://github.com/moraroy/NonSteamLaunchers-On-Steam-Deck): Installation of alternative launchers to Steam. Requires installing the Chrome browser from Discover so that some of the installed stores can be launched.
* Dual boot menus:
    * [SteamDeck_rEFInd](https://github.com/jlobue10/SteamDeck_rEFInd)
    * [SteamDeck-Clover-dualboot ](https://github.com/ryanrudolfoba/SteamDeck-Clover-dualboot)
* [Installing Arch Linux](../2024-09-04_steam_deck_arch.md)

## Boot modes

|Key combination|Description|
|:--------------|:----------|
|`Power`|Normal boot.|
|`Power` + `Volume+`|BIOS menu.|
|`Power` + `Volume-`|Boot menu.|
|`Power` + `⋯`|Bootloader menu.|
|`Power` + `Volume- + ⋯`|Reset UEFI settings. Press and hold both `Volume- + ⋯` buttons after the first blinking of the LED. The LED will blink during the operation and stop after it is finished, then release the buttons.|

## BIOS backup

The Steam Deck [does not have the BIOS settings in a CMOS memory maintained with a battery](https://steamdeckhq.com/news/undervolting-and-overclocking-push-your-steam-deck-beyond-its-limits/#comment-1995), but in a Winbond flash that if corrupted, the machine will not boot. It is important to make a backup as soon as possible in case there are problems in the future. The backup can be done with the following command from a terminal in desktop mode:

```bash
sudo /usr/share/jupiter_bios_updater/h2offt /home/deck/biosbkp.fd -O
```

Extract the resulting file to `/home/deck/biosbkp.fd` and save it in a safe place. The file contains elements particular to each console, so it is not useful to backup another console. That is why it is important to backup our unit.

## Interesting file system paths

|Path|Description|
|:---|:----------|
|`/run/media/`|SD card mounting point.|
|`/home/deck/.steam/steam/`|Steam directory.|
|`/home/deck/.steam/steam/steamapps/compatdata`|Directory of the installed games/applications where the sandbox is created with the Windows file structure for them.|
|`/home/deck/.steam/steam/steamapps/common`|Directory of installed games.|

## Interesting applications

#### Steam Store

* `Proton BattlEye Runtime`: Makes the BattlEye system used by some games accessible to Linux.
* `Proton Easy Anti-Cheat Runtime`: Makes Epic's Easy Anti-Cheat system accessible to Linux games.
* `Proton Experimental`: Latest (non-stable) version of Proton.

#### Discover

* `ProtonUp-Qt`: To install different versions of Proton GE.
* `Heroic Games Launcher`: Opensource alternative to Epic Games store, GOG and Amazon Prime Games Launcher.
* `Lutris`: Retro games and emulators installer.
* `Mount Unmount ISO`: Mount and unmount ISO images from Dolphin file explorer.
* `PeaZip`: File compressor and decompressor.

## Interesting plugins

We need to have [Decky](https://decky.xyz/) installed.

* `AutoFlatpaks`: Notifies and allows you to update packages that are normally updated from desktop mode.
* `Bluetooth`: Bluetooth device management that would normally be done from desktop mode.
* `Battery Tracker`: Battery information for both Steam Deck and linked controllers.
* `CSS Loader`: Change themes in Steam UI.
* `EmuDecky`: Official EmuDeck plugin to make quick adjustments to emulators.
* `Fantastic`: Change the fan curve.
* `Free Loader`: Displays when free games appear in some of the stores.
* `Game Theme Music`: Allows you to listen to the music of the games in the game tab of the Steam library.
* `HLTB for Deck`: Displays the duration of the games.
* `PlayTime`: Displays the time played in non-Steam games.
* `ProtonDB Badges`: Shows the compatibility of games with Steam Deck according to [ProtonDB](https://www.protondb.com/).
* `SteamGridDB`: To be able to change the covers and artwork of games in the Steam library.
* `Storage Cleaner`: Cleaning of residual files.

## Enable SSH

1. Open `Konsole` in desktop mode.
2. Change the password of the `deck` user:

    ```bash
    passwd
    ```

3. Enable SSHD:

    ```bash
    sudo systemctl start sshd
    ```

4. Enable SSHD at startup:

    ```bash
    sudo systemctl enable sshd
    ```

## Install any Windows application

Once we have the installer (.exe or .msi):

1. Open Steam application from desktop mode.
2. Click the `+ Add a product` button at the bottom left.
3. Select `Add a non-Steam program...`.
4. Click `Search...` at the bottom left in the window that appears.
5. Select the executable of the program you want to install (if the executable is not `.exe` change the filter to `All files`).
6. Click `Add selected`.
7. Select the program in the Steam library (under `Uncategorized`), click the gear icon (`Manage`) and select `Properties...` from the dropdown.
8. Select the `Compatibility` group of options and force the use of the last version of Proton GE that we have available (for this we must have previously installed `ProtonUp-Qt` from the `Discover` store and have installed some version of Proton GE).
9. Click on `Play`.
10. It will start the installer whose assistant we will follow as if we were in Windows.
11. When it finishes and the installer closes, we will see that the `Play` button in Steam is activated again.
12. We erase the executable of the route where we had it.
13. What we have just installed will have finished in the same sandbox that has been created with the steps 1 to 8. If we eliminated the entry in the library, everything would be lost, therefore we must modify the launcher of the installer so that it behaves like the launcher of what we have installed. To do this open the file explorer and go to the path `/home/deck/.steam/steam/steamapps/compatdata`. There we will find the folders of the installed games/applications. We find out the folder with the identifier corresponding to the installation that we have just done (for example helping us with the dates of creation of the folders). Inside this folder we will look for the launching of what we have just installed (it can be a `.exe` or a `.lnk` that appears in the Windows desktop or in the start menu).
14. We should still have in front the entry corresponding to the installer in the Steam library, if not select it.
15. Click the gear icon (`Manage`) and select `Properties...` from the drop-down menu.
16. Change the Shortcut name and the `Destination` and `Start at` entries to the paths we found out in step 13.
17. Change the game art to look better in the Steam library (for this we must have installed [`Decky`](#plugins-interesting) and the `SteamGridDB` plugin).

## Dependency solution in Windows games with Proton

If a game does not start because of a missing dependency, we can install it and then link it to the game launcher in the following way. We are going to see it for example with the `Microsoft Windows C++ Runtime`:

1. Search for the dependency. In the case of the `Micrsoft Windows C++ Runtime` we can download it from [this page](https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist).
2. We create a launcher in Steam for the installer of the dependency using steps 1 to 8 of [previous section](#install-any-windows-application) (do not forget to select ProtonGE as compatibility tool).
3. We open the launcher to install the dependency.
4. We find out the folder with the identifier corresponding to the installation that we have just made inside the directory `/home/deck/.steam/steam/steamapps/compatdata` (for example helping us with the dates of creation of the folders). We imagine for the example that the path where the dependency has ended up installed is `/home/deck/.steam/steam/steam/steamapps/compatdata/12345678/`.
5. Delete the launcher created in step 2.
6. Select the game in the Steam library that requires the dependency, click the gear icon (`Manage`) and select `Properties...` from the drop-down.
7. In the `Direct Access` section, in the `Launch Parameters` field, enter the following (changing the path to the appropriate path):

    ```bash
    STEAM_COMPAT_DATA_PATH="/home/deck/.steam/steam/steamapps/compatdata/12345678" %command%
    ```

8. Close the Properties window and click `Play`.

In case a game requires several dependencies, we can incorporate as many `STEAM_COMPAT_DATA_PATH` entries as needed separated by a space.

## EmuDeck

#### Links

* [EmuDeck](https://emudeck.com/)
* [EmuDeck Wiki](https://emudeck.github.io/)
* [BIOS and ROMs Cheat Sheet](https://emudeck.github.io/cheat-sheet/)
