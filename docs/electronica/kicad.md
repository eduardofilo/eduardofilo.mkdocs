---
layout: default
permalink: /electronica/arduino.html
---

# KiCad

## Enlaces

* Creating A PCB In Everything: KiCad: [Part 1](https://hackaday.com/2016/11/17/creating-a-pcb-in-everything-kicad-part-1/), [Part 2](https://hackaday.com/2016/12/09/creating-a-pcb-in-everything-kicad-part-2/) y [Part 3](https://hackaday.com/2016/12/23/creating-a-pcb-in-everything-kicad-part-3/)
* [KiCad Best Practices: Library Management](https://hackaday.com/2017/05/18/kicad-best-practises-library-management/)
* [Desing Rules recomendadas para minimizar problemas en fabricación PCB's](http://support.seeedstudio.com/knowledgebase/articles/447362-fusion-pcb-specification)

## Gestión de librerías

1. Crear la siguiente estructura de directorios al crear un nuevo proyecto:

        mi_proyecto
         ↳3d_models     // .STEP and .WRL model files for all footprints
         ↳datasheets    // data sheets for components used
         ↳gerber        // final production files
         ↳images        // SVG images and 3D board renders
         ↳lib_sch       // schematic symbols
         ↳lib_fp.pretty // footprints
         ↳pdf           // schematics, board layouts, dimension drawings

2. Conforme se va editando un esquemático, KiCad va incorporando todos los símbolos utilizados (procedentes de las librerías de la aplicación y de las creadas para el proyecto) a una librería de backup llamada "mi_proyecto-cache.lib". Una vez que el esquemático esté completo, copiar dicha librería al directorio `lib_sch`, renombrándola para quitar el sufijo `-cache` del nombre, es decir quedando `lib_sch/mi_proyecto.lib`.
3. En el editor del esquemático abrir el comando de menú `Preferencias > Administrar librerías de símbolos...`, seleccionar la pestaña `Librerías específicas del proyecto` y añadir la librería que hemos copiado en el paso anterior por medio del botón con forma de carpeta (`Add existing library to table`). De esta forma nunca perderemos los símbolos utilizados durante la creación del esquema (se podrían modificar al actualizar las librerías del programa):

    ![lib_sch](/images/pages/kicad/lib_sch.png)

## Cheatsheet

En general KiCad se utiliza con atajos de teclado. Para obtener los atajos de teclado que sirven en una de las aplicaciones, pulsar `Ctrl+F1`.

1. Crear proyecto:
    1. Desde la ventana principal del programa, `File > New > Project...`
2. Diseñar símbolo:
    1. Abrir el programa `Symbol Editor`: <img src="/images/pages/kicad/add_component.svg" width="30"/>
    2. Crear una nueva librería con el comando `File > New library...` en el directorio `lib_sch`.
    3. En el popup `Add To Library Table` que aparece seleccionar la opción `Project`.
    4. Pulsar el botón `Create new symbol`: <img src="/images/pages/kicad/add_component.svg" width="30"/>
    5. Se nos preguntará por la librería donde incorporarlo. Seleccionar la que acabamos de crear (aparecerá al final).
    6. Rellenar el cuadro `Symbol Properties`. Fundamentalmente tenemos que dar un nombre para el componente.
    7. Crear el símbolo del componente utilizando fundamentalmente los siguientes atajos de teclado:
        * `M`: Mover objeto.
        * `P`: Crear pin. El círculo al final de la línea representa el punto donde se hará la conexión. <img src="/images/pages/kicad/add_pin.svg" width="30"/>
        * `Supr`: Eliminar objeto.
    8. Decorar el símbolo con las herramientas de dibujo.
    9. Guardar los cambios. <img src="/images/pages/kicad/save.svg" width="30"/>
2. Diseñar esquemático:
    1. Abrir el programa `Schematic Layout Editor (eeschema)`: <img src="/images/pages/kicad/icon_eeschema.svg" width="30"/>
    2. Añadir los símbolos que van a componer el esquemático con la ayuda de los siguientes atajos:
        * `A`: Añadir símbolo. <img src="/images/pages/kicad/add_component.svg" width="30"/>
        * `P`: Añadir fuente de alimentación o masa. <img src="/images/pages/kicad/add_power.svg" width="30"/>
        * `C`: Copiar símbolo.
    3. Una vez que tengamos todos los símbolos a la vista los reorganizaremos y cablearemos con los siguientes atajos de teclado:
        * `M`: Mover objeto (rompe las conexiones).
        * `G`: Arrastrar objeto (mantiene las conexiones).
        * `R`: Rotar objeto.
        * `E`: Editar propiedades del objeto como Referencia (`U`), Valor (`V`) o Footprint (`F`).
        * `W`: Conexión entre símbolos. <img src="/images/pages/kicad/add_line.svg" width="30"/>
        * `K`: Terminar el trazado de una conexión.
        * `Q`: Añadir no conexión.
        * `L`: Añadir etiqueta de red. <img src="/images/pages/kicad/add_line_label.svg" width="30"/>
        * `I`: Añadir polilínea. <img src="/images/pages/kicad/add_dashed_line.svg" width="30"/>
        * `T`: Añadir texto.
    4. Dar valores a los componentes que lo necesiten (Resistencias, Condesadores, Diodos, etc.) con el atajo `V` o `E`.
    5. Dar nombre a los componentes. Se puede hacer automáticamente con la herramienta de anotación a la que se accede con el botón <img src="/images/pages/kicad/annotate.svg" width="30"/> de la barra superior.

## Generación modelo 3D de la placa

1. Bajar el repositorio con los modelos de los componentes:

    ```bash
    cd ~/git
    git clone git@github.com:KiCad/kicad-packages3D.git
    ```

2. Abrir el menú `Preferencias > Configure Paths...".
3. Configurar el repositorio recien bajado como la nueva ruta de la librería `KISYS3DMOD` (originalmente la ruta es `/usr/share/kicad/modules/packages3d/`):

    ![KISYS3DMOD path](/images/pages/kicad/configure_KISYS3DMOD_path.png))

4. En Pcbnew editar las propiedades de las huellas y en la solapa `Opciones 3D` añadir la ruta del modelo 3D o ajustarla si es que existe.

    ![Opciones 3D propiedades huella](/images/pages/kicad/opciones_3d_propiedades_huella.png))

5. Abrir el menú `Ver > Visor 3D`.
