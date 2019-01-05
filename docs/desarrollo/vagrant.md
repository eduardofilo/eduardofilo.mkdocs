---
layout: default
permalink: /desarrollo/vagrant.html
---

# Vagrant

## Instalación

Instalar VirtualBox de la distribución (`virtualbox` en Ubuntu) y bajar el instalable de Vagrant de su [sitio web](https://www.vagrantup.com/downloads.html).

## Creación de entorno

Desde el directorio raíz de nuestro proyecto de desarrollo, ejecutar:

```
$ vagrant init
```

Esto crea el fichero `Vagrantfile` que mantendrá la configuración de nuestro entorno. Este fichero conviene incluirlo en el control de versiones.

Modificamos el fichero `Vagrantfile` para que use la máquina que nos interesa. En el ejemplo vamos a usar `ubuntu/xenial64` (consultar [aquí](https://app.vagrantup.com/boxes/search) el catálogo completo de máquinas).

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
end
```

Cuando se levante por primera el entorno configurado en el `Vagrantfile` se bajará la máquina. Si queremos adelantar este proceso podemos bajar la máquina con el siguiente comando:

```
$ vagrant box add ubuntu/xenial64
```

Ahora ya podemos levantar el entorno y conectar con él:

```
$ vagrant up
$ vagrant ssh
```

El comando `vagrant ssh` automatiza una conexión ssh cuyos parámetros manuales se pueden obtener ejecutando el comando `vagrant ssh-config`. Por ejemplo, una conexión manual podría lograrse a partir de los siguientes resultados así:

```
$ vagrant ssh-config
Host default
  HostName 127.0.0.1
  User ubuntu
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/edumoreno/git/django_test/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL
$ ssh -i /home/edumoreno/git/django_test/.vagrant/machines/default/virtualbox/private_key -p 2222 ubuntu@127.0.0.1
```

Tal y como se indica en el log del arranque de la máquina (durante el `vagrant up`), el directorio del proyecto de la máquina host se monta sobre `/vagrant` de la máquina guest:

```
==> default: Mounting shared folders...
    default: /vagrant => /home/edumoreno/git/niubit_lms
```

## Provisión de componentes

Por ejemplo vamos a configurar la instalación de un entorno Python3/Django. La máquina que hemos instalado (`ubuntu/xenial64`) viene con Python3 preinstalado. Vamos a instalar Django de forma controlada con Vagrant para que pueda reproducir esa instalación de forma automática si creamos este entorno en otro lugar. Para ello escribimos un script que luego integramos en el `Vagrantfile` de la siguiente forma:

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision "shell", inline: <<-SHELL
    #!/usr/bin/env bash
    apt-get update
    apt-get install -y python3-pip
    pip3 install Django
  SHELL
end
```

Si no habíamos arrancado la máquina todavía, el script se ejecutará en el primer arranque. Si ya lo habíamos hecho habrá que decirle a Vagrant que ejecute la configuración de provisioning:

```
$ vagrant reload --provision
```

En caso de tener que ejecutar muchos scripts o ser muy grandes, tal vez sea mejor escribirlos en archivos separados que luego se pueden referenciar en el `Vagrantfile` de esta forma (tal y como está en el ejemplo, el script `script.sh` deberá estar en la misma ruta que el `Vagrantfile`):

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "script.sh"
end
```

## Redirección de puertos

Aparte del acceso SSH que se consigue fácilmente a través del comando `vagrant ssh` como hemos visto, será habitual que necesitemos otro tipo de accesos por red hacia la máquina virtual. Por ejemplo en el caso de que estemos desarrollando una aplicación web necesitaremos redireccionar el puerto que sirva la máquina virtual. Por ejemplo, si queremos redireccionar el puerto 8000 de la máquina virtual hacia la host, deberemos añadir la siguiente línea al bloque de configuraciones del `Vagrantfile`:

```
  config.vm.network :forwarded_port, guest: 8000, host: 8000
```

Tras ello hay que ejecutar `vagrant reload` o `vagrant up` dependiendo de si la máquina virtual está arrancada o parada. En Vagrant hay muchas más posibilidades para configurar la red además del nat que acabamos de hacer. Todas estas posibilidades se describen [aquí](https://www.vagrantup.com/docs/networking/).

>Nota para Python/Django. En caso de querer acceder al miniservidor que se ejecuta con `python manage.py runserver`, además de la redirección del puerto (precisamente se usa el 8000 de forma predeterminada), tal y como se explica [aquí](https://stackoverflow.com/questions/18157353/connection-reset-when-port-forwarding-with-vagrant), hay que lanzar el miniservidor especificando que se escucha cualquier interfaz de la máquina (por defecto se escucha sólo el interfaz de loopback) ejecutando así:
>
>```
>python manage.py runserver 0.0.0.0:8000
>```
