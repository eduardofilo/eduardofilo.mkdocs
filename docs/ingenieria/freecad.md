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
        * `Tools`: [![Cube](/images/pages/freecad/part_cube.png)](https://www.youtube.com/watch?v=dOdAtUmgW4k) [![Cylinder](/images/pages/freecad/part_cylinder.png)](https://www.youtube.com/watch?v=jDaJpLadCjE) [![Sphere](/images/pages/freecad/part_sphere.png)](https://www.youtube.com/watch?v=FChk-69h8SY) [![Cone](/images/pages/freecad/part_cone.png)](https://www.youtube.com/watch?v=eqh_KMsePPU) [![Torus](/images/pages/freecad/part_torus.png)](https://www.youtube.com/watch?v=1G78YHRapsI)
        * `Parametrized geometric primitives`: [![Parametrized geometric primitives](/images/pages/freecad/part_parametrized.png)](https://www.youtube.com/watch?v=UynsLGouRKg) Hélices, espirales...
        * `Extrude`: [![Extrude](/images/pages/freecad/part_extrude.png)](https://www.youtube.com/watch?v=iuAQdwnlWlY) Extrusión de trayectorias. [Calcado de dibujos con Inkscape](https://www.youtube.com/watch?v=sgtjP79H36w). [Extrusión de texto con Inkscape](https://www.youtube.com/watch?v=C94Y4uduI08).
        * `Mirror`: [![Mirror](/images/pages/freecad/part_mirror.png)](https://www.youtube.com/watch?v=Guq7BBR8eMk) Simetría de espejo.
        * `Fillet`: [![Fillet](/images/pages/freecad/part_fillet.png)](https://www.youtube.com/watch?v=jdCREzRmiro) Redondeo de aristas.
        * `Chamfer`: [![Chamfer](/images/pages/freecad/part_chamfer.png)](https://www.youtube.com/watch?v=jdCREzRmiro) Chaflán en aristas.
        * `Loft`: [![Loft](/images/pages/freecad/part_loft.png)](https://www.youtube.com/watch?v=caO6IHavJMI) Interpolación entre dos bocetos de objetos.
        * `Sweep`: [![Sweep](/images/pages/freecad/part_sweep.png)](https://www.youtube.com/watch?v=afPX6_MQk10) Extruir el boceto de un objeto a lo largo de una trayectoria. Puede hacerse [con torsión](https://www.youtube.com/watch?v=PQUEa2YRVng) si la trayectoria es una hélice.
        * `Offset`: [![Offset](/images/pages/freecad/part_offset.png)](https://www.youtube.com/watch?v=IcJ691adlik) Offset de objetos.
        * `Thickness`: [![Thickness](/images/pages/freecad/part_thickness.png)](https://www.youtube.com/watch?v=BweNSLvQxkc) Carcasas o recipientes a partir de objetos.
        * `Fusion`: [![Fusion](/images/pages/freecad/part_fusion.png)](https://www.youtube.com/watch?v=mntnhxidqoA) Unión de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Cut`: [![Cut](/images/pages/freecad/part_cut.png)](https://www.youtube.com/watch?v=3LsHR57grk0) Sustracción de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
    * `Draft`:
        * `Array`: ![Array](/images/pages/freecad/array.png) Multiplicación de objetos en 1, 2 o 3 dimensiones. [Lineal](https://www.youtube.com/watch?v=bxKOFY2vgqM), [Axial](https://www.youtube.com/watch?v=BhkFGKmM1gQ)
    * `Part Design`:
        * `Create sketch`: ![Create Sketch](/images/pages/freecad/part-design_create_sketch.png) Crear boceto (plano) de un objeto.
        * `Pad`: [![Pad](/images/pages/freecad/part-design_pad.png)](https://www.youtube.com/watch?v=5fK9_Ux6t8k) Extruir el boceto de un objeto linealmente.
        * `Revolve`: [![Revolve](/images/pages/freecad/part-design_revolve.png)](https://www.youtube.com/watch?v=vE-KlUTqzJs) Extruir el boceto de un objeto axialmente.
        * `Pocket`: [![Pocket](/images/pages/freecad/part-design_pocket.png)](https://www.youtube.com/watch?v=dSSEbTNAGts) Vaciar boceto de un objeto.
        * `Mirror`: [![Mirror](/images/pages/freecad/part-design_mirror.png)](https://www.youtube.com/watch?v=Guq7BBR8eMk) Simetría de espejo.
        * `Linear Pattern`: [![Linear Pattern](/images/pages/freecad/part-design_linear_pattern.png)](https://www.youtube.com/watch?v=ny2wTmZEDT4) Multiplicación lineal de una operación.
        * `Polar Pattern`: [![Polar Pattern](/images/pages/freecad/part-design_polar_pattern.png)](https://www.youtube.com/watch?v=ny2wTmZEDT4) Multiplicación polar de una operación.
    * `Sketcher`:
        * `Tools`: ![Point](/images/pages/freecad/sketcher_point.png) ![Line](/images/pages/freecad/sketcher_line.png) [![Arc](/images/pages/freecad/sketcher_arc.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Circle](/images/pages/freecad/sketcher_circle.png)](https://www.youtube.com/watch?v=bA06HZKR40E) ![Polyline](/images/pages/freecad/sketcher_polyline.png) ![Rectangle](/images/pages/freecad/sketcher_rectangle.png)
        * `Fillet`: [![Fillet](/images/pages/freecad/sketcher_fillet.png)](https://www.youtube.com/watch?v=ntNaY2O2v4w) Redondea un vértice de un plano.
        * `Trim`: [![Trim](/images/pages/freecad/sketcher_trim.png)](https://www.youtube.com/watch?v=V0eLXQoFYmM) Recorta las líneas sobrantes de un plano.
        * `Create edge`: [![Create edge](/images/pages/freecad/sketcher_create_edge.png)](https://www.youtube.com/watch?v=n0OcbjvGdlM) Crea linea de referencia en base a una arista de un objeto externo al sketch.
        * `Toggles to/from construction mode`: [![Construction Mode](/images/pages/freecad/construction_mode.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4) Alterna un objeto entre el modo normal y el auxiliar.
        * `Constraints`: [![Coincident](/images/pages/freecad/constraint_coincident.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Fix](/images/pages/freecad/constraint_fix.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4) [![Vertical](/images/pages/freecad/constraint_vertical.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Horizontal](/images/pages/freecad/constraint_horizontal.png)](https://www.youtube.com/watch?v=dVg5uBciurs) ![Parallel](/images/pages/freecad/constraint_parallel.png) [![Perpendicular](/images/pages/freecad/constraint_perpendicular.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Tangent](/images/pages/freecad/constraint_tangent.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Equality](/images/pages/freecad/constraint_equality.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Symmetry](/images/pages/freecad/constraint_symmetry.png)](https://www.youtube.com/watch?v=bA06HZKR40E) [![Horizontal distance](/images/pages/freecad/constraint_horizontal_distance.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Vertical distance](/images/pages/freecad/constraint_vertical_distance.png)](https://www.youtube.com/watch?v=dVg5uBciurs) ![Fix length](/images/pages/freecad/constraint_fix_length.png) [![Radius](/images/pages/freecad/constraint_radius.png)](https://www.youtube.com/watch?v=bA06HZKR40E) [![Angle](/images/pages/freecad/constraint_angle.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4)
