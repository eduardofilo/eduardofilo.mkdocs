---
layout: default
permalink: /sistemas/ubuntu_phone.html
---

# Ubuntu Phone

## Enlaces

* [Installing Ubuntu](https://developer.ubuntu.com/en/phone/devices/installing-ubuntu-for-devices)
* [Install Android On BQ Aquaris Ubuntu Phone In Linux](https://itsfoss.com/install-android-ubuntu-phone/)

## Activar SSH

    sudo service ssh start
    sudo setprop persist.service.ssh true
    sudo reboot

## Permitir cambios en /

    sudo mount -o remount,rw /

## Ejecutar en modo desktop

    gsettings set com.canonical.Unity8 usage-mode Windowed

## Retornar a interfaz teléfono

    gsettings set com.canonical.Unity8 usage-mode Staged
