title: 2019-01-29 Bloqueo de llamadas entrantes en Telsome
summary: Bloqueo de llamadas entrantes en proveedor de VoIP Telsome.
date: 2019-01-29 19:20:00

![Telsome Logo](/images/posts/telsome.png)

## Enlaces

* [Cómo bloquear llamadas de determinados números](https://blog.telsome.es/manuales/telefonia-ip/bloquear-llamadas-determinados-numeros/)
* [Informe detallado de llamadas – CDR](https://blog.telsome.es/manuales/telefonia-ip/informe-detallado-llamadas-cdr/)

## Procedimiento

Vamos a describir cómo impedir que se produzca la entrada de una llamada desde un número determinado en el servicio de VoIP Telsome. Típicamente nos interesará esto para bloquear las llamadas comerciales SPAM.

Necesitamos el número que queremos bloquear. Si no lo recordamos o no tenemos registro de llamadas en el terminal, se puede consultar en la información detallada de las llamadas recibidas a través del servicio. Para ello iniciar sesión en [la cuenta Telsome](https://www.telsome.es/mi-cuenta.html) con nuestras credenciales. Una vez dentro, navegar siguiendo la siguiente ruta:

```
Configuración avanzada > Enlaces rápidos > Costos de llamada
```

Allí encontraremos el detalle de todas las llamadas emitidas y recibidas. Una vez conozcamos el número que queremos bloquear, navegaremos siguiendo la ruta:

```
Configuración avanzada > Extensiones > (clic sobre nuestra extensión) >
Telefonía > Reglas de llamadas entrantes
```

Allí rellenaremos el pequeño formulario con el rótulo `Agregar desvíos`:

![Telsome Bloqueo](/images/posts/telsome-bloqueo.png)

Sustituyendo el número del ejemplo anterior (999888777) por el que nos interese. En el formulario, el primer desplegable nos permite elegir el efecto que observará el llamante. En el ejemplo he seleccionado `reproductor ocupado`, pero también servirían las opciones `reproductor congestionado` o `colgar`. Una vez que pulsemos el botón `OK` se incorporará a la lista inferior y pasará a ser efectiva.
