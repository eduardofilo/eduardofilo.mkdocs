title: RG350 Mirror de pantalla
summary: Streaming de pantalla con la consola RG350.
date: 2020-06-25 12:45:00

## Compilación de https://github.com/eduardofilo/stream350client

1. Instalar Docker en máquina host:

    ```
    $ sudo apt install docker.io
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER
    $ sudo systemctl enable docker
    $ sudo systemctl start docker
    ```

2. Bajar el código del cliente:

    ```
    $ cd ~/git
    $ git clone git@github.com:eduardofilo/stream350client.git
    ```

3. Arrancar contenedor pasando el directorio `~/git` como volumen:

    ```
    $ docker run -it -v ~/git:/root/git --name buster_bash debian:buster-slim
    ```

4. Ya en la terminal dentro del contenedor (se nota porque ahora el prompt es de superuser), hacemos algunos ajustes en el sistema e instalamos paquetes:

    ```
    # export TZ=Europe/Madrid
    # ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
    # apt-get update && apt-get -y -o Dpkg::Options::="--force-confold" upgrade
    # apt-get install -y nuget mono-devel mono-xbuild
    # nuget update -self
    ```

5. Nos situamos en el directorio donde está el código y compilamos:

    ```
    # cd ~/git/stream350client
    # nuget restore
    # xbuild stream350client.sln
    ```
