---
layout: default
permalink: /sistemas/trucos_windows.html
---

# Trucos Windows

## Acelerar la exploración de equipos en red e incrementar el rendimiento general
Borrar la clave siguiente ([fuente](http://www.pc-soluciones.com.ar/acelerarequiposenredxp.htm)):

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RemoteComputer\NameSpace\{D6277990-4C6A-11CF-8D87-00AA0060F5BF}
```

## Cambiar la clave de producto en Windows XP
Proceder como sigue ([fuente](http://www.pc-soluciones.com.ar/cambiarclavexp.htm)):

 1.  Ejecutar regedit y buscar la clave `HKEY_LOCAL_MACHINE\Software\Microsoft\WindowsNT\CurrentVersion\WPAEvents`
 2.  Abrir la clave oobetimer, borrar el valor hexadecimal CA, y cerrar regedit
 3.  Ir a Inicio, Ejecutar y escribir %systemroot%\system32\oobe\msoobe.exe /a
 4.  Nos aparecerá la pantalla de activación de Windows XP, seleccionar activación por teléfono, pulsar en Cambiar clave del producto e introducir la nueva clave y pulsar actualizar. (Las claves que comienzan por F o D han sido baneadas por Microsoft en el SP1)
 5.  Ejecutar de nuevo %systemroot%\system32\oobe\msoobe.exe /a, y con esto finalizará el proceso de activación



## Averiguar la clave de producto

Por medio de alguno de estos programas:

* [Magical Jelly Bean Keyfinder](http://www.magicaljellybean.com/keyfinder.shtml)
* [CD Key Reader](http://www.skaro.net/cd-keyreader/)


## Sustituir archivos en uso en Windows XP

"inuse.exe” es una herramienta que antaño formaba parte del kit de recursos de Windows 2000, y que con la liberación de Windows XP Microsoft ha decidido ponerla a disposición de forma gratuita.  
Su cometido es permitir la sustitución de archivos que estén en uso por parte del Sistema Operativo y que de otra manera no podrían ser sustituidos. Su sintaxis es:

```
INUSE origen destino /y
```

*  origen: especifica el nombre del archivo actualizado
*  destino: especifica el nombre del archivo existente que será reemplazado
*  /y elimina la petición de confirmación para reemplazar el archivo.

Nota: los cambios no surtirán efecto hasta que reiniciemos el ordenador.  
Esta utilidad junto a todas las del kit de recursos de Windows 2000 se puede obtener de [Windows 2000 Resource Kit Tools](http://support.microsoft.com/kb/927229).  
([Fuente](http://www.pc-soluciones.com.ar/sustituirarchivos.htm))

## Evitar la activación de Windows XP

Como es bien sabido Windows XP debe ser activado después de su instalación, porque de lo contrario dejará de funcionar a los 30 días. Hasta este punto todo correcto, se instala Windows XP, se activa y listo, pero el problema viene una vez que por cualquier circunstancia hay que formatear el PC o reinstalar Windows, que nuevamente tenemos que activarlo, para evitar esto debemos hacer lo siguiente ([fuente](http://www.pc-soluciones.com.ar/activacionxp.htm)):

1.  Una vez que se activa Windows XP por primera vez, se guarda un archivo en nuestro PC, este archivo debemos copiarlo y guardarlo muy bien para la siguiente vez que borremos el disco duro y así evitaremos la activación nuevamente.
2.  Sigue estos pasos para buscar y guardar el archivo que guarda las configuraciones del hardware y la activación de tu copia de Windows XP.
  * Haces clic con el botón Inicio y a continuación en Ejecutar.
  * Escribe wpa.dbl y pulsa el boton Aceptar, después de unos segundos aparecerá el archivo en el cuadro buscar.
  * Ahora fijate bien donde está el archivo (normalmente estará en el directorio C:\Windows\System32), copia este archivo en un disquete o en cualquier otro lugar del disco duro donde esté a salvo de errores y lo puedas conservar hasta que lo necesites.
3.  La próxima vez que formatees el disco duro, o por cualquier otra causa necesites activar tu copia de Windows XP simplemente copia el archivo que acabas de guardar al directorio Windows, reinicias y listo ya está activada nuevamente tu copia de Windows XP

## Evitar colapsos de conexión de red

Activar el servicio "Programador de paquetes QoS". Se puede configurar el valor de reserva de ancho de banda con:

```
gpedit.msc / Configuración del equipo / Plantillas administrativas /
Red / Programador de paquetes QoS / Limitar ancho de banda reservado
```

## Reparar registro de Windows
([Fuente](http://support.microsoft.com/kb/307545/es))

*  Arrancar con la consola de reparación del CD de instalación.
*  Copiar los archivos del registro de la versión de instalación:

```
copy c:\windows\repair\system c:\windows\system32\config\system
copy c:\windows\repair\software c:\windows\system32\config\software
copy c:\windows\repair\sam c:\windows\system32\config\sam
copy c:\windows\repair\security c:\windows\system32\config\security
copy c:\windows\repair\default c:\windows\system32\config\default
```

*  Con esta configuración se puede arrancar en Modo a Prueba de Fallos. Elegir un conjunto de archivos de un punto de restauración en la ruta:

```
C:\System Volume Information\_restore{27BBF476-A824-438F-93A9-39BC37483C34}\RPn\Snapshot
(el ClassID y el n de RPn son variables)
```

*  Copiar los siguientes ficheros a una carpeta accesible como C:\Windows\tmp renombrándolos como se indica:

```
_REGISTRY_USER_.DEFAULT -> default
_REGISTRY_MACHINE_SECURITY -> security
_REGISTRY_MACHINE_SOFTWARE -> software
_REGISTRY_MACHINE_SYSTEM -> system
_REGISTRY_MACHINE_SAM -> sam
```

*  Volver a arrancar con la consola de reparación y sustituir los ficheros de C:\Windows\tmp a c:\windows\system32\config.

## Clonado de equipos

 1.  Instalar un equipo el cual servira de modelo, una vez instalado el sistema operativo y sus parches vamos al paso 2.
 2.  Extraer el archivo DEPLOY.CAB de [CD_WIN]:\support\tools\ en directorio C:\sysprep
 3.  Ejecutar sysprep.exe para crear el sysprep.inf. Existen unos botones al ejecutar sysprep. Darle a Factory.
 4.  Instalar los programas y todo lo que utilizaran los PCs, una vez terminado esta parte le damos en la opcion de Sellar equipo en sysprep.
 5.  Hacemos la imagen con Ghost, g4u o similar.
 6.  Volcamos esta imagen en los demas PCs y sin poner el disquete de sysprep, alli vuelve a pedir los datos del Key de Windows, Nombre de PC y todo lo demas, dejando los programas listos e incluso con sus acesos directos y con el escritorio como en la imagen.

### Enlaces:
* [Guía rápida a la preinstalación de Windows](http://support.microsoft.com/default.aspx?scid=kb;es-es;314472#XSLTH3123121123120121120120)

## Comandos útiles

*  Mostrar lista de procesos con servicios asociados:

```
tasklist /svc
```

*  Lista de conexiones con PID de procesos asociados:

```
netstat -aon
```

*  Eliminar unidades de red:

```
net use /d A:
```

*  Añadir unidades de red:

```
net use A: \\Servidor\Directorio
```

*  Muestra la diferencia de hora del sistema con un servidor NTP externo:

```
w32tm /stripchart /computer:es.pool.ntp.org /samples:3 /dataonly
```

*  Utilidad de configuración del sistema (WinXP):

```
msconfig
```

## Bloqueo y desbloqueo del Registro

Para deshabilitarlo, accedemos al registro, nos situamos en HKEY_CURENT_USER/Software/Microsoft/Windows/CurrentVersion/Policies/System. En la parte de la derecha creamos un nuevo valor DWORD y le damos el nombre DisableRegistryTools, otorgándole el 1 para deshabilitar las funciones de edición del Registro.  
Una vez realizada esta operación, nadie podrá acceder a él hasta que no lo volvamos a activar. Para habilitarlo, abrimos un editor de texto y escribimos:

```
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\system] "DisableRegistryTools"=dword:00000000
```

Ahora, guardamos el archivo con el nombre unlock.reg y, a partir de ese momento, cuando queramos activar el Registro de Windows, después de haberlo deshabilitado, sólo tendremos que hacer doble clic sobre el archivo que acabamos de crear.

## Escritorio Remoto / Editar registro con comandos

La funcionalidad "Escritorio Remoto" se encuentra desactivada por defecto. Se puede activar editando el registro del ordenador que nos interese. Esto se puede hacer remotamente por medio del siguiente comando:

```
reg add \\[NombreEquipo]\HKLM\SYSTEM\CurrentControlSet\Services\PolicyAgent /V EnableRemoteMgmt /T REG_DWORD /F /D 1
```

## Edición ficheros BKS de la utilidad Copia de Seguridad

En estos ficheros se almacena la selección de directorios/ficheros que entran en el backup. Hay que respetar el formato que les da la utilidad cuando los genera. Es texto Unicode, pero si se edita con Notepad no queda exactamente en el formato esperado y luego aparece en el log el error "No se encontró el archivo de selección...". Una forma de conseguirlo es editando con Notepad, guardando en formato "Codificación: Unicode" y luego usar un editor hexadecimal para eliminar los dos primeros bytes que se incluyen con este formato.

## Procesos de inicio

En las siguientes rutas del registro:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
```

En el caso de Windows 98 y Windows ME será necesario revisar también en los 2 archivos:

```
WIN.INI
```

Son las entradas que inician con "run=" o "load="

```
SYSTEM.INI
```

Son las entradas que inician con "shell=" . Hay que tener en cuenta que la única entrada legal es shell=Explorer.exe y que algún virus podría agregar una línea del tipo shell=Explorer.exe %Windows% ombredelviruse.exe

Otro lugar donde se debería revisar son las carpetas de los programas de inicio que por ejemplo en Windows XP serán:

```
C:\Documents and Settings\tucuenta\Menú Inicio\Programas\Inicio

C:\Documents and Settings\All Users\Menú Inicio\Programas\Inicio
```

y en Windows 98 será:

```
C:\Windows\Menú Inicio\Programas\Inicio
```

([Fuente](http://www.trucoswindows.net/explicapro.html))

## Ajustes tras instalación Windows 10
Recien instalado, Windows 10 trae preconfiguradas unas cuantas cosas que estarían mejor desactivadas. [Aquí](http://www.adslzone.net/2016/06/14/9-cosas-desactivar-windows-10/) tenemos una lista de ajustes a efectuar tras la instalación o actualización.
