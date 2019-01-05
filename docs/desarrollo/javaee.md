---
layout: default
permalink: /desarrollo/javaee.html
---

# JavaEE

## DisplayTag & Struts2

### Subtabla en base a lista anidada

```xml
<display:table name="platformList" id="platform" pagesize="0" requestURI="" class="displaytag">
<display:column property="name" title="Platform" />
<s:set name="formats" value="#attr.platform.formats" />
<display:column title="Formats">
<display:table name="formats" id="format" class="simple sublist">
<s:set name="screenRes" value="#attr.format.screenWidth + 'x' + #attr.format.screenHeight" />
<s:set name="wpRes" value="#attr.format.wallpaperWidth + 'x' + #attr.format.wallpaperHeight" />
<display:column title="Screen Resolution"><s:property value="screenRes"/></display:column>
<display:column title="Wallpaper Resolution"><s:property value="wpRes"/></display:column>
<display:column title="File"><s:file name="pic" label="Pic" theme="simple"/></display:column>
</display:table>
</display:column>
</display:table>
```
    
###  SessionID en Action

```java
public class MyActionClass extends ActionSupport implements ServletRequestAware {
   //...

   // Objeto HttpServletRequest asociado a la request. Inyectado por el interceptor servletConfig
   private HttpServletRequest servletRequest;

   /**
    * Implementación de interfaz ServletRequestAware
    * @param servletRequest Objeto HttpServletRequest asociado a la request
    */
   @Override
   public void setServletRequest(HttpServletRequest servletRequest) {
       this.servletRequest = servletRequest;
   }

   public HttpServletRequest getServletRequest() {
       return this.servletRequest;
   }

   //...

   @Override
   public String execute() throws Exception {
       //...
       // Obtenemos el ID de la sesión
       String sessionID = this.servletRequest.getSession().getId();
       //...
   }
}
```

### Mapa de Session

```java
public class MyActionClass extends ActionSupport implements SessionAware {
   //...

   // Mapa de parámetros de la sesión. Inyectado por el interceptor servletConfig
   private Map<String, Object> session;

   /**
    * Implementación de interfaz SessionAware
    * @param session El mapa de session Servlet
    */
   @Override
   public void setSession(Map<String, Object> session) {
       this.session = session;
   }

   public Map<String, Object> getSession() {
       return this.session;
   }

   //...

   @Override
   public String execute() throws Exception {
       //...
       // Ponemos y cogemos datos de la sessión
       getSession().put("objeto", objeto);
       objeto = getSession().get("objeto");
       //...
   }
}
```

## JSP

### Prepoblado de combo desde el propio JSP

```jsp
<s:select label="Priority" name="wallpaper_priority" list="#{-2:'Very Low',-1:'Low',0:'Normal',1:'High',2:'Very High'}" />
```

### Inyectar cabecera HTTP en JSP

```jsp
<% response.setHeader("P3P", "CP=\"HONK\""); %>
```
