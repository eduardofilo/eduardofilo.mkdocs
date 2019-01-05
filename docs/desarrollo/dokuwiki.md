---
layout: default
permalink: /desarrollo/dokuwiki.html
---

# Dokuwiki

## Thumbnail's automáticos de imágenes

Para ello basta con instalar en el servidor PHP que ejecute DokuWiki el módulo GD para PHP. En Ubuntu el paquete se llama `php5-gd`.

## Template Monobook

Hay un template que proporciona el mismo interfaz que el de MediaWiki (Wikipedia) a DokuWiki. Se trata de [Monobook](http://tatewake.com/wiki/projects:monobook_for_dokuwiki).

### Instalación

Además de instalar la plantilla y configurarla, es necesario instalar el plugin [Display Wiki Page](http://www.dokuwiki.org/plugin:displaywikipage).

### Cambios recientes

Se puede añadir al menú de herramientas el enlace "Cambios recientes" haciendo lo siguiente:

* Añadir las siguientes lineas al fichero `$DOKU_BASE/lib/tpl/monobook/context.php`:

```php
$monobook['defaulttoolbox']['recent']['href'] = DOKU_BASE."doku.php?do=recent";
$monobook['defaulttoolbox']['recent']['text'] = $lang['monobook_recent'];
$monobook['defaulttoolbox']['recent']['rel'] = "nofollow";
```
* Inmediatamente antes de la linea (en la versión de 2007-10-03 es la linea #354):

```php
$monobook['defaulttoolbox']['whatlinkshere']['href'] = DOKU_BASE."doku.php?id=".$ID."&amp;do=backlink";
```
* Añadir la linea siguiente al fichero `$DOKU_BASE/lib/tpl/monobook/lang/es/lang.php`:

```php
$lang['monobook_recent'] = "Cambios recientes";
```

### Índice

Se puede añadir al menú de herramientas el enlace "Índice" haciendo lo siguiente:

* Añadir las siguientes lineas al fichero `$DOKU_BASE/lib/tpl/monobook/context.php`:

```php
$monobook['defaulttoolbox']['index']['href'] = DOKU_BASE."doku.php?do=index";
$monobook['defaulttoolbox']['index']['text'] = $lang['monobook_index'];
$monobook['defaulttoolbox']['index']['rel'] = "nofollow";
```
* Inmediatamente antes de la linea (en la versión de 2007-10-03 es la linea #354):

```php
$monobook['defaulttoolbox']['whatlinkshere']['href'] = DOKU_BASE."doku.php?id=".$ID."&amp;do=backlink";
```
*Añadir la linea siguiente al fichero `$DOKU_BASE/lib/tpl/monobook/lang/es/lang.php`:

```php
$lang['monobook_index'] = "Índice";
```

### Logo

El logo que aparece arriba a la izquierda es el fichero `logo.png` que se encuentra en el directorio `$DOKU_BASE/lib/tpl/monobook/user`. El icono que aparece en la barra de dirección del navegador es el fichero `favicon.ico` del mismo directorio.

## Backup automático

Programar diariamente el script siguiente:

```bash
#!/bin/bash

# Backup de IMSWiki.

# Creamos un identificador con la fecha para diferenciar los backups
fecha=`date +%m%d`

# Si el fichero ya existe no repetimos el backup
if [ -f $HOME.backupWiki/backupWiki$fecha.tgz ]; then
        echo "El backup ya existe"
        exit
fi

# Hacemos el backup sobre el servidor
ssh aire@192.168.11.3 tar -czvf /tmp/backupWiki$fecha.tgz /var/www/data/

# Lo copiamos a nuestra máquina
scp aire@192.168.11.3:/tmp/backupWiki$fecha.tgz $HOME/.backupWiki

# Borramos el bote recien creado y que ya ha sido transmitido a nuestra máquina
ssh aire@192.168.11.3 rm /tmp/backupWiki$fecha.tgz

# Purgamos los backups de hace más de un mes en nuestra máquina
find $HOME/.backupWiki -name 'backupWiki*.tgz' -mtime +30 -type f|xargs rm -rf
```

El script anterior tal y como está diseñado deposita el backup sobre el directorio `$HOME/.backupWiki` por lo que deberá existir dicho directorio. La programación se puede hacer de muchas maneras (por ejemplo en Gnome añadiendo una entrada al panel de control Sesiones, solapa "Programas de inicio").
