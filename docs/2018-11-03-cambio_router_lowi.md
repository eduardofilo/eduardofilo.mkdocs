title: Cambio de router con Lowi
summary: Sustitución de router Lowi por Xiaomi MiWiFi 3G con OpenWRT.
date: 2018-11-03 18:00:00
draft: true

Sustitución de router Lowi por Xiaomi MiWiFi 3G con OpenWRT.

## Enlaces

* [Cambiar Router Lowi H 500-S por otro](https://bandaancha.eu/foros/cambiar-router-lowi-h-500-s-otro-1729084)
* [Como conseguir admin del router Sercomm H500-s de Vodafone después de la telecarga](https://bandaancha.eu/articulos/conseguir-admin-router-sercomm-h500-s-9602)

## Procedimiento

1. Apagar el ONT.
2. Resetear el router manteniendo el botón de reset durante 20 segundos.
3. Conectar con el router (http://192.168.0.1) y entrar con el usuario:
    * user: `admin`
    * pwd: `l033i-h500s`
4. Acceder a la pestaña `Staus & Support` y dentro de ella seleccionar la sección `Port Mirroring` (abajo del todo).
5. Introducir el comando `-i ppp1` y pulsar `Start`.
6. Conectamos el PC a la boca 1 del router, abrimos Wireshark y empezamos a caputurar el interfaz Ethernet (`eth0` normalmente).
7. Encendemos el ONT y esperamos a tener salida a internet.
8. Detenemos la captura y la guardamos.
9. Buscamos un paquete de tipo `HTTP/XML` 200 OK que contenga la cadena `InternetGatewayDevice.X_Management.LoginAccount.1.Password`. Éste será el nuevo password del usuario `admin` del router (en lugar del predeterminado `l033i-h500s`).
10. Conectar con el router (http://192.168.0.1) y entrar con el usuario:
    * user: `admin`
    * pwd: El obtenido del parámetro `InternetGatewayDevice.X_Management.LoginAccount.1.Password` de la captura.
11. Ir al menú `Configuración > WAN > WAN FIBER > FTTh-Data_NEBA` y pinchar en el lápiz para editar. En la página que aparece tenemos los parámetros de nuestra conexión. El único dato que no podemos obtener de aquí es el password ya que está encriptado. Hay que obtenerlo de la captura Wireshark, concretamente el parámetro con el identificador `InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.2.Password`. El resto de parámetros son:
    * Description: FTTH-Data_NEBA
    * Used For: Data only
    * NAT: Sí
    * Firewall: Sí
    * 802.1P Priority [0-7]: 0
    * 802.1Q VLAN ID [0-4094]: 24
    * Connection Type: PPPoE
    * Username: El obtenido del parámetro `InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.2.Username` de la captura.
    * Password: El obtenido del parámetro `InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.2.Password` de la captura.
    * Service Name:
    * Authentication Method: AUTO
    * Connection Trigger: AlwaysOn
    * LCP Echo request interval (sec): 10
    * LCP Echo retry times: 5
    * MTU [68-1500]: 1492
    * Idle Time (sec): 0
    * Obtain DNS Servers automatically: Sí
12. En el nuevo router introducimos estos datos. En un OpenWRT sería en la sección `Network > Interfaces > WAN > Edit`. Introducimos los siguientes valores:
    * Protocol: `PPPeE`
    * PAP/CHAP username: El obtenido del parámetro `InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.2.Username` de la captura.
    * PAP/CHAP password: El obtenido del parámetro `InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.2.Password` de la captura.
    * A partir de aquí los parámetros están en `Advanced Settings`.
    * LCP echo failure threshold: `5`
    * LCP echo interval: `10`
    * Override MTU: `1492`
13. Finalmente acudir a la sección `Network > Switch` para poner el VLAN ID 24 necesario para la conexión. Concretamente dejar la tabla que allí vemos de la siguiente forma:

| VLAN ID | CPU (eth0) | LAN 1      | LAN 2      | WAN     |
|---------|------------|------------|------------|---------|
| 1       | tagged     | untagged   | untagged   | off     |
| 24      | tagged     | off        | off        | tagged  |
