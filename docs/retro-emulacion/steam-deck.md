---
layout: default
permalink: /retro-emulacion/steam-deck.html
---

# Steam Deck

## Enlaces

* [Proton DB](https://www.protondb.com/): Lista los juegos compatibles con Steam Deck y ofrece soluciones para los que no lo son.
* [Decky](https://decky.xyz/): Plugins.

## Rutas interesantes sistema de archivos

* `/home/steam/.local/share/Steam/steamapps/compatdata/`: Juegos instalados.
* `/home/steam/.local/share/Steam/steamapps/common/`: Juegos instalados.
* `/home/steam/.local/share/Steam/steamapps/`: Juegos instalados.
* `/home/steam/.local/share/Steam/`: Configuración de Steam.
* `/home/steam/.steam/`: Configuración de Steam.
* `/home/steam/.config/`: Configuración de aplicaciones.
* `/home/steam/.local/share/`: Configuración de aplicaciones.
* `/home/steam/.local/share/Steam/steamapps/compatdata/`: Juegos instalados.

## Activar SSH

1. Abrir `Konsole` en modo escritorio.
2. Cambiar la contraseña del usuario `deck`:

    ```bash
    passwd
    ```

3. Habilitar SSHD:

    ```bash
    sudo systemctl start sshd
    ```

4. Habilitar SSHD en el arranque:

    ```bash
    sudo systemctl enable sshd
    ```

## EmuDeck

#### Enlaces

* [EmuDeck](https://emudeck.com/)
* [EmuDeck Wiki](https://emudeck.github.io/)
* [Tutorial vídeo instalación](https://www.youtube.com/watch?v=N6BGOOLV7-Y)