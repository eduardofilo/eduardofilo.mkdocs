---
layout: default
permalink: /retro-emulacion/steam-deck.html
---

# Steam Deck

## Enlaces

* [Proton DB](https://www.protondb.com/): Lista los juegos compatibles con Steam Deck y ofrece soluciones para los que no lo son.
* [Decky](https://decky.xyz/): Plugins.

## Rutas interesantes sistema de archivos

|Ruta|Descripción|
|:---|:----------|
|`/run/media/`| Punto de montaje de las tarjetas SD.|

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