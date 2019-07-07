---
layout: default
permalink: /desarrollo/eclipse.html
---

# Eclipse

## Cambio de tipo de letra del editor

Acceder al siguiente elemento de las preferencias: "General / Appearence / Colors and Fonts". Desplegar el lenguaje que se esté utilizando en el proyecto (Java por ejemplo). Seleccionar el elemento "Java Editor Text Font" y pulsar el botón "Change".

## Atributos de ficheros XML uno por linea

*  [Fuente](http://www.androidpolice.com/2009/11/04/auto-formatting-android-xml-files-with-eclipse/)

Acceder al siguiente elemento de las preferencias: "XML / XML FIles / Editor". Seleccionar el elemento "Split multiple attributes each on a new line".

## Columnas admitidas por el indentador automático

Por defecto Eclipse admite 80 columnas de texto cuando se aplica el formateador automático (Comando/Ctrl + Shift + F). Para cambiar este valor hay que acudir a la siguiente ruta en Preferencias:

	Java / Code Style / Formatter

Aquí hay que crear un profile nuevo que podamos editar (dado que los predeterminados son de sólo lectura). Una vez creado (nos podemos basar en el predeterminado de nombre "Eclipse [built-in]") iremos a:

	Edit... / Line Wrapping / General settings / Maximun line width

Y le daremos el valor deseado (120 en mi caso). Para reforzar la situación de ese límite, podemos cambiar el siguiente ajuste en preferencias y darle el mismo valor (120 en mi caso):

	General / Editors / Text Editors / Print margin column (previamente hay que activar "Show print margin")
