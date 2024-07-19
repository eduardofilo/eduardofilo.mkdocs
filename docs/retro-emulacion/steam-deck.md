---
layout: default
permalink: /retro-emulacion/steam-deck.html
---

# Steam Deck

![Steam Deck](/images/pages/steam_deck/steam_deck.png)

## Enlaces

* [Proton DB](https://www.protondb.com/): Lista los juegos compatibles con Steam Deck y ofrece soluciones para los que no lo son.
* [Decky](https://decky.xyz/): Plugins.
* [NonSteamLaunchers](https://github.com/moraroy/NonSteamLaunchers-On-Steam-Deck): Instalación de launchers alternativos a Steam. Requiere instalar el navegador Chrome desde Discover para que luego se puedan lanzar algunas de las tiendas instaladas.

## Rutas interesantes sistema de archivos

|Ruta|Descripción|
|:---|:----------|
|`/run/media/`|Punto de montaje de las tarjetas SD.|
|`/home/deck/.steam/steam/`|Directorio de Steam.|
|`/home/deck/.steam/steam/steamapps/compatdata`|Directorio de los juegos/aplicaciones instalados donde se crea el sandbox con la estructura de ficheros de Windows para ellos.|

## Aplicaciones interesantes

#### Steam Store

* `Proton BattlEye Runtime`: Soluciona restricciones de ejecución de algunos juegos (zona por ejemplo).
* `Proton Easy Anti-Cheat Runtime`: Soluciona restricciones de ejecución de algunos juegos (zona por ejemplo).
* `Proton Experimental`: Última versión (no estable) de Proton.

#### Discover

* `ProtonUp-Qt`: Para instalar distintas versiones de Proton GE.
* `Heroic Games Launcher`: Alternativa opensource a la tienda de Epic Games, GOG y Amazon Prime Games Launcher.
* `Lutris`: Instalador de juegos retro y emuladores.
* `Mount Unmount ISO`: Monta y desmonta imágenes ISO desde el explorador de archivos Dolphin.
* `PeaZip`: Compresor y descompresor de archivos.

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

## Instalar cualquier aplicación Windows

Una vez que tengamos el instalador (.exe o .msi):

1. Abrir Steam desde el escritorio.
2. Pulsar el botón `+ Añadir un producto` en la parte inferior izquierda.
3. Seleccionar `Añadir un programa que no es de Steam...`.
4. Pulsar `Buscar...` abajo a la izquierda en la ventana que aparece.
5. Seleccionar el ejecutable del programa que se quiere instalar (si el ejecutable no es `.exe` cambiar el filtro a `Todos los archivos`).
6. Pulsar `Añadir seleccionados`.
7. Seleccionar el programa en la biblioteca de Steam (en `Sin categoría`), pulsar el icono de rueda dentada (`Administrar`) y seleccionar `Propiedades...` en el desplegable.
8. Seleccionar el grupo de opciones `Compatibilidad` y forzar el uso de la última versión de Proton GE que tengamos disponible (para ello previamente deberemos haber instalado `ProtonUp-Qt` desde la tienda `Discover` y haber instalado alguna versión de Proton GE).
9. Pulsar `Jugar`.
10. Arrancará el instalador cuyo asistente seguiremos como si nos encontráramos en Windows.
11. Cuando termine y se cierre el instalador, veremos que vuelve a activarse el botón `Jugar` en Steam.
12. Borramos el ejecutable de la ruta donde lo tuviéramos.
13. Lo que acabamos de instalar habrá terminado en el mismo sandbox que se ha creado con los pasos 2 a 6. Si elimináramos la entrada en la biblioteca, se perdería todo, por tanto debemos modificar el lanzador del instalador para que se comporte como el lanzador de lo que hemos instalado. Para ello abrir el explorador de archivos y acudir a la ruta `/home/deck/.steam/steam/steamapps/compatdata`. Allí encontraremos las carpetas de los juegos/aplicaciones instalados. Averiguamos la carpeta con el identificador correspondiente a la instalación que acabamos de hacer (por ejemplo ayudándonos de las fechas de creación de las carpetas). Dentro de dicha carpeta buscaremos el lanzado de lo que acabamos de instalar (puede ser un `.exe` o un `.lnk` que aparezca en el escritorio de Windows o en el menú inicio).
14. Deberíamos seguir teniendo delante la entrada correspondiente al instalador en la biblioteca de Steam, si no seleccionarla.
15. Pulsar el icono de rueda dentada (`Administrar`) y seleccionar `Propiedades...` en el desplegable.
16. Cambiar el nombre del Acceso directo y las entradas `Destino` y `Iniciar en` por las rutas que hemos averiguado en el paso 13.

## EmuDeck

#### Enlaces

* [EmuDeck](https://emudeck.com/)
* [EmuDeck Wiki](https://emudeck.github.io/)
* [Tutorial vídeo instalación](https://www.youtube.com/watch?v=N6BGOOLV7-Y)

<iframe width="640" height="480" src="https://www.youtube.com/watch?v=GHwpTh-cReE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>