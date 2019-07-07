---
layout: default
permalink: /desarrollo/php.html
---

# PHP

## Configuración

Se pueden cambiar los ajustes de PHP para el sitio por medio del fichero de configuración de Apache. Ver página 244 del libro "Desarrollo Web con PHP 6 y MySQL 5.1".

## Cadenas

Se pueden definir de tres formas:
##### Con comillas simples

```php
<?php
$cadena = 'Esto es una cadena.';
```

Para incluir el caracter comilla simple hay que escaparlo:

```php
<?php
$cadena = 'Esto es una comilla: \'.';
```

##### Con comillas dobles

Permiten incluir variables:

```php
<?php
$i = 12;
$cadena = "Un año tiene $i meses.";
```

También permite escapar una serie de caracteres como:

*  \": Comilla doble
*  \n: Retorno de carro
*  \t: Tabulador
*  \$: Símbolo de dolar

##### En bloque

Ejemplo:

```php
<?php
$i = 12;
$cadena = <<<CADENA
Esto es una cadena
definida en bloque.
Podemos utilizar variables como
en las cadenas de comillas dobles.
Esto es un ejemplo: $i.
CADENA;
```

## Volcado de variables

*  `var_dump($var);`: Para variables normales
*  `print_r($array);`: Para arrays
*  `CVarDumper::dump($param, 10, true);`: Sólo en Yii

## Comparadores

Debido a la flexibilidad de PHP con los tipos de datos, los comparadores normales (`==` por ejemplo) pueden producir resultados erróneos si no forzamos que además del valor se compare el tipo. Por ejemplo la función `strpos()` devuelve 0 si se encuentra la subcadena al principio y FALSE si no lo encuentra, pero en PHP, ambos tienen el mismo significado. El operador `==` compara si la expresión de la izquierda y la derecha tienen el mismo valor, mientras que `===` compara además que sean del mismo tipo. Así se distingue 0 (entero) de FALSE (lógico). [Aquí](http://php.net/manual/es/language.operators.comparison.php) se encuentra la documentación completa de los operadores de comparación.
