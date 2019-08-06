title: 2019-08-06 Creación de un sitio Django desde cero
summary: Creación de un sitio Django desde cero.
date: 2019-08-06 16:30:00


Procedimiento de creación de un entorno de desarrollo y producción para un sitio Django.

## Entorno DEV

1. Creo repositorio git y lo sincronizo con el directorio de desarrollo.
2. Creo entorno Python con pipenv. Dos opciones:

    * Con una versión de Python compilada previamente en nuestra máquina:

        ```bash
        $ cd ~/git/remote_james
        $ pipenv install --python /home/usuario/Python-3.6.5/bin/python3
        ```

    * Con la versión de Python3 instalada en el sistema:

        ```bash
        $ cd ~/git/remote_james
        $ pipenv install --three
        ```

3. Instalo Django, creo proyecto y aplicación:

    ```bash
    $ pipenv shell
    $ pipenv install django
    $ django-admin startproject remote_james .
    $ python manage.py startapp james
    ```

4. Incorporo nueva app en fichero `settings.py`:

    ```
    INSTALLED_APPS = [
        'james.apps.JamesConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

5. Ejecuto migraciones, creo superusuario y arranco servidor desarrollo:

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver 0.0.0.0:8000
    ```

## Entorno PROD

1. Bajo el repositorio:

    ```bash
    $ cd ~
    $ git clone git@bitbucket.org:eduardofilo/remote_james.git
    ```

2. Creo el entorno (de nuevo existe la opción de utilizar la versión de Python3 del sistema como en el punto 2 del entorno de desarrollo):

    ```bash
    $ cd remote_james
    $ pipenv install --python /home/niubit/Python-3.6.5/bin/python3
    ```

3. Creo base de datos y usuario admin:

    ```bash
    $ pipenv shell
    $ python manage_ovh.py migrate
    $ python manage_ovh.py createsuperuser
    ```

4. Creo sitio en Apache (`/etc/apache2/sites-available/008-remote_james.conf`):

    ```
    <VirtualHost *:80>
            ServerName remotejames.example.com
            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html

            ErrorLog ${APACHE_LOG_DIR}/error-remotejames.log
            CustomLog ${APACHE_LOG_DIR}/access-remotejames.log combined

            Alias /static /home/servidor/remote_james/static
            <Directory /home/servidor/remote_james/static>
                    Require all granted
            </Directory>

            Alias /media /home/servidor/remote_james/media
            <Directory /home/servidor/remote_james/media>
                    Require all granted
            </Directory>

            <Directory /home/servidor/remote_james/remote_james>
                    <Files wsgi.py>
                            Require all granted
                    </Files>
            </Directory>

            WSGIDaemonProcess remote_james python-path=/home/servidor/remote_james python-home=/home/servidor/.virtualenvs/remote_james-Sjv1LfIa
            WSGIProcessGroup remote_james
            WSGIScriptAlias / /home/servidor/remote_james/remote_james/wsgi.py
    </VirtualHost>

    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    ```

5. Activo sitio:

    ```bash
    $ sudo a2ensite 008-remote_james.conf
    $ sudo systemctl reload apache2
    ```
