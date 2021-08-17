---
layout: default
permalink: /desarrollo/git.html
---

# Git

## Enlaces

* [Libro Pro Git en español](http://git-scm.com/book/es)
* [Cheat Sheat](http://cheat.errtheblog.com/s/git)
* [git - la guía sencilla](http://rogerdudler.github.com/git-guide/index.es.html) :exclamation:
* [Git Tutorials & Training by Atlassian](http://atlassian.com/git) :exclamation:
* [Detached HEAD en Git](http://mundogeek.net/archivos/2015/08/11/detached-head-en-git/)
* [Github git tutorial](https://try.github.io/levels/1/challenges/1)
* [La Parábola de Git @ CAPSiDE HQ](https://www.youtube.com/watch?v=sXudMl5x_5g)
* [Lleva Git al próximo nivel con Git Flow](http://mundogeek.net/archivos/2018/10/31/lleva-git-al-proximo-nivel-con-git-flow/)
* [git-flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.es_ES.html)
* [Github Release Stats](https://somsubhra.github.io/github-release-stats/)

## Comandos básicos

Config:

```bash
$ git config --global user.name "Eduardo Moreno"
$ git config --global user.email user@dominio.com
$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.st status
$ git config --global core.editor "subl -w"
```

Alternativamente se pueden hacer todos los cambios simultáneamente editando el fichero `~/.gitconfig`. Una configuración podría ser:

```
[user]
        name = Eduardo Moreno
        email = user@dominio.com
[alias]
        co = checkout
        ci = commit
        st = status
[core]
        editor = subl -w
```

Creación repositorio (local; crea el subdirectorio `.git`):

```bash
$ cd first_app
$ git init
```

Add ([fuente](http://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add)):

```bash
# stages All
$ git add -A
# stages new and modified, without deleted
$ git add .
# stages modified and deleted, without new
$ git add -u
```

Commit:

```bash
$ git commit
```

Commit general de cambios:

```bash
$ git commit -a
```

Status:

```bash
$ git status
```

Restituir ficheros borrados:

```bash
$ git checkout -f
```

Log:

```bash
$ git log
```

Log indicando los ficheros modificados:

```bash
$ git log --name-status
$ git log --stat
```

Ficheros modificados en un branch:

```bash
$ git diff --name-status master..sip-economy
$ git diff --stat master..sip-economy
```

Log indicando los commits que afectan a un fichero ([fuente](http://stackoverflow.com/questions/3701404/list-all-commits-for-a-specific-file)):

```bash
$ git log --follow filename
```

Localizar el commit inicial de la rama `branch_name` surgida de `master` ([fuente](
http://stackoverflow.com/questions/18407526/git-how-to-find-first-commit-of-specific-branch)):

```bash
$ git log master..branch_name --oneline | tail -1
```

Rename:

```bash
$ git mv fichero.txt fichero.log
```

Preparar un servidor:

```bash
$ cd first_app/..
$ git clone --bare first_app first_app.git
$ scp -r first_app.git usuario@dominio.com:git
```

Conectar la copia de trabajo con un servidor:

```bash
$ cd first_app
$ git remote add origin usuario@dominio.com:git/first_app.git
```

(`origin` es el nombre de la conexión; puede ser cualquier cosa, aunque si se pone otra cosa habrá que especificar el nombre al hacer `push`, ya que `origin` es el nombre de destino predeterminado)

Mostrar la lista de conexiones de la copia de trabajo con servidores:

```bash
$ git remote -v
```

Desconectar la copia de trabajo con un servidor:

```bash
$ git remote rm origin
```

(`origin` es el nombre de la conexión; puede ser cualquier otro)

Checkout (remoto):

```bash
$ git clone usuario@dominio.com:git/first_app.git
```

Sincronizar con el servidor remoto:

```bash
$ git push [origin master]
```

Info (parecido a svn info):

```bash
$ cat .git/config
```

Crear un tag

```bash
$ git tag -a tag_id -m "Creación de tag tag_id."
$ git push --follow-tags
```

Eliminación de un tag

```bash
$ git tag -d tag_id
$ git push origin :refs/tags/tag_id
```

Eliminación de último commit ([fuente](http://stackoverflow.com/questions/1338728/delete-commits-from-a-branch-in-git))

```bash
$ git reset --hard HEAD~1
```

Si el commit ya ha subido al repositorio hacer además:

```bash
$ git push origin HEAD --force
```

Para olvidar cambios (incluso commits) hechos en local ([fuente](http://stackoverflow.com/questions/12845507/git-confusion-how-to-revert-local-changes-to-latest-remote-push)):

```bash
$ git reset --hard origin/master
```

## Diff's

Distintos tipos de diff's:

* working vs staging: `git diff`
* staging vs snapshot: `git diff --staged`
* working vs snapshot: `git diff HEAD`
* snapshot vs snapshot: `git diff <from_SHA1> <to_SHA1>`

Ficheros modificados entre dos commits:

```bash
$ git diff --name-only SHA1 SHA2
$ #o
$ git diff --stat SHA1 SHA2
```

Diferencias en un fichero entre dos commits:

```bash
$ git diff SHA1 SHA2 FICHERO
```

Muestra la versión de un fichero en un determinado commit:

```bash
$ git show SHA:FILE
```

## Branches

Creación:

```bash
$ git checkout -b alta-usuarios
```

Listado de branches:

```bash
$ git branch
```

Listado de branches locales y remotos:

```bash
$ git branch -a
```

Seleccionar un branch:

```bash
$ git checkout alta-usuarios
```

Sincronizar con el servidor remoto:

```bash
$ git push origin alta-usuarios
```

Seleccionar trunk:

```bash
$ git checkout master
```

Merge:

```bash
$ git checkout master
$ git merge alta-usuarios
$ git branch -d alta-usuarios
```

Abandonar y borrar un branch local:

```bash
$ git checkout master
$ git branch -D alta-usuarios
```

Borrar un branch remoto. Si después de hacer lo anterior hacemos un git pull la rama local volverá a crearse, ya que seguía estando en el servidor. Esto podemos arreglarlo de la siguiente manera:

```bash
$ git push origin :alta-usuarios #suponiendo que la rama en el servidor se llama igual que nuestra ex-rama local
```

o

```bash
$ git push origin --delete alta-usuarios
```

Seleccionar un branch remoto ([fuente](http://git-scm.com/book/ch3-5.html#Tracking-Branches)):

```bash
$ git checkout -b fix#3413 origin/fix#3413
```

## Stash

Borrado de la lista:

```bash
$ git stash clear
```

Guardar y recuperar con nombre ([fuente](http://stackoverflow.com/questions/11269256/how-to-name-and-retrieve-a-stash-by-name-in-git)):

```bash
# Guardar
git stash save nombre
# Listar
git stash list
    stash@{0}: On branch: nombre
# Aplicar
git stash apply stash@{0}
# Borrar
git stash drop stash@{0}
```

Ver los cambios que contiene un stash ([fuente](http://stackoverflow.com/questions/10725729/git-see-whats-in-a-stash-without-applying-stash)):

```bash
# Para ver el contenido del stash más reciente
git stash show -p
# Para ver el contenido de un stash en concreto
git stash show -p stash@{1}
```

## Ignorar cambios de un fichero incluido en el repositorio

([Fuente](http://stackoverflow.com/questions/6317169/using-gitignore-to-ignore-but-not-delete-files)) No se trata de la típica entrada en `.gitignore` dado que los ficheros allí listados se supone que ni siquiera forman parte del repositorio. Se trata de tener una versión del fichero en el repositorio pero luego no queremos actualizarlo. Para ello ejecutar:

```bash
git update-index --assume-unchanged <file>
```

Para averiguar los ficheros que estamos ignorando de esta forma:

```bash
git ls-files -v | grep '^h'
```

Y si en algún momento queremos recuperar la detección de cambios en el fichero:

```bash
git update-index --no-assume-unchanged <file>
```

## Salir de estado "HEAD detached at"

En este estado básicamente es que HEAD deja de apuntar al final de una rama (secuencia de commits) para apuntar a un commit concreto directamente. La forma de salir es o volver a hacer checkout de cualquier branch si no se quieren conservar los cambios hechos tras recuperar ese commit, o bien crear un branch temporal para commitear esos cambios y ya luego si se desea incorporarlos a la rama de la que nos habíamos descolgado.

A continuación se describen las dos opciones:

* Si no nos importa perder los cambios

```bash
git checkout <branch>
```

* Si hay cambios tras hacer el checkout del commit:

```bash
git checkout -b temp
git checkout <branch>
git merge temp
```

En la [fuente](http://stackoverflow.com/questions/5772192/how-can-i-reconcile-detached-head-with-master-origin) de estas ideas se describe un procedimiento más elaborado para reapuntar el `<branch>` (`master` en el ejemplo que ponen) a este nuevo branch temporal.

## Cambiar el message del último commit

([Fuente](https://help.github.com/articles/changing-a-commit-message/)) Esto sirve si aún no hemos propagado el commit hacia otros repositorios remotos:

```bash
git commit --amend
```

## gitbook

La utilidad de línea de comando para compilar los libros a `epub` por ejemplo se instala con `npm`:

```
sudo npm install gitbook-cli -g
sudo npm install svgexport -g
```

Una vez disponible, entraremos en el directorio del repositorio que contenga un gitbook y generaremos un epub:

```
$ cd git/
$ git clone https://github.com/DjangoGirls/tutorial.git
$ cd tutorial/es/
$ gitbook epub ./ ./tutorial.epub
```

## Borrar último commit

Para borrar el último commit cuando aún no lo hemos publicado (push) hacer lo siguiente ([fuente](http://aprendegit.com/como-deshacer-el-ultimo-commit-en-git/)):

```bash
$ git reset --hard HEAD~1
```

Con esto conseguimos que el puntero del branch apunte al commit anterior al HEAD actual. Es importante que el commit que vayamos a borrar sólo esté en nuestro repositorio. Si ya ha sido propagado a otros repositorios, será mejor deshacer los cambios mediante otro commit.

## Sustituir autor de todos los commits

[Fuente](https://docs.github.com/en/github/using-git/changing-author-info)

1. Crear un clon bare del repositorio

    * A partir de origen remoto (suponemos que tenemos todas las copias de trabajo en `~/git`):

        ```
        $ cd ~/git
        $ git clone --bare https://github.com/user/repo.git
        ```

    * A partir de origen local:

        ```
        $ cd ~/git
        $ git clone --bare repo repo.git
        ```

2. Nos situamos en el directorio con el repositorio bare que se acaba de crear:

    ```
    $ cd repo.git
    ```

3. Copiar y pegar en la terminal el siguiente script sustituyendo las siguientes variables por lo que corresponda:

    * `OLD_EMAIL`
    * `CORRECT_NAME`
    * `CORRECT_EMAIL`

    ```
    #!/bin/sh

    git filter-branch --env-filter '

    OLD_EMAIL="your-old-email@example.com"
    CORRECT_NAME="Your Correct Name"
    CORRECT_EMAIL="your-correct-email@example.com"

    if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
    then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
    fi
    if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
    then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
    fi
    ' --tag-name-filter cat -- --branches --tags
    ```

4. Pulsar Enter para ejecutar el script.
5. Revisar el log de Git.
6. Sincronizar los cambios al origin:

    ```
    $ git push --force --tags origin 'refs/heads/*'
    ```

7. Borrar el clon temporal:

    ```
    $ cd ..
    $ rm -rf repo.git
    ```

## Submódulos

Documentación: [Enlace 1](https://git-scm.com/book/en/v2/Git-Tools-Submodules), [Enlace 2](https://training.github.com/downloads/es_ES/submodule-vs-subtree-cheat-sheet/).

Añadir submódulo (el directorio PATH que se pone al final no debe existir):

```bash
$ git submodule add SUBMODULE_URL PATH
```

Clonar un repositorio con submódulos:

```bash
$ git clone --recursive REPO_URL       # si los submódulos tienen a su vez submódulos
$ git clone --recurse-submodules URL   # si no hay submódulos recursivos
```

Actualizar repositorio y submódulos:

```bash
$ git pull --recurse-submodules
```

## Borrar commits en repositorio remoto

Es importante recordar que si los cambios ya han sido compartidos, es decir otras personas los han sincronizado, se va a romper el histórico para estas personas. Pero si el repositorio es personal, se puede hacer lo siguiente:

1. Situarnos en el commit que nos interese:

    1. Para borrar sólo el último: `git reset HEAD^ --hard`
    2. Para borrar varios: `git reset <hash_commit> --hard`

2. Forzar los cambios en el repositorio remoto: `git push origin -f`
