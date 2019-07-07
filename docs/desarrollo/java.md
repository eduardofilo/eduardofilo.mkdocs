---
layout: default
permalink: /desarrollo/java.html
---

# Java

## Enlaces

* [Java Decompiler](http://jd.benow.ca/)
* [Project Lombok](https://projectlombok.org/)

## Reempaquetar un jar

Para re-enlatar un jar que hemos explotado para retocar su contendido, hay que ejecutar el siguiente comando desde el directorio raíz donde descomprimimos el jar original:

```bash
$ jar cvf nombre.jar *
```

## Contar lineas

Para contar las lineas de un proyecto, lanzar desde la raíz del proyecto ( el directorio src/java de un proyecto NetBeans, por ejemplo):

```bash
$ find . -name "*.java" | xargs wc -l
```

## Imprimir callstack

Para averiguar la pila de llamadas de funciones que nos permiten llegar a la ejecución del punto que estamos revisando. Viene muy bien cuando la ejecución implica llamadas JNI ya que esa parte del código suele quedar oculta en una librería nativa (.so o .dll).

```java
for (StackTraceElement ste : Thread.currentThread().getStackTrace()) {
    Log.w(TAG, ste);
}
```

## Iterar un Map

Para el caso de un `Map<String, String>`:

```java
Iterator it = mapa.entrySet().iterator();
while (it.hasNext()) {
    Map.Entry e = (Map.Entry) it.next();
    String name = (String) e.getKey();
    String value = (String) e.getValue();
    //...
}
```

## log4j

([Fuente](http://es.wikipedia.org/wiki/Log4j))

El proyecto FHoSS utiliza la librería log4j como casi todos los proyectos Java actuales. **Log4j**  es una librería open source desarrollada en [Java](http://es.wikipedia.org/wiki/Java platform) por la [Apache Software Foundation](http://es.wikipedia.org/wiki/Apache_Software_Foundation) que permite a los desarrolladores de software elegir la salida y el nivel de granularidad de los mensajes o “logs” a tiempo de ejecución y no a tiempo de compilación como es comúnmente realizado.  La configuración de salida y granularidad de los mensajes es realizada a tiempo de ejecución mediante el uso de archivos de configuración externos. Log4J ha sido implementado en otros lenguajes como: [C](http://es.wikipedia.org/wiki/Lenguaje de programación C), [C++](http://es.wikipedia.org/wiki/C++), [C#](http://es.wikipedia.org/wiki/C Sostenido), [Perl](http://es.wikipedia.org/wiki/Perl), [Python](http://es.wikipedia.org/wiki/Python), [Ruby](http://es.wikipedia.org/wiki/Ruby) y [Eiffel](http://es.wikipedia.org/wiki/Lenguaje de programación Eiffel).


### Conceptos

#### Niveles de prioridad de los mensajes
Por defecto Log4J tiene 6 niveles de prioridad para los mensajes (debug, info, warn, error, fatal, trace). Además existen otros dos niveles extras (all y off):

*  DEBUG:  se utiliza para escribir mensajes de depuración, este log no debe estar activado cuando la aplicación se encuentre en producción.
*  INFO:  se utiliza para mensajes similares al modo "verbose" en otras aplicaciones.
*  WARN:  se utiliza para mensajes de alerta sobre eventos que se desea mantener constancia, pero que no afectan el correcto funcionamiento del programa.
*  ERROR:  se utiliza en mensajes de error de la aplicación que se desea guardar, estos eventos afectan al programa pero lo dejan seguir funcionando, como por ejemplo que algún parámetro de configuración no es correcto y se carga el parámetro por defecto.
*  FATAL:  se utiliza para mensajes críticos del sistema, generalmente luego de guardar el mensaje el programa abortará.
*  TRACE: se utiliza para mostrar mensajes con un mayor nivel de detalle que debug.
*  ALL: este es el nivel más bajo posible, habilita todos los logs.
*  OFF: este es el nivel más alto posible, deshabilita todos los logs.

#### Appenders

En Log4J los mensajes son enviados a una (o varias) salida de destino, lo que se denomina un *appender*.

Existen varios appenders disponibles y configurados, aunque también podemos crear y configurar nuestros propios appenders.

Típicamente la salida de los mensajes es redirigida a un fichero de texto *.log* (*FileAppender*, *RollingFileAppender*), a un servidor remoto donde almacenar registros (*SocketAppender*), a una dirección de [correo electrónico](http://es.wikipedia.org/wiki/correo electrónico) (*SMTPAppender*), e incluso en una [base de datos](http://es.wikipedia.org/wiki/base de datos) (*JDBCAppender*).

Casi nunca es utilizado en un entorno de producción la salida a la consola (*ConsoleAppender*) ya que perdería gran parte de la utilidad de Log4J.

#### Layouts

Es el responsable de dar un formato de presentación a los mensajes.

Permite presentar el mensaje con el formato necesario para almacenarlo simplemente en un archivo de texto *.log* (*SimpleLayout* y *PatternLayout*), en una tabla [HTML](http://es.wikipedia.org/wiki/HTML) (*HTMLLayout*), o en un archivo [XML](http://es.wikipedia.org/wiki/XML) (*XMLLayout*).

Además podemos añadir información extra al mensaje, como la fecha en que se generó, la clase que lo generó, el nivel que posee...

### Configuración

La [API](http://es.wikipedia.org/wiki/API) es totalmente configurable, ya que se realiza mediante un archivo en formato [XML](http://es.wikipedia.org/wiki/XML) o en formato Java Properties (clave=valor), generalmente llamado *log4j.properties*.

En el siguiente ejemplo implementamos un fichero properties de configuración, y configuramos dos registros.

*  CONSOLE imprimirá los mensajes en la consola por líneas (%m%n).
*  LOGFILE añadirá (append) los mensajes a un fichero (aplicacion.log), reservando los primeros 4 caracteres para los milisegundos en que se generó el mensaje (%-4r), entre corchetes quién generó el mensaje ( [%t]), cinco espacios para la prioridad del mensaje (%-5p), la categoría del mensaje (%c) y finalmente el propio mensaje junto con un retorno de carro (%m%n).

```
################################################################
### Configuración para LOCAL                                 ###
###   Nivel de trazas máximo                                 ###
###   Salida por consola y fichero                           ###
################################################################
#log4j.rootCategory=DEBUG, LOGFILE, CONSOLE

#log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
#log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
#log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
#log4j.appender.CONSOLE.layout.ConversionPattern=%-5p %c %x - %m%n

################################################################
### Configuración para DESARROLLO, PREPRODUCCION, PRODUCCION ###
###   Sólo nos interesa el nivel de ERROR                    ###
###   No hay salida de consola                               ###
################################################################
log4j.rootCategory=ERROR, LOGFILE

log4j.appender.LOGFILE=org.apache.log4j.DailyRollingFileAppender
log4j.appender.LOGFILE.file=${catalina.base}/logs/aplicacion.log
log4j.appender.LOGFILE.append=true
log4j.appender.LOGFILE.DatePattern='.'yyyy-MM-dd
log4j.appender.LOGFILE.layout=org.apache.log4j.PatternLayout
log4j.appender.LOGFILE.layout.ConversionPattern=%-4r [%t] %-5p %c - %m%n
```

Para el caso de utilizar PatternLayout, la definición de las piezas de información que se pueden incorporar al patrón se encuentra en [esta página](http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/PatternLayout.html).

Si se desea únicamente log de las clases pertenecientes a un paquete (es una forma de evitar los logs del servidor de aplicación en una aplicación J2EE), se indica de añadiendo esta línea:

```java
log4j.logger.<paquete>=<nivel_de_trazas>
```
por ejemplo:

```java
log4j.logger.es.eduardofilo.ccm=DEBUG
```
