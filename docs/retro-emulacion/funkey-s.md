---
layout: default
permalink: /retro-emulacion/funkey-s.html
---

# FunKey S

## Instalación toolchain

Se descarga de [aquí](https://doc.funkey-project.com/developer_guide/tutorials/build_system/build_program_using_sdk/).

Una vez descomprimido, ejecutar desde el directorio donde haya quedado (por ejemplo `/home/usuario/funkey/FunKey-sdk-2.3.0`):

```
./relocate-sdk.sh
. environment-setup
sudo ln -s /home/usuario/funkey/FunKey-sdk-2.3.0 /opt/FunKey-sdk
```

## Compilación sdlretro

Se descarga de [aquí](https://github.com/DrUm78/sdlretro).

Una vez bajado el código se compila siguiendo los pasos (o ejecutando directamente) del script `package`.

## Compilación cores RetroArch

### mgba

Se descarga de [aquí](https://github.com/FunKey-Project/mgba-libretro). Se compila directamente con `make`.

### retro8

Se descarga de [aquí](https://github.com/FunKey-Project/retro8-libretro). Se compila directamente con `make`.