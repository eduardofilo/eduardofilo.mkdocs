---
layout: default
permalink: /retro-emulacion/zx-uno.html
---

# ZX-Uno

## Enlaces

* [ZX-Uno [Clon de ordenador ZX Spectrum basado en FPGA]](http://zxuno.speccy.org/)
* [Verkami: ZX-UNO](http://www.verkami.com/projects/14074-zx-uno)
* [Verkami: ZX-box](https://www.verkami.com/projects/14684-zx-box)
* [ZX-Uno case, a Sinclair ZX Spectrum clone](http://www.thingiverse.com/thing:594804): Carcasa de Mejias3D para ZX-Uno oficial.
* [ZX-Uno FAQ by @uto_dev](http://www.ngpaws.com/zxunofaq.html)
* [INSTRUCCIONES PARA ACTUALIZAR LOS ZX-UNO DEL CROWDFUNDING CON ROMS DE SPECTRUM](http://zxuno.speccy.org/instrucciones.shtml)
* [I am newbie. Where to start? / Soy novato, ¿por dónde empezar?](http://www.zxuno.com/forum/viewtopic.php?f=27&t=754)
* Manual de esxDOS: [Parte 1](http://www.vintagenarios.com/manual-esxdos-parte-t1120.html) y [Parte 2](http://www.vintagenarios.com/manual-esxdos-parte-t1122.html)
* [ZX-Uno FAQ](http://uto.speccy.org/zxunofaq.html)
* [ZX-Uno Wiki](http://www.zxuno.com/wiki/index.php/ZX_Spectrum): Contiene el diagrama de bloques del sistema, la lista de registros, descripción de los modos gráficos disponibles, etc.
* [Sinclair FAQ Wiki](http://faqwiki.zxnet.co.uk/wiki/Main_Page)
* [ZX-UNO (XL) ISSUE2](https://www.8bits4ever.net/product-page/zx-uno-xl-issue2): Versión de ZX-Uno para integrar en carcasa de Spectrum original.
* [RetroRadionics](http://retroradionics.co.uk/): Carcasas y repuestos para Spectrum original.
* [Distribución para ZX-Uno - Summer of '22 Edition](http://retrowiki.es/viewtopic.php?f=110&t=200038436)

## Comandos

* NMI - EsxDOS: Ctrl-Alt-F5
* Soft Reset: Ctrl-Alt-Supr
* Hard Reset: Ctrl-Alt-Del
* Configuración: Hard Reset + F2 (Edit)
* Cambio de Core durante arranque: Caps Lock
* Cambio de modo de vídeo: Scroll Lock
* Huevo de pascua: Pulsar `:` (o SYMBOL SHIFT+Z) durante los 2 primeros segundos tras el arranque o tras hacer master reset (Ctrl-Alt-BkSpace).

## POKEs

([Fuente](http://uto.speccy.org/zxunofaq.html#megafaq))

1. Arrancar con la ROM "cargandoleches".
2. Con esa ROM no se pueden cargar juegos con el menú de NMI así que hay que usar comandos de ESXDOS, después de hacer BREAK al arracar la ROM. Para cargar taps hay que acceder al directorio donde estén usando así:

    ```
    .cd <directorio>
    ```

3. Luego cargar el juego así:

    ```
    .tapein <nombre del fichero tap>
    LOAD ""
    ```

4. Una vez cargado el juego, pulsar NMI. Saldrá arriba a la izquierda un recuadro donde primero hay que escribir la dirección del POKE (lo que va antes de la coma), pulsar enter, y después teclear el valor del POKE (lo que va detrás de la coma). Para terminar simplemente pulsar enter en lugar de escribir la dirección y volverá al juego ya pokeado.
