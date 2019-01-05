---
layout: default
permalink: /desarrollo/android.html
---

# Android

## Entorno

* [Todos los drivers para instalar ADB en Windows sin morir en el intento](http://www.elandroidelibre.com/2016/09/instalar-adb-en-windows.html)

## Compilación AOSP

* [Getting Started: Building Android From Source](http://xda-university.com/as-a-developer/getting-started-building-android-from-source)
* [How to Build an Android ROM](http://xda-university.com/as-a-developer/introduction-how-an-android-rom-is-built)

## Documentación clave

* [ID's de los View's](https://developer.android.com/guide/topics/ui/declaring-layout.html#id)

## Tips varios

*  [Activity restart on rotation Android](http://stackoverflow.com/questions/456211/activity-restart-on-rotation-android)
*  [Lint, eliminando la pelusa de nuestras aplicaciones](http://androcode.es/2011/12/lint-eliminando-la-pelusa-de-nuestras-aplicaciones/)

## Librerías

*  [RoboGuice la librería que exprime nuestro código](http://androcode.es/2011/12/roboguice-la-libreria-que-exprime-nuestro-codigo/)
*  [OrmLite - Lightweight Object Relational Mapping (ORM) Java Package](http://ormlite.com/)
*  [Mobile Framework that uses the actual features of #HTML5, #CSS3 and #JavaScript](http://www.lungojs.com/)

## Tutoriales

*  [Android Development Tutorial (Lars Vogel)](http://www.vogella.de/articles/Android/article.html)
*  [Android ListView and ListActivity (Lars Vogel)](http://www.vogella.de/articles/AndroidListView/article.html)
*  [Pasando información entre Actividades (Activity) en Android](http://www.metafisicainformatica.com/2011/03/02/pasando-informacion-entre-actividades-activity-en-android/)
*  [Avoid memory leaks on Android](http://www.curious-creature.org/2008/12/18/avoid-memory-leaks-on-android/)

## Snippets

*  [WikiDroid](http://www.wikidroid.es/index.php?title=P%C3%A1gina_Principal)
*  [Categoría Android en WikiCode](http://es.wikicode.org/index.php/Categor%C3%ADa:Android)
*  [Androcode](http://androcode.es/)
*  [Android Snippets](http://www.androidsnippets.com/)

## Estructuras de datos

*  [Android DataFramework, creando la estructura de la Base de Datos](http://androcode.es/2011/10/android-dataframework-creando-la-estructura-de-la-base-de-datos/)
*  [Usando Android DataFramework en nuestro proyecto](http://androcode.es/2011/10/usando-android-dataframework-en-nuestro-proyecto/)

## Sobre Diseño

*  [Hello, Views](http://developer.android.com/resources/tutorials/views/index.html)
*  [Common Layout Objects](http://developer.android.com/guide/topics/ui/layout-objects.html)
*  [Android Interaction Desing Patterns](http://www.androidpatterns.com/) :!:
*  [Icon Design Guidelines](http://developer.android.com/guide/practices/ui_guidelines/icon_design.html)
*  [Widget Design Guidelines](http://developer.android.com/guide/practices/ui_guidelines/widget_design.html)
*  [Android App Developers GUI Kits, Icons, Fonts and Tools](http://speckyboy.com/2010/05/10/android-app-developers-gui-kits-icons-fonts-and-tools/)
*  [Android R Drawable Explorer](http://androiddrawableexplorer.appspot.com/)
*  [20 herramientas útiles para Desarrolladores Android](http://www.elandroidelibre.com/2011/12/20-herramientas-utiles-para-desarrolladores-android.html)
*  [Android Design](http://developer.android.com/design/index.html)
*  [El cambio de tendencia en la UI de Android: el Menú Lateral](http://www.elandroidelibre.com/2012/06/el-cambio-de-tendencia-en-la-ui-de-android-el-men-lateral.html)

## Mapas

*  [Obtener APIKey](http://code.google.com/intl/es-ES/android/add-ons/google-apis/mapkey.html)

Tu clave es:

    0V21y2J7NRVSVKA...5C9Ag

Esta clave es válida para todas las aplicaciones firmadas con el certificado cuya huella dactilar sea:

    C2:EC:22:8F:...:56:39

Incluimos un diseño xml de ejemplo para que puedas iniciarte por los senderos de la creación de mapas:

```xml
<com.google.android.maps.MapView
   android:layout_width="fill_parent"
   android:layout_height="fill_parent"
   android:apiKey="0V21y2J7NRVSVKA...5C9Ag"
   />
```

## Depurar

Añadir el atributo siguiente al bloque "application":

	android:debuggable="true"


Solicitar el permiso siguiente:

	<uses-permission android:name="android.permission.SET_DEBUG_APP" />

## Logcat filtrado

Ejemplo de una expresión de filtrado que suprime (silencia) todos los mensajes de log excepto los que tienen el tag "ActivityManager" con una prioridad Info o superior, y los que tienen el tag "MyApp" con una prioridad Debug o superior:

```bash
$ adb logcat ActivityManager:I MyApp:D *:S
```

Las prioridades de log son:

*  V — Verbose (lowest priority)
*  D — Debug
*  I — Info
*  W — Warning
*  E — Error
*  F — Fatal
*  S — Silent (highest priority, on which nothing is ever printed)

## Dumpsys y Dumpstate

Hace un volcado de los datos del sistema. Viene bien para encontrar componentes instalados (Aplicaciones, ContentProvider's, etc.):

```bash
$ adb shell dumpsys
```

```bash
$ adb shell dumpstate
```

## Buscar CallerID

```java
import android.database.Cursor;
import android.net.Uri;
import android.provider.ContactsContract;

Uri uri = Uri.withAppendedPath(ContactsContract.PhoneLookup.CONTENT_FILTER_URI, Uri.encode("+34976010101"));
Cursor c = getContentResolver().query(uri, new String[]{ContactsContract.PhoneLookup.DISPLAY_NAME}, null, null, null);
```

## Manejo de URI's de contactos

La API de Contacts de Android es muy potente y compleja. Los conceptos básicos se describen [aquí](http://developer.android.com/resources/articles/contacts.html).

Se manejan dos tipos de URI's:

*  URI's de tipo tabla: Apuntan por ejemplo a una tabla completa como puede ser la de RawContacts.
*  URI's de tipo item: Apuntan a un registro concreto de una tabla, por ejemplo un RawContact.

### URI de la tabla raíz Contacts

```java
import android.net.Uri;
import android.provider.ContactsContract;
Uri contactsUri = ContactsContract.Contacts.CONTENT_URI;
```

### URI de la subtabla RawContacts

```java
import android.net.Uri;
import android.provider.ContactsContract;
Uri rawContactsUri = ContactsContract.RawContacts.CONTENT_URI;
```

### URI de la subtabla Data

```java
import android.net.Uri;
import android.provider.ContactsContract;
Uri datasUri = ContactsContract.Data.CONTENT_URI;
```

### URI de la subtabla Data sólo con los registros de un RawContact concreto

```java
import android.net.Uri;
import android.provider.ContactsContract;
// Tenemos en rawContactUri el URI de un RawContact. Será del tipo content://com.android.contacts/raw_contacts/_id
Uri datasUri = Uri.withAppendedPath(rawContactUri, RawContacts.Entity.CONTENT_DIRECTORY);
```

### Obtener ID a partir de una URI de tipo item

Por ejemplo el método para insertar un RawContact devuelve una URI de tipo item (no tabla). Para obtener el ID de dicho elemento podemos usar algunas funciones que hay en la clase ''android.content.ContentUris''.

```java
import android.content.ContentUris;
long rawContactId = ContentUris.parseId(rawContactUri);
```

### Obtener la URI de tipo item de un elemento concreto a partir de la tabla

Por ejemplo tenemos el ID de un elemento y queremos una URI para él.

```java
import android.net.Uri;
import android.provider.ContactsContract;
import android.content.ContentUris;
Uri rawContactUri = ContentUris.withAppendedId(ContactsContract.RawContacts.CONTENT_URI, rawContactId);
```

Resumiendo:

| Significado | URI (string) | URI (constant) |
|:----------- |:------------ |:-------------- |
| URI de toda la tabla RawContacts | content://com.android.contacts/raw_contacts | Uri rawContactsUri = android.provider.ContactsContract.RawContacts.CONTENT_URI |
| URI de un registro concreto de RawContacts | content://com.android.contacts/raw_contacts/<_id> | Uri rawContactUri = ContentUris.withAppendedId(android.provider.ContactsContract.RawContacts.CONTENT_URI, rawContactId); |
| URI de una subtabla (subdirectorio lo llaman en la documentación) con los Datas asociados a un RawContact concreto | content://com.android.contacts/raw_contacts/<_id>/entity | Uri datasUri = Uri.withAppendedPath(rawContactUri, RawContacts.Entity.CONTENT_DIRECTORY); |

## Obtener el ID de un recurso en el ContentProvider de audio externo

```java
String outText = "";
Uri externalMediaUri = android.provider.MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
String[] projection = new String[] {android.provider.BaseColumns._ID};
String where = android.provider.MediaStore.MediaColumns.TITLE + "=?";
String[] whereArgs = new String[] { "Space Oddity" };
Cursor c = managedQuery(externalMediaUri, projection, where, whereArgs, null);
while (c.moveToNext()) {
    for (int i = 0; i < c.getColumnCount(); i++) {
        outText += c.getColumnName(i) + "= " + c.getString(i) + "\n";
    }
}
```

## Inserción de un RawContact de tipo "vnd.sec.contact.phone"

```java
ArrayList<ContentProviderOperation> operationList = new ArrayList<ContentProviderOperation>();
Builder builder = ContentProviderOperation.newInsert(RawContacts.CONTENT_URI);
builder.withValue(RawContacts.ACCOUNT_NAME, "vnd.sec.contact.phone");
builder.withValue(RawContacts.ACCOUNT_TYPE, "vnd.sec.contact.phone");
operationList.add(builder.build());

builder = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI);
builder.withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0);
builder.withValue(ContactsContract.Data.MIMETYPE,
        ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE);
builder.withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, "Felipito");
operationList.add(builder.build());

builder = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI);
builder.withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0);
builder.withValue(ContactsContract.Data.MIMETYPE, CommonDataKinds.Phone.CONTENT_ITEM_TYPE);
builder.withValue(CommonDataKinds.Phone.TYPE, CommonDataKinds.Phone.TYPE_MAIN);
builder.withValue(CommonDataKinds.Phone.NUMBER, "976010101");
operationList.add(builder.build());

builder = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI);
builder.withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0);
builder.withValue(ContactsContract.Data.MIMETYPE, CommonDataKinds.Photo.CONTENT_ITEM_TYPE);
ByteArrayOutputStream stream = new ByteArrayOutputStream();
bitmap.compress(Bitmap.CompressFormat.JPEG, 75, stream);
builder.withValue(CommonDataKinds.Photo.PHOTO, stream.toByteArray());
builder.withValue(RawContacts.Data.IS_SUPER_PRIMARY, 1);
operationList.add(builder.build());

try {
    getContentResolver().applyBatch(ContactsContract.AUTHORITY, operationList);
} catch (RemoteException e) {
    e.printStackTrace();
} catch (OperationApplicationException e) {
    e.printStackTrace();
}
```

## Extraer el nombre, el número y la foto de los Contacts de tipo "vnd.sec.contact.phone"

```java
Uri rawContactsUri = ContactsContract.RawContacts.CONTENT_URI;
String[] projection = new String[] { ContactsContract.RawContacts._ID };
String where = ContactsContract.RawContacts.ACCOUNT_TYPE + "=? AND "
        + ContactsContract.RawContacts.ACCOUNT_NAME + "=? AND "
        + ContactsContract.RawContacts.DELETED + "=?";
String[] whereArgs = new String[] { "vnd.sec.contact.phone", "vnd.sec.contact.phone", "0" };
String sortOrder = "display_name ASC";
Cursor c = managedQuery(rawContactsUri, projection, where, whereArgs, sortOrder);
outText += rawContactsUri.toString() + "\n";
outText += c.getCount() + "\n";
while (c.moveToNext()) {
    int colPos = c.getColumnIndex(ContactsContract.RawContacts._ID);
    long rawContactId = Long.parseLong(c.getString(colPos));
    Uri rawContactUri = ContentUris.withAppendedId(ContactsContract.RawContacts.CONTENT_URI,
            rawContactId);
    Uri datasUri = Uri.withAppendedPath(rawContactUri, RawContacts.Entity.CONTENT_DIRECTORY);
    String name = "";
    String number = "";
    Bitmap bitmap = null;

    String[] projection1 = new String[] { CommonDataKinds.StructuredName.DISPLAY_NAME };
    String where1 = Data.MIMETYPE + "=?";
    String[] whereArgs1 = new String[] { CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE };
    Cursor c1 = managedQuery(datasUri, projection1, where1, whereArgs1, null);
    if (c1.moveToNext()) {
        name = c1.getString(c1.getColumnIndex(CommonDataKinds.StructuredName.DISPLAY_NAME));
        c1.close();
    }

    String[] projection2 = new String[] { CommonDataKinds.Phone.NUMBER };
    String where2 = Data.MIMETYPE + "=?";
    String[] whereArgs2 = new String[] { CommonDataKinds.Phone.CONTENT_ITEM_TYPE };
    Cursor c2 = managedQuery(datasUri, projection2, where2, whereArgs2, null);
    if (c2.moveToNext()) {
        number = c2.getString(c2.getColumnIndex(CommonDataKinds.Phone.NUMBER));
        c2.close();
    }

    String[] projection3 = new String[] { CommonDataKinds.Photo.PHOTO };
    String where3 = Data.MIMETYPE + "=?";
    String[] whereArgs3 = new String[] { CommonDataKinds.Photo.CONTENT_ITEM_TYPE };
    Cursor c3 = managedQuery(datasUri, projection3, where3, whereArgs3, null);
    if (c3.moveToNext()) {
        byte[] photo = c3.getBlob(c3.getColumnIndex(CommonDataKinds.Photo.PHOTO));
        bitmap = BitmapFactory.decodeByteArray(photo, 0, photo.length);
        c3.close();
    }

    outText += "ID= " + rawContactId + "; Nombre= " + name + "; Número= " + number;
    if (bitmap != null) {
        outText += "; Ancho foto= " + bitmap.getWidth() + "; Alto foto= " + bitmap.getHeight();
    }
    outText += "\n";
}
c.close();
```

## Borrado de los contactos de un tipo

```java
Uri rawContacts = ContactsContract.RawContacts.CONTENT_URI;
String where = ContactsContract.RawContacts.ACCOUNT_TYPE + "=?";
String[] whereArgs = new String[] { "es.eduardofilo.app" };
getContentResolver().delete(rawContacts, where, whereArgs);
```

## Borrado de un contacto

```java
Uri rawContacts = ContactsContract.RawContacts.CONTENT_URI;
Uri rawContactUri = ContentUris.withAppendedId(ContactsContract.RawContacts.CONTENT_URI, 13);
getContentResolver().delete(rawContactUri, null, null);
```

## Actualizar el nombre de un contacto

```java
long rawContactId = 14;
Uri data = ContactsContract.Data.CONTENT_URI;
ContentValues values = new ContentValues();
values.put(CommonDataKinds.StructuredName.DISPLAY_NAME, "Jorgito");
String where = Data.MIMETYPE + "=? AND " + ContactsContract.Data.RAW_CONTACT_ID + "=?";
String[] whereArgs = new String[] { CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE, Long.toString(rawContactId) };
getContentResolver().update(data, values, where, whereArgs);
```

## Inserción de un RawContact de tipo "vnd.sec.contact.phone"

```java
ContentValues values = new ContentValues();
values.put(RawContacts.ACCOUNT_TYPE, "vnd.sec.contact.phone");
values.put(RawContacts.ACCOUNT_NAME, "vnd.sec.contact.phone");
Uri rawContactUri = getContentResolver().insert(RawContacts.CONTENT_URI, values);
long rawContactId = ContentUris.parseId(rawContactUri);

values.clear();
values.put(Data.RAW_CONTACT_ID, rawContactId);
values.put(Data.MIMETYPE, CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE);
values.put(CommonDataKinds.StructuredName.DISPLAY_NAME, "Pepito");
Uri data1Uri = getContentResolver().insert(ContactsContract.Data.CONTENT_URI, values);
values.clear();

values.put(Data.RAW_CONTACT_ID, rawContactId);
values.put(Data.MIMETYPE, CommonDataKinds.Phone.CONTENT_ITEM_TYPE);
values.put(CommonDataKinds.Phone.TYPE, CommonDataKinds.Phone.TYPE_MAIN);
values.put(CommonDataKinds.Phone.NUMBER, "976010101");
Uri data2Uri = getContentResolver().insert(ContactsContract.Data.CONTENT_URI, values);
```

## Inserción de un RawContact de tipo "vnd.sec.contact.phone"

Igual que antes pero hecho con el sistema de operaciones por lotes de los ContentProvider's.

```java
ArrayList<ContentProviderOperation> operationList = new ArrayList<ContentProviderOperation>();
Builder builder = ContentProviderOperation.newInsert(RawContacts.CONTENT_URI);
builder.withValue(RawContacts.ACCOUNT_NAME, "vnd.sec.contact.phone");
builder.withValue(RawContacts.ACCOUNT_TYPE, "vnd.sec.contact.phone");
operationList.add(builder.build());

builder = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI);
builder.withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0);
builder.withValue(ContactsContract.Data.MIMETYPE,
        ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE);
builder.withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, "Debianito");
operationList.add(builder.build());

builder = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI);
builder.withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0);
builder.withValue(ContactsContract.Data.MIMETYPE, CommonDataKinds.Phone.CONTENT_ITEM_TYPE);
builder.withValue(CommonDataKinds.Phone.TYPE, CommonDataKinds.Phone.TYPE_MAIN);
builder.withValue(CommonDataKinds.Phone.NUMBER, "976010101");
operationList.add(builder.build());

try {
    getContentResolver().applyBatch(ContactsContract.AUTHORITY, operationList);
} catch (RemoteException e) {
    e.printStackTrace();
} catch (OperationApplicationException e) {
    e.printStackTrace();
}
```

## Localizar un Launcher que no sea el nuestro

```java
PackageManager pm = getPackageManager();
Intent intent = new Intent(Intent.ACTION_MAIN);
intent.addCategory(Intent.CATEGORY_HOME);
List<ResolveInfo> launchers = pm.queryIntentActivities(intent, 0);
String packageName = null;
String name = null;
for (ResolveInfo ri : launchers) {
    if (!ri.activityInfo.name.equals("es.eduardofilo.app.mobile.IdentificarTerminal")) {
        name = ri.activityInfo.name;
        packageName = ri.activityInfo.packageName;
        break;
    }
}

Intent myIntent = new Intent();
myIntent.setClassName(packageName, name);
startActivity(myIntent);
```

## Obtener un authToken de un Account

```java
mAccountManager = AccountManager.get(this);
Account[] accounts = mAccountManager.getAccountsByType(ACCOUNT_TYPE);
for (Account account : accounts) {
    outText += account.toString() + "\n";
    AccountManagerFuture<Bundle> accountManagerFuture = mAccountManager.getAuthToken(account,
                    "es.eduardofilo.app", true, null, null);
    Bundle authTokenBundle;
    String token = null;
    try {
        authTokenBundle = accountManagerFuture.getResult();
        token = authTokenBundle.get(AccountManager.KEY_AUTHTOKEN).toString();
    } catch (OperationCanceledException e) {
        e.printStackTrace();
    } catch (AuthenticatorException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    }

    if (!TextUtils.isEmpty(token)) {
        outText += token + "\n";
    }
}
```
