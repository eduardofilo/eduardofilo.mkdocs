---
layout: default
permalink: /sistemas/docker.html
---

# Docker

## Enlaces

* [Tutorial](https://docs.docker.com/get-started/)
* [Instalación en Raspberry según uGeek](https://ugeek.github.io/blog/post/2019-02-03-instalar-docker-en-raspberry-pi-con-raspbian.html)

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
$ docker exec -it <hash> bash                         # Shell en un contenedor
$ docker update --restart=always <hash>               # Añadir opción de reinicio a un contenedor que ya está arrancado
```

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
