---
layout: default
permalink: /cursos/phonegap.html
---

# Apuntes Curso Phonegap

Profesor: [@ciberado](https://github.com/ciberado)

## Días 1 a 5: 18/11/2014 -> 24/11/2014

### Enlaces

* [Presentación sobre Phonegap](https://www.pue.es/website/contents/events/2014/phonegap/slides/#/ "PHONEGAP 3.3. Primeros pasos y algo más")
* [Freelance Corner](http://freelancecorner.org/): Listas de distribución de proyectos para freelancers.
* [Socrative](http://www.socrative.com/): Gestor de aula (tests de profesor a alumnos).
* [Brackets](http://brackets.io/): Editor de código.
* [10 trucos para mejorar la terminal de Windows](http://www.emezeta.com/articulos/mejorar-terminal-windows)
* [JSLint](http://www.jslint.com/):Chequeador sintaxis JS.
* [Cursos MongoDB](https://university.mongodb.com/courses/catalog)
* [Microjs](http://microjs.com/#): Microjs: Fantastic Micro-Frameworks and Micro-Libraries for Fun and Profit!
* [Leaflet](http://leafletjs.com/): An Open-Source JavaScript Library for Mobile-Friendly Interactive Maps.
* [Vídeos de Douglas Crockford](https://www.google.es/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=douglas+crockford&tbm=vid) (evangelizador JavaScript).
* [Emmet](http://emmet.io/): Plugin para Brackets. Macros para crear documentos fácilmente.
* [Beautify](https://github.com/drewhamlett/brackets-beautify): Plugin para Brackets para formatear la indentación automáticamente.
* [Mockable](http://www.mockable.io/): Para construir mocks de web services.
* Proveedores de WebServices:
  * [Digital Ocean](https://www.digitalocean.com/)
  * [AWS](http://aws.amazon.com/es/): Una máquina micro (estilo Raspberry Pi) gratis durante un año.
  * [AWS Lambda](http://aws.amazon.com/es/lambda/)
  * [Google AppEngine](https://cloud.google.com/appengine/): Gratis hasta un umbral. [Especial](http://wedevelopers.com/2014/11/06/we-developers-036-google-app-engine/) sobre AppEngine de We.Developers.
* [DonDominio.com](http://www.dondominio.com/): Proveedor de dominios recomendado por alumno curso.
* [json.org](http://json.org/): Definición/documentación de JSON.
* [Firefox REST Easy addon](https://addons.mozilla.org/en-US/firefox/addon/rest-easy/): Cliente de servicios REST para testeos.
* [jQuery](http://jquery.com/): Librería Javascript.
* [Angular](https://angularjs.org/): Framework Javascript.
* [CanIUse](http://caniuse.com/): Indica las tecnologías soportadas por los distintos navegadores.
* [W3C TRs](http://www.w3.org/TR/): Listado de estándares y borradores del W3C.
* [Mozilla Developer Network](https://developer.mozilla.org/es/): Alternativa al W3C para consultar la documentación de HTML.
* [DevDocs](http://devdocs.io/): Filtrado de la documentación MDN.
* [Jade](http://jade-lang.com/) y [HAML](http://haml.info/): Alternativas a HTML.
* [JSFiddle](http://jsfiddle.net/): Prototipos HTML/CSS/JS.
* [Transit](http://ricostacruz.com/jquery.transit/): Plugin jQuery para animaciones.
* [Adobe Color CC](http://color.adobe.com): Ruedas cromáticas.
* [Express](http://expressjs.com/): Fast, unopinionated, minimalist web framework for Node.js
* [Heroku](https://www.heroku.com/): Cloud Application Platform con soporte a Node.js

### Instalación entorno

Módulos necesarios:

* JDK (instalado en `C:\jdk1.8`)
  * Poner en el PATH: `C:\jdk1.8\bin`
* [Ant](http://ant.apache.org/) (instalado en `C:\ant`)
  * Poner en el PATH: `C:\ant\bin`
* Android SDK (instalado en `C:\android-sdk`)
  * Definir variable de entorno `ANDROID_HOME` con: `C:\android-sdk`
* [Node](http://nodejs.org/) ([en Ubuntu](https://github.com/creationix/nvm))
* Phonegap: `npm install -g phonegap`
* [Genymotion](http://www.genymotion.com/): Emulador Android (muy rápido).
* [Vagrant](https://www.vagrantup.com/) (opcional): Empaquetador de entornos de desarrollo

### Creación de proyecto Phonegap

```bash
$ phonegap create 00HolaMundo --name HolaMundo --id es.eduardofilo.hm
```

### Compilación y ejecución de proyecto Phonegap

```bash
$ cd 00HolaMundo
$ phonegap build android
$ phonegap run android
```

En realidad la tarea `run` hace `build`.

### Inspeccionar dispositivos externos en Chrome

    about:inspect

### REST WebServices

Servidor mock ([mockable](http://www.mockable.io/)): demo0034470.mockable.io

* *url*: http://demo0034470.mockable.io/votaciones/38/yes
* *type*: POST
* *dataType*: json

Respuesta:

```json
{
	"votosTotal": 6000,
	"votosPositivos": 3500,
	"votosNegativos": 2500,
	"fecha": "2013-04-17T12:32:12"
}
```

### jQuery

Hay una convención por la cual cuando invocamos jQuery ($) para localizar un elemento del DOM, la variable donde se carga se pone con el prefijo $. Por ejemplo:

```javascript
var $paragrafos = $('p');
```

#### Ejemplo1

```javascript
var $paragraphs = $('p');
for (var i=0; i < $paragraphs.length ; i++) {
    console.log(i, $paragraphs[i]);
}
$paragraphs.css('color', 'red');
$paragraphs.css('background-color', 'green');

$paragraphs.css({'color': 'blue',
                 'background-color': 'yellow'});

console.log($paragraphs.css('color'));
$firstp = $('p:first');
//$firstp = $('p').first();
//$firstp = $('p').eq(0);
$firstp.addClass('importante');
```

#### Ejemplo2

```javascript
var $firstp = $('p:first');
var texto = $firstp.text();
$firstp.text(texto.toUpperCase());
//var $strong = $('<strong>');
//$strong.text('contenido');
//$firstp.prepend($strong);

$('<strong>')
    .text('contenido')
    .prependTo($firstp);
```

#### Ejemplo3

```javascript
var colores = ['Rojo', 'Verde', 'Azul'];
var $ol = $('ol');
$ol.empty();
for (var i=0; i<colores.length; i++) {
    $ol.append($('<li>').text(colores[i]));
    //$('<li>').text(colores[i]).appendTo($ol);
}
```

#### Ejemplo4

```javascript
$('p').on('click', function(evt) {
    evt.preventDefault();
    $(this).css('background-color', 'green');
});
```

#### Ejemplo5

```javascript
$('p').on('click', function(evt) {
    $(this).fadeOut(function() {
        $(this).text($(this).text().toUpperCase());
        $(this).fadeIn();
    });
});
```

## Día 6: Martes 25/11/2014

### Enlaces
 
* [Git](http://git-scm.com/)
* [SourceTree](http://www.sourcetreeapp.com/): GUI de Git.
* [La parábola de git](https://www.youtube.com/watch?v=sXudMl5x_5g): Vídeo interesante.
* [gitflow](http://danielkummer.github.io/git-flow-cheatsheet/): Patrón de uso de git.
* [Yeoman](http://yeoman.io/): Plantillas/Scaffolding.
* [Webapp](https://github.com/yeoman/generator-webapp): Plantilla de Yeoman para webapps.
* [Grunt](http://gruntjs.com/): Gestor de tareas.
* [Gulp](http://gulpjs.com/): Gestor de tareas. Equivalente a Grunt. Está de moda ahora.
* [Bower](http://bower.io/): Gestor de librerías (como npm pero a nivel de librerías JS, tipo leaflet o bootstrap). Depende de git.

### Montaje de entorno y workflow

1. Bajamos el instalador de git y lo instalamos. Durante la instalación, en una página del asistente, marcamos la tercera opción que lleva una leyenda en rojo.
2. Inicializamos el proyecto local:
  * `mkdir 06YesNoGit`
  * `cd 06YesNoGit`
  * `git init`
3. Entramos con nuestra cuenta (o creamos una) en GitHub y creamos un repositorio con el mismo nombre que el local (`06YesNoGit`).
4. Creamos un "remote" desde el git local hacia GitHub:
  * `git remote add origin https://github.com/eduardofilo/06YesNoGit.git`
5. Sincronizamos:
  * `git pull origin master`
6. Modificamos un fichero en local (.gitignore), lo commiteamos en local y sincronizamos con GitHub:
  * `git add .gitignore`
  * `git commit -m "Primer commit"`
  * `git push origin master`
7. Inicializamos gitflow en SourceTree (pulsando el botón de la toolbar).
8. Instalamos Bower (la opción g lo instala en global, es decir accesible desde todos los proyectos):
  * `npm install -g bower`
9. Grunt no se suele instalar de forma global porque cambia mucho de versión. Vamos a instalar algo que ejecuta el grunt local del proyecto:
  * `npm install -g grunt-cli`
10. Instalamos Yeoman:
  * `npm install -g yo`
11. Si falla la descarga de algún paquete, es mejor no reejecutar yeoman. Se habrá generado un fichero `package.json` que contiene los paquetes npm que necesitamos. Ejecutando lo siguiente se bajará lo que falte:
  * `npm install`
12. Si `npm install` nos da warnings se puede solucionar inicializando npm (que genera el fichero `package.json`):
  * `npm init`
13. Instalamos la plantilla webapp de Yeoman:
  * `npm install -g generator-webapp`
14. En este punto tenemos todas las herramientas instaladas.
15. “Start New Feature” en gitflow@SourceTree. Le damos el nombre “InicializarConYeoman”.
16. Generamos un proyecto con la plantilla webapp de Yeoman:
  * `yo`
  * Instalamos “webapp”
  * Incluimos las librerías Bootstrap y Modernizr
  * Hacemos overwrite de `.gitignore`
17. Lanzamos los tests para probar Grunt:
  * `grunt test`
18. Compilamos con Grunt:
  * `grunt build`
19. Aparece el directorio `dist` con la versión final (lista para desplegar) de nuestro proyecto.
20. Arrancamos un servidor web para probar el proyecto:
  * `grunt serve`

## Día 7: Miércoles 26/11/2014

### Enlaces
 
* [Phonegap developer app](http://app.phonegap.com/): Sincroniza la app desplegada por Phonegap en el teléfono o en Genymotion para pasar los cambios directamente sin necesidad de volver a desplegar.
* [Genymotion with Google Play Services](https://gist.github.com/wbroek/9321145): Instalación de Google Play Services en Genymotion.

### Bower

La diferencia con npm es que éste instala cosas en máquina; Bower añade librerías al proyecto. Lo vamos a manejar con los siguientes comandos por terminal:
 
* `bower search leaflet`: Busca las librerías que contienen “leaflet”.
* `bower install --save leaflet`: Instala la librería leaflet. La opción `--save` hace que se apunte en un fichero de referencia de librerías (`bower.json`) para luego no tener que subir las librerías al control de versiones (evitaríamos subir el directorio `bower_components`, que es donde se almacenan las librerías instaladas y sus dependencias). Es parecido al `package.json` de npm.
* `grunt wiredep`: Conecta las dependencias. Por ejemplo vincula los ficheros CSS de las librerías en la posición del comentario `<!-- bower:css -->` del fichero `index.html`. Los CSS de las librerías que había instaladas previamente (bootstrap y modernizr) se habían conectado cuando instalamos la plantilla webapp con yeoman. Esta tarea está incluida en la tarea `build`.
* `bower uninstall --save leaflet`: Desinstala la librería leaflet.

### Grunt

El fichero de configuración tiene forma de script Javascript. Es el fichero `Gruntfile.js`.

### git

Vamos a hacer el merge de la feature que creamos ayer en la rama develop:

1. SourceTree / Commit / Marcamos “Unstage all” para pasar a stage todos los ficheros modificados / Incluimos el comentario del commit en la caja de abajo.
2. SourceTree / Gitflow / Finish Feature (marcamos Delete branch)
3. SourceTree / Push (marcamos las dos ramas: develop y master)

### Phonegap app developer

1. Se instala en el emulador o dispositivo la aplicación.
2. Se abre la aplicación “PhoneGap” en el dispositivo o emulador.
3. Se configura poniendo la URL que aparece al arrancar el servidor phonegap en la máquina de desarrollo:
  * `phonegap serve`

## Día 8: Jueves 27/11/2014

### Enlaces

* [Fundation](http://foundation.zurb.com/): Framework CSS basado en em. Bootstrap está basado en px.
* [QuirksMode](http://www.quirksmode.org/about/): Peter Paul Koch. Buscar sus conferencias sobre display.
* [Media Queries](http://mediaqueri.es/): Catálogo de sitios responsive.
* [Swwweet](http://www.swwweet.com/): Estudio de Barcelona con buena filosofía web.
* [CSS Zen garden](http://www.csszengarden.com/): Juego para modificar con CSS un HTML fijado desde hace años.
* [Pedro Arilla](http://pedroarilla.com/es/): Especialista en tipografía de Zaragoza.
* [Fontsinuse](http://fontsinuse.com/): Galería de sitios con tipografía interesante.
* [Unos tipos duros](http://www.unostiposduros.com/): Teoría y práctica de la tipografía.
* [Font Awesome](http://fortawesome.github.io/Font-Awesome/): 479 iconos vectorizados. Recomendado por Merche.

### CSS

Siguiendo la [lección sobre CSS del curso de HTML5 de Javier](https://github.com/ciberado/javiermoreno-dominahtml5-intro/tree/master/05_css).

#### Unidades de medida

`em` es una de las más interesantes. Procede del mundo de la tipografía y es la anchura de la M mayúscula en un tamaño que se considera legible con facilidad por un usuario normal. Las `em` se basan en el tamaño de letra del elemento y son relativas entre elementos que se contienen, es decir, si un elemento tiene `2em` pero está afectado por un contenedor en el que se aplica `2em`, el tamaño resultante será equivalente a `6em`. Para evitar la acumulación está la unidad `rem` (=root em).

#### Preferencias

Hay un orden de prioridad entre los selectores de CSS. Algunos detalles:
 
* Prioridades generales de menos a más: Reglas definidas por el navegador (useragent stylesheet rules) -> Reglas que seleccionan elementos -> Reglas que seleccionan atributos (`id` o `class`).
* `id` prioriza sobre `class`.
* `!important` se salta las prioridades, es decir se aplica siempre.

#### Position

`top` y `left` no aplican si `position` es `static`. El `position: absolute` toma el origen de coordenadas del primer contenedor que no es `static`.

#### Display

El `display` de un `div` por defecto (useragent stylesheet rules) es `block`. El de `span` es `inline`. Se puede modificar tanto un caso como el otro. Por ejemplo si ponemos `display: inline` a un `div`, pasa a comportarse como un `span`. El `display: inline` hace que se ignore el `width`. Con `display: inline-block` sí que se tiene en cuenta el `width`. Hay un truco para conservar la indentación en el código HTML mientras se evita que se introduzca un carácter espacio que ocupa sitio y descoloca la maquetación y es introducir un comentario entre líneas de esta forma:

```html
   <section>
   …
   </section><!--
--><section>
   …
   </section>
```

#### Float

La propiedad `clear` sólo funciona si el `display` no es `inline`. Se usa mucho el apaño del clearfix para solucionar la pérdida de dimensión vertical de un contenedor cuando todo su contenido más alto flota. El selector `:after` selecciona después del contenido al que se aplica el estilo, no el contenido del siguiente elemento en el DOM. El clearfix favorito de Javier es:

```css
.clearfix:after {
    content: ".";
    visibility: hidden;
    display: block;
    height: 0;
    clear: both;
}
```

#### viewport

Diferencia entre layout-viewport y display-viewport. La relación entre ambos es el nivel de zoom. El layout-viewport predeterminado es 960px. Se definió pixel-ratio cuando apareció iPhone 4, inicialmente con un valor de 2 (pantalla retina de 640px de ancho por los 320px del iPhone original). Terminales con pantallas QuadHD tienen un pixel-ratio de alrededor de 4. Tiene el inconveniente de que hace que las imágenes se redimensionen, lo que en terminales con mucha densidad de pixel produce desenfoque. La solución es enviar la imagen adecuada a cada dispositivo. De momento se hace con condiciones en CSS.

#### mediaqueries

Permite hacer condiciones en CSS. `@media` es un if. En las mediaqueries los `em` son siempre `rem` es decir son absolutos, no relativos. Más que hablar de resoluciones debemos pensar en tamaños. Se suelen considerar cuatro tamaños:
 
* Móvil: 360 px CSS
* Tablet: 768 px CSS
* Desktop: 1200 px CSS
* TV

### Tipografía

La tipografía cada vez tiene más importancia. Para pantalla, Javier no recomienda Helvetica. Existen muchos tipos buenos, muy legibles y gratuitos, como:

* [Mozilla Fira](https://www.mozilla.org/en-US/styleguide/products/firefox-os/typeface/)
* [Ubuntu](http://font.ubuntu.com/)
* [Google OpenSans](http://www.google.com/fonts/specimen/Open+Sans)

Javier recomienda no descartar las fuentes de pago. La inversión puede tener un impacto muy importante en el proyecto. Algunas foundries:

* [Typekit](https://typekit.com/): Foundry de Adobe.
* [Google Fonts](http://www.google.com/fonts): Foundry de Google.

Nos describe el uso de [Google Fonts](http://www.google.com/fonts) usando el sitio para definir un paquete con dos fuentes.

### Frameworks

Algunos framewoks:

* [Bootstrap](http://getbootstrap.com/): es el más importante ahora mismo. El favorito de Javier, sobre todo por su ecosistema.
* [Bootsnipp](http://bootsnipp.com/): Componentes para bootstrap.
* [Foundation](http://foundation.zurb.com/)
* [Skeleton](http://getskeleton.com/)
* [Ionic](http://ionicframework.com/): Perfecto para pantallas pequeñas.
* [Ratchet](http://goratchet.com/): También para móviles.
* [Sencha Touch](http://www.sencha.com/products/touch/): Para móviles. No recomendado por Javier.
* [jQuery Mobile](http://jquerymobile.com/): No recomendado por Javier.

## Día 9: Viernes 28/11/2014

### Enlaces

* [UI Bootstrap](http://angular-ui.github.io/bootstrap/): Bootstrap adaptado a Angular.
* [Bootsnipp](http://bootsnipp.com/): Galería de elementos para Bootstrap.
* [Couchbase Mobile](http://www.couchbase.com/nosql-databases/couchbase-mobile): Plugin Phonegap para tener una base de datos noSQL local con opción de sincronizar con el servidor.

### Bootstrap

En [Customize](http://getbootstrap.com/customize/) se puede compilar una versión personalizada (sólo con los componentes que vayamos a utilizar, lo que además hace más pequeña la librería). Dentro de este Customize se pueden cambiar por ejemplo los Media queries breakpoints que son los que hacen que el diseño cambie entre los distintos tamaños de pantalla.  
Es recomendable instalarlo con Bower si se va a integrar en Phonegap (para tenerlo en local y minimizar la latencia que supondría el descargarlo).  
El menú superior del sitio de Bootstrap está bien estructurado en cuanto a la dificultad de menor a mayor de izquierda a derecha. Conviene leer por lo menos la sección [Getting Started](http://getbootstrap.com/getting-started/).  
Bootstrap utiliza CDN para minimizar la latencia.  
Si vamos a utilizar Angular, en lugar de poner bootstrap normal hay que integrar UI Bootstrap que no utiliza jQuery.  
Es importante meter en la cabecera lo siguiente (aparece en [Basic Template](http://getbootstrap.com/getting-started/#template)):

```html
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Importante leer todo el [documento sobre CSS](http://getbootstrap.com/css/), sobre todo lo relativo al [Grid System](http://getbootstrap.com/css/#grid) y a los [Forms](http://getbootstrap.com/css/#forms).  
Los componentes que no encontremos en Bootstrap buscarlos en [Bootsnipp](http://bootsnipp.com/).  
Si utilizamos la parte de JS de Bootstrap hay que integrar jQuery.

### Buenas prácticas con Bootstrap

Interesa poner siempre un label en los campos de formulario por accesibilidad, pero en pantallas pequeñas se suele usar un placeholder, lo que es redundante. Para evitarlo se oculta añadiendo la clase `sr-only` (sr de Screen Reader), lo que mantiene el label en el código pero no lo muestra.

### JavaScript

Almacenamiento de un conjunto de variables en localStorage:

```javascript
var l1 = ["Alice", "Bob", "Charly"];
var l2 = [1, 2, 3]
var listas = { listaPrincipal: l1, listaSecundaria: l2};
var listasComoCadena = JSON.stringify(listas);
localStorage.setItem('listas', listasComoCadena);
```

### Deberes para el fin de semana
 
* Landing page con tres zonas y call for action superior (= jumbotron).
  * Qué hacemos
  * Por qué somos buenos
  * Pasta
* Repasar [Closures de JS](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Closures).


## Día 10: Lunes 1/12/2014

### Enlaces

* [famo.us](http://famo.us/): Free, open source JavaScript framework that helps you create smooth, complex UIs for any screen.
* [EggHead](https://egghead.io/): Screencasts.

### Proyecto

Vamos a montar el proyecto poniéndolo todo junto desde cero:

1. Creamos el proyecto dentro del directorio \curso:
  * `cd \curso`
  * `phonegap create 10Votaciones --name Votaciones --id es.eduardofilo.yesno`
2. Nos metemos en el directorio y lanzamos Yeoman para instalar la plantilla web:
  * `cd 10Votaciones`
  * `yo`
3. Durante la configuración de Yeoman indicamos que incluya Bootstrap.
4. Configuramos en Gruntile.js (línea 21 del fichero que la carpeta de la aplicación es `www` en lugar de `app` que es la que viene por defecto.
5. Movemos carpeta `10Votaciones\www\res` a `10Votaciones\res`, es decir un nivel hacia arriba. Esta carpeta contiene los recursos que utilizará Phonegap (por ejemplo el icono de escritorio que ajustará en las distintas plataformas). No tiene mucho sentido que esté dentro de `www` ya que Phonegap duplicará hacia el directorio `dist` los recursos correspondientes a la plataforma con la que estemos trabajando. Si está en `www` es porque cuando utilizamos el servidor de compilación de Adobe para montar las aplicaciones nativas, sólo pasamos el directorio `www` y el que contenga `res` es una forma de enviar todo de una vez.
6. Configuramos en `config.xml` el movimiento del directorio `res` que acabamos de hacer. Para ello sustituimos las rutas de los recursos, es decir `www/res` por `res`.
7. Borramos el contenido de `www` y lo sustituimos por el de `app`.
8. Borramos la carpeta `app` que ha quedado vacía.
9. Movemos la carpeta `bower_components` al interior de `www`.
10. Cambiamos la configuración de Bower en el fichero `.bowerrc` poniendo `www/bower_components` donde sólo ponía `bower_components`.
11. Finalmente lanzamos la tarea que inyectará las dependencias entre los ficheros de código:
  * `grunt wiredep`

Con esto ya tendríamos la base.

Vamos a utilizar el patrón MVC. Pondremos tanto el modelo como el controlador en el mismo fichero `main.js`, aunque sería más correcto separarlo.

Vamos a hacer una Single Page Application. Cada página “virtual” de la app lo vamos a codificar mediante un `div` de clase `pagina`. Ese div tendrá un atributo personalizado “data-title” que contendrá el título de la página. El controlador sólo va a hacer:

* Reacciona a la pantalla
* Modifica la pantalla

Todo lo que no tenga que ver con esto irá al modelo/servicio.

## Día 11: Martes 2/12/2014

### Enlaces

* [history.js](https://github.com/browserstate/history.js/)

### Proyecto

Vamos a programar el envío del voto al servidor (mockable) en un POST. El voto va en la URL por lo que aunque utilicemos https no ocultamos la información. Sería más correcto enviar el voto en el cuerpo del POST, por ejemplo:

```javascript
var url = this.URL_POST_NUEVO_VOTO.replace('{value}', tipoDeVoto);
var promesa = $.post(url, {value: ‘yes’});
```

En segundo lugar programamos la gestión de la navegación, es decir cómo cambia la aplicación de pantalla, ya sea hacia delante o hacia atrás (incluyendo por ejemplo el evento “Back” del dispositivo que equivale al botón “Atrás” del navegador). Javier nos comenta el truco de añadir anchors (#) a la URL. Con esto se consigue que no se recargue el documento y que sí afecte al historial. Como nuestra app es SPA nos viene muy bien este truco. En Phonegap, la tecla “Atrás” de los dispositivos equivale al Back del WebView. La gestión del historial la vamos a hacer con [history.js](https://github.com/browserstate/history.js/).

1. Buscamos/instalamos history.js con Bower (`--save` actualiza el fichero `bower.json` con lo que hacemos que la inclusión de este componente sea persistente, es decir, si luego borramos los componentes, para no subirlos al control de versiones por ejemplo, lo podremos recuperar fácilmente):
  * `bower search history`
  * `bower install --save history.js`
2. Inyectamos dependencias (`grunt wiredep` no funciona => hay que mirar en la documentación). Elegimos la librería que nos conviene consultando la documentación. En `index.html` incluimos la referencia en el bloque `scripts/main.js` del `build.js` final:
  * `<script src="bower_components/history.js/scripts/bundled/html4+html5/native.history.js"></script>`

Con history.js manejamos el historial del navegador/webview por medio del objeto `History`. El objeto `history` sería la parte nativa del navegador. En muchas ocasiones se comportan igual.

Los parámetros de la función `pushState` tanto de `history` como de `History` son:

```javascript
history.pushState({
    id: idDestino
}, $('#' + idDestion).attr('data-title'), idDestion);
```

1. Objeto arbitrario en el que podemos almacenar datos
2. Descripción o Título de esa entrada en el historial 
3. Dirección/URL

## Día 12: Miércoles 3/12/2014

### Enlaces
 
* [Using Location Hash To Enable BACK/FORWARD Navigation](https://developers.google.com/tv/web/articles/location-hash-navigation)
* [Web Fundamentals](https://developers.google.com/web/fundamentals/): Cómo adaptar experiencias web a dispositivos de distintos tamaños.
* [seen.js](http://seenjs.io/): Render 3D scenes into SVG or HTML5 Canvas.
* [jQuery-Color](https://github.com/jquery/jquery-color/): Animaciones con colores.
* [Removing the 300ms tap delay in Chrome 32](https://www.youtube.com/watch?v=AjUpiwvIa5A): Se hace con la librería [fastclick](https://github.com/ftlabs/fastclick).
* [QuoJS](http://quojs.tapquo.com/): Librería de gestures.
* [HammerJS](http://hammerjs.github.io/): Librería de gestures.
* [TouchSwipe-Jquery-Plugin](https://github.com/mattbryson/TouchSwipe-Jquery-Plugin): Librería de swipes.
* [iScroll](http://cubiq.org/iscroll-5): Librería para gestionar listas y los eventos físicos de arrastre.
* [CancelBubble](https://twitter.com/cancelBubble): Cuenta de Twitter que comenta muchas librerías buenas.
* [r/javascript](http://www.reddit.com/r/javascript): Subreddit de Javascript en el que comentan también librerías.
* [Q](http://documentup.com/kriskowal/q/): Librería js para la gestión de promesas.

### Proyecto

`document` recibe todos los eventos. Implementamos un cartel “Cargando…” que aparece/desaparece cuando hay peticiones AJAX mientras se espera la respuesta del servidor. Se gestiona mediante los eventos `ajaxStart` y `ajaxStop`.

Instalamos [jQuery-Color](https://github.com/jquery/jquery-color/) para hacer un efecto de transición al jumbotron:

1. Buscamos/instalamos:
  * `bower search jquery-color`
  * `bower install --save jquery-color`
2. Inyectamos la librería a mano al final del index.html ya que Bower no puede:
  * `<script src="bower_components/jquery-color/jquery.color.js"></script>`

Hasta ahora había algo mal en el proyecto. No esperábamos a que cargara el DOM ni jQuery. Para conseguirlo envolvemos la función de inicialización de la siguiente forma:

```javascript
$(document).ready(function () {
    controlador.inicializar();
});
```

Vemos una forma de [desactivar](http://stackoverflow.com/questions/12665511/eliminate-tap-highlight-in-windows-phone-7) el highlight en el tap que hace el sistema operativo en WindowsPhone. Se consigue añadiendo la siguiente etiqueta `meta` en el `head` del HTML:

```html
<meta name="msapplication-tap-highlight" content="no"/>
```

Vamos a programar un gesto para volver a la pantalla de votaciones desde resultados.  
Instalamos [TouchSwipe-Jquery-Plugin](https://github.com/mattbryson/TouchSwipe-Jquery-Plugin):

1. Buscamos/instalamos:
  * `bower search touchswipe`
  * `bower install --save jquery-touchswipe`

Sustituimos el servicio votar para que guarde en local. Hay que generar promesa. Se puede hacer con la librería [Q](http://documentup.com/kriskowal/q/) o con [jQuery](http://api.jquery.com/category/deferred-object/). Lo hacemos así:

```javascript
var servicioPreguntas = {
    //...

    votar: function (tipoDeVoto) {
        localStorage.setItem('voto', tipoDeVoto);
        var deferred = $.Deferred();
        var promesa = deferred.promise();
        deferred.resolve({
            total: 0,
            positives: 0,
            negatives: 0
        });
        return promesa;
    }
};
```

## Día 13: Jueves 4/12/2014

### Enlaces
 
* [Documentación Phonegap Command Line](http://docs.phonegap.com/en/4.0.0/guide_cli_index.md.html#The%20Command-Line%20Interface)
* [Documentación Phonegap Plugins API](http://docs.phonegap.com/en/4.0.0/cordova_plugins_pluginapis.md.html#Plugin%20APIs)
* [Repositorio de Cordova Plugins](http://plugins.cordova.io/)
* [La estafa de la linterna molona que ilumina más en Android](http://www.elladodelmal.com/2014/01/la-estafa-de-la-linterna-molona-que.html)
* [InfoTelefonoPlugin](https://github.com/ciberado/domina-phonegap-infotelefonoplugin): Plugin de Javier para obtener datos de identificación del teléfono.

### Proyecto Plugins

Vamos a hacer una pequeña aplicación para consultar la geolocalización:

1. Creamos el proyecto:
    1. `cd \curso`
    2. `phonegap create 13GeoDemo --name GeoDemo --id es.eduardofilo.geodemo`
2. Añadimos el plugin de geolocalización:
    1. `cd 13GeoDemo`
    2. `phonegap plugin add org.apache.cordova.geolocation`

Buscar el código nativo para Android en [git](https://git-wip-us.apache.org/repos/asf?p=cordova-plugin-geolocation.git;a=tree;f=src/android;h=d2223b59460ffc4e37333908e5ff0daec1ca1951;hb=7393e84b319fe3dd65d047f23b1051b1067e6b3b).

Javier no recomienda getCurrentPosition porque da timeout rápidamente si estás en HighAccuracy. Mejor con watchPosition.

Vamos a ver cómo se crearía un plugin. Para ello instalamos un plugin hecho por Javier y estudiamos detenidamente su sencillo código:

1. Creamos el proyecto:
    1. `cd \curso`
    2. `phonegap create 13.1DatosTelefono --name DatosTelefono --id es.eduardofilo.datostfn`
2. Añadimos el [plugin de Javier](https://github.com/ciberado/domina-phonegap-infotelefonoplugin):
    1. `cd 13.1DatosTelefono`
    2. `phonegap plugin add https://github.com/ciberado/domina-phonegap-infotelefonoplugin.git`

## Día 14: Viernes 5/12/2014

### Enlaces
 
* [Cordova Device Motion Plugin](http://plugins.cordova.io/#/package/org.apache.cordova.device-motion)
* [MakeAppIcon](http://makeappicon.com/)
* [Web2Splash](https://github.com/mwbrooks/web2splash)
* [Pastebin de Javier](http://pastebin.com/u/javi)
* [Adobe PhoneGap Build](https://build.phonegap.com/)
* [c9](https://c9.io/): IDE web.

### Proyecto Plugins

Continuamos con el proyecto de ayer:

3. Comprobamos la instalación:
    1. `phonegap plugin list`

### Proyecto Acelerómetro

Vamos a hacer un pequeño proyecto que controlará un pequeño cuadrado por pantalla con los acelerómetros del teléfono. En el proyecto haremos uso del [plugin oficial de Phonegap](http://plugins.cordova.io/#/package/org.apache.cordova.device-motion) que se encarga de acceder al dispositivo.

1. Creamos el proyecto:
    1. `phonegap create 14DemoAcelerometro --name DemoAcelerometro --id es.eduardofilo.demoaccel`
2. Instalamos plugin:
    1. `phonegap plugin add org.apache.cordova.device-motion`

Por defecto `watchAcceleration` llama al callback cada 10 segundos:

```javascript
var watchID = navigator.accelerometer.watchAcceleration(
      accelerometerSuccess,
      accelerometerError,
      accelerometerOptions);
```

* **accelerometerOptions**: An object with the following optional keys:
  * **period**: requested period of calls to accelerometerSuccess with acceleration data in Milliseconds.(Number) (Default: 10000)

Para conseguir que la aplicación sea más "responsiva", se puede cambiar el periodo de consulta pasando un objeto con un parámetro de clave frecuency en su interior (aunque la documentación menciona `period`, es `frecuency`). Hubiera funcionado cada segundo por ejemplo llamando al watchAcceleration así:

```javascript
var options = { frequency: 1000 };
var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
```

### Subir a Google Play

Para generar un certificado con que firmar las aplicaciones:

```bash
$ keytool -genkey -alias demoiconos -keyalg RSA -validity 20000 -keystore demoiconos.keystore
```

### Compilar en Adobe PhoneGap Build

Para delegar la construcción del proyecto en el [servicio de compilación de Adobe en la nube](https://build.phonegap.com/):

```bash
$ phonegap remote build android
```
Se puede firmar la aplicación desde Adobe subiendo el fichero keystore que hemos creado antes.

### Inicialización del controlador

Si usamos jQuery:

```javascript
$(document).ready(function () {
    document.addEventListener('deviceready', function () {
        controlador.inicializar();
    });
});
```

Si no usamos jQuery:

```javascript
document.addEventListener('deviceready', function () {
    controlador.inicializar();
});
```

### Pendiente de preguntar

* [JSONP vs CORS](http://stackoverflow.com/questions/12296910/so-jsonp-or-cors)
* Workspaces en Chrome.
