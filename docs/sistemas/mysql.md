---
layout: default
permalink: /sistemas/mysql.html
---

# MySQL

## Recomendaciones

*  Utilizar siempre el tipo de dato DOUBLE para los reales (pag. 125 de libro "Desarrollo Web con PHP 6 y MySQL 5.1")

## Instalación

Instalamos el paquete `mysql-server`:

```bash
$ apt-get install mysql-server
```

En caso de no haberlo configurado durante la instalación del paquete, ajustar el password de root con el comando:

```bash
$ mysql -u root
mysql> SET PASSWORD FOR 'root'@'localhost" = PASSWORD('new_password');
```

Por defecto sólo podemos entrar con el usuario root en local. Para permitir el acceso remoto ejecutar el siguiente comando:

```bash
$ mysql -u root -p
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
mysql> exit
```

También hay que permitir las conexiones remotas a nivel de red comentando la siguiente linea del fichero de configuración `/etc/mysql/my.cnf`:

	bind-address = 127.0.0.1


## Conexión

### MySQL Client
    mysql -u <usuario> -h <host> -P <puerto> <database> -p

```
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 89 to server version: 4.1.11-Debian_4-log

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>  
```

## Trabajando con Bases de Datos

### Creación de BBDD

```sql
mysql> CREATE DATABASE irontec_db;
Query OK, 1 row affected (0.03 sec)
```

### Selección de BBDD

Cambiar o elegir base de datos a utilizar:

```sql
mysql> USE irontec_db;
Database changed
```

Ver la base de datos seleccionada:

```sql
mysql> SELECT DATABASE();
+------------+
| database() |
+------------+
| irontec_db |
+------------+
1 row in set (0.00 sec)
```

### Eliminación de BBDD

```sql
mysql> DROP DATABASE irontec_db;
Query OK, 0 rows affected (0.60 sec)
```

## Trabajando con Usuarios / Privilegios

### Creación de Usuarios
Usuarios con **todos** los privilegios:

```sql
mysql> GRANT ALL PRIVILEGES ON irontec_db.* TO irontec_user_allpriv@localhost IDENTIFIED BY 'irontec_pass';
Query OK, 0 rows affected (0.14 sec)
```

Usuarios **sin privilegios** (solo introduce el usuario en la tabla `mysql.user`):

```sql
mysql> GRANT USAGE ON irontec_db.* TO irontec_user_nopriv@localhost IDENTIFIED BY 'irontec_pass';
Query OK, 0 rows affected (0.01 sec)
```

Usuarios con privilegios de **solo lectura** en registros:

```sql
mysql> GRANT SELECT ON irontec_db.* TO irontec_user_ro@localhost IDENTIFIED BY 'irontec_pass';
Query OK, 0 rows affected (0.02 sec)
```

Usuarios con priligegios de **solo inserción o modificación** de registros:

```sql
mysql> GRANT INSERT,UPDATE on irontec_db.* TO irontec_user_wo@localhost IDENTIFIED BY 'irontec_pass';
Query OK, 0 rows affected (0.01 sec)
```

### Selección de Usuarios

Ver el usuario con el que se está trabajando:

```sql
mysql> SELECT user();
+------------------------+
| user()                 |
+------------------------+
| irontec_user@localhost |
+------------------------+
1 row in set (0.00 sec)
```

### Visualización de Privilegios de Usuarios

```sql
mysql> show grants for 'irontec_user_allpriv'@'localhost';
+------------------------------------------------------------------------------------------------+
| Grants for irontec_user_allpriv@localhost                                                      |
+------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'irontec_user_allpriv'@'localhost' IDENTIFIED BY PASSWORD '1a7f0760d48e' |
| GRANT ALL PRIVILEGES ON `irontec_db`.* TO 'irontec_user_allpriv'@'localhost'                   |
+------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
```

### Eliminación de Usuarios

```sql
mysql> REVOKE ALL PRIVILEGES ON irontec_db.* from 'irontec_user_allpriv'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> show grants for 'irontec_user_allpriv'@'localhost';
+------------------------------------------------------------------------------------------------+
| Grants for irontec_user_allpriv@localhost                                                      |
+------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'irontec_user_allpriv'@'localhost' IDENTIFIED BY PASSWORD '1a7f0760d48e' |
+------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> revoke usage on *.* from 'irontec_user_allpriv'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> drop user 'irontec_user_allpriv'@'localhost';
Query OK, 0 rows affected (0.00 sec)
```

## Trabajando con Tablas

###  Tipos de Tablas y Motores de Almacenamiento

[Referencia manual MySQL](http://dev.mysql.com/doc/mysql/en/storage-engines.html)

### Tipos de Campos

[Referencia manual MySQL](http://dev.mysql.com/doc/mysql/en/column-types.html)

### Creación Tablas

#### MyISAM

```sql
mysql> CREATE TABLE clientes (
  -> id_cliente INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  -> razon_social VARCHAR (50) NOT NULL,
  -> domicilio VARCHAR (100) NOT NULL,
  -> nif VARCHAR (9) NOT NULL,
  -> contacto VARCHAR (40)
  -> ) ENGINE=MyISAM;
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE presupuestos (
  -> id_presupuesto INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  -> empresa INT(8) NOT NULL,
  -> asunto VARCHAR (60),
  -> precio FLOAT DEFAULT 0.0,
  -> fecha DATE,
  -> ) ENGINE=MyISAM;
Query OK, 0 rows affected (0.20 sec)
```

#### InnoDB

```sql
mysql> CREATE TABLE clientes (
  -> id_cliente INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  -> razon_social VARCHAR (50) NOT NULL,
  -> domicilio VARCHAR (100) NOT NULL,
  -> nif VARCHAR(9) NOT NULL,
  -> contacto VARCHAR(40)
  -> ) ENGINE=InnoDB;
Query OK, 0 rows affected (0.10 sec)

mysql> CREATE TABLE presupuestos (
  -> id_presupuesto INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  -> empresa INT(8) NOT NULL,
  -> asunto VARCHAR (60),
  -> precio FLOAT DEFAULT 0.0,
  -> fecha DATE,
  -> index (empresa),
  -> FOREIGN KEY (empresa) REFERENCES clientes(id_cliente) ON DELETE CASCADE ON UPDATE CASCADE
  -> ) ENGINE=InnoDB;
Query OK, 0 rows affected (0.06 sec)
```

### Visualización Tablas

Tablas contenidas en una Base de Datos:

```sql
mysql> show tables;
+------------------+
| Tables_in_prueba |
+------------------+
| clientes         |
| presupuestos     |
+------------------+
2 rows in set (0.00 sec)
```

Estructura de una tabla:

```sql
mysql> DESC presupuestos;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id_presupuesto | int(8)      |      | PRI | NULL    | auto_increment |
| empresa        | varchar(50) |      |     |         |                |
| asunto         | varchar(60) | YES  |     | NULL    |                |
| precio         | float       | YES  |     | 0       |                |
| fecha          | date        | YES  |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)
```

Estado de todas las tablas:

```sql
mysql> show table status;
```

### Modificación Tablas

[Referencia manual MySQL](http://dev.mysql.com/doc/mysql/en/alter-table.html)

#### Añadir un nuevo campo

    mysql> ALTER TABLE [database.]tabla ADD campo_nuevo tipo AFTER campo_viejo;

```sql
mysql> ALTER TABLE presupuestos ADD adjunto BLOB AFTER fecha ;
Query OK, 0 rows affected (0.06 sec)
Registros: 0  Duplicados: 0  Peligros: 0
```

#### Cambiar el nombre de una tabla

    mysql> ALTER TABLE [database.]tabla RENAME tabla_nueva;

```sql
mysql> ALTER TABLE presupuestos RENAME proyectos;
Query OK, 0 rows affected (0.03 sec)
```

#### Cambiar el tipo de dato de un campo

    mysql> ALTER TABLE [database.]tabla CHANGE campo campo nuevo_tipo;

```sql
mysql> ALTER TABLE presupuestos CHANGE asunto asunto VARCHAR(100);
Query OK, 0 rows affected (0.23 sec)
Registros: 0  Duplicados: 0  Peligros: 0
```

#### Eliminar un campo existente

    mysql> ALTER TABLE [database.]tabla DROP campo;

```sql
mysql> ALTER TABLE presupuestos DROP adjunto;
Query OK, 0 rows affected (0.05 sec)
Registros: 0  Duplicados: 0  Peligros: 0
```

### Eliminación Tablas

    mysql> DROP TABLE [database.]tabla;

```sql
mysql> DROP TABLE presupuestos;
Query OK, 0 rows affected (0.44 sec)
```

## Trabajando con Registros

**Nota:** Si no se indica la Base de Datos a la que una tabla hace referencia, es necesario seleccionar previamente dicha BBDD (`use database`).

### Consultas

    mysql> SELECT campo1,campo2,.. FROM [database.]tabla;

```sql
mysql> SELECT * FROM proyectos;
Empty set (0.10 sec)
```


### Inserción de datos

    mysql> INSERT INTO [database.]tabla (campo1,campo2,..) VALUES ('valor_campo1','valor_campo2',..);

```sql
mysql> INSERT INTO presupuestos (empresa,asunto,precio,fecha) VALUES ('UPV','Formación GNU/Linux','600','2005-07-01');
Query OK, 1 row affected (0.00 sec)
```

### Modificación de datos

    mysql> UPDATE [database.]tabla SET campo1='valor_nuevo_campo1',campo2='valor_nuevo_campo2' WHERE condición;

```sql
mysql> UPDATE presupuestos SET empresa='UPV/EHU' WHERE empresa='UPV';
```

### Eliminación de datos

    mysql> DELETE FROM [database.]tabla WHERE condición;

```sql
mysql> DELETE FROM presupuestos WHERE id='1';
Query OK, 1 row affected (0.04 sec)
```


## Trabajando con MySQL

### Variables de Sistema

Ver variables de sistema:

```sql
mysql> SHOW VARIABLES;
+---------------------------------+----------------------------------------------------------+
| Variable_name                   | Value                                                    |
+---------------------------------+----------------------------------------------------------+
| back_log                        | 50                                                       |
| basedir                         | /usr/                                                    |
| bdb_cache_size                  | 8388600                                                  |
| bdb_home                        | /var/lib/mysql/                                          |
| bdb_log_buffer_size             | 32768                                                    |
| bdb_logdir                      |                                                          |
| bdb_max_lock                    | 10000                                                    |
| bdb_shared_data                 | OFF                                                      |
| bdb_tmpdir                      | /tmp/                                                    |
| binlog_cache_size               | 32768                                                    |
..............................................................................................
| version                         | 4.1.11-Debian_4-log                                      |
| version_bdb                     | Sleepycat Software: Berkeley DB 4.1.24: (April  1, 2005) |
| version_comment                 | Source distribution                                      |
| version_compile_machine         | i386                                                     |
| version_compile_os              | pc-linux-gnu                                             |
| wait_timeout                    | 28800                                                    |
+---------------------------------+----------------------------------------------------------+
196 rows in set (0.01 sec)
```

## Configuración

`/etc/mysql/my.cnf`

### Tablas InnoDB por defecto

    [mysqld]
    default-table-type=innodb

### Localización

    [mysqld]
    language  = /usr/share/mysql/spanish

### UTF8 por defecto

Como cabrea tener bases de datos en latin1 y cosas así que siempre dan problemas al cambiarlas de servidor o de versión de BDD, o con los programas. Cuando aprendes eso empiezas a configurar todo en UTF8, el apache, el mysql, las locales del sistema, etc...

Y cada vez que creas una BDD en mysql este se empeña en ponerte "latin1" o "unicode_swedish_ci" ¿Swedish? ¿Que es esto? ¿Un rollo chovinusta?

Después para cada tabla, incomprensiblemente, también tienes que especificar que es "utf8_unicode_ci".

Para evitar esto lo que podemos hacer es configurar mysql añadiendo estas líneas en la sección **[mysqld]** de `/etc/mysql/my.cnf`:


	# UTF8:
	skip-character-set-client-handshake
	collation_server=utf8_unicode_ci
	character_set_server=utf8


Si después pedimos un status:


	mysql> status
	--------------
	mysql  Ver 14.12 Distrib 5.0.51a, for debian-linux-gnu (x86_64) using readline 5.2

	Connection id:          31
	Current database:
	Current user:           root@localhost
	SSL:                    Not in use
	Current pager:          stdout
	Using outfile:          `
	Using delimiter:        ;
	Server version:         5.0.51a-24+lenny2 (Debian)
	Protocol version:       10
	Connection:             Localhost via UNIX socket
	Server characterset:    utf8
	Db     characterset:    utf8
	Client characterset:    utf8
	Conn.  characterset:    utf8
	UNIX socket:            /var/run/mysqld/mysqld.sock
	Uptime:                 11 min 21 sec

	Threads: 1  Questions: 86  Slow queries: 0  Opens: 23  Flush tables: 1  Open tables: 17  Queries per second avg: 0.126
	--------------


Ahora si, ya podemos dormir tranquilos.

## Backups

### mysqldump

Programa incluído en el paquete `mysql-client`

[Referencia manual MySQL](http://dev.mysql.com/doc/mysql/en/mysqldump.html)

Backup de todas las bases de datos:

```bash
$ mysqldump --opt -d -h host --all-databases --user=root --password=contraseña > backup_irontec_mysql.sql
```

Para cargar un backup hecho previamente:

```bash
$ mysql -h host --user=root --password=contraseña < backup_irontec_mysql.sql
```

Backup de una base de datos (`database`):

```bash
$ mysqldump --opt -d -h host --user=root --password=contraseña database > backup_irontec_mysql.sql
```

Backup de una lista de tablas (`t1`, `t2`) de una base de datos (`database`):

```bash
$ mysqldump --opt -d -h host --user=root --password=contraseña database t1 t2 > backup_irontec_mysql.sql
```

Para cargar un backup hecho previamente sobre una base de datos concreta:

```bash
$ mysql -h host --user=root --password=contraseña database < backup_irontec_mysql.sql
```

Si se quita la opción `-d` en el volcado se incluirán los datos que contengan las tablas. Para tablas muy grandes, para evitar los bloqueos que se producen durante su respaldo, añadir la opción `--single-transaction`.

## BCPs

El comando equivalente al `bcp` de otros gestores es `mysqlimport`. [Aquí](http://dev.mysql.com/doc/refman/5.0/es/mysqlimport.html) está la página de ayuda del comando.

Un ejemplo de uso sería:

```bash
$ mysqlimport -h localhost -u adw -p -v -L --delete adw keywords.csv
```

Para que no de errores hay que guardar el fichero en formato UTF8 (revisar con el comando `od -c fichero.csv` si no hay caracteres extraños al principio). Por defecto se espera el carácter TAB como separador de columnas y el retorno de carro como separador de registros. El fichero será un CSV con las columnas en el mismo orden que la tabla en que se desea cargar los datos. El nombre del fichero sin extensión se debe corresponder con el nombre de la tabla. En el ejemplo anterior, la tabla sería `keywords`.

Para indicar un separador de campos y registros diferentes se pueden usar las opciones siguientes (ver man):


	--fields-terminated-by=..., --fields-enclosed-by=..., --fields-optionally-enclosed-by=..., --fields-escaped-by=..

El mismo efecto se consigue con la siguiente query:

```sql
LOAD DATA LOCAL INFILE 'keywords_clean.csv'
INTO TABLE keywords
FIELDS
  TERMINATED BY ','
  ENCLOSED BY '\"';
```

Para que el cliente acepte la opción `LOCAL` debe ser ejecutado con la opción `--local-infile`, por ejemplo:

```bash
$ mysql -h localhost --local-infile -u adw -p adw
```

## Otras Herramientas

### mysqladmin
Para cambiar la contraseña del usuario root:

    $ mysqladmin -u root password `<nueva_password>`

Muestra las variables del gestor:

    $ mysqladmin -u root -p variables

## Solución de problemas

### Tabla de Schrödinger
La única forma de solucionar un caso de [tablas de Schrödingers](http://stackoverflow.com/questions/10538908/schrodingers-mysql-table-exists-yet-it-does-not) fue purgando la instalación de MySQL y borrando el directorio de datos:

```bash
$ sudo dpkg --purge mysql-server-5.5 mysql-server-core-5.5 mysql-server
$ sudo mv /var/lib/mysql /var/lib/mysql.bak
$ sudo apt-get install mysql-server-5.5 mysql-server-core-5.5 mysql-server
```

Otra forma menos agresiva fue encontrada [aquí](http://www.randombugs.com/linux/crash-innodb-table.html) y consiste en borrar los ficheros siguientes con el servidor parado y luego arrancarlo:

```bash
$ sudo service mysql stop
$ sudo rm /var/lib/mysql/ibdata1
$ sudo rm /var/lib/mysql/ib_logfile0
$ sudo rm /var/lib/mysql/ib_logfile1
$ sudo service mysql start
```

La última vez que sucedió borré todas las tablas. Ver si borrando estos ficheros en cuanto ocurre se restituyen todas las tablas.

### Información en error

Para tener más información de un error, si es sobre tablas InnoDB, se puede lanzar el siguiente comando:

```mysql
SHOW ENGINE INNODB STATUS;
```

Concretamente la sección `LATEST FOREIGN KEY ERROR` muestra más detalle en los errores relacionados con foreign keys.
