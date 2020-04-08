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
        * `Tools`: ![Cube](/images/pages/freecad_cube.png) ![Cylinder](/images/pages/freecad_cylinder.png) ![Sphere](/images/pages/freecad_sphere.png) ![Cone](/images/pages/freecad_cone.png) ![Torus](/images/pages/freecad_torus.png)
        * `Fusion`: ![Fusion](/images/pages/freecad_fusion.png) Unión de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Cut`: ![Cut](/images/pages/freecad_cut.png) Sustracción de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Fillet`: ![Fillet](/images/pages/freecad_fillet.png) Redondeo de aristas.
        * `Chamfer`: ![Chamfer](/images/pages/freecad_chamfer.png) Chaflán en aristas.
    * `Draft`:
        * `Array`: ![Array](/images/pages/freecad_array.png) Multiplicación de objetos en 1, 2 o 3 dimensiones.
    * `Part Design`:
        * `Create sketch`: ![Create Sketch](/images/pages/freecad_create_sketch.png) Crear plano de un objeto.
        * `Pad`: ![Pad](/images/pages/freecad_pad.png) Extruir plano de un objeto.
        * `Pocket`: ![Pocket](/images/pages/freecad_pocket.png) Vaciar plano de un objeto.
    * `Sketcher`:
        * `Tools`: ![Point](/images/pages/freecad_sketcher_point.png) ![Line](/images/pages/freecad_sketcher_line.png) ![Arc](/images/pages/freecad_sketcher_arc.png) ![Circle](/images/pages/freecad_sketcher_circle.png) ![Polyline](/images/pages/freecad_sketcher_polyline.png) ![Rectangle](/images/pages/freecad_sketcher_rectangle.png)
        * `Trim`: ![Trim](/images/pages/freecad_sketcher_trim.png): Recorta las líneas sobrantes de un plano.
        * `Toggles to/from construction mode`: ![Construction Mode](/images/pages/freecad_construction_mode.png) Alterna un objeto entre el modo normal y el auxiliar.
        * `Constraints`: ![Coincident](/images/pages/freecad_constraint_coincident.png) ![Fix](/images/pages/freecad_constraint_fix.png) ![Vertical](/images/pages/freecad_constraint_vertical.png) ![Horizontal](/images/pages/freecad_constraint_horizontal.png) ![Parallel](/images/pages/freecad_constraint_parallel.png) ![Perpendicular](/images/pages/freecad_constraint_perpendicular.png) ![Tangent](/images/pages/freecad_constraint_tangent.png) ![Equality](/images/pages/freecad_constraint_equality.png) ![Symmetry](/images/pages/freecad_constraint_symmetry.png) ![Horizontal distance](/images/pages/freecad_constraint_horizontal_distance.png) ![Vertical distance](/images/pages/freecad_constraint_vertical_distance.png) ![Fix length](/images/pages/freecad_constraint_fix_length.png) ![Radius](/images/pages/freecad_constraint_radius.png) ![Angle](/images/pages/freecad_constraint_angle.png)
