---
layout: default
permalink: /ingenieria/arduino.html
---

# KiCad

## Enlaces

* Creating A PCB In Everything: KiCad: [Part 1](https://hackaday.com/2016/11/17/creating-a-pcb-in-everything-kicad-part-1/), [Part 2](https://hackaday.com/2016/12/09/creating-a-pcb-in-everything-kicad-part-2/) y [Part 3](https://hackaday.com/2016/12/23/creating-a-pcb-in-everything-kicad-part-3/)
* [KiCad Best Practices: Library Management](https://hackaday.com/2017/05/18/kicad-best-practises-library-management/)
* [Desing Rules recomendadas para minimizar problemas en fabricación PCB's](http://support.seeedstudio.com/knowledgebase/articles/447362-fusion-pcb-specification)
* [Sizing Logos in KiCAD](https://defproc.co.uk/blog/kicad-logo-size/)
* [Librería de componentes de JLCPCB para Assembly Service](https://jlcpcb.com/client/index.html#/parts)
* [Calculadoras de conversión en línea por DigiKey](https://www.digikey.com/es/resources/online-conversion-calculators)
* [Svg2Shenzhen](https://github.com/badgeek/svg2shenzhen): Inkscape extension for exporting drawings into a KiCad PCB.
* Descarga de footprints y modelos 3D:
    * [SnapEDA](https://www.snapeda.com/)
    * [PARTcommunity](https://b2b.partcommunity.com/community/)
* [Interactive HTML BOM plugin for KiCad](https://github.com/openscopeproject/InteractiveHtmlBom/wiki)

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

## Workflow

En general KiCad se utiliza con atajos de teclado. Para obtener los atajos de teclado que sirven en una de las aplicaciones, pulsar `Ctrl+F1`.

1. Crear proyecto:
    1. Desde la ventana principal del programa, `File > FNew > Project...`
2. Diseñar símbolo:
    1. Abrir el programa `Symbol Editor`. <img src="/images/pages/kicad/add_component.svg" width="30"/>
    2. Para mantener los ficheros del nuevo símbolo, escoger uno de estos caminos en función de si se quiere mantener el símbolo exclusivamente dentro del proyecto o de forma global:
        * Crear una nueva librería con el comando `File > New Library...` en el directorio `lib_sch`. En el popup `Add To Library Table` que aparece seleccionar la opción `Project`.
        * Instalar a nivel global (`Preferences > Manage Symbol Libraries...`) las que se mantienen en [este repositorio](https://github.com/eduardofilo/kicad_footprints).
    3. Seleccionar la librería recien creada o importada y pulsar el botón `Create new symbol`. <img src="/images/pages/kicad/add_component.svg" width="30"/>
    4. Se nos preguntará por la librería donde incorporarlo. Seleccionar la que acabamos de crear (aparecerá al final).
    5. Rellenar el cuadro `Symbol Properties`. Fundamentalmente tenemos que dar un nombre para el componente.
    6. Crear el símbolo del componente utilizando fundamentalmente los siguientes atajos de teclado:
        * `M`: Mover objeto.
        * `P`: Crear pin. El círculo al final de la línea representa el punto donde se hará la conexión. <img src="/images/pages/kicad/add_pin.svg" width="30"/>
        * `Supr`: Eliminar objeto.
    7. Decorar el símbolo con las herramientas de dibujo.
    8. Guardar los cambios. <img src="/images/pages/kicad/save.svg" width="30"/>
3. Diseñar esquemático:
    1. Abrir el programa `Schematic Layout Editor (eeschema)`. <img src="/images/pages/kicad/icon_eeschema.svg" width="30"/>
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
4. Asociar símbolos del esquemático con huellas PCB ejecutando CvPCB. <img src="/images/pages/kicad/cvpcb.svg" width="30"/>. Aprovechar los botones de filtrado, sobre todo `Filter footprint list using a partial name or a pattern`.
5. Diseñar las huellas que no se encuentren en la librería:
    1. Abrir el programa `Footprint Editor`. <img src="/images/pages/kicad/new_footprint.svg" width="30"/>
    2. Para mantener los ficheros de la nueva huella, escoger uno de estos caminos en función de si se quiere mantener exclusivamente dentro del proyecto o de forma global:
        * Crear una nueva librería con el comando `File > New Library...` en el directorio `lib_fp.pretty`. En el popup `Select Library Table` que aparece seleccionar la opción `Project`.
        * Instalar a nivel global (`Preferences > Manage Footprint Libraries...`) las que se mantienen en [este repositorio](https://github.com/eduardofilo/kicad_footprints) en el directorio `eduardofilo_footprints.pretty`.
    3. Seleccionar en la lista de librerías la que acabamos de crear o incorporar en el paso anterior. De esta forma la nueva huella que vamos a crear se creará dentro de esta librería.
    4. Pulsar el botón `New footprint`. <img src="/images/pages/kicad/new_footprint.svg" width="30"/>
    5. Darle nombre en el popup que aparece.
    6. Crear la huella utilizando fundamentalmente los siguientes atajos de teclado:
        * `M`: Mover objeto.
        * `R`: Rotar objeto.
        * Add pad: <img src="/images/pages/kicad/pad.svg" width="30"/>
        * `E`: Editar propiedad de objeto. Cuando se aplica sobre los pads es importante asignar correctamente el valor del `Pad number` ya que es como se enlazan los símbolos con las huellas.
    7. Decorar la huella con las herramientas de dibujo.
    8. Guardar los cambios. <img src="/images/pages/kicad/save.svg" width="30"/>
6. Diseñar la PCB:
    1. En `Schematic Layout Editor (eeschema)` pulsar el botón `Generate netlist`. <img src="/images/pages/kicad/netlist.svg" width="30"/>
    2. En el popup que aparece pulsar el botón `Generate Netlist`.
    3. Guardar el fichero que genera en la raíz del proyecto.
    4. Abrir el programa `PCB Layout Editor (pcbnew)`. <img src="/images/pages/kicad/pcbnew.svg" width="30"/>
    5. Importar el netlist utilizando el botón `Load netlist`. <img src="/images/pages/kicad/netlist.svg" width="30"/>
    6. En el popup que aparece seleccionar el fichero que hemos generado en el punto 3 anterior.
    7. Pulsar el botón `Update PCB`.
    8. Cerrar el popup y hacer clic sobre la PCB para colocar las huellas.
    9. Utilizando los atajos `M` y `R` recolocar todos los componentes como más convenga.
    10. Ocultar las etiquetas que no interesen, pulsando `E` sobre ellas y desmarcando el check `Visible`.
    11. Dibujar el perfil de la PCB con las herramientas de dibujo en la capa `Edge.Cuts`.
    12. Rutear haciendo uso de los siguientes atajos de teclado:
        * `X`: Añadir pista.
        * `V`: Añadir vía.
        * `M`: Mover componente.
        * `R`: Rotar componente.
        * `D`: Arrastrar pista.
    13. Crear las zonas rellenas de cobre (normalmente para las *nets* +5V y GND):
        1. Seleccionar la capa donde queremos crear la zona rellena de cobre (`F.Cu` o `B.Cu` normalmente).
        2. Seleccionar la herramienta `Add filled zones`. <img src="/images/pages/kicad/add_zone.svg" width="30"/>
        3. Delimitar una superficie que englobe la parte de la PCB que queremos rellenar de cobre. Al pinchar el primer vértice aparecerá una ventana en la que tendremos que indicar las propiedades de la zona a rellenar donde indicaremos la *net* y la capa de cobre.
        4. En caso de modificar las pistas más adelante, pulsar `B` para recalcular las zonas rellenas de cobre.
    14. Ejecutar las DRC pulsando el botón `Perform design rules check`. <img src="/images/pages/kicad/drc.svg" width="30"/>
7. Exportar Gerber:
    1. Pulsar el botón `Plot (HPGL, Postscript, or GERBER format)`. <img src="/images/pages/kicad/plot.svg" width="30"/>
    2. En la ventana que aparece, seleccionar las capas que queremos incluir y las opciones que se ven a continuación e indicar el directorio `gerber` del proyecto.
        ![plot](/images/pages/kicad/plot.png)
    3. Pulsar el botón `Plot`.
    4. Pulsar el botón `Generate Drill Files` y en la nueva ventana que aparece encima pulsar el botón `Generate Drill File`.
8. Exportar BOM:
    1. Pulsar el botón `Generate bill of materials`. <img src="/images/pages/kicad/bom.svg" width="30"/>
    2. De la lista `BOM plugins` que aparece seleccionar `bom2grouped_csv` y pulsar `Generate`.
9. Cambios en esquemático y propagación:
    1. Hacer el cambio en `Schematic Layout Editor (eeschema)`.
    2. Dar nombre a los nuevos componentes. Se puede hacer automáticamente con la herramienta de anotación a la que se accede con el botón <img src="/images/pages/kicad/annotate.svg" width="30"/> de la barra superior.
    3. Volver a `PCB Layout Editor (pcbnew)` y pulsar el botón `Update PCB from schematic`. <img src="/images/pages/kicad/update_pcb_from_sch.svg" width="30"/>
    4. En el popup que aparece pulsar el botón `Update PCB`. Nos hará un informe de los cambios. En caso de que los cambios impliquen componentes nuevos, cuando lo cerremos se nos cargarán en el cursor para incorporarlos al PCB.

Las capas más importantes son:

* `F.Cu`: Capa superior de cobre. Atajo de teclado: `RePag`.
* `B.Cu`: Capa inferior de cobre. Atajo de teclado: `AvPag`.
* `Edge.Cuts`: Perfil de corte de la PCB.
* `F.SilkS`: Silkscreen superior o capa donde se representan los símbolos y textos de los componentes habitualmente en blanco.
* `B.SilkS`: Silkscreen inferior.
* `F.Mask`: Máscara de soldado superior, habitualmente en verde.
* `B.Mask`: Máscara de soldado inferior.

## Generación modelo 3D de la placa

Es recomendable instalar los paquetes recomendados con apt cuando se instala KiCad. Se puede hacer con la siguiente opción en el comando de instalación:

```bash
$ sudo apt install --install-recommends kicad
```

En caso de no tener las librerías de paquetes 3D o querer forzar el tener la última versión de Github, se puede proceder como sigue:

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

## Designación de componentes

|Referencia|Tipo de componente|
|:----- |:------- |
|AT  |Attenuator|
|BR  |Bridge Rectifier|
|BT  |Battery|
|C   |Capacitor|
|CN  |Capacitor network|
|D   |Diode (including zeners, thyristors and LEDs)|
|DL  |Delay line|
|DS  |Display|
|F   |Fuse|
|FB or FEB   |Ferrite bead|
|FD  |Fiducial|
|J   |Jack connector (female)|
|JP  |Link (Jumper)|
|K   |Relay|
|L   |Inductor|
|LS  |Loudspeaker or buzzer|
|M   |Motor|
|MK  |Microphone|
|MP  |Mechanical part (including screws and fasteners)|
|P   |Plug connector (male)|
|PS  |Power supply|
|Q   |Transistor (all types)|
|R   |Resistor|
|RN  |Resistor network|
|RT  |Thermistor|
|RV  |Varistor|
|S   |Switch (all types, including push-buttons)|
|T   |Transformer|
|TC  |Thermocouple|
|TUN |Tuner|
|TP  |Test point|
|U   |Integrated circuit|
|V   |Vacuum Tube|
|VR  |Variable Resistor (potentiometer or rheostat)|
|X   |Transducer not matching any other category|
|Y   |Crystal or oscillator|
|Z   |Zener Diode|


## Componentes

### Tiendas

* [LCSC](https://lcsc.com/)
* [Viinko Electronics HK Ltd](https://viinko.es.aliexpress.com/store/1361740): Acepta pedidos BOM.

### Componentes interesantes

|Componente|Enlace compra|Footprint KiCad|
|:---------|:------------|:--------|
|Resistencia 1/4W P=10,16mm| |`Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`|
|Condensador cerámico 100nF P=2,54mm| |`Capacitors_ThroughHole:C_Disc_D3.0mm_W1.6mm_P2.50mm`|
|LED D=5mm| |`LED_THT:LED_D5.0mm`|
|USB micro-B|[LCSC](https://lcsc.com/product-detail/USB-Connectors_Amphenol-ICC-10118194-0001LF_C132563.html)|`Connect:USB_Micro-B`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_HRS-Hirose_DM3AT-SF-PEJM5_HRS-Hirose-HRS-DM3AT-SF-PEJM5_C114218.html)|`Connector_Card:microSD_HC_Hirose_DM3AT-SD-PEJMS`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_Korean-Hroparts-Elec-TF-04A_C145799.html)|`Connector_Card:microSD_HC_Wuerth_693072010801`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_XUNPU-TF-104_C266612.html)| |
|Transistor TO-92| |`TO_SOT_Packages_THT:TO-92_Inline_Wide`|
|Switch horizontal|[LCSC](https://lcsc.com/product-detail/Toggle-Switches_SHOU-HAN-SK12D07VG4_C393937.html)|`Buttons_Switches_ThroughHole:SW_CuK_OS102011MA1QN1_SPDT_Angled`|
|Tactile button horizontal|[LCSC](https://lcsc.com/product-detail/Others_C-K-PTS645VM832LFS_C285530.html)|`Button_Switch_THT/SW_Tactile_SPST_Angled_PTS645Vx83-2LFS`|
|Tactile button 6mm|[LCSC](https://lcsc.com/product-detail/Others_E-Switch_TL1105AF160Q_E-Switch-TL1105AF160Q_C273465.html)|`Buttons_Switches_ThroughHole:SW_PUSH_6mm`|
|Zócalo 8 pin (ATtiny85)| |`Housings_DIP:DIP-8_W7.62mm`|
|Conector alimentación jack barril 5.5mm|[LCSC](https://lcsc.com/product-detail/Power-Connectors_XKB-Enterprise-DC-005-5A-2-0_C381116.html)|`Connector_BarrelJack:BarrelJack_Wuerth_6941xx301002`|
|Transistor NPN 2N3904 TO-92| |`Package_TO_SOT_THT:TO-92L_Inline_Wide` o `Package_TO_SOT_THT:TO-92L_HandSolder`|

### Símbolos y footprints propios KiCad

En [este repositorio](https://github.com/eduardofilo/kicad_footprints).

Antes de crear los símbolos o los footprints, tratar de buscarlos en sitios como [SnapEDA](https://www.snapeda.com/).

|Componente|Symbol|Footprint|Compra|
|:---------|:-----|:--------|:-----|
|Switch horizontal|eduardofilo_symbols.lib/SK12D07VG4|`Buttons_Switches_ThroughHole:SW_CuK_OS102011MA1QN1_SPDT_Angled`|[LCSC](https://lcsc.com/product-detail/Toggle-Switches_SHOU-HAN-SK12D07VG4_C393937.html)|
|AY-8760|eduardofilo_symbols.lib/AY-3-8760|`Package_DIP:DIP-28_W15.24mm_Socket_LongPads`| |
|SNES Connector|eduardofilo_symbols.lib/SNES_Connector|eduardofilo_footprints.pretty/SNES.kicad_mod|[Aliexpress](https://es.aliexpress.com/item/32828768824.html)|
|EURO conector|`Connector:SCART-F`|eduardofilo_footprints.pretty/SCART.kicad_mod|[Aliexpress](https://es.aliexpress.com/item/32997772379.html)|
|Portapilas 2xAA|eduardofilo_symbols.lib/Battery_Holder|eduardofilo_footprints.pretty/BatteryHolder.kicad_mod|[LCSC](https://lcsc.com/product-detail/Battery-Holders-Clips-Contacts_Keystone-1013_C238059.html)|
|Logo Niubit| |eduardofilo_footprints.pretty/NiubitLogo.kicad_mod| |
|Lector microSD|eduardofilo_symbols.lib/Micro_SD_Cd|eduardofilo_footprints.pretty/Micro_SD_Cd.kicad_mod|[Aliexpress](https://es.aliexpress.com/item/32802051702.html), [LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_HOAUC-HYC77-TF09-200_C341092.html)|

### Valores habituales de resistencias

A pesar de que se fabrican resistencias de prácticamente cualquier valor, como tienen una tolerancia de fabricación amplia (lo normal es utilizar resistencias de en torno al 1-5% de tolerancia), lo habitual es utilizar valores nominales que comiencen con los siguientes valores: 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2

[Aquí](https://unicrom.com/tolerancia-valores-normalizados-de-resistores-resistencias/) puede verse una tabla donde se ven los valores normalizados en función de la tolerancia (a menor tolerancia mayor número de valores normalizados).
