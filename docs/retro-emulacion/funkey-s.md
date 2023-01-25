---
layout: default
permalink: /retro-emulacion/funkey-s.html
---

# FunKey S

## Enlaces

* [Super Mario 64 DOS Port](https://github.com/DrUm78/sm64-funkey)

## Instalación toolchain

Prerrequisitos:

```
$ sudo apt install bash bc binutils build-essential bzip2 ca-certificates cpio cvs expect file g++ gcc git gzip liblscp-dev libncurses5-dev locales make mercurial openssh-client patch perl procps python3 python3-dev python3-distutils python3-setuptools rsync rsync sed subversion sudo tar unzip wget xxd
```

Se descarga de [aquí](https://github.com/FunKey-Project/FunKey-OS/releases/download/FunKey-OS-2.3.0/FunKey-sdk-2.3.0.tar.gz).

Una vez descomprimido, ejecutar desde el directorio donde haya quedado (por ejemplo `/home/usuario/funkey/FunKey-sdk-2.3.0`):

```
$ ./relocate-sdk.sh
$ . environment-setup
$ sudo ln -s /home/usuario/funkey/FunKey-sdk-2.3.0 /opt/FunKey-sdk
```

## Compilación sdlretro

Se descarga de [aquí](https://github.com/DrUm78/sdlretro).

Una vez bajado el código se compila siguiendo los pasos (o ejecutando directamente) del script `package`.

El OPK resultante es `libretro_funkey-s.opk`. Copiarlo a la carpeta app de la consola, crear el directorio `/mnt/FunKey/.sdlretro/cores` y poner allí los cores.

## Compilación cores RetroArch

### mgba

Se descarga de [aquí](https://github.com/FunKey-Project/mgba-libretro). Se compila directamente con `make`.

### retro8

Se descarga de [aquí](https://github.com/FunKey-Project/retro8-libretro). Se compila directamente con `make`.