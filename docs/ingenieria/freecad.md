---
layout: default
permalink: /ingenieria/freecad.html
---
![FreeCAD](/images/pages/freecad/logo.svg)

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
        * `Tools`: ![Cube](/images/pages/freecad/cube.png) ![Cylinder](/images/pages/freecad/cylinder.png) ![Sphere](/images/pages/freecad/sphere.png) ![Cone](/images/pages/freecad/cone.png) ![Torus](/images/pages/freecad/torus.png)
        * `Fusion`: ![Fusion](/images/pages/freecad/fusion.png) Unión de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Cut`: ![Cut](/images/pages/freecad/cut.png) Sustracción de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Fillet`: ![Fillet](/images/pages/freecad/fillet.png) Redondeo de aristas.
        * `Chamfer`: ![Chamfer](/images/pages/freecad/chamfer.png) Chaflán en aristas.
    * `Draft`:
        * `Array`: ![Array](/images/pages/freecad/array.png) Multiplicación de objetos en 1, 2 o 3 dimensiones.
    * `Part Design`:
        * `Create sketch`: ![Create Sketch](/images/pages/freecad/create_sketch.png) Crear plano de un objeto.
        * `Pad`: ![Pad](/images/pages/freecad/pad.png) Extruir plano de un objeto.
        * `Pocket`: ![Pocket](/images/pages/freecad/pocket.png) Vaciar plano de un objeto.
    * `Sketcher`:
        * `Tools`: ![Point](/images/pages/freecad/sketcher_point.png) ![Line](/images/pages/freecad/sketcher_line.png) ![Arc](/images/pages/freecad/sketcher_arc.png) ![Circle](/images/pages/freecad/sketcher_circle.png) ![Polyline](/images/pages/freecad/sketcher_polyline.png) ![Rectangle](/images/pages/freecad/sketcher_rectangle.png)
        * `Fillet`: ![Fillet](/images/pages/freecad/sketcher_fillet.png) Redondea un vértice de un plano.
        * `Trim`: ![Trim](/images/pages/freecad/sketcher_trim.png) Recorta las líneas sobrantes de un plano.
        * `Create edge`: ![Create edge](/images/pages/freecad/sketcher_create_edge.png) Crea linea de referencia en base a una arista de un objeto externo al sketch.
        * `Toggles to/from construction mode`: ![Construction Mode](/images/pages/freecad/construction_mode.png) Alterna un objeto entre el modo normal y el auxiliar.
        * `Constraints`: ![Coincident](/images/pages/freecad/constraint_coincident.png) ![Fix](/images/pages/freecad/constraint_fix.png) ![Vertical](/images/pages/freecad/constraint_vertical.png) ![Horizontal](/images/pages/freecad/constraint_horizontal.png) ![Parallel](/images/pages/freecad/constraint_parallel.png) ![Perpendicular](/images/pages/freecad/constraint_perpendicular.png) ![Tangent](/images/pages/freecad/constraint_tangent.png) ![Equality](/images/pages/freecad/constraint_equality.png) ![Symmetry](/images/pages/freecad/constraint_symmetry.png) ![Horizontal distance](/images/pages/freecad/constraint_horizontal_distance.png) ![Vertical distance](/images/pages/freecad/constraint_vertical_distance.png) ![Fix length](/images/pages/freecad/constraint_fix_length.png) ![Radius](/images/pages/freecad/constraint_radius.png) ![Angle](/images/pages/freecad/constraint_angle.png)
