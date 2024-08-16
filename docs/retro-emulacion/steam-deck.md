---
layout: default
permalink: /retro-emulacion/steam-deck.html
---

# Steam Deck

![Steam Deck](/images/pages/steam_deck/steam_deck.png)

## Enlaces

* [Steam Deck Recovery Instructions](https://help.steampowered.com/en/faqs/view/1b71-edf2-eb6d-2bb3)
* [Proton DB](https://www.protondb.com/): Lista los juegos compatibles con Steam Deck y ofrece soluciones para los que no lo son.
* [NonSteamLaunchers](https://github.com/moraroy/NonSteamLaunchers-On-Steam-Deck): Instalación de launchers alternativos a Steam. Requiere instalar el navegador Chrome desde Discover para que luego se puedan lanzar algunas de las tiendas instaladas.
* Dual boot menus:
    * [SteamDeck_rEFInd](https://github.com/jlobue10/SteamDeck_rEFInd)
    * [SteamDeck-Clover-dualboot ](https://github.com/ryanrudolfoba/SteamDeck-Clover-dualboot)

## Modos arranque

|Combinación teclas|Descripción|
|:-----------------|:----------|
|`Power`|Arranque normal.|
|`Power` + `Volume+`|Arranque en modo BIOS.|
|`Power` + `Volume-`|Boot menú.|
|`Power` + `⋯`|Bootloader menú.|
|`Power` + `Volume- + ⋯`|Reset de ajustes UEFI. Mantener pulsados los dos botones `Volume- + ⋯` tras el primer parpadeo del LED. El LED parpadeará durante la operación y se detendrá una vez finalizada, entonces soltar los botones|

## Backup de la BIOS

La Steam Deck [no tiene los ajustes de la BIOS en una memoria CMOS mantenida con una pila](https://steamdeckhq.com/news/undervolting-and-overclocking-push-your-steam-deck-beyond-its-limits/#comment-1995), sino en una flash Winbond que si se corrompe, la máquina no arrancará. Interesa hacer un backup cuanto antes por si hubiera problemas en el futuro. El backup puede hacerse con el siguiente comando desde un terminal en el modo escritorio:

```bash
sudo /usr/share/jupiter_bios_updater/h2offt /home/deck/biosbkp.fd -O
```

Extraeremos el fichero resultante en `/home/deck/biosbkp.fd` y lo guardaremos en un lugar seguro. El fichero contiene elementos particulares de cada consola, por lo que no sirve el backup de otra consola. Por eso es importante hacer backup en nuestra unidad.

## Rutas interesantes sistema de archivos

|Ruta|Descripción|
|:---|:----------|
|`/run/media/`|Punto de montaje de las tarjetas SD.|
|`/home/deck/.steam/steam/`|Directorio de Steam.|
|`/home/deck/.steam/steam/steamapps/compatdata`|Directorio de los juegos/aplicaciones instalados donde se crea el sandbox con la estructura de ficheros de Windows para ellos.|
|`/home/deck/.steam/steam/steamapps/common`|Directorio de los juegos instalados.|

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

## Plugins interesantes

Necesitamos tener instalado [Decky](https://decky.xyz/).

* `AutoFlatpaks`: Notifica y permite actualizar paquetes que normalmente se actualizan desde el modo escritorio.
* `Bluetooth`: Gestión de disposivos Bluetooth que normalmente se haría desde el modo escritorio.
* `Battery Tracker`: Información sobre las baterías tanto de Steam Deck como de los controladores vinculados.
* `CSS Loader`: Cambiar themes en Steam UI.
* `EmuDecky`: Plugin oficial de EmuDeck para hacer ajustes rápidos en los emuladores.
* `Fantastic`: Cambiar la curva del ventilador.
* `Free Loader`: Muestra cuando aparecen juegos gratuitos en algunas de las tiendas.
* `Game Theme Music`: Permite escuchar la música de los juegos en la ficha del juego de la biblioteca de Steam.
* `HLTB for Deck`: Muestra la duración de los juegos.
* `PlayTime`: Muestra el tiempo jugado en juegos que no son de Steam.
* `ProtonDB Badges`: Muestra la compatibilidad de los juegos con Steam Deck según [ProtonDB](https://www.protondb.com/).
* `SteamGridDB`: Para poder cambiar las portadas y el arte de los juegos en la biblioteca de Steam.
* `Storage Cleaner`: Limpieza de archivos residuales.

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
13. Lo que acabamos de instalar habrá terminado en el mismo sandbox que se ha creado con los pasos 1 a 8. Si elimináramos la entrada en la biblioteca, se perdería todo, por tanto debemos modificar el lanzador del instalador para que se comporte como el lanzador de lo que hemos instalado. Para ello abrir el explorador de archivos y acudir a la ruta `/home/deck/.steam/steam/steamapps/compatdata`. Allí encontraremos las carpetas de los juegos/aplicaciones instalados. Averiguamos la carpeta con el identificador correspondiente a la instalación que acabamos de hacer (por ejemplo ayudándonos de las fechas de creación de las carpetas). Dentro de dicha carpeta buscaremos el lanzado de lo que acabamos de instalar (puede ser un `.exe` o un `.lnk` que aparezca en el escritorio de Windows o en el menú inicio).
14. Deberíamos seguir teniendo delante la entrada correspondiente al instalador en la biblioteca de Steam, si no seleccionarla.
15. Pulsar el icono de rueda dentada (`Administrar`) y seleccionar `Propiedades...` en el desplegable.
16. Cambiar el nombre del Acceso directo y las entradas `Destino` y `Iniciar en` por las rutas que hemos averiguado en el paso 13.
17. Cambiar el arte del juego para que tenga un mejor aspecto en la biblioteca de Steam (para ello deberemos tener instalado [`Decky`](#plugins-interesantes) y el plugin `SteamGridDB`)

## Solución de dependencias en juegos Windows con Proton

Si un juego no arranca por falta de alguna dependencia, podemos instalarla y luego vincularla al lanzador del juego de la siguiente forma. Vamos a verlo por ejemplo con el `Microsoft Windows C++ Runtime`:

1. Buscar la dependencia. En el caso del `Micrsoft Windows C++ Runtime` podemos descargarlo de [esta página](https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist).
2. Creamos un lanzador en Steam para el instalador de la dependencia utilizando los pasos 1 a 8 del [apartado anterior](#instalar-cualquier-aplicacion-windows) (no olvidar seleccionar ProtonGE como herramienta de compatibilidad).
3. Abrimos el lanzador para instalar la dependencia.
4. Averiguamos la carpeta con el identificador correspondiente a la instalación que acabamos de hacer dentro del directorio `/home/deck/.steam/steam/steamapps/compatdata` (por ejemplo ayudándonos de las fechas de creación de las carpetas). Imaginamos para el ejemplo que la ruta donde ha terminado instalada la dependencia es `/home/deck/.steam/steam/steamapps/compatdata/12345678/`
5. Borrar el lanzador creado en el paso 2.
6. Seleccionar el juego en la biblioteca de Steam que requiera la dependencia, pulsar el icono de rueda dentada (`Administrar`) y seleccionar `Propiedades...` en el desplegable.
7. En la sección `Acceso directo`, en el campo `Parámetros de lanzamiento`, introducir lo siguiente (cambiando la ruta por la que corresponda):

    ```bash
    STEAM_COMPAT_DATA_PATH="/home/deck/.steam/steam/steamapps/compatdata/12345678" %command%
    ```

8. Cerrar la ventana de Propiedades y pulsar `Jugar`.

En caso de que un juego requiriera varias dependencias, podemos incorporar tantas entradas `STEAM_COMPAT_DATA_PATH` como sean necesarias separadas por un espacio.

[Tutorial en vídeo de @Hooandee](https://www.youtube.com/watch?v=WBjUcVzknQg)

## EmuDeck

#### Enlaces

* [EmuDeck](https://emudeck.com/)
* [EmuDeck Wiki](https://emudeck.github.io/)
* [BIOS and ROMs Cheat Sheet](https://emudeck.github.io/cheat-sheet/)
* [Tutorial vídeo instalación de @Hooandee](https://www.youtube.com/watch?v=N6BGOOLV7-Y)

## Videotutorial general de @Hooandee

<iframe width="531" height="298" src="https://www.youtube.com/embed/GHwpTh-cReE" title="¡El tutorial más completo DEL MUNDO para STEAM DECK! De CERO a EXPERTO 2024 ❤️‍🔥" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>