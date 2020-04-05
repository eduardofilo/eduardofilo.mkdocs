---
layout: default
permalink: /ingenieria/freecad.html
---
![FreeCAD](/images/pages/freecad_logo.svg)

# FreeCAD

## Enlaces

* [Curso de ObiJuan](http://www.iearobotics.com/wiki/index.php?title=Dise%C3%B1o_de_piezas_con_Freecad)
* [Manuales FreeCAD oficiales](https://www.freecadweb.org/manual/)
* [Wiki oficial](https://wiki.freecadweb.org/Main_Page/es)
* [KiCAD StepUp cheat sheet](https://github.com/easyw/kicadStepUpMod/raw/master/demo/kicadStepUp-cheat-sheet.pdf)

## Cheat sheet

* Configuración:
    * Auto refine:
        * `Edit > Preferences... > Part design > General > Model settings > Automatically check model after boolean operation`: ON
        * `Edit > Preferences... > Part design > General > Model settings > Automatically refine model after boolean operation`: ON
        * `Edit > Preferences... > Part design > General > Model settings > Automatically refine model after sketch-based operation`: ON
    * Tipo de navegación:
        * `Right click > Navigation styles`: Gesture
* `Tools > Dependency graph`: Árbol de dependencias entre objetos.
* Workbench:
    * `Parts`: Diseño de volúmenes 3D. Algunas de sus herramientas:
        * `Fusion`: ![Fusion](/images/pages/freecad_fusion.png) Unión de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Cut`: ![Cut](/images/pages/freecad_cut.png) Sustracción de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
