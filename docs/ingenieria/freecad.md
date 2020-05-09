---
layout: default
permalink: /ingenieria/freecad.html
---
![FreeCAD](/images/pages/freecad/logo.svg)

# FreeCAD

## Enlaces

* Curso de ObiJuan: [Temporada 1](http://www.iearobotics.com/wiki/index.php?title=Dise%C3%B1o_de_piezas_con_Freecad), [Temporada 2](http://www.iearobotics.com/wiki/index.php?title=Tutorial_Freecad._Temporada_2)
* [Manuales FreeCAD oficiales](https://www.freecadweb.org/manual/)
* [Wiki oficial](https://wiki.freecadweb.org/Main_Page/es)
* [KiCAD StepUp cheat sheet](https://github.com/easyw/kicadStepUpMod/raw/master/demo/kicadStepUp-cheat-sheet.pdf)
* [Repositorio de Addons](https://github.com/freecad/freecad-addons)

## Importación modelo 3D KiCad

[KiCad StepUp Cheat Sheeet](/files/pages/kicadStepUp-cheat-sheet.pdf).

1. Instalar `kicadStepUpMod` desde `Addon manager` en FreeCAD.
2. Conviene que en KiCad esté instalado el paquete `kicad-packages3d` para que además de la PCB se exporten los volúmenes 3D de los componentes.
3. Comprobar que se corresponde la ruta del parámetro KISYS3DMOD en ambos programas (`Preferences...` en FreeCAD y `Configure Paths...` en KiCad).
4. Cambiar al workbench `kicadStepUp`.
5. Pulsar el botón ![](/images/pages/freecad/kicadstepup_load.png) para importar el diseño 3D de la PCB.

## Cheat sheet

* Configuración recomendada:
    * [Preferences...](https://www.youtube.com/watch?v=6HaHc7xY4I8&list=PLmnz0JqIMEzUqEM-nxqhZoDaqszVXijOb&index=2)
        * General:
            * `Document > Save thumbnail into project file when saving document`: ON
            * `Document > Authoring and License > Author name`: Nuestro nombre
            * `Document > Authoring and License > Default license`: CreativeCommons Attribution-ShareAlike
            * `Output window > Redirect internal Python output to report view`: ON
            * `Output window > Redirect internal Python errors to report view`: ON
        * Display:
            * `3D View > 3D Navigation`: Gesture
        * (Workbench `Part`) Part design:
            * `General > Model settings > Automatically check model after boolean operation`: ON
            * `General > Model settings > Automatically refine model after boolean operation`: ON
            * `General > Model settings > Automatically refine model after sketch-based operation`: ON
    * Tipo de navegación:
        * `Right click > Navigation styles`: Gesture
* [`File > Import...`](https://www.youtube.com/watch?v=uXeYTfEMu1I): Permite importar ficheros STEP para hacer modificaciones.
* [`Edit > Aligment...`](https://www.youtube.com/watch?v=eNCsavtEpzA): Permite situar un sólido sobre un plano.
* `Tools > Dependency graph`: Árbol de dependencias entre objetos.
* [Duplicado de objetos](https://www.youtube.com/watch?v=9a6rE8XzIgE) (Copias totales, copias simples y piezas clonadas)
* Workbench:
    * `Draft`: [Diseño de volúmenes a partir de puntos, aristas y caras](https://www.youtube.com/watch?v=gfSIwmD8Nnk).
        * [`Working plane`](https://www.youtube.com/watch?v=i7Gele0oFzM)
        * `Tools`: ![Line](/images/pages/freecad/draft_line.png) [![Polyline](/images/pages/freecad/draft_polyline.png)](https://www.youtube.com/watch?v=CjKaygrjNaM) ![Circle](/images/pages/freecad/draft_circle.png) ![Arc](/images/pages/freecad/draft_arc.png) ![Ellipse](/images/pages/freecad/draft_ellipse.png) ![Polygon](/images/pages/freecad/draft_polygon.png) ![Rectangle](/images/pages/freecad/draft_rectangle.png) [![Annotation](/images/pages/freecad/draft_annotation.png)](https://www.youtube.com/watch?v=cIEBKVfepZI) ![Dimension](/images/pages/freecad/draft_dimension.png) ![B-Spline](/images/pages/freecad/draft_spline.png) ![Point](/images/pages/freecad/draft_point.png) [![Text](/images/pages/freecad/draft_text.png)](https://www.youtube.com/watch?v=Bi2IAR1Ya8w)
        * `Move`: [![Move](/images/pages/freecad/draft_move.png)](https://www.youtube.com/watch?v=dZLE-6m030c)
        * `Rotate`: [![Rotate](/images/pages/freecad/draft_rotate.png)](https://www.youtube.com/watch?v=hPoq7fJEJzQ)
        * `Array`: ![Array](/images/pages/freecad/array.png) Multiplicación de objetos en 1, 2 o 3 dimensiones. [Lineal](https://www.youtube.com/watch?v=bxKOFY2vgqM), [Axial](https://www.youtube.com/watch?v=BhkFGKmM1gQ)
        * `Clone`: [![Clone](/images/pages/freecad/draft_clone.png)](https://www.youtube.com/watch?v=9a6rE8XzIgE) Duplicado de objetos vinculados al original con opción de escalado.
        * `Snap tools`: ![Snap nearest](/images/pages/freecad/draft_snap_nearest.png) ![Snap extension](/images/pages/freecad/draft_snap_extension.png) ![Snap parallel](/images/pages/freecad/draft_snap_parallel.png) [![Snap grid](/images/pages/freecad/draft_snap_grid.png)](https://www.youtube.com/watch?v=i7Gele0oFzM) [![Snap endpoint](/images/pages/freecad/draft_snap_endpoint.png)](https://www.youtube.com/watch?v=dZLE-6m030c) [![Snap midpoint](/images/pages/freecad/draft_snap_midpoint.png)](https://www.youtube.com/watch?v=yQR4HBXZ0HE) ![Snap perpendicular](/images/pages/freecad/draft_snap_perpendicular.png) ![Snap angle](/images/pages/freecad/draft_snap_angle.png) [![Snap center](/images/pages/freecad/draft_snap_center.png)](https://www.youtube.com/watch?v=DWVpIESz1yI) ![Snap ortho](/images/pages/freecad/draft_snap_ortho.png) ![Snap intersection](/images/pages/freecad/draft_snap_intersection.png) ![Snap special](/images/pages/freecad/draft_snap_special.png) ![Snap dimensions](/images/pages/freecad/draft_snap_dimensions.png) ![Snap workingplane](/images/pages/freecad/draft_snap_workingplane.png)
    * `Drawing`:
        * `New drawing`: [![New drawing](/images/pages/freecad/new_drawing.png)](https://www.youtube.com/watch?v=GDE4erbMaS4) Crear plano de diseño.
        * `Insert projection`: [![Insert projection](/images/pages/freecad/insert_projection.png)](https://www.youtube.com/watch?v=GDE4erbMaS4) Insertar proyección en plano de diseño.
        * `Export to SVG`: [![Export to SVG](/images/pages/freecad/export.png)](https://www.youtube.com/watch?v=GDE4erbMaS4) Exportar a SVG.
    * `Part Design`:
        * `Create sketch`: ![Create Sketch](/images/pages/freecad/part-design_create_sketch.png) Crear boceto (plano) de un objeto.
        * `Pad`: [![Pad](/images/pages/freecad/part-design_pad.png)](https://www.youtube.com/watch?v=5fK9_Ux6t8k) Extruir el boceto de un objeto linealmente.
        * `Revolve`: [![Revolve](/images/pages/freecad/part-design_revolve.png)](https://www.youtube.com/watch?v=vE-KlUTqzJs) Extruir el boceto de un objeto axialmente.
        * `Pocket`: [![Pocket](/images/pages/freecad/part-design_pocket.png)](https://www.youtube.com/watch?v=dSSEbTNAGts) Vaciar boceto de un objeto.
        * `Mirror`: [![Mirror](/images/pages/freecad/part-design_mirror.png)](https://www.youtube.com/watch?v=Guq7BBR8eMk) Simetría de espejo.
        * `Linear Pattern`: [![Linear Pattern](/images/pages/freecad/part-design_linear_pattern.png)](https://www.youtube.com/watch?v=ny2wTmZEDT4) Multiplicación lineal de una operación.
        * `Polar Pattern`: [![Polar Pattern](/images/pages/freecad/part-design_polar_pattern.png)](https://www.youtube.com/watch?v=ny2wTmZEDT4) Multiplicación polar de una operación.
    * `Part`: Diseño de volúmenes 3D. Algunas de sus herramientas:
        * `Tools`: [![Cube](/images/pages/freecad/part_cube.png)](https://www.youtube.com/watch?v=dOdAtUmgW4k) [![Cylinder](/images/pages/freecad/part_cylinder.png)](https://www.youtube.com/watch?v=jDaJpLadCjE) [![Sphere](/images/pages/freecad/part_sphere.png)](https://www.youtube.com/watch?v=FChk-69h8SY) [![Cone](/images/pages/freecad/part_cone.png)](https://www.youtube.com/watch?v=eqh_KMsePPU) [![Torus](/images/pages/freecad/part_torus.png)](https://www.youtube.com/watch?v=1G78YHRapsI)
        * `Parametrized geometric primitives`: ![Parametrized geometric primitives](/images/pages/freecad/part_parametrized.png) Hélices, [espirales](https://www.youtube.com/watch?v=UynsLGouRKg), [cuñas](https://www.youtube.com/watch?v=jSv-xPEBg48), [prismas](https://www.youtube.com/watch?v=0qNhy-HsN_I), [localización en un plano](https://www.youtube.com/watch?v=2uO1U2MS9Kc)...
        * `Shapes`: [![Shapes](/images/pages/freecad/part_shapes.png)](https://www.youtube.com/watch?v=d-JAkkMnHYI) Piezas a partir de aristas y caras.
        * `Extrude`: [![Extrude](/images/pages/freecad/part_extrude.png)](https://www.youtube.com/watch?v=iuAQdwnlWlY) Extrusión de trayectorias. [Calcado de dibujos con Inkscape](https://www.youtube.com/watch?v=sgtjP79H36w). [Extrusión de texto con Inkscape](https://www.youtube.com/watch?v=C94Y4uduI08). [Importar SVG y convertir a Sketch](https://forum.freecadweb.org/viewtopic.php?t=29704). [Extrusión en diagonal de polilíneas](https://www.youtube.com/watch?v=CjKaygrjNaM)
        * `Mirror`: [![Mirror](/images/pages/freecad/part_mirror.png)](https://www.youtube.com/watch?v=Guq7BBR8eMk) Simetría de espejo.
        * `Fillet`: [![Fillet](/images/pages/freecad/part_fillet.png)](https://www.youtube.com/watch?v=jdCREzRmiro) Redondeo de aristas.
        * `Chamfer`: [![Chamfer](/images/pages/freecad/part_chamfer.png)](https://www.youtube.com/watch?v=jdCREzRmiro) Chaflán en aristas.
        * `Loft`: [![Loft](/images/pages/freecad/part_loft.png)](https://www.youtube.com/watch?v=caO6IHavJMI) Interpolación entre dos bocetos de objetos.
        * `Sweep`: [![Sweep](/images/pages/freecad/part_sweep.png)](https://www.youtube.com/watch?v=afPX6_MQk10) Extruir el boceto de un objeto a lo largo de una trayectoria. Puede hacerse [con torsión](https://www.youtube.com/watch?v=PQUEa2YRVng) si la trayectoria es una hélice.
        * `Offset`: [![Offset](/images/pages/freecad/part_offset.png)](https://www.youtube.com/watch?v=IcJ691adlik) Offset de objetos.
        * `Thickness`: [![Thickness](/images/pages/freecad/part_thickness.png)](https://www.youtube.com/watch?v=BweNSLvQxkc) Carcasas o recipientes a partir de objetos.
        * `Fusion`: [![Fusion](/images/pages/freecad/part_fusion.png)](https://www.youtube.com/watch?v=mntnhxidqoA) Unión de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * `Cut`: [![Cut](/images/pages/freecad/part_cut.png)](https://www.youtube.com/watch?v=3LsHR57grk0) Sustracción de volúmenes. Si se ha activado el autorefine se mantendrá la relación entre el volumen fusionado y los constituyentes de manera que podremos modificar sus parámetros.
        * [`Create shape from mesh`](https://www.youtube.com/watch?v=_lbkuSu_c9w): Crear objetos a partir de mallas 3D. El resumen del procedimiento sería:
            * Importar STL
            * Pasar al banco de trabajo `Part`
            * `Part > Create shape from mesh`
            * `Part > Convert to solid`
            * `Part > Refine shape`
        * [`Create simple copy`](https://www.youtube.com/watch?v=9a6rE8XzIgE)
        * [`Measure`](https://www.youtube.com/watch?v=mkTZ-6UI2ts): ![Linear](/images/pages/freecad/part_measure_linear.png) ![Angular](/images/pages/freecad/part_measure_angular.png)
    * `Sketcher`:
        * `Tools`: ![Point](/images/pages/freecad/sketcher_point.png) ![Line](/images/pages/freecad/sketcher_line.png) [![Arc](/images/pages/freecad/sketcher_arc.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Circle](/images/pages/freecad/sketcher_circle.png)](https://www.youtube.com/watch?v=bA06HZKR40E) ![Polyline](/images/pages/freecad/sketcher_polyline.png) ![Rectangle](/images/pages/freecad/sketcher_rectangle.png)
        * `Fillet`: [![Fillet](/images/pages/freecad/sketcher_fillet.png)](https://www.youtube.com/watch?v=ntNaY2O2v4w) Redondea un vértice de un plano.
        * `Trim`: [![Trim](/images/pages/freecad/sketcher_trim.png)](https://www.youtube.com/watch?v=V0eLXQoFYmM) Recorta las líneas sobrantes de un plano.
        * `Create edge`: [![Create edge](/images/pages/freecad/sketcher_create_edge.png)](https://www.youtube.com/watch?v=n0OcbjvGdlM) Crea linea de referencia en base a una arista de un objeto externo al sketch.
        * `Toggles to/from construction mode`: [![Construction Mode](/images/pages/freecad/construction_mode.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4) Alterna un objeto entre el modo normal y el auxiliar.
        * `Constraints`: [![Coincident](/images/pages/freecad/constraint_coincident.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Fix](/images/pages/freecad/constraint_fix.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4) [![Vertical](/images/pages/freecad/constraint_vertical.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Horizontal](/images/pages/freecad/constraint_horizontal.png)](https://www.youtube.com/watch?v=dVg5uBciurs) ![Parallel](/images/pages/freecad/constraint_parallel.png) [![Perpendicular](/images/pages/freecad/constraint_perpendicular.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Tangent](/images/pages/freecad/constraint_tangent.png)](https://www.youtube.com/watch?v=lalGueRwZfU) [![Equality](/images/pages/freecad/constraint_equality.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Symmetry](/images/pages/freecad/constraint_symmetry.png)](https://www.youtube.com/watch?v=bA06HZKR40E) [![Horizontal distance](/images/pages/freecad/constraint_horizontal_distance.png)](https://www.youtube.com/watch?v=dVg5uBciurs) [![Vertical distance](/images/pages/freecad/constraint_vertical_distance.png)](https://www.youtube.com/watch?v=dVg5uBciurs) ![Fix length](/images/pages/freecad/constraint_fix_length.png) [![Radius](/images/pages/freecad/constraint_radius.png)](https://www.youtube.com/watch?v=bA06HZKR40E) [![Angle](/images/pages/freecad/constraint_angle.png)](https://www.youtube.com/watch?v=Q-fzfRTVhg4)
