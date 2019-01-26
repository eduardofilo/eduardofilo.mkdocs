title: 2019-01-26 Conversión del sitio de Apuntes a MkDocs
summary: Migración del motor de apuntes de Rubi/Jekyll a Python/MkDocs.
date: 2019-01-26 19:00:00

Migración del motor de apuntes de Rubi/Jekyll a Python/MkDocs.

## Procedimiento
1. Renombro el antiguo repositorio construido con Jekyll de `eduardofilo.github.io` a `eduardofilo.jekyll` para dejar libre el repositorio que contendrá el nuevo sitio.
2. Creo directorio:
        $ mkdir ~/git/eduardofilo.mkdocs
        $ cd ~/git/eduardofilo.mkdocs
3. Creo entorno Python3 con pipenv:
        $ pipenv install --three
4. Instalo mkdocs, el tema [Material](https://squidfunk.github.io/mkdocs-material/) y algunas [extensiones](https://squidfunk.github.io/mkdocs-material/extensions/admonition/):
        $ pipenv install mkdocs pygments mkdocs-material
5. Instalo versión beta de módulo pyyaml por un aviso de seguridad que da GitHub sobre la versión 3.13 que se instala normalmente. Para ello añado lo siguiente al fichero `Pipfile` en la sección `[packages]`. Tras ello ejecuto `pipenv install`:
        pyyaml = ">=4.2b1"
6. Arranco shell en el entorno:
        $ pipenv shell
7. Creo el proyecto mkdocs desde el directorio anterior:
        $ cd ..
        $ mkdocs new eduardofilo.mkdocs
        $ cd eduardofilo.mkdocs
8. Copio los directorios con los contenidos del sitio Jekyll (`cursos`, `desarrollo`, `images`, `proyectos`, `sistemas` y `varios`) al directorio `docs`.
9. Configuro el fichero `mkdocs.yml` con el siguiente contenido:

        # Project information
        site_name: Apuntes de eduardofilo
        site_description: Apuntes varios sobre algunas de las cosas que necesito recordar, principalmente sobre Desarrollo y         Sistemas.
        site_author: Eduardo Moreno Lamana

        # Repository
        repo_name: 'eduardofilo.mkdocs'
        repo_url: https://github.com/eduardofilo/eduardofilo.mkdocs

        # Configuration
        use_directory_urls: false
        plugins:
            - search:
                lang: ['es']
        theme:
            name: material
            logo: 'images/eduardofilo.png'
            language: es
            feature:
                tabs: true
            palette:
                primary: 'deep orange'
                accent: 'amber'


        # Customization
        extra:
            social:
                - type: github-alt
                  link: https://github.com/eduardofilo
                - type: twitter
                  link: https://twitter.com/eduardofilo
                - type: linkedin
                  link: https://linkedin.com/in/edumoreno/
                - type: tumblr
                  link: https://eduardofilo.es
                - type: youtube
                  link: https://www.youtube.com/c/EduardoMorenoLamana
            search:
                language: 'es'
            manifest: 'manifest.webmanifest'

        # Extensions
        markdown_extensions:
            - codehilite:
                linenums: true
            - toc:
                permalink: True
            - admonition

10. Copio todos los ficheros del directorio `_posts` de Jekyll al directorio `docs`.
11. Modifico cada uno de los posts que allí hay de la siguiente manera:
    1. Retiro los delimitadores del YAML, es decir los tres guiones que hay al principio y al final del bloque.
    2. Retiro las propiedad `layout` y `published` y añado una llamada `summary`.
12. Genero estructura de navegación en bloque `nav:` al final de `mkdocs.yml`
13. Creo fichero `CNAME` dentro del directorio `docs` con el nombre del dominio personalizado.
14. Creo repositorio en GitHub con nombre `eduardofilo.github.io`.
15. Creo copia de trabajo del repsitorio anterior:

        $ cd ~/git
        $ git clone git@github.com:eduardofilo/eduardofilo.github.io.git

16. Finalmente publico el sitio ejecutando el siguiente comando desde el directorio de trabajo del repositorio anterior:

        $ cd ~/git/eduardofilo.github.io
        $ mkdocs gh-deploy --config-file ../eduardofilo.mkdocs/mkdocs.yml --remote-branch master

Falta crear un RSS con el [feed](http://apuntes.eduardofilo.es/feed.xml) que generaba Jekyll antiguamente.
