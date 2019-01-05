---
layout: default
permalink: /desarrollo/ror.html
---

# Ruby on Rails

## Enlaces

*  [Ruby on Rails Tutorial](http://ruby.railstutorial.org/book/ruby-on-rails-tutorial)
*  [Programming Ruby: The Pragmatic Programmer's Guide](http://www.ruby-doc.org/docs/ProgrammingRuby/)
*  [Why's (Poignant) Guide to Ruby](http://mislav.uniqpath.com/poignant-guide/)
*  [Ruby User's Guide](http://www.rubyist.net/~slagell/ruby/index.html)
*  [Try Ruby](http://tryruby.org/levels/1/challenges/0)
*  [Aptana Studio (IDE)](http://www.aptana.com/products/radrails)
*  [Ruby on Rails Screencasts](http://railscasts.com/) :exclamation:
*  [Ruby on Rails Guides](http://guides.rubyonrails.org/) :exclamation:
*  [Ruby Tutorial](http://www.tutorialspoint.com/ruby/index.htm)
*  [Rails 3 para Windows y Linux Ubuntu (libro en español)](http://r3uw.herokuapp.com/)
*  [Rails Examples and Tutorials](http://railsapps.github.com/)
*  [Ruby QuickRef](http://www.zenspider.com/Languages/Ruby/QuickRef.html)
*  [Rails Tutorial Sublime Text setup](https://github.com/mhartl/rails_tutorial_sublime_text)
*  [Metaprogramming in Ruby: It’s All About the Self](http://yehudakatz.com/2009/11/15/metaprogramming-in-ruby-its-all-about-the-self/)
*  [Comprobación de entorno de ejecución en código](http://stackoverflow.com/questions/9297446/how-to-use-a-route-helper-method-from-a-file-in-the-lib-directory) :exclamation:

## Performance Tunning

*  [Performance Tuning for Phusion Passenger (an Introduction)](http://www.alfajango.com/blog/performance-tuning-for-phusion-passenger-an-introduction/) :exclamation:
*  [Phusion Corporate Blog - Tuning Phusion Passenger’s concurrency settings](http://blog.phusion.nl/2013/03/12/tuning-phusion-passengers-concurrency-settings/)
*  [Production Rails Tuning with Passenger: PassengerMaxProcesses](http://blog.scoutapp.com/articles/2009/12/08/production-rails-tuning-with-passenger-passengermaxprocesses)
*  [Passenger tuning for rails application](http://blog.railsupgrade.com/2011/11/passenger-tuning-for-rails-application.html)
*  [Phusion Passenger users guide, Apache version - Resource control and optimization options](http://www.modrails.com/documentation/Users%20guide%20Apache.html#_resource_control_and_optimization_options)

## El lío del respond_with

*  [Bringing Merb's provides/display into Rails 3](http://david.heinemeierhansson.com/posts/37-bringing-merbs-providesdisplay-into-rails-3)
*  [Embracing REST with mind, body and soul](http://blog.plataformatec.com.br/2009/08/embracing-rest-with-mind-body-and-soul/)
*  [What's New in Edge Rails: Cleaner RESTful Controllers w/ respond_with](http://archives.ryandaigle.com/articles/2009/8/6/what-s-new-in-edge-rails-cleaner-restful-controllers-w-respond_with)
*  [Respond With An Explanation](http://bendyworks.com/geekville/tutorials/2012/6/respond-with-an-explanation)

## Módulos interesantes

*  [Devise: Engine de autenticación/autorización](http://devise.plataformatec.com.br/)
*  [Forem: Engine para implementar un foro](https://github.com/radar/forem#readme)
*  [carmen-rails](https://github.com/jim/carmen-rails): Seed con datos de los países y las regiones del mundo.
*  [RailsCasts #328 Twitter Bootstrap Basics](http://railscasts.com/episodes/328-twitter-bootstrap-basics)
*  [Twitter Bootstrap Gem](https://github.com/thomas-mcdonald/bootstrap-sass)
*  [FasterCSV](http://fastercsv.rubyforge.org/): Carga y generación de ficheros CSV hacia y desde tablas. [Ejemplo de uso](http://www.funonrails.com/2012/01/csv-file-importexport-in-rails-3.html).
*  [Entity-Relationship Diagrams for Ruby on Rails](http://rails-erd.rubyforge.org/): Obtiene el esquema de relación entre entidades de una aplicación en base al análisis de sus modelos.

## Instalación en Ubuntu

### Algunas guías

*  [How to install Ruby on Rails in Ubuntu 12.04 LTS](http://blog.sudobits.com/2012/05/02/how-to-install-ruby-on-rails-in-ubuntu-12-04-lts/)
*  [Buena guía de `railsapps` sobre instalación de Ruby/Rails](http://railsapps.github.com/installing-rails.html)
*  [Otra guía de `railsapps` sobre actualización](http://railsapps.github.com/updating-rails.html)

### Procedimiento Ubuntu <=13.04

 1.  Instalar los paquetes:
    * `ruby`
    * `ruby-dev`
    * `libsqlite3-dev`
    * `libmysqlclient-dev`
    * `nodejs`
    * `nodejs-dev`
 2.  Instalar RubyGems bajándolo de [aquí](http://rubygems.org/pages/download) y siguiendo las instrucciones de instalación de esa misma página.
 3.  Instalar Bundler:
    * `sudo gem install bundler`
 4.  Instalación de Rails:
    * `sudo gem install rails`
 5.  Instalar passenger (el propio instalador da instrucciones sobre los paquetes necesarios):
    * `sudo gem install passenger`
 6.  Instalar el módulo en Apache:
    * `sudo passenger-install-apache2-module`
 7.  Tal y como indica la salida del comando anterior, hay que habilitar el módulo recién instalado por medio de la configuración de Apache. Se puede hacer añadiendo los dos siguientes ficheros:
	
```
#/etc/apache2/mods-available/passenger.load
LoadModule passenger_module /usr/lib/ruby/gems/1.9.1/gems/passenger-3.0.19/ext/apache2/mod_passenger.so
```

```	
#/etc/apache2/mods-available/passenger.conf
PassengerRoot /usr/lib/ruby/gems/1.9.1/gems/passenger-3.0.19
PassengerRuby /usr/bin/ruby1.9.1
```

(las rutas contenidas en los ficheros anteriores dependerán de la instalación; la salida del comando que instala el módulo nos indica los valores correctos).

Finalmente hay que habilitar el módulo:

```bash
$ sudo a2enmod passenger
```

Y reiniciamos Apache:

```bash
$ sudo service apache2 restart
```

### Procedimiento Ubuntu >=13.10

 1.  Instalar los paquetes:
    * `ruby`
    * `ruby-dev`
    * `libsqlite3-dev`
    * `libmysqlclient-dev`
    * `nodejs`
    * `nodejs-dev`
 2.  Instalar RubyGems bajándolo de [aquí](http://rubygems.org/pages/download) y siguiendo las instrucciones de instalación de esa misma página.
 3.  Instalar Bundler:
    * `sudo gem install bundler`
 4.  Instalación de Rails:
    * `sudo gem install rails`
 5.  Instalar passenger siguiendo [esta guía](http://www.modrails.com/documentation/Users%20guide%20Apache.html#install_on_debian_ubuntu). Recomienda instalarlo con los paquetes de la distribución. A continuación se indica un resumen de los pasos.
 6.  Instalar la clave PGP del repositorio que vamos a añadir:
    * `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7`
 7.  Instalar el siguiente paquete:
    * `apt-transport-https`
 8.  Crear el fichero `/etc/apt/sources.list.d/passenger.list` con el siguiente contenido:
    * `deb https://oss-binaries.phusionpassenger.com/apt/passenger saucy main`
 9.  Actualizar el repositorio e instalar el siguiente paquete:
    * `libapache2-mod-passenger`

## Buenas prácticas

*  [Skinny Controller, Fat Model](http://weblog.jamisbuck.org/2006/10/18/skinny-controller-fat-model)
*  [Nesting resources](http://weblog.jamisbuck.org/2007/2/5/nesting-resources): Resources should never be nested more than 1 level deep.

## Tips

### Visibilidad de Helpers

Los métodos definidos en los módulos Helper (`app/helpers/<controller>_helper.rb`) son visibles en las vistas por defecto. Para que estén disponibles en los controllers hay que hacer un `include`. Si lo hacemos en el controller base (`ApplicationController`) estará disponibles en todos los controllers dado que éstos heredan de `ApplicationController`.

### Mejora en rendimiento en Desarrollo

Rails 3.1 introdujo el concepto del [asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html). Desafortunadamente esto causa problemas de rendimiento en el entorno de desarrollo. Para mejorarlo se puede utilizar la tarea de precompilador siguiente:

```bash
$ bundle exec rake assets:precompile:nondigest
```

Esto provoca que los cambios en los ficheros asset no sean incluidos automáticamente cuando recargamos la página. Para forzar su refresco hay que volver a ejecutar el comando anterior.

### Borrado de assets

Rails proporciona la siguiente tarea de precompilador que borrará el directorio `public/assets`, cosa que puede resultar útil antes de un commit.

```bash
$ bundle exec rake assets:clean
```

Esta orden puede solucionar el problema con el `font-awesome`, que en ocasiones se dibuja mal.

También puede merecer la pena incluir el directorio `public/assets` en el fichero `.gitignore`.

### Actualización de paquetes

Comandos interesantes relacionados con las versiones de los paquetes y su gestión:

*  `bundle outdated`: Informe de paquetes desactualizados.
*  `bundle outdated <paquete>`: Informa sobre el nivel de actualización de un paquete.
*  `bundle update`: Actualiza todos los paquetes.
*  `bundle update <paquete>`: Actualiza el paquete.

### Muestra el mapa de rutas

```bash
$ bundle exec rake routes
```

### Muestra todas las tareas

```bash
$ bundle exec rake -T
```

### Instalación de gem

Tras la instalación de un gem generalmente hay que instalar y ejecutar las migraciones de base de datos con los siguientes comandos:

```bash
$ rake railties:install:migrations
$ rake db:migrate
```

Para instalar una versión específica de una gem hay que añadir el argumento `--version`, como por ejemplo:

```bash
$ gem install --version '3.0.13' passenger
```

### Activar modo debug

Instalar primero la gem `debugger`:

```bash
$ sudo gem install debugger
```

Añadir al Gemfile lo siguiente (probablemente sólo sea necesario en el entorno de desarrollo):

	group :development do
	  gem 'debugger'
	end

Insertar en el código una llamada a `debugger` en el punto del código donde queramos que se detenga la ejecución.

Finalmente para arrancar el servidor en modo debug:

```bash
$ bundle exec rails s --debugger
```

Lo anterior sirve para depurar sobre Webrick. Para hacerlo bajo Passenger seguir las instrucciones de este [post](http://chrisadams.me.uk/2009/04/28/how-to-set-up-a-debugger-with-mod_railspassenger/) (con la ayuda de [este otro](http://stackoverflow.com/questions/10678779/debugging-rails-with-passenger-and-apache)). De forma resumida consiste en ejecutar:

```bash
$ cd <app_root>
$ sudo gem install ruby-debug19
```

Generar un task con:

```bash
$ bundle exec rails g task myapplication restart
```

Añadir lo siguiente al final del fichero `config/environments/development.rb`:

```ruby
if File.exists?(File.join(RAILS_ROOT,'tmp', 'debug.txt'))
  require 'ruby-debug'
  Debugger.wait_connection = true
  Debugger.start_remote
  File.delete(File.join(RAILS_ROOT,'tmp', 'debug.txt'))
end
```

Ejecutar:

```bash
$ bundle exec rake myapplication:restart DEBUG=true
```

Y una vez que hagamos una request para que se reinicie la aplicación ejecutar:

```bash
$ rdebug -c
```

### Generación de un modelo

El siguiente comando creará un modelo para una entidad además de la migration correspondiente en la base de datos:

```bash
$ bundle exec rails g model spree/product_layout name:string view:string description:text
```

### Path Helpers

Dada la siguiente definición de resources anidados:

```ruby
resources :magazines do
  resources :ads
end
```

Alternativamente al uso de los path helpers habituales, cuando se pasa como argumento un objeto se puede dejar a Rails que decida automáticamente el path helper necesario, es decir las siguientes líneas serán equivalentes:

```ruby
<%= link_to "Ad details", magazine_ad_path(@magazine, @ad) %>
<%= link_to "Ad details", url_for([@magazine, @ad]) %>
```

En helpers como `link_to` podemos indicar simplemente los objetos:

```ruby
<%= link_to "Ad details", [@magazine, @ad] %>
```

O si queremos enlazar directamente a la `magazine` en lugar de un array pasaremos directamente el objeto padre:

```ruby
<%= link_to "Magazine details", @magazine %>
```

### Tareas en base de datos

*  `db:create`: creates the database for the current env
*  `db:create:all`: creates the databases for all envs
*  `db:drop`: drops the database for the current env
*  `db:drop:all`: drops the databases for all envs
*  `db:migrate`: runs migrations for the current env that have not run yet
*  `db:migrate:up`: runs one specific migration
*  `db:migrate:down`: rolls back one specific migration
*  `db:migrate:status`: shows current migration status
*  `db:migrate:rollback`: rolls back the last migration
*  `db:migrate:redo`: runs (`db:migrate:down` `db:migrate:up`) or (`db:migrate:rollback` `db:migrate`) depending on the specified migration
*  `db:migrate:reset`: runs `db:drop` `db:create` `db:migrate`
*  `db:forward`: advances the current schema version to the next one
*  `db:seed`: (only) runs the db/seed.rb file
*  `db:schema:load`: loads the schema into the current env's database
*  `db:schema:dump`: dumps the current env's schema (and seems to create the db aswell)
*  `db:setup`: runs `db:schema:load` `db:seed`
*  `db:reset`: runs `db:drop` `db:setup`

### Gestión del plural/singular

Cuando un modelo/recurso tenga un plural irregular, se puede gestionar manualmente por medio de un `Inflector`. Consultar esta [guía](http://guides.rubyonrails.org/routing.html#overriding-the-singular-form).

### Relación entre modelos

Estos serían los pasos para establecer una relación 1:n entre dos modelos preexistentes. Se basa en [este apartado](http://guides.rubyonrails.org/association_basics.html#creating-foreign-keys-for-belongs_to-associations) de las Rails Guides.

Partimos de los modelos `Spree::Product` de la gem `spree_core` y el modelo `Spree::ProductLayout` propio de nuestra aplicación. La relación será un `belongs_to` de Product a ProductLayout, es decir un n:1. Empezamos añadiendo la relación al modelo Product. Como es una entidad de una gem lo haremos con un fichero decorator:

```ruby
#app/models/spree/product_decorator.rb
Spree::Product.class_eval do
  belongs_to :product_layout
end
```

A continuación generamos un migration para añadir el campo que establece la relación en la tabla que mantiene el modelo Product:

```bash
$ bundle exec rails g migration AddProductLayoutRelationToProducts
```

Ahora lo editamos para incorporar el campo:

```ruby
#db/migrate/20130228153926_add_product_layout_relation_to_products.rb
class AddProductLayoutRelationToProducts < ActiveRecord::Migration
  def change
    change_table :spree_products do |t|
      t.references :product_layout
    end
  end
end
```

Finalmente ejecutamos el migrate:

```bash
$ bundle exec rake db:migrate
```

### Inspeccionar la definición de un método

Si queremos averiguar en qué módulo se encuentra definido un método ejecutamos en consola IRB lo siguiente:

```ruby
puts Objeto.new.method(:metodo).source_location
```

o

```ruby
puts Objeto.instance_method(:metodo).source_location
```

Sustituyendo "Objeto" y "metodo" por lo que corresponda. [Fuente](http://www.jonathanleighton.com/articles/2012/finding-methods/).

Si se trata de un helper partimos de `helper`, por ejemplo:

```ruby
helper.method(:tab).source_location
```

### Listar gems instalados

```bash
$ gem list --local
```

Si queremos sólo las versiones de una gem, de `rails` por ejemplo:

```bash
$ gem list --local rails
```

### Generar el API de rails

Para tener en local la versión actualizada del API de rails:

```bash
$ rails new dummy_app
$ cd dummy_app
$ bundle exec rake doc:rails
```

Luego mover el subdirectorio `doc/api/index.html` a donde nos interese y borrar la dummy_app.

### RubyGems Documentation

Para visualizar la documentación de todas las gems instaladas en el sistema ejecutar:

```bash
$ gem server
```

Y abrir la dirección: http://localhost:8808

### Problema con el encoding de algunas fuentes en UTF-8

Al incorporar el gem [spree_sermepa](https://github.com/picazoH/spree_sermepa) se produjo el problema descrito [aquí](https://github.com/carlhuda/bundler/issues/1570).

Hay varias formas de solucionarlo. Una es añadir:

```ruby
if RUBY_VERSION =~ /1.9/
  Encoding.default_external = Encoding::UTF_8
  Encoding.default_internal = Encoding::UTF_8
end
```

en la parte superior del Gemfile.

Si se utiliza Passenger para servir la aplicación, otra opción es sustituir la siguiente variable del fichero `/etc/apache2/envvars`:

	export LANG=C

por:

	export LANG=es_ES.UTF-8

### Downgrade de Rubygems

Tras actualizar a la versión 2.0.3 de Rubygems empecé a tener problemas a la hora de hacer `bundle install`. Aunque me pedía el password de root luego se producían errores de permisos en los directorios donde se almacenan las gems. La solución fue volver a una versión anterior de Rubygems. En concreto la misma que había en ese momento en el servidor de DinaHosting, es decir la 1.8.23. Se hizo con el siguiente comando:

```bash
$ sudo gem update --system 1.8.23
```

### Solución a error "Could not find rake-10.0.4 in any of the sources" con Passenger

En el alojamiento de DinaHosting, al ejecutar por primera vez una aplicación Ruby ejecutada con Passport, se produce el error siguiente:

    Could not find rake-10.0.4 in any of the sources

Instalando las gemas en el home del usuario se soluciona el error:

```bash
$ bundle install --deployment
```

Esto instala las gem's en el directorio `vendor/bundle`.

### Especificar entorno

Para especificar el entorno en una tarea `rake` añadir al final de la orden `RAILS_ENV=<entorno>`. Por ejemplo para desarrollo:

```bash
$ bundle exec rake routes RAILS_ENV=development
```

Con el script `rails`, depende. Si se quiere arrancar la consola añadir al final el entorno sin más. Por ejemplo para desarrollo:

```bash
$ bundle exec rails c development
```

Si se quiere arrancar el servidor Webrick añadir el entorno por medio de la opción `-e`. Por ejemplo para desarrollo:

```bash
$ bundle exec rails s -e development
```

### Desinstalación de todas las gems

Con el siguiente comando:

```bash
$ gem list | cut -d" " -f1 | xargs gem uninstall -aIx
```

Posteriormente habrá que volver a instalar Bundler y el resto de gems. Para ello:

```bash
$ sudo gem install bundler
$ cd <proyecto>
$ bundle install
```

### Plurales/Singulares de resources

Recurso de tipo colección dentro de un namespace:

| Elemento                 | Plural/Singular | Ejemplo                                            |
|:--------                 |:--------------- |:-------                                            |
| Tabla en base de datos   | Plural          | spree_posts                                        |
| Clase del modelo         | Singular        | Spree::Post                                        |
| Fichero del modelo       | Singular        | spree/post.rb                                      |
| Clase del controlador    | Plural          | Spree::PostsController                             |
| Fichero del controlador  | Plural          | spree/posts_controller.rb                          |
| rails generator          | Singular        | rails g resource spree/post title:string body:text |
| Ruta en config/routes.rb | Plural          | resources :posts                                   |
| Directorio en views      | Plural          | spree/posts                                        |

### Ejecutar una versión concreta de rails

Si tenemos instaladas varias versiones del gem de rails, para forzar que se utilice el script `rails` de una versión concreta, pondremos la versión de la siguiente forma:

```bash
$ rails _3.2.13_ -v
```

De forma que si por ejemplo queremos generar un nuevo proyecto con la versión 3.2.13 haremos:

```bash
$ rails _3.2.13_ new nueva_app
```

### Ejecutar una versión concreta de spree

Si tenemos instaladas varias versiones del gem de spree, para forzar que se utilice el script `spree` de una versión concreta, pondremos la versión de la siguiente forma:

```bash
$ spree _1.3.3_ -v
```

De forma que si por ejemplo queremos hacer la instalación dentro de una aplicación rails nueva con la versión 1.3.3 de Spree haremos:

```bash
$ spree _1.3.3_ install
```

### Diagramas ERD

A continuación se indica el comando para obtener una serie de diagramas ERD interesantes. La documentación de todos los parámetros de ERD está [aquí](http://rails-erd.rubyforge.org/customise.html).

Modelado de producto en Spree:

```bash
$ bundle exec rake erd attributes=foreign_keys only="Spree::Product,Spree::OptionType,Spree::OptionValue,Spree::Variant,Spree::ProductOptionType" title='Productos'
```
