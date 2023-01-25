---
layout: default
permalink: /retro-emulacion/funkey-s.html
---

# FunKey S

## Links

* [Super Mario 64 DOS Port](https://github.com/DrUm78/sm64-funkey)

## Toolchain installation

Prerequisites:

```
$ sudo apt install bash bc binutils build-essential bzip2 ca-certificates cpio cvs expect file g++ gcc git gzip liblscp-dev libncurses5-dev locales make mercurial openssh-client patch perl procps python3 python3-dev python3-distutils python3-setuptools rsync rsync sed subversion sudo tar unzip wget xxd
```

Download from [here](https://github.com/FunKey-Project/FunKey-OS/releases/download/FunKey-OS-2.3.0/FunKey-sdk-2.3.0.tar.gz).

Once uncompressed, run from the directory where installed (for example `/home/user/funkey/FunKey-sdk-2.3.0`):

```
$ ./relocate-sdk.sh
$ . environment-setup
$ sudo ln -s /home/user/funkey/FunKey-sdk-2.3.0 /opt/FunKey-sdk
```

## sdlretro build

Download from [here](https://github.com/DrUm78/sdlretro).

Once the code is downloaded, it is compiled by following the steps (or by executing directly) of the `package` script.

The built OPK is `libretro_funkey-s.opk`. Copy `libretro_funkey-s.opk` to app folder, create `/mnt/FunKey/.sdlretro/cores` and put core files in the directory.

## RetroArch cores build

### mgba

Download from [here](https://github.com/FunKey-Project/mgba-libretro). Built directly with `make`.

### retro8

Download from [here](https://github.com/FunKey-Project/retro8-libretro). Built directly with `make`.