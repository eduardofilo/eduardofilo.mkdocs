---
layout: default
permalink: /sistemas/router_xiaomi.html
---

# Router Xiaomi MiWiFi 3G

## Enlaces

* [Serie de artículos de Carlos Monge sobre OpenWRT instalado en Xiaomi MiWiFi 3G](https://elblogdelazaro.gitlab.io/tags/openwrt/)
* [Página del router en OpenWRT](https://openwrt.org/toh/xiaomi/mir3g): Incluye instrucciones para debrick.
* [Xiaomi WiFi Router 3G](https://forum.openwrt.org/t/xiaomi-wifi-router-3g/5377): Hilo del foro OpenWRT sobre el Xiaomi MiWiFi 3G router.
* [Xiaomi Wifi Router 3G - 18.06.X / feedback and help](https://forum.openwrt.org/t/xiaomi-wifi-router-3g-18-06-x-feedback-and-help/19840): Hilo del foro OpenWRT sobre el firmware 18.06 en el Xiaomi MiWiFi 3G router.
* [Things to do after installing Linux LEDE 17.01](https://tutorials.technology/tutorials/44-things-to-do-after-installing-linux-LEDE-17_01.html)

## Actualización firmware

Siguiendo [este artículo](https://elblogdelazaro.gitlab.io/articles/openwrt-actualizar-firmware/):

1. Bajar el paquete pinchando uno de los enlaces siguientes según si se desea la versión de desarrollo o la estable de la [página de soporte del router en OpenWRT](https://openwrt.org/toh/hwdata/xiaomi/xiaomi_miwifi_3g):
    * Estable: Firmware OpenWrt Upgrade URL
    * Desarrollo: Firmware OpenWrt snapshot Upgrade URL
2. En el interfaz web (Luci) acudir a la ruta `System > Backup / Flash Firmware`.
3. En la sección `Flash new firmware image` pulsar el botón `Examinar...` y seleccionar el fichero .tar bajado en el punto anterior.
4. Pulsar el botón `Flash image...`.
5. En la siguiente página confirmar el flasheo comprobando si se quiere los checksums.
6. Cuando termine el proceso habremos perdido los paquetes adicionales. Instalarlos conectando por SSH y ejecutando los siguientes comandos:

        # opkg update
        # opkg install luci
        # opkg install luci-ssl
        # /etc/init.d/uhttpd start
        # /etc/init.d/uhttpd enable
7. Si se desea la interfaz en español (no se aconseja), instalar también:

        # opkg install luci-i18n-base-es

## Configuración desde cero

1. Instalar Luci:

        # opkg update
        # opkg install luci
        # opkg install luci-ssl
        # /etc/init.d/uhttpd start
        # /etc/init.d/uhttpd enable

2. Descarga de paquetes por HTTPS:

    1. Instalar:

            # opkg update
            # opkg install ca-certificates

    2. Editar el fichero `/etc/opkg/distfeeds.conf` y cambiar http por https.

3. Crear usuario normal y permitirle usar sudo:

    1. Ejecutar:

            # opkg update
            # opkg install shadow-useradd
            # useradd miusuario
            # passwd miusuario
            # mkdir /home
            # mkdir /home/miusuario
            # chown miusuario:miusuario /home/miusuario
            # opkg install sudo

    2. Editar el fichero `/etc/passwd` y poner shell al usuario nuevo:

            miusuario:x:1000:1000::/home/miusuario:/bin/ash

    3. Ejecutar el comando `visudo` y añadir la siguiente línea bajo la correspondiente a root:

            miusuario ALL=(ALL) ALL

4. Desactivar ping:

    1. En Luci ir a la ruta `Network > Firewall`
    2. Abrir la solapa `Traffic Rules`
    3. Desactivar las reglas (desmarcando el check) `Allow-Ping`, `Allow-ICMPv6-Input` y `Allow-ICMPv6-Forward`
    4. Pulsar el botón `Save & Apply` abajo a la derecha

5. Bloquear la publicidad desde el fichero hosts:

    1. Iniciar sesión SSH.
    2. Hacer backup de fichero hosts:

            $ sudo cp /etc/hosts /etc/hosts.bkp

    3. Editar crontab de root con comando `sudo crontab -e` y añadir la siguiente línea:

            0 */12 * * * wget -O /etc/hosts https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts; cat /etc/hosts.bkp >> /etc/hosts

    4. Hay varias configuraciones posibles para el fichero hosts descritas [aquí](https://github.com/StevenBlack/hosts).

## Configuración de ProtonVPN

Siguiendo [esta guía](https://stitchroads.blogspot.com/2017/11/how-to-setup-protonvpn-openvpn-on.html).

Antes de empezar es recomendable hacer un backup de la configuración del router por si es necesario volver a empezar.

1. Instalación de paquetes (el comando siguiente instala además los siguientes paquetes dependientes `kmod-tun liblzo zlib libopenssl`):

        $ sudo opkg install luci-app-openvpn openvpn-openssl

2. Creamos un nuevo interface para lo que en Luci vamos a `Network > Interfaces`.
3. Pulsamos el botón `Add new interface...`.
4. En el formulario que aparece rellenamos los siguientes campos:

    * `Name of the new interface`: openvpn
    * `Protocol of the new interface`: Unmanaged
    * `Cover the following interface`: Custom Interface: "tun0"

5. Pulsar el botón `Submit`.
6. Seleccionar la pestaña `Advanced Settings`.
7. Marcar la opción `Bring up on boot`.
8. Seleccionar la pestaña `Firewall Settings`.
9. En el desplegable `Create / Assign firewall-zone` crear una zona con nombre `vpn`.
10. Pulsar el botón `Save & Apply`.
11. Ir a la sección `Network > Firewall`.
12. Los siguientes cambios son muy sensibles, por lo que muestro un pantallazo del estado de las zonas antes de los cambios:

    ![firewall-zones](/images/pages/firewall-zones.png)

13. En la zona `wan` cambiar `Input` y `Forward` a `drop` y desmarcar los checks `Masquerading` y `MSS clamping`.
14. En la zona `vpn` cambiar `Input` y `Forward` a `drop` y marcar los checks `Masquerading` y `MSS clamping`.
15. Pulsar el botón `Save & Apply`.
16. Pulsar el botón `Edit` de la zona `lan`.
17. En la sección `Inter-Zone Forwarding` abrir el desplegable `Allow forward to destination zones` y marcar la sección `vpn` y desmarcar `wan`.

    ![forward-to-destination](/images/pages/forward-to-destination.png)

18. Pulsar el botón `Save & Apply`
19. Pantallazo de cómo deberían de quedar las zonas:

    ![firewall-zones](/images/pages/firewall-zones_end.png)

20. Descargar el perfil `.ovpn` deseado de la sección "Downloads" de nuestro perfil en ProtonVPN seleccionando como plataforma `Router` y protocolo `UDP`. Vamos a suponer que el fichero se llama `is-es-01.protonvpn.com.udp.ovpn`.
21. Editar el fichero y modificar la línea que contiene el parámetro `auth-user-pass` dejándola como sigue:

        auth-user-pass '/etc/openvpn/protonvpn/auth'

22. Transferir el fichero descargado al router y situarlo en la ruta `/etc/openvpn/protonvpn` (habrá que crear el directorio `protonvpn`).
23. Ir a la sección "Account" de nuestro perfil en ProtonVPN y tomar nota de los valores de "OpenVPN/IKEv2 Username" y "OpenVPN/IKEv2 Password".
24. Crear en el router el fichero `/etc/openvpn/protonvpn/auth`, editarlo y escribir en la primera línea el username anterior y en la segunda el password.
25. Editar en el router el fichero `/etc/config/openvpn` y añadir las siguientes líneas:

        config openvpn 'protonvpn'
            option config '/etc/openvpn/protonvpn/is-es-01.protonvpn.com.udp.ovpn'
            option enabled '1'

26. Reiniciar el servicio openvpn en el router:

        $ sudo /etc/init.d/openvpn restart

27. Ir a `Network > Interfaces > LAN` y en el parámetro `Use custom DNS servers` dejar únicamente la IP `10.8.8.1` (en caso de utilizar OpenVPN por protocolo TCP usar `10.7.7.1` en su lugar).
28. Pulsar el botón `Save & Apply`.

Para mantener acceso desde el exterior de la red, estudiar [este artículo](https://www.reddit.com/r/ProtonVPN/comments/7npcjd/newbie_to_vpn_trying_to_use_rdp/).
