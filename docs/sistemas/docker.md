---
layout: default
permalink: /sistemas/docker.html
---

# Docker

## Enlaces

* [Tutorial](https://docs.docker.com/get-started/)
* [Instalación en Raspberry según uGeek](https://ugeek.github.io/blog/post/2019-02-03-instalar-docker-en-raspberry-pi-con-raspbian.html)
* [Instalación en Ubuntu de versión Community Edition](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [JDownloader 2: Download the Internet with Docker!](https://dbtechreviews.com/2020/06/jdownloader-2-download-the-internet-with-docker/)

## Instalación

### Instalación de Docker CE

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
$ sudo systemctl enable docker
$ sudo systemctl start docker
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```

Hay que reiniciar el sistema para que tenga efecto el último comando que añade el usuario al grupo `docker`.

### [Instalación de Docker compose](https://docs.docker.com/compose/install/)

Sustituir la versión por el último tag encontrado en la [página de releases del repositorio](https://github.com/docker/compose/releases). En el momento de escribir esto era la `v2.17.1`.

```bash
$ mkdir -p $HOME/.docker/cli-plugins
$ sudo curl -L "https://github.com/docker/compose/releases/download/v2.17.1/docker-compose-$(uname -s)-$(uname -m)" -o $HOME/.docker/cli-plugins/docker-compose
$ sudo chmod +x $HOME/.docker/cli-plugins/docker-compose
```

### Instalación Portainer

Cerrar y volver a abrir la consola para que se aplique el último cambio del bloque anterior.

1. Crear un directorio para almacenar la configuración:
    ```bash
    $ sudo mkdir /etc/config/portainer
    ```

2. Ejecutar el comando:
    ```bash
    $ docker run -d --name=Portainer --restart=always -p 9000:9000 -v /etc/config/portainer:/data -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer
    ```

## Comandos

### List Docker CLI commands

```bash
$ docker
$ docker container --help
```

### Display Docker version and info

```bash
$ docker --version
$ docker version
$ docker info
```

### Execute Docker image

```bash
$ docker run hello-world
$ docker run --name mi-couchdb -p 5984:5984 apache/couchdb                       # Ejecución con log
$ docker run --name mi-couchdb -d -p 5984:5984 apache/couchdb                    # Ejecución sin log (modo detached)
$ docker run --name mi-couchdb --restart=always -d -p 5984:5984 apache/couchdb   # Ejecución con reinicio si se para o reinicia el servidor
```

### List Docker images

```bash
$ docker image ls
```

### List Docker containers (running, all, all in quiet mode)

```bash
$ docker container ls
$ docker container ls --all
$ docker container ls -aq
```

### Varios

```bash
$ docker build -t friendlyhello .                     # Create image using this directory's Dockerfile
$ docker run -p 4000:80 friendlyhello                 # Run "friendlyname" mapping port 4000 to 80
$ docker run -d -p 4000:80 friendlyhello              # Same thing, but in detached mode
$ docker container ls                                 # List all running containers
$ docker container ls -a                              # List all containers, even those not running
$ docker container logs <hash>                        # Logs
$ docker container logs -f <hash>                     # Logs en tiempo real
$ docker container start <hash>                       # Arranca un contenedor
$ docker container stop <hash>                        # Gracefully stop the specified container
$ docker container kill <hash>                        # Force shutdown of the specified container
$ docker container rm <hash>                          # Remove specified container from this machine
$ docker container rm $(docker container ls -a -q)    # Remove all containers
$ docker image ls -a                                  # List all images on this machine
$ docker image rm <image id>                          # Remove specified image from this machine
$ docker image rm $(docker image ls -a -q)            # Remove all images from this machine
$ docker login                                        # Log in this CLI session using your Docker credentials
$ docker tag <image> username/repository:tag          # Tag <image> for upload to registry
$ docker push username/repository:tag                 # Upload tagged image to registry
$ docker run username/repository:tag                  # Run image from a registry
$ docker run -it username/repository:tag              # Run image from a registry in interactive mode
$ docker exec -it <hash> bash                         # Shell en un contenedor
$ docker update --restart=always <hash>               # Añadir opción de reinicio a un contenedor que ya está creado
$ docker update --restart=no <hash>                   # Quitar opción de reinicio a un contenedor que ya está creado
$ docker port <hash>                                  # Muestra el mapeo de puertos del contenedor
$ docker inspect <hash>                               # Muestra todo el JSON con la configuración del contenedor
$ docker volume prune                                 # Borra volúmenes sin uso
$ docker builder prune                                # Borra build caché de imágenes
$ docker system prune -a                              # Borra contenedores parados, networks no usadas, imágenes no usadas y build caché
```

### Diferencias entre create, start, run y exec

* `create` se ejecuta sobre una imagen. Crea pero no arranca un contenedor en base a una imagen.
* `run` se ejecuta sobre una imagen. Crea y arranca un contenedor en base a una imagen.
* `start` se ejecuta sobre un contenedor parado. Arranca el contenedor.
* `exec` se ejecuta sobre un contenedor arrancado. Ejecuta un proceso en el contenedor.

Algunos ejemplos:

* `docker create --name test-ubuntu ubuntu`: Crea un contenedor con una imagen de ubuntu y la nombra `test-ubuntu`.
* `docker run -it --name test-ubuntu ubuntu`: Crea un contenedor con una imagen de ubuntu, lo nombra `test-ubuntu` y la arranca en modo interactivo (devuelve prompt).
* `docker run -it --rm --name test-ubuntu ubuntu`: Igual que el anterior pero borrando el contenedor al terminar la sesión interactiva.
* `docker start -i test-ubuntu`: Arranca el contenedor de nombre `test-ubuntu` en modo interactivo (devuelve prompt). El contenedor debe existir previamente y debe estar parado.
* `docker exec -it test-ubuntu /bin/bash`: Ejecuta el proceso bash en el contenedor de nombre `test-ubuntu` que debe estar previamente arrancado.

## Crear volume para persistir información

Para poder recrear el contenedor sin perder la información que haya podido generar, conviene montar los distintos directorios que queremos conservar en volúmenes.

1. Crear volumen:
    ```bash
    $ docker volume create mi_volumen
    ```

2. Posteriormente incluir en el comando de arranque del contenedor `-v mi_volumen:ruta_en_contenedor` donde `ruta_en_contenedor` será la ruta dentro del contenedor que queremos "delegar" al volumen.


## Montar un contenedor Ubuntu para aislar aplicaciones

1. Creación contenedor:

    ```bash
    docker run -it --name test-ubuntu ubuntu
    ```

2. Arrancar y abrir shell:

    ```bash
    docker start test-ubuntu
    docker exec -it test-ubuntu /bin/bash
    ```

3. Instalar paquetes mínimos:

    ```bash
    apt-get update
    apt-get install vim sudo
    ```

## Crear contenedor y subirlo a Docker Hub

1. Crear Dockerfile
2. Crear repositorio en Docker hub
3. Iniciar sesión en docker

    ```
    $ docker login
    ```

4. Compilar imagen y etiquetarla

    ```
    $ docker build -t eduardofilo/rg350_buildroot .
    ```

5. Subir imagen a repositorio

    ```
    $ docker push eduardofilo/rg350_buildroot
    ```

## Imágenes recomendables

* `phusion/baseimage`: Para imágenes basadas en Ubuntu. [Documentación](https://phusion.github.io/baseimage-docker/)
* **Passenger-docker**. Varias imágenes para servidores de aplicación Ruby, Python o NodeJS. Consultar [documentación](https://github.com/phusion/passenger-docker)
