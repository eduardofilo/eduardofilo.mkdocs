---
layout: default
permalink: /desarrollo/joomla.html
---

# Joomla

## Enlaces

*  [Envío de mail desde FacileForms (Joomla)](http://www.facileforms.biz/wiki/To_Changing_The_Email_Subject)

## Codificación de la página

*  La codificación de caracteres que se usa para enviar la página al navegador se ajusta en el fichero globals.php añadiendo la siguiente linea:

```php
header( 'Content-Type: text/html; charset=UTF-8');
```
*  La codificación que se informa en la sección header del código fuente html de la página se ajusta en el fichero language/spanish.php en la linea que dice:

```php
DEFINE('_ISO','charset=utf-8');
```

Ver comentario de Mitsurugi en [este foro](http://www.joomlaspanish.org/foros/showthread.php?t=261&page=3).


## allow_url_fopen desactivado

Para el problema del eWeather del tipo ([fuente](http://www.joomlaspanish.org/foros/showthread.php?t=5412)):

```
Warning: file_get_contents(): URL file-access is disabled in the server configuration in /(lo que sea)/includes/domit/xml_domit_parser.php on line 1645
```

El problema es seguramente del servidor, ya que el archivo php.ini tiene el parámetro allow_url_fopen deshabilitado. La solución es utilizar la librería cURL para evitar el uso de la función file_get_contents().

* Localizar el archivo que está en la carpeta donde esté alojado el Joomla en la siguiente ruta: /includes/domit/xml_domit_parser.php
* Editarlo e ir a la linea 1645
* En esa linea pone: return file_get_contents($filename);
* Eliminamos la línea y ponemos esto en su lugar:

```php
$ch = curl_init();
$timeout = 5;
curl_setopt ($ch, CURLOPT_URL, $filename);
curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
return curl_exec($ch);
curl_close($ch);
```
* Guardamos el archivo y lo subimos al servidor sustituyendo al antiguo.
