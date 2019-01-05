---
layout: default
permalink: /desarrollo/svn.html
---

# SVN

## Diferencia entre dos revisiones distintas (N y M) del mismo fichero (con ruta `Path`)

```bash
$ svn diff -r N:M Path
```

## Limpiar meta-información SVN en una copia de trabajo

```bash
$ rm -rf `find . -type d -name .svn`
```

En algunos sistemas lo anterior no funciona bien si los directorios tienen espacios en el nombre. Usar en este caso:

```bash
$ find . -type d -name .svn -exec rm -rf '{}' \;
```

## Información sobre la copia de trabajo

```bash
$ svn info
```

## Redireccionar una copia de trabajo tras movimiento de repositorio

```bash
$ svn switch --relocate FROM TO [Path copia trabajo]
```

Por ejemplo:

```bash
edumoreno@walqa347:~/NetBeansProjects/MobileDesktopDemo$ svn switch --relocate svn+ssh://eduardo.moreno@172.22.1.63/var/lib/subversion/ims/MobileDesktopDemo  svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/MobileDesktopDemo .
```

## Creación de un proyecto nuevo en un repositorio

Vamos a mostrarlo con el ejemplo del proyecto `CCM` dentro de la ruta `svn.servidor.com/var/lib/subversion/ims`, siendo la ruta de la copia de trabajo `/home/edumoreno/NetBeansProjects/CCM`.

```bash
$ svn mkdir svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM -m "Creación directorio."
```

Antes de hacer el import sería interesante eliminar o mover los directorios o ficheros que no se desea que se sincronicen con el repositorio. Por ejemplo, en el caso de un proyecto NetBeans, éstos son:

*  `CCM/build`
*  `CCM/dist`
*  `CCM/nbproject/private`

Una vez eliminados o movidos hacemos el import:

```bash
$ cd /home/edumoreno/NetBeansProjects/CCM
$ svn import . svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM -m "Import inicial."
```

Ahora habría que hacer un checkout de lo que se ha subido para obtener la meta-información del repositorio:

```bash
$ cd /home/edumoreno/NetBeansProjects
$ rm -rf CCM
$ svn checkout svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/
```

Finalmente hay que hacer ajustes para que se ignoren los siguientes directorios del nuevo repositorio:

*  build
*  dist
*  nbproject/private

Esto en teoría se puede hacer con los siguientes comandos, pero aun no se ha probado:

```bash
$ cd /home/edumoreno/NetBeansProjects/CCM
$ svn propset svn:ignore 'build
dist' .
$ svn propset svn:ignore 'private' nbproject/
$ svn commit -m "Ignoramos una serie de directorios del proyecto."
```

(Nota: El retorno de carro que hay al final del primer comando `svn propset` es intencionado)

Si por algún motivo los directorios hubieran entrado por descuido en el repositorio, habría que borrarlos tanto en el servidor como en local, ya que aunque se haya establecido la propiedad svn:ignore, se seguirían sincronizando:

```bash
$ svn delete build
$ svn delete dist
$ svn delete nbproject/private
$ svn delete svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/build
$ svn delete svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/dist
$ svn delete svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/nbproject/private
$ svn commit -m "Eliminamos una serie de directorios del proyecto."
```

## Creación de un branch

Para crear el branch simplemente hay que hacer una copia del trunk sin salir del repositorio. Para ello utilizar el siguiente comando:

```bash
$ svn copy -m "Creación de branch b1_svg." svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/trunk/ svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/
```

Luego si se desea trabajar en el branch recién creado habrá que bajar una copia de trabajo con el comando siguiente:

```bash
edumoreno@walqa347:~$ cd ~/NetBeansProjects/
edumoreno@walqa347:~/NetBeansProjects$ svn checkout svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/ CCM_b1_svg
```

## Merge con el trunk

Cuando llegue el momento de hacer el merge, habrá que proceder de la siguiente forma. Como punto de partida necesitaremos una copia de trabajo del trunk:

Averiguamos la revisión en que construimos el branch. Esto se puede conseguir haciendo un log con la opción `--stop-on-copy` (que detiene la salida del comando en cuanto se detecta que la rama fue copiada o renombrada). Así, la entrada más antigua muestra lo que buscamos:

```bash
$ svn log -v --stop-on-copy svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/|tail
```

Averiguamos la última revisión que contiene cambios en el branch:

```bash
$ svn log -v --stop-on-copy svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/|head
```

Nos situamos en el directorio de la copia de trabajo correspondiente al trunk y hacemos `update`:

```bash
edumoreno@walqa347:~$ cd ~/NetBeansProjects/CCM
edumoreno@walqa347:~/NetBeansProjects/CCM$ svn update
```

Antes de hacer el `merge` se puede simular, es decir, lanzarlo sin que aplique los cambios y que sólo muestre lo que va a hacer, incorporando la opción `--dry-run`. El comando sería:

```bash
$ svn merge --dry-run -r 549:634 svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/
```

Una vez que estemos seguros hacemos el `merge` indicando la release inicial del branch como origen del intervalo de releases:

```bash
$ svn merge -r 549:634 svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/
```

Resolvemos manualmente los conflictos que inevitablemente existirán.

Hacemos el commit en el trunk de los cambios del branch recién incorporados:

```bash
$ svn commit -m "Merge de los cambios r549:634 del branch 'b1_svg' sobre el trunk."
```

## Análisis de diferencias ante un conflicto

Para listar los ficheros que tienen conflictos:

```bash
$ svn status|grep "^C"
```

Para listar los ficheros diferenciales de un conflicto:

```bash
$ ls -l <fichero_base>*
```

La interpretación de los sufijos que se añaden a los ficheros es (siendo MMMM la release de creación del branch y NNNN la del momento del merge):

*  `<fichero_base>`: Fichero de merge
*  `<fichero_base>.copia-de-trabajo`: Última versión de la copia destino del merge (normalmente el trunk)
*  `<fichero_base>.derecha-fusion.rNNNN`: Última versión de la copia origen del merge (normalmente el branch)
*  `<fichero_base>.izquierda-fusion.rMMMM`: Versión común a ambas ramas, es decir, el punto del tiempo en que empezaron a diferenciarse

Para obtener una descripción de las diferencias habidas sobre la rama destino (normalmente el trunk):

```bash
$ diff <fichero_base>.izquierda-fusion.rMMMM <fichero_base>.copia-de-trabajo
```

Para obtener una descripción de las diferencias habidas sobre la rama origen (normalmente el branch):

```bash
$ diff <fichero_base>.izquierda-fusion.rMMMM <fichero_base>.derecha-fusion.rNNNN
```

## Borrado de la rama

Si una vez hecho el merge no se va a continuar trabajando en el branch, se puede considerar su borrado. Esto se hace con la simple orden siguiente:

```bash
$ svn delete svn+ssh://eduardo.moreno@svn.servidor.com/var/lib/subversion/ims/CCM/branches/b1_svg/
```
