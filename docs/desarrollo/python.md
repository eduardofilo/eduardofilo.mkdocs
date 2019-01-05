---
layout: default
permalink: /desarrollo/python.html
---

# Python/Django

## Enlaces

### Cheatsheet

* [Classy Class-Based Views](https://ccbv.co.uk/projects/Django/1.11/): Detailed descriptions, with full methods and attributes, for each of Django's class-based generic views.

### Aprendizaje

* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/intro/learning/)
* [Alter model to add “through” relationship to order a ManytoMany field](https://stackoverflow.com/questions/26348260/alter-model-to-add-through-relationship-to-order-a-manytomany-field-django-1)
* [How to Reset Migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)
* [Django Admin Cookbook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/index.html)
* [Django data migration when changing a field to ManyToMany](https://stackoverflow.com/questions/2224410/django-data-migration-when-changing-a-field-to-manytomany?rq=1): Cuando queremos cambiar de un modelo ForeignKey a ManyToMany.
* [Alter model to add “through” relationship to order a ManytoMany field](https://stackoverflow.com/questions/26348260/alter-model-to-add-through-relationship-to-order-a-manytomany-field-django-1): Cuando queremos cambiar la tabla intermedia automática a una gestionada con un modelo propio.
* [Django Inline formsets example](https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d)

### Módulos interesantes

* [django-tinymce](https://github.com/aljosa/django-tinymce)
* [django-autocomplete-light](https://github.com/yourlabs/django-autocomplete-light)
* [wesome Django](http://awesome-django.com/): A curated list of awesome Django apps, projects and resources.

## Entorno Django

Para tener un entorno aislado (sin depender con los paquetes y versiones del sistema), instalar primero `pip` de Python3. Se puede hacer instalando el paquete `python3-pip` de Ubuntu, pero dado que interesa actualizar a la última versión, es mejor instalarlo de forma independiente bajando el script `get-pip.py` de [aquí](https://pip.pypa.io/en/stable/installing/) ejecutándolo así:

```
$ sudo python3 get-pip.py
```

Después ejecutar en terminal:

```
$ sudo pip3 install virtualenv
$ virtualenv --python=`which python3` djangodev
$ source djangodev/bin/activate
(djangodev) $ pip install Django
```

Cada vez que se quiera adaptar el entorno de la sesión del terminal a este entorno aislado, hay que ejecutar el penúltimo comando anterior (`source`).

## Entorno Django en Synology NAS

1. Instalo módulo Python3 desde el Centro de Paquetes.
2. Instalo pip en Python3:

        $ wget -nd https://bootstrap.pypa.io/get-pip.py
        $ python get-pip.py
        $ cd /usr/local/bin
        $ sudo ln -s /volume1/@appstore/py3k/usr/local/bin/pip3

3. Instalo virtualenv:

        $ sudo pip3 install virtualenv
        $ python3 /volume1/@appstore/py3k/usr/local/lib/python3.5/site-packages/virtualenv.py --python=`which python3` djangodev

4. Arranco el entorno virtual e instalo Django:

        $ source djangodev/bin/activate
        (djangodev) $ pip install Django

## Creación de proyecto Django

Desde el directorio donde queremos que se cree ejecutamos:

```
(djangodev) $ django-admin startproject project01
```

## Creación de aplicación Django

Desde el directorio del proyecto (donde se encuentre el fichero `manage.py`) ejecutamos:

```
(djangodev) $ python manage.py startapp app01
```

Para incorporar los modelos de la nueva aplicación al mantenimiento automático que proporciona el módulo `admin` de Django, hay que incorporar al fichero `project01/settings.py` lo siguiente en la sección `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    'app01.apps.App01Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Luego ejecutamos el siguiente comando para generar las migraciones a partir de los modelos definidos en la app:

```
(djangodev) $ python manage.py makemigrations app01
```

Finalmente ejecutamos las migraciones propiamente dichas:

```
(djangodev) $ python manage.py migrate
```

Para poder utilizar el módulo `admin` de Django, hay que crear al menos un usuario:

```
(djangodev) $ python manage.py createsuperuser
```

## Personalización del modelo User

Es recomendable cuando se empieza un proyecto, sustituir la gestión del modelo User por uno propio, ya que si se quiere hacer más adelante con la aplicación ya en marcha, es muy complicada la migración entre tablas. Un par de buenos artículos sobre el tema son:

* [Extending User Model Using a Custom Model Extending AbstractUser](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser)
* [How to Implement Multiple User Types with Django](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)

Creamos el modelo así:

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

Y lo activamos definiendo la siguiente propiedad en el fichero `settings.py`:

    AUTH_USER_MODEL = 'app01.User'

Si no queremos perder los formularios especiales de la aplicación `admin` para el modelo original, además hay que personalizar la clase `UserAdmin` de la siguiente forma:

```python
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    model = User

admin.site.register(User, MyUserAdmin)
```

## Gestión de migraciones

Una vez generadas las migraciones, si queremos obtener el código SQL a que equivalen hay que ejecutar el comando (en el ejemploo solicitamos el código correspondiente a la migración `0008`):

```
(djangodev) $ python manage.py sqlmigrate app01 0008
```

Para situarnos en un punto concreto de la serie de migraciones (deshaciendo por tanto las posteriores cuyos ficheros se podrán borrar):

```
(djangodev) $ python manage.py migrate app01 0010
```

Para mostrar los nombres de todas las migraciones (si no ponemos el nombre al final se muestran las de todo el sitio):

```
(djangodev) $ python manage.py showmigrations app01
```

Para deshacer todas las migraciones:

```
(djangodev) $ python manage.py migrate app01 zero
```

Para crear una migración vacía que podremos utilizar para hacer transferencias de datos (ver ejemplo [aquí](https://stackoverflow.com/questions/2224410/django-data-migration-when-changing-a-field-to-manytomany?rq=1)):

```
(djangodev) $ python manage.py makemigrations app01 --empty
```

## Formateo de cadenas

* Con tuplas (no se puede cambiar el orden de los parámetros):

    ```python
    "%s parte de %s la cadena" % (var1, var2)
    ```

* Con diccionario (se puede cambiar el orden de los parámetros):

    ```python
    "%(par1)s parte de %(par2)s la cadena" % {'par1': var1, 'par2': var2}
    ```

## Directorio instalación Django

Para averiguar dónde están los ficheros de Django, ejecutar el siguiente comando:

```
(djangodev) $ python -c "import django; print(django.__path__)"
```

## Tutorial Django

* Escribiendo una view:
    * [Escribiendo directamente la HTTP Response](https://docs.djangoproject.com/es/1.11/intro/tutorial01/#write-your-first-view)
    * [Renderizando una plantilla](https://docs.djangoproject.com/es/1.11/intro/tutorial03/#write-views-that-actually-do-something)
    * [Gestión de URL's](https://docs.djangoproject.com/es/1.11/intro/tutorial03/#removing-hardcoded-urls-in-templates)
    * [Formulario manual](https://docs.djangoproject.com/es/1.11/intro/tutorial04/#write-a-simple-form)
    * [Formulario con vistas genéricas](https://docs.djangoproject.com/es/1.11/intro/tutorial04/#use-generic-views-less-code-is-better)
* [Creando modelos](https://docs.djangoproject.com/es/1.11/intro/tutorial02/#creating-models)
* [Manipulación del modelo de datos por CLI](https://docs.djangoproject.com/en/1.11/intro/tutorial02/#playing-with-the-api)
* [Tests](https://docs.djangoproject.com/es/1.11/intro/tutorial05/)
* [Ficheros estáticos](https://docs.djangoproject.com/es/1.11/intro/tutorial06/): Inserción de CSS en las vistas.
* [Modificación representación detalle modelos](https://docs.djangoproject.com/en/1.11/intro/tutorial07/#customize-the-admin-form): fields, fieldsets
* [Objetos relacionados en detalle modelos](https://docs.djangoproject.com/en/1.11/intro/tutorial07/#adding-related-objects): Inlines
* [Modificación representación lista modelos](https://docs.djangoproject.com/en/1.11/intro/tutorial07/#customize-the-admin-change-list): list_display, list_filter, search_fields
* [Sustitución de templates en el sitio admin](https://docs.djangoproject.com/en/1.11/intro/tutorial07/#customize-the-admin-look-and-feel)
* [Empaquetado de aplicaciones](https://docs.djangoproject.com/es/1.11/intro/reusable-apps/)
* [Envío de mails](https://docs.djangoproject.com/en/1.11/topics/email/)

## Tutorial Django de Mozilla Developer Network

* [Using models - Searching for records](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models#Searching_for_records)
* [Utilizando las listas genéricas y vistas de detalle](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Generic_views)
* [Personalización del subsistema de autenticación](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Authentication): Páginas de login, logout, cambio de password, etc.
* [Propiedad calculada en modelo](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Authentication#Models): Sin correspondencia en base de datos.
* Formularios:
    * [Usando Form y view función](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms#Renew-book_form_using_a_Form_and_function_view)
    * [Usando ModelForm y CRUD Views](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms#ModelForms)

## Referencia Django

* [Directorio](https://docs.djangoproject.com/en/1.11/)
* [Admin actions](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/actions/): Creación de actions, páginas intermedias al ejecutar actions, gestión de actions.
* [Autenticación](https://docs.djangoproject.com/es/1.11/topics/auth/default/)

## Temas interesantes

* [filter, list comprehension y generators](https://stackoverflow.com/questions/1205375/filter-by-property). Para filtrar por ejemplo una lista de objetos se pueden utilizar estos tres elementos. Hay que tener en cuenta que `filter` devuelve un iterator. Si por eejemplo sólo queremos el número de elementos habrá que generar una lista o set con él.
* [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser). [Este](https://stackoverflow.com/questions/30495979/django-1-8-multiple-custom-user-types) artículo es un ejemplo del caso 4.

## Uso de Class Views

### Básicas

Documentadas [aquí](https://docs.djangoproject.com/es/1.11/ref/class-based-views/base/).

#### TemplateView

La más sencilla. Sólo necesita definir la propiedad `template_name` apuntando a la plantilla. Para añadir datos al contexto (esto funciona en todas las view classes) se puede definir la función `get_context_data` (ver ejemplo e apartado `Passing variables to the template` [aquí](https://hellowebbooks.com/news/introduction-to-class-based-views/))

#### RedirectView

Se puede usar tal cual para definir redirecciones en los ficheros `url.py`. Por ejemplo:

```python
urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    ...
]
```

Pero también se puede heredar de ella para por ejemplo hacer una vista "proxy" para actualizar un contador de visitas a otra vista, como el ejemplo que hay [aquí](https://docs.djangoproject.com/es/1.11/ref/class-based-views/base/#redirectview).

### Genéricas para visualización de modelos

Son las diseñadas para generar listados y vistas de detalle de un modelo. Son más adecuadas para visualización, como la que se haría por ejemplo en un blog. Documentadas [aquí](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/).

En las dos clases de este tipo, sólo se necesita definir la propiedad `model`.

#### DetailView

La plantilla se define por convención añadiendo `_detail.html` al nombre del modelo. Dentro de la plantilla, el objeto que se quiere representar aparece en la variable de contexto `object`.

#### ListView

La plantilla se define por convención añadiendo `_list.html` al nombre del modelo. Dentro de la plantilla, la colección de objetos que se quiere representar aparece en la variable de contexto `object_list`.

### Genéricas para edición de modelos

Permiten personalizar las vistas típicas del mantenimiento de un modelo (creación, actualización y borrado). Documentadas [aquí](https://docs.djangoproject.com/es/1.11/ref/class-based-views/generic-editing/).

En cualquiera de las cuatro siguientes clases, en la plantilla incluiremos los tags HTML para el formulario (no se generan automáticamente porque la página podría contener varios formularios o por si no estamos generando HTML). Se suele hacer algo así:

```
<form action="" method="post">{{ "{% csrf_token " }}%}
    {{ "{{ form " }}}}
    <input type="submit" value="Save" />
</form>
```

El tag para el formulario tiene tres variantes:

* `{{ "{{ form.as_p " }}}}`: Cada campo del formulario se genera como un `<p>`.
* `{{ "{{ form.as_table " }}}}`: Cada campo del formulario se genera como una fila de una tabla.
* `{{ "{{ form.as_ul " }}}}`: Cada campo del formulario se genera como una lista sin numerar.

Para máximo control siempre podemos generar cada campo del formulario por separado o incluso escribir el formulario completo a mano (ver documentación [Working with forms](https://docs.djangoproject.com/es/1.11/topics/forms/)).

#### FormView

Gestiona la vista con un formulario genérico. Si se produce error en la validación, vuelve a cargar la misma URL con los campos rellenos e información sobre los errores; Si se supera la validación se redirije a otra URL. En el contexto de la plantilla tendremos el formulario bajo la variable `form`.

Necesita definir las propiedades siguientes:

* `form_class`: Clase formulario.
* `success_url`: URL a la que se redirije en caso de superar la validación.
* `template_name`: Plantilla.

También es interesante definir el método siguiente:

* `form_valid`: Se ejecutará cuando el formulario se valide correctamente. Obtendremos los datos del formulario del diccionario `self.form.cleaned_data`.

Ver ejemplos [aquí](https://docs.djangoproject.com/es/1.11/ref/class-based-views/generic-editing/#formview) y en apartado `Now for a FormView` de [aquí](https://hellowebbooks.com/news/introduction-to-class-based-views/).

#### CreateView

Para la creación de un modelo.

#### UpdateView

Para la actualización de un modelo.

#### DeleteView

Para el borrado de un modelo.

### Empaquetadas

#### FilterView

Es una especie de ListView con filtros. Ver documentación [aquí](https://django-filter.readthedocs.io/en/master/guide/usage.html).

## Idioms

* Retorno seguro del primer elemento de una lista: `return (get_list()[:1] or [None])[0]`
* Acceso seguro al atributo de un objeto: `getattr(object, name[, default])` La función [getattr](https://docs.python.org/3/library/functions.html#getattr) nos permite indicar un valor predeterminado si un objeto no tiene el atributo que buscamos. Funciona también si el objeto es None, lo que nos permite acceder de forma segura a un objeto cuando no sabemos si existe.

## Snippets

* Colección completa de objetos de un modelo: `Unidad.objects.all()`
* Colección completa de objetos de un modelo ordenada: `Unidad.objects.all().order_by('nombre')`
* Colección filtrada de objetos de un modelo: `Actividad.objects.filter(fecha__year=2017)`
* Filtro OR (es necesario hacer `from django.db.models import Q`): `GrupoUnidades.objects.filter(Q(pausada=True) | Q(fecha_fin__isnull=False))`
* Instancia concreta de un objeto: `Unidad.objects.get(pk=3)`
* Servidor HTTP en el directorio actual: `python -m SimpleHTTPServer 8080`
* Convertir un set en un list ordenado: `una_lista = sorted(un_set, key=lambda x: x.position)`
* Template filters:
    * Valor predeterminado: `{{ "{{ elemento_de_context|default_if_none:'Valor predeterminado' " }}}}`

### Filtro en ListView

```python
# urls.py
from django.conf.urls import url
from . import views

app_name = 'lms'
urlpatterns = [
    url(r'^asistencia/(?P<pk>\d+)/grupo/(?P<admin>\w+)/$', views.AsistenciaGrupoView.as_view(), name='asistencia_grupo')
]


# views.py
class AsistenciaGrupoView(generic.ListView):
    template_name = 'lms/asistencia_grupo.html'

    def get_queryset(self):
        semanas = int(self.request.GET.get('semanas', '12'))
        return Jornada.objects.filter(grupo__id=self.kwargs['pk'], fecha__gte=datetime.today() - timedelta(weeks=semanas)).order_by('fecha')

    def get_context_data(self, **kwargs):
        context = super(AsistenciaGrupoView, self).get_context_data(**kwargs)
        # Lista de semanas que mostraremos en el combo para filtrar
        context['lista_semanas'] = [(4, 1),
                                    (8, 2)]
        # Parámetro de filtrado del querystring (12 semanas como valor predeterminado)
        context['semanas'] = int(self.request.GET.get('semanas', '12'))
        # Valor del PK del grupo recogido de la URL
        context['pk'] = self.kwargs['pk']

        return context


# template
    <form method="get" action="{{ "{% url 'lms:asistencia_grupo' pk " }}%}">
        <label for="semanas_id">Meses</label>
        <select class="form-control" name="semanas" id="semanas_id" onchange='if(this.value != 0) { this.form.submit(); }'>
            {{ "{% for v, d in lista_semanas " }}%}
            <option value="{{ "{{ v " }}}}"{{ "{% if semanas == v " }}%} selected='selected'{{ "{% endif " }}%}>{{ "{{ d " }}}}</option>
            {{ "{% endfor " }}%}
        </select>
    </form>
```

## Logging

### Log a fichero

Configurar un logger en el fichero de settings correspondiente añadiendo esto:

```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'log': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

En el módulo donde queramos obtener log, añadir al principio lo siguiente:

```python
import logging

logger = logging.getLogger('log')
```

Y dentro de la función donde queramos emitir algo al log:

```python
logger.debug('lo que sea')
```

### Log a consola

Si sólo queremos imprimir en consola una traza rápida, es más fácil escribiendo simplemente:

```python
print('lo que sea', file=sys.stderr)
```

### Traza de queries a consola

Configurar el siguiente logger en el fichero de settings correspondiente:

```
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
```

## pip

### Instalación versión específica

```bash
$ pip install Django==1.11.6
```

## Pienv

### Enlaces

* [How to manage your Python projects with Pipenv](https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv)

### Instalación

```bash
$ sudo -H pip install pipenv
```

### Creación de entorno con versión específica de Python y de paquetes

1. Instalar algunos paquetes necesarios:

        $ sudo apt-get install build-essential checkinstall
        $ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

2. Bajamos la versión `source` de [aquí](https://www.python.org/downloads/source/).
3. Descomprimimos:

        $ tar -xzvf Python-3.6.6.tgz

4. Renombramos el directorio de las fuentes para no confundirlo con el de los binarios:

        $ mv Python-3.6.5 Python-3.6.5_src

5. Creamos el directorio para los binarios:

        $ mkdir Python-3.6.5

6. Entramos en el directorio de las fuentes y compilamos:

        $ cd /home/usuario/Python-3.6.5_src
        $ ./configure --disable-ipv6 --prefix=/home/usuario/Python-3.6.5
        $ make
        $ make test
        $ make install

7. Creamos el entorno:

        $ cd directorio_proyecto
        $ pipenv install --python /home/usuario/Python-3.6.5/bin/python3
        $ pipenv install Django==1.11.12
        $ pipenv install _resto_de_paquetes_
        $ pipenv shell

## Usando Webpack para construir el frontend

### Enlaces:

* [Django + webpack + Vue.js - setting up a new project that's easy to develop and deploy (part 1)](https://ariera.github.io/2017/09/26/django-webpack-vue-js-setting-up-a-new-project-that-s-easy-to-develop-and-deploy-part-1.html)
* [Using Webpack transparently with Django + hot reloading React components as a bonus](https://owais.lone.pw/blog/webpack-plus-reactjs-and-django/)
* [webpack-bundle-tracker](https://github.com/owais/webpack-bundle-tracker)
* [django-webpack-loader](https://github.com/owais/django-webpack-loader)
* [django-vue-webpack](https://github.com/longtranista/django-vue-webpack): A boilerplate of using Django as backend framework, Vue js and webpack as the frontend setup.
* [Building Modern Applications with Django, Vue.js and Auth0: Part 2](https://www.techiediaries.com/django-vuejs-auth0/)

### Procedimiento

1. Instalamos Vue-CLI en la máquina de desarrollo:

        sudo npm install -g @vue/cli
        sudo npm install -g @vue/cli-init

2. Generamos el scaffolding para vue y webpack ejecutando lo siguiente desde el directorio que queremos que contenga el proyecto (en el ejemplo lo llamaremos `vue_test`):

        vue init webpack vue_test

3. Durante la generación del proyecto se nos hacen las siguientes preguntas:

    1. Vue build: Elegimos `Runtime + Compiler`
    2. Install vue-router?: Elegimos `Y`
    3. Use ESLint to lint your code?: n
    4. Set up unit tests: n
    5. Setup e2e tests with Nightwatch?: n
    6. Should we run `npm install` for you after the project has been created?: Yes, use NPM

4. Generamos el scaffolding para Django:

        cd vue_test/
        django-admin startproject vue_test .

5. Instalamos el plugin de webpack `webpack-bundle-tracker` y el módulo Django `django-webpack-loader` (con pipenv):

        npm install --save-dev webpack-bundle-tracker
        pipenv install django-webpack-loader

6. Añadimos `webpack_loader` a las aplicaciones Django:

        # ./vue_test/settings.py
        INSTALLED_APPS = [
        'webpack_loader',
        #...
        ]

7. Configurar webpack para que use `BundleTracker`:

        // build/webpack.base.conf.js
        let BundleTracker = require('webpack-bundle-tracker')
        module.exports = {
          // ...
          plugins: [
            new BundleTracker({filename: './webpack-stats.json'}),
          ],
        }

8. Definir las rutas estáticas:

    * Configuración webpack:

            // ./config/index.js
            module.exports = {
              build: {
                assetsRoot: path.resolve(__dirname, '../dist/'),
                assetsSubDirectory: '',
                assetsPublicPath: '/static/',
                // ...
              },
              dev: {
                assetsPublicPath: 'http://localhost:8080/',
                // ...
              }
            }

    * Configuración Django:

            # ./vue_test/settings.py
            STATICFILES_DIRS = (
                os.path.join(BASE_DIR, 'dist'),
                os.path.join(BASE_DIR, 'static'),
            )
            STATIC_ROOT = os.path.join(BASE_DIR, 'public')
            STATIC_URL = '/static/'

            WEBPACK_LOADER = {
                'DEFAULT': {
                    'BUNDLE_DIR_NAME': '',
                    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
                }
            }

9. Configuración webpack para que resuelva los ficheros estáticos desde `/static`:

        // build/webpack.base.conf.js
        module.exports = {
          resolve: {
            alias: {
              // ...
              '__STATIC__': resolve('static'),
            },
        }

10. Configuración del Hot Reload:

        // build/webpack.dev.conf.js
        devServer: {
          headers: {
            "Access-Control-Allow-Origin":"\*"
          },
          // ...
        }

Los contenidos estáticos se servirán desde uno y otro entorno de la siguiente forma:

    <!-- in a Django template -->
    <img src="{{ "{% static 'logo.png' " }}%}">

    <!-- in a Vue component -->
    <img src="~__STATIC__/logo.png">

Finalmente, para servir los contenidos cliente en desarrollo hay que ejecutar:

    cd vue-test
    npm run dev

Y para servir los contenidos del backend:

    cd vue-test
    pipenv shell
    python manage.py runserver

Cuando hagamos `npm run build` todo lo gestionado por webpack se compilará dentro del directorio `dist`.

La documentación de webpack se encuentra [aquí](https://vuejs-templates.github.io/webpack).
