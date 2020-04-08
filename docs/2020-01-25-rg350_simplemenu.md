title: 2020-01-25 RG350 SimpleMenu
summary: Instalación y configuración de SimpleMenu en RG350.
date: 2020-01-25 17:25:00

![SimpleMenu](/images/posts/simplemenu.png)

!!! Info "Actualización 2020-04-08"
    Se modifica el artículo para que las instrucciones correspondan con la nueva [versión 4.5](https://github.com/fgl82/simplemenu/releases/tag/4.5).

Se ilustra a continuación el proceso de instalación y configuración del launcher [SimpleMenu](https://github.com/fgl82/simplemenu) para RG350.

## Instalación

La instalación consiste únicamente en copiar el [OPK](https://github.com/fgl82/simplemenu/releases/download/4.5/SimpleMenu-RG-350.opk) que ofrece su autor a una de las dos rutas que lee Gmenu2x para mostrar el lanzador, es decir:

* Tarjeta interna: `/media/data/apps`
* Tarjeta externa: `/media/sdcard/apps`

Tras hacerlo aparece el lanzador en la sección `applications` de GMenu2X. Si lo abrimos en este momento, seguramente veremos que no reconoce los emuladores y/o ROMs que tengamos instalados. Esto es normal puesto que todavía no hemos adaptado la configuración:

![SimpleMenu Launching1](/images/posts/simplemenu_launching1.png)
![SimpleMenu Launching2](/images/posts/simplemenu_launching2.png)

## Configuración

!!! Warning "Aviso"
    Las tres últimas versiones del programa han modificado el formato de los ficheros de configuración, por lo que si contábamos con una instalación de las versiones previas (2 ó 3) nos va a tocar adaptarlos, es decir no se pueden utilizar directamente ya que no son compatibles. Lo mejor será renombrar el directorio `/media/data/local/home/.simplemenu` para que se vuelva a generar en el siguiente arranque y así además mantener copia de la configuración anterior para que nos sirva de modelo para crear la nueva.

    Entre la versión 4.1 y la 4.2 ha habido un cambio importante en la gestión del tema gráfico.

    Entre la versión 4.2 y la 4.5 el cambio ha sido en la división del fichero `sections.ini` en varios para agrupar las distintas máquinas por tipos.

De serie SimpleMenu trae una configuración con varios sistemas precargados, pero como apunta de forma estática a las rutas de los distintos emuladores y ROMs, es casi seguro que nos va a tocar ajustar esta configuración a los que nosotros tengamos instalados en la consola. Aún así interesa que lo ejecutemos al menos una vez para que se genere el directorio `.simplemenu` dentro del home de la consola para que tengamos la plantilla sobre la que empezar a modificar.

#### Sistemas

Los ficheros clave son los que se encuentran en la ruta `/media/data/local/home/.simplemenu/section_groups`. Allí encontramos los siguientes ficheros (una vez que hayamos ejecutado SimpleMenu al menos una vez):

```
RG350:/media/data/local/home/.simplemenu/section_groups # ls -l
-rw-r--r--    1 root     root           235 Jan 28 17:35 apps and games.ini
-rw-r--r--    1 root     root         10716 Jan 28 17:35 apps and games.png
-rw-r--r--    1 root     root           936 Jan 28 17:35 arcades.ini
-rw-r--r--    1 root     root         14746 Jan 28 17:35 arcades.png
-rw-r--r--    1 root     root          1889 Jan 28 17:35 consoles.ini
-rw-r--r--    1 root     root         19669 Jan 28 17:35 consoles.png
-rw-r--r--    1 root     root          1188 Jan 28 17:35 handhelds.ini
-rw-r--r--    1 root     root          8626 Jan 28 17:35 handhelds.png
-rw-r--r--    1 root     root           949 Jan 28 17:35 home computers.ini
-rw-r--r--    1 root     root         17383 Jan 28 17:35 home computers.png
```

Como vemos hay una imagen y un fichero `.ini` para 5 tipos de máquinas. Esta agrupación es flexible, es decir, podemos ampliar o reducir el número de tipos a nuestro gusto. El fichero de imagen tiene que llamarse exactamente igual que el de configuración. Será lo que se vea en la pantalla al seleccionar el tipo correspondiente.

A no ser que seamos expertos con el editor `vi` que podemos ejecutar por SSH, lo mejor será transferir los ficheros al ordenador de alguna manera (pasándolos a la tarjeta externa con DinguxCmdr si no se conoce otra forma más directa) y editarlos allí con un editor que soporte los retornos de carro y la codificación utilizada habitualmente en sistemas Linux (como [Notepad++](https://notepad-plus-plus.org/)).

A partir de aquí nos vamos a centrar en el tipo `handhelds` para seguir la explicación, pero todo lo que digamos se puede aplicar exactamente igual a cualquiera de los otros tipos.

En el fichero `handhelds.ini` tenemos al principio la lista de sistemas en la propiedad `consoleList` del apartado `[CONSOLES]`. En esta propiedad se van añadiendo los distintos sistemas que definiremos a continuación, separados por comas. Podemos *seleccionar* un subconjunto de los sistemas definidos más abajo, es decir, podemos ocultar algunos simplemente no incluyéndolos en `consoleList`.

```
[CONSOLES]
consoleList =GAME BOY,GAME BOY COLOR,GAME BOY ADVANCE,GAME & WATCH,GAME GEAR,NEO GEO POCKET,WONDERSWAN,LYNX
```

Luego por cada sistema tenemos un bloque como el siguiente:

```
[GAME BOY]
execs = /media/data/apps/gambatte-multi-r572u4-20200127.opk
romDirs = /media/data/roms/GB/
romExts = .gb,.gz,.zip
```

El formato del archivo es el que se utiliza habitualmente para los ficheros de configuración tipo [INI](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)). El significado de los parámetros es:

* `execs`: OPKs de los emuladores del sistema con sus rutas, separados por comas.
* `romDirs`: Directorios donde se encuentran las ROMs de este sistema, separados por comas.
* `romExts`: Extensiones de los ficheros que se incluirán en el listado de ROMs, separadas por comas.

Una vez que devolvamos los ficheros de configuración a su lugar en `/media/data/local/home/.simplemenu/section_groups`, ya podremos tratar de ejecutarlo para comprobar si ha cargado bien los sistemas y previews de las ROMs. Al menos en mi caso lo que me encuentro en este momento es:

![SimpleMenu First Launch](/images/posts/simplemenu_first_launch.png)

Como vemos en la definición de los parámetros, ahora puede haber varios emuladores y varios directorios de ROMs en cada sistema. En el primer caso podremos elegir el emulador a utilizar pulsando `Start` cuando esté seleccionada la ROM que queremos emular. Por ejemplo, tras añadir el emulador GPSP a la configuración de GBA podemos ver lo siguiente al pulsar `Start` en el listado de ROMs de GBA:

![SimpleMenu GBA1](/images/posts/simplemenu_gba1.png)
![SimpleMenu GBA2](/images/posts/simplemenu_gba2.png)

En caso de que necesitemos volver a Gmenu2x, podremos encontrarlo en la sección APPS:

![SimpleMenu 5](/images/posts/simplemenu_gmenu2x.png)

Como punto de partida dejo aquí mis ficheros de configuración que contienen la mayoría de los emuladores y la [estructura de directorios para las ROMs](/retro-emulacion/rg-350.html#las-roms-y-su-organizacion) que se utilizan habitualmente.

* [simplemenu.zip](/files/posts/simplemenu.zip)

!!! Note "Nota"
    A partir de la versión 4.2, SimpleMenu es mucho más robusto respecto a defectos o carencias en la configuración tanto de los sistemas como del tema, por lo que arrancará siempre. Cuando por ejemplo no exista correspondencia de un sistema en el tema, nos mostrará el nombre del mismo en lugar de un logotipo, lo que nos servirá como indicación de que debemos incorporarlo nosotros.

#### Configuración general

Dentro de `/media/data/local/home/.simplemenu` hay otro fichero que nos interesa modificar. Se trata del `config.ini`. Su contenido es el siguiente por defecto:

```
[GENERAL]
media_folder = media
theme = default

[FULLSCREEN_MODE]
display_footer = 0
display_menu = 1

[SYSTEM]
screen_timeout_in_seconds = 30
allow_shutdown = 0

[CPU]
underclocked_speed = 408
normal_speed = 702
overclocked_speed = 732
sleep_speed = 200
```

Los parámetros dentro del grupo `[CPU]` son ignorados en RG350 (en principio son para modificar las frecuencias del procesador). El resto de parámetros sí los podemos modificar. Su significado es el siguiente:

* `media_folder`: Directorio donde se buscan las previsualizaciones de las ROMs. Interesa cambiar este valor del `media` que viene por defecto a `.previews` para que sea compatible con la ruta utilizada por Gmenu2x.
* `theme`: A partir de la versión 4.2 se pueden incorporar varios temas (en distintos directorios dentro de `/media/data/local/home/.simplemenu/themes`) que luego se pueden seleccionar mediante este parámetro.
* `display_footer`: Muestra el nombre de la ROM cuando estamos en modo preview (0=No; 1=Sí).
* `display_menu`: Muestra la lista de ROMs de una sección cuando nos desplazamos entre las ROMs en modo preview (0=No; 1=Sí).
* `screen_timeout_in_seconds`: Número de segundos a partir del cual salta el salvapantallas. Cuando éste entre, la forma de salir es pulsar cualquier botón.
* `allow_shutdown`: Si tiene el valor `1` hace que al pulsar `Start+Select` la consola se apague. Si tiene el valor `0` simplemente se cierra SimpleMenu.

## Manejo

Como hemos visto durante la configuración, a partir de la versión 4.5 se pueden definir varios grupos de máquinas. Por defecto existen 5 grupos definidos por tipo de máquinas. Entramos en el modo de selección de un grupo pulsando `B`. En ese momento vemos por ejemplo:

![SimpleMenu Group](/images/posts/simplemenu_group.png)

En esta situación cambiamos de grupo pulsando `Arriba` y `Abajo` en la cruceta, y entramos en el grupo pulsando `A`.

## Arranque

Tenemos dos opciones para utilizar este lanzador, convertirlo en el lanzador predeterminado o abrirlo desde Gmenu2x. Vamos a ver cómo configurar las dos situaciones:

!!! Warning "Aviso"
    Si optamos por la opción de configurar SimpleMenu como lanzador predeterminado, es conveniente que también configuremos el parámetro `allow_shutdown` a 1, ya que si lo dejamos a 0 al pulsar `Select + Start` sólo conseguiremos reiniciar SimpleMenu.

#### Como lanzador predeterminado

1. Bajar el fichero siguiente de la lista de assets de la release:
	* [frontend_start](https://github.com/fgl82/simplemenu/releases/download/4.5/frontend_start)
2. Copiarlo a la raíz de la microSD externa.
3. Montar la microSD externa en la RG350 y arrancar. La ruta del fichero se encuentra en `/media/sdcard/frontend_start`.
4. Copiar el fichero `frontend_start` a la ruta `/media/data/local/sbin`:

	![SimpleMenu 3](/images/posts/simplemenu_screenshot003.png)

5. Hacer ejecutable el fichero instalado. Desafortunadamente DinguxCmdr no nos ayuda en este caso. Tendremos que ejecutar el siguiente comando desde consola, ya sea por SSH o utilizando una aplicación de terminal como `ST-SDL`:

	```
	# chmod +x /media/data/local/sbin/frontend_start
	```

#### Desde Gmenu2x

Simplemente abriremos el lanzador que encontraremos en la sección `applications` de GMenu2X:

![SimpleMenu Launching1](/images/posts/simplemenu_launching1.png)

## Previews

SimpleMenu soporta previsualización de las ROMs. Para que aparezcan hay que hacer dos cosas:

1. Colocar las imágenes con el mismo nombre que las ROMs pero con extensión `.png` en un directorio al mismo nivel que las ROMs cuyo nombre se corresponda con el definido en el parámetro `media_folder` del fichero de configuración `config.ini`. Inicialmente este nombre es `media`. Por ejemplo la previsualización de la ROM `/media/sdcard/roms/GB/DKLAND.gb` iría en `/media/sdcard/roms/GB/media/DKLAND.png`.
2. Activar la visualización de las miniaturas. Para ello hay que pulsar la tecla `Y`. Volviéndola a pulsar volvemos al listado normal.

Como hemos comentado en el apartado de [Configuración general](#configuracion-general), podemos modificar el directorio que se utiliza de forma predeterminada (`media`) por el `.previews` que utiliza Gmenu2x para así hacerlos compatibles y no tener que duplicar las previsualizaciones.

El resultado:

<iframe width="853" height="480" src="https://www.youtube.com/embed/CcW0NGFRTCg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Controles

La página de documentación de controles es [ésta](https://github.com/fgl82/simplemenu/wiki/Controls), pero resulta un poco confusa porque mezcla varias máquinas, por lo que se listan a continuación de forma explícita los controles para RG350:

|Shortcut|Modo|Función|
|:-------|:---|:------|
|`R1` / `L1`|Listado de ROMs|Cambia de sistema desde la lista de ROMs. Si está activada la previsualización de las ROMs, se mostrará el logotipo del sistema durante un segundo|
|`Arriba` / `Abajo`|Listado de ROMs|Selecciona la ROM anterior/siguiente|
|`Izquierda` / `Derercha`|Listado de ROMs|Avanza 10 ROMs anteriores/siguientes|
|`B+Izquierda` / `B+Derecha`|Listado de ROMs|Cambia de sistema mostrando el logotipo de los sistemas|
|`B+Arriba` / `B+Abajo`|Listado de ROMs|Pasa a la letra anterior/siguiente|
|`Y`|Listado de ROMs|Activa/desactiva la previsualización de las ROMs|
|`A`|Listado de ROMs|Lanza la ROM seleccionada|
|`B+Select`|Listado de ROMs|Lanza una ROM aleatoria|
|`Select`|Listado de ROMs|Limpia los nombres de las ROMs retirando las variantes indicadas entre paréntesis|
|`Select+Start`|Listado de ROMs|Apaga la consola o cierra SimpleMenu (dependiendo del parámetro `allow_shutdown` en `config.ini`)|
|`X`|Listado de ROMs|Añade la ROM seleccionada a Favoritos|
|`L2`|Listado de ROMs|Entra en la lista de Favoritos|
|`X`|Listado de Favoritos|Borra la ROM seleccionada de Favoritos|
|`L2`|Listado de Favoritos|Sale de la lista de Favoritos|
|`B`|Listado de ROMs|Sube al nivel de seleción de grupos|
|`A`|Listado de grupos|Entra en el grupo seleccionado|
