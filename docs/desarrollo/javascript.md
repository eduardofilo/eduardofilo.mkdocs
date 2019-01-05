---
layout: default
permalink: /desarrollo/javascript.html
---

# JavaScript

## JSON
La siguiente sentencia serializa en forma de JSON cualquier objeto. Es muy útil para analizar un objeto:

```javascript
alert(JSON.stringify(object));
```

Es más limpio escribir en la consola del navegador. Aquí por ejemplo se muestra el objeto `data` de una instancia Vue.js:

```javascript
console.log(JSON.stringify(vm._data));
```

## NPM
Uso básico del gestor de paquetes de [Node.js](https://www.npmjs.com/).

Para gestionar las dependencias de paquetes en un proyecto hay que generar un fichero de seguimiento llamado `package.json`. Se genera con el comando (si añadimos la opción `-y` dará todos los valores predeterminados automáticamente, incluso recogerá los datos del repositorio git si éste ya está inicializado):

    npm init

Para descargar un paquete (por ejemplo [lodash](https://www.npmjs.com/package/lodash)) e incorporarlo al fichero `package.json` ejecutar:

    npm install lodash --save

Encontraremos que el paquete se ha descargado en un subdirectorio llamado `node_modules` e incorporado a la sección `dependencies` de `packages.json` (si no hubiéramos puesto la opción `--save` sólo se habría descargado). Si la dependencia la queremos sólo para el entorno de desarrollo (típico por ejemplo en los paquetes de testing), en lugar de `--save` pondremos `--save-dev`.

Algunos comandos útiles de npm son:

* `npm install`: Descarga todos los paquetes indicados en `package.json`.
* `npm install -g grunt-cli`: Descarga e instala el paquete indicado en global. Es lo habitual en herramientas de tipo CLI como [Grunt](https://gruntjs.com/).
* `npm ls`: Muestra los paquetes instalados.
* `npm outdated`: Muestra cuáles de los paquetes instalados están desactualizados, es decir, existen nuevas versiones.
* `npm update`: Descarga las ultimas versiones de los paquetes instalados.
* `npm show [package]@* version`: Muestra las versiones disponibles (en el repositorio npm) del paquete indicado. Por ejemplo: `npm show lodash@* version`.
* `npm uninstall lodash`: Desinstala el paquete (lo elimina de `node_modules`). Si además queremos que desaparezca de `package.json` hay que añadir la opción `--save`
