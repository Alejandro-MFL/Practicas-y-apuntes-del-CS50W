# HTTP 
siglas = " Protocolo de transfernecia de hipertexto"
respuestas = """ 
    200 Ok
    301 Moved Permanently
    403 Forbidden
    404 Not Found
    500 Internal Server Error
"""

# Estructura basica de Django
Elementos = """ 
# Cuando creas un proyecto inicia con una estructura basica, la cual sera el marco
    Estructura:
    x/
    ├── manage.py           # 1. Desde donde controlaremos los comandos
    ├── db.sqlite3          # 2. Base de datos que usa sqlite3
    ├── y(app)              # 3. Aplicacion
    └── x/
        ├── __init__.py     # 4. Archivo vacio, suele quedarse asi. Permite importar modulos
        ├── asgi.py         # 5. Punto de entrada para servidores ASGI (Asynchronous Server Gateway Interface)
        ├── settings.py     # 6. Donde reside la configuracion del proyecto
        ├── urls.py         # 7. Enrutador principal del proyecto.
        └── wsgi.py         # 8. Punto de entrada para servidores WSGI (Web Server Gateway Interface)

        1. manage.py: Es el nucleo, sirve como entrada de los comandos de Django y es quien carga settings
        6. settings.py: Es donde reside la configuracion del proyecto, las bases de datos,
            las distintas aplicaciones, zona horaria , seguridad, plantillas, etc.
            Por lo que requiere que se añadan aqui los distintos elementos que crees.
        3. app: no esta al inicio, son como subproyectos especializados dentro del proyecto, modulos funcionales.
            Tienen sus propios elementos dentro:
                y/
                ├── __init__.py         # 9.  como 4, marca la carpeta como paquete Python
                ├── admin.py            # 10. registro de modelos para que aparezcan en el panel de administracion de Django
                ├── apps.py             # 11. configuración de la app
                ├── migrations/         # 12. historial de migraciones de base de datos para esta app
                │   └── __init__.py
                ├── models.py           # 13. aqui defines las clases de datos (el ORM). Cada clase es igual a una tabla en la base de datos.
                ├── tests.py            # 14. donde defines tests unitarios
                ├── views.py            # 15. aqui va la logica que responde a las requests
                │ * No se crean automaticamente pero seran necesarios
                ├── templates           # 16. carpeta donde guardar los archivos HTML
                ├── static              # 17. archivos staticos como imagenes
                └── urls.py             # 18. enlaza rutas especificas de esta app con sus vistas
"""
views = """ 
    Es la funcion o clase que recibe una petcion HTTP y que devuelve una vista.
    Esa vista puede ser:
        - Vista basada en funcion (FBV = Function Based View)
        ###
            from django.http import HttpResponse

            def hola(request):
                return HttpResponse("Hola desde Django 👋")
            def pepe(request, name):
                return render( request , "uffs/index.html",
                    {"name": name.capitalize()                  
                })
        ###
                
        - Vista basada en clase (CBV = Class Based View)
        ###
            from django.views import View
            from django.http import HttpResponse

            class HolaView(View):
                def get(self, request):
                    return HttpResponse("Hola desde una Class-Based View")        
        ###

        - Vistas genéricas (Generic Views)
        ###
            from django.views.generic import ListView
            from .models import Post

            class PostListView(ListView):
                model = Post
                template_name = "blog/post_list.html"
        ###

    Creacion de formularios  
        ###
        from django import forms    

        class NuevoFormulario(forms.Form):
            elemento = forms.CharField(label="Nuevo Elemento")
            prioridad = forms.IntegerField(label="Prioridad", min_value=1, max_value=10)

        # Con esto se comprueba que la informacion es correcta por parte del servidor
        def x(request):
            if request.method == "POST":
                form = NuevoFormulario(request.POST)
                if form.is_valid():
                    elemento = form.cleaned_data["elemento"]    # Esto asegura que los datos estan en una forma correcta
                    elementos.append(elemento)
                    return HttpResponseRedirect(reverse("appName :index"))
                else:
                    return render(request, direccionDelhtmlQueEnviaElFormulario, {"form": form})

            return render(request, direccionDelhtmlQueEnviaElFormulario, {"form": NuevoFormulario() })
        ###


"""
urls = """
# Aqui se colocan las rutas propias, las de el proyecto y las de la aplicacion
Ejemplo:
    -App:
    ###
        from django.urls import path
        from . import views   # Importamos las vistas de la misma app

        app_name = "search"
        urlpatterns = [
            path('', views.index, name='index'),                    # /blog/
            path('post/<int:id>/', views.ver_post, name='post'),    # /blog/post/5/
        ]
    ###
    -Proyecto:
    ###
        from django.contrib import admin
        from django.urls import path, include
        from . import views                             # opcional: si tienes vistas directas en el proyecto

        urlpatterns = [
            path('admin/', admin.site.urls),            # panel admin            
            path('', views.home, name='home'),          # página raíz del proyecto
            path('blog/', include('blog.urls')),        # delega en la app "blog"
            path('tienda/', include('tienda.urls'))     # delega en la app "tienda"
        ]
    ###

"""
templates = """ 
# Es la carpeta en la que se guardan los distintos archivos HTML, tanto los modelos como los deribados
    Para realizar un modelo, has de definir las zonas que son modificables:
        {% block head %}{% endblock %}
    Despues para usarlo de patron, en el derivado usa al principio 
        {% extends "direccion/nombrePatron.html" %}
        {% block head %} x {% endblock %}
    Tendra todo lo establecido en el modelo y lo añadido en el deribado.    
"""
statics = """ 
    Para usar un elementos de static has de poner en la primera linea {% load static %}
        CSS : <link href="{% static 'direccion/styles.css' %}" rel="stylesheet">
"""
models = """ 
#Es donde se definen los modelos que son las clases a traves de las cuales
    se manipula la base de datos.
En el apartado SQL modelos y migraciones estan desarrollados
"""
admins = """ 
# Su funcion es conectar los modelos con la aplicacion de administrador que ya tiene Django
    puede alterar la forma en la es estos son mostrados.
    A traves de crear clases de administracion de modelo podemos personalizar como sale, orden, filtros etc
    
    Ejemplo:
    ###
    from .models import x,y

    class yAdmin(admin.ModelAdmin):
        list_display = ("id", "y" , "x")

    admin.site.register(x)
    admin.site.register(y, yAdmin)

    ###

    Opciones de ModelAdmin:    
    - Visualización en la lista
        list_display                    # columnas que se muestran en la lista.
        list_display_links              # cuáles de esas columnas son clicables.
        list_editable                   # cuáles se pueden editar en la lista sin entrar al detalle.
        ordering                        # orden por defecto de la lista.
        list_per_page                   # número de filas por página. 
    - Filtros y búsquedas
        list_filter                     # crea filtros en la barra lateral.
        search_fields                   # activa un buscador arriba.
        date_hierarchy                  # navegación jerárquica por fechas.
    - Formularios de edición
        fields                          # ordena y limita los campos del formulario.
        exclude                         # oculta campos.
        readonly_fields                 # campos visibles pero no editables.
        fieldsets                       # organiza el formulario en secciones.
    - Relaciones
        raw_id_fields                   # muestra un cuadro de búsqueda en lugar de un desplegable enorme (útil en ForeignKey).
        autocomplete_fields             # lo mismo pero con autocompletado.
        filter_horizontal               # para campos ManyToMany, interfaz más cómoda.
        filter_vertical                 # para campos ManyToMany, interfaz más cómoda.
    - Acciones
    actions                             # define acciones personalizadas en lote.
    - Otras opciones útiles
        prepopulated_fields             # autocompletar un campo a partir de otro (ej. slug desde título).
        save_on_top                     # pone botones de guardar también arriba.
        show_full_result_count          # muestra el número total de resultados
"""

# Funciones basicas
shell = """ 
    a traves de python manage.py shell puedes abrir el terminal para escribir python directamente
    Ejemplo:
        >>> from blog.models import Post
        >>> Post.objects.create(titulo="Hola desde shell", contenido="Probando")
        <Post: Hola desde shell>

        >>> Post.objects.count()
        1

        >>> post = Post.objects.get(id=1)
        >>> post.titulo
        'Hola desde shell'


"""
usuarios = """ 
# Django crea una tabla llamada auth_user:
    Elementos mas importantes de la tabla auth_user
        - username
        - password 
        - email
        - first_name,
        - last_name
        - is_staff                  # puede entrar al admin
        - is_superuser              # permisos totales
        - is_active                 # activo o deshabilitado
        - last_login, date_joined

    La contraseña se guarda siempre por defecto con un sistema PBKDF2 + SHA256 
     con un hash unidireccional con sal. 
     Esto hace que todas las contraseñas tengan un tiempo relativo muy similar, evitando ataques por tiempo 

    El sistema de login y logout viene implementado, se puede añadir a views
        ###
        from django.contrib.auth import views as auth_views

        urlpatterns = [
            path("login/", auth_views.LoginView.as_view(), name="login"),
            path("logout/", auth_views.LogoutView.as_view(), name="logout"),
        ]
        ###

    Ejemplo de login y logout:
        ###
        from django.contrib.auth import authenticate, login, logout


        user = authenticate(request, username="pepe", password="1234")
        if user is not None:
            login(request, user)  
        else:
            print("Usuario o contraseña incorrectos")

        logout(request)
        ###
    
    Ejemplo de chequeo de autentificacion:
        ###
        def dashboard(request):
            if request.user.is_authenticated:
                return HttpResponse(f"Bienvenido {request.user.username}")
            else:
                return HttpResponse("Por favor inicia sesión")
        ###
     
"""


# Inicio de Django 
activarEntorno = """ 
    Esta en un entorno virtual aparte para evitar que afecte a otros proyectos,
    por lo que requiere activarlo:
        - source Scripts/activate     # Git Bash
        - Scripts\activate            # CMD
            Aparecera (venv) al final cuando esta activo   
"""
funcionesIniciales = """ 
    django-admin startproject PROJECT_NAME      # Comenzar proyecto
    python manage.py runserver                  # Activar el servidor
    python manage.py startapp APP_NAME          # Crear aplicacion 
"""

# DTL (django template language) ~ Jinja2
diferencias = """ 
    El lenguaje es muy similar, Jinja2 se desarrollo a partir de DTL por lo que son muy similares, 
    tienen algunas funciones, filtros y tags distintos
"""
sintaxisLoops = """ 
if
    {% if lista %}
        x
    {% else %}
        y
    {% endif %}

for
    {% for item in lista %}
        x
    {% empty %}
        no item
    {% endfor %}

"""
sintaxisEspeciales= """ 
insercion de valor
    {{ nombre }}

enlace
    <a href = "{% url 'x' %}"> ir a x </a>
    # x es el nombre de un path establecido en urls, tambien se puede introducir
    # el nombre de la app previamente establecido en urls ''
"""

# Seguridad
csrf_token = """ 
# Son codigos de seguridad para evitar peticiones falsas a usuarios ya autentificados, en django esta 
  por defecto, genera un codigo especial de forma automatica y para cualquier metodo vulnerable 
  (PORT, PUT, DELETE , PATCH) es requerido, por lo que se debe incorporar el tag especial. Si no se 
  hace, la pagina dara el error 403:
    -html            {% csrf_token %}
    -javascript      "X-CSRFToken": getCookie("csrftoken")

"""

########################             SQL            ########################

# Modelos y migraciones
modelo = """ 
    Es una clase de python que define la estructura u comportamiento de los datos. Consta de tres partes:
        - Cada modelo es una tabla de la base de datos
        - Cada atributo de la clase es una columna
        - Cada instancia es una fila

    # Creacion del modelo
        class Modelo(models.Model):
            atributoA = models.charField(max_length=64)
            atributoB = models.ForeignKey(Modelo2, on_delete=models.CASCADE, related_name="AtributoX")
            atributoC = models.charField(max_length=64)

        def __str__(self):              # Al ser una clase se le pueden definir logica dentro
        return self.atributoA             __str__ define como se muestra el objeto la consola
"""
CamposModelo = """ 
    CharField(max_length=...)        # texto corto.
    TextField()                      # texto largo.
    IntegerField()                   # enteros.
    FloatField() / DecimalField()    # decimales.
    BooleanField()                   # verdadero/falso.
    DateTimeField()                  # fecha y hora.
    EmailField(), URLField()         # validaciones específicas.
    ForeignKey()                     # relación muchos-a-uno.
    ManyToManyField()                # relación muchos-a-muchos.
    OneToOneField()                  # relación uno-a-uno.

"""
parametrosModelo = """ 
comunes o casi:
    null	        #Permite NULL en la base de datos	
    edad = models.IntegerField(null=True)
    blank	        #Permite campo vacío en formularios	
    bio = models.TextField(blank=True)
    default	        #Valor por defecto	
    activo = models.BooleanField(default=True)
    unique	        #Valor único en la tabla	
    email = models.EmailField(unique=True)
    choices	        #Lista de opciones permitidas	
    estado = models.CharField(max_length=1, choices=[("B","Borrador"),("P","Publicado")])
    db_index	    #Crea un índice en la columna	
    codigo = models.CharField(max_length=20, db_index=True)
    verbose_name	#Nombre legible en el admin	
    precio = models.DecimalField(..., verbose_name="Precio (€)")
    help_text	    #Texto de ayuda en admin/formularios	
    email = models.EmailField(help_text="Introduce tu correo")
relacion:
    on_delete           # Obligatorio en Django ≥ 2.0, que ocurre si se elimina el origen
         models.CASCADE      # elimina también el objeto hijo.
        models.PROTECT       # impide borrar si hay referencias (lanza error).
        models.SET_NULL      # pone NULL (requiere null=True).
        models.SET_DEFAULT   # pone el valor por defecto.
        models.DO_NOTHING    # no hace nada (puede romper integridad).

    related_name        # Nombre del atributo inverso para acceder desde el modelo relacionado       
    related_query_name  # Nombre alternativo para usar en consultas inversas
    to_field            # Permite enlazar la relación a una columna distinta de la PK
    through             # Define una tabla intermedia personalizada en relaciones muchos-a-muchos   
    symmetrical         # Establece en relacion ManyToMany si las relaciones implican bidireccionalidad
        = False or True
    
    """     
migracion = """ 
# Como en django no manipulas directamente las bases de datos, manipulas los modelos, 
    generas una migracion, un archivo que da las instrucciones para traducir el modelo 
    a la sintaxis de la base de datos. 
    Despues procedes con la migracion, siguiendo las instruciones, realizas los cambios en la base de datos 
"""
cicloMigracion = """ 
    - Definir modelo
    - Crear migracion
        python manage.py makemigrations
    - Aplicar migracion
        python manage.py migrate

    Las migraciones se guardan en django-migrations, se pueden ver por:
        python manage.py showmigrations
    o una concreta con: 
        python manage.py sqlmigrate app_name 0001
"""

########################          javascript         ########################

# Dom (Document Object Model)
document = """ 
#funciones importantes de document: 

    Seleccionar elementos:
        getElementById(id)              # selecciona un elemento por su id.
            let titulo = document.getElementById("titulo");
        getElementsByClassName(clase)   # colección de elementos con esa clase.
            let items = document.getElementsByClassName("item");
        getElementsByTagName(tag)       # por etiqueta (div, p, ul…).
            let divs = document.getElementsByTagName("div");
        querySelector(selector)         # primer elemento que cumple el selector CSS.
            let boton = document.querySelector(".btn-primary");
        querySelectorAll(selector)      # todos los elementos que cumplen el selector CSS.
            let links = document.querySelectorAll("a[href^='http']");

    Crear y modificar elementos:
        createElement(tag)          # crea un nodo HTML.
            let nuevoDiv = document.createElement("div");
        createTextNode(texto)       # crea un nodo de texto.
            let texto = document.createTextNode("Hola mundo");
            nuevoDiv.appendChild(texto);
        appendChild(nodo)           # añade un hijo al final.
            document.body.appendChild(nuevoDiv);
        removeChild(nodo)           # elimina un hijo.
            document.body.removeChild(nuevoDiv);

    Eventos:
        Puedes asignar eventos a elementos del DOM:
            ###
            let boton = document.getElementById("miBoton");
            boton.addEventListener("click", function() {
            alert("Botón pulsado");
            });
            ###          

    Propiedades del documento:
        document.title          # título de la página
        document.URL            # URL actual
        document.domain         # dominio
        document.cookie         # cookies 
        document.forms          # lista de formularios
        document.images         # lista de imágenes

    Acceso rápido al contenido:
        innerHTML                    # HTML interno de un elemento
            document.getElementById("contenido").innerHTML = "<b>Nuevo texto</b>";
        innerText / textContent      # solo texto, sin HTML
            document.getElementById("contenido").textContent = "Nuevo texto";
            
            
""" 
eventos = """ 
    Eventos de ratón:
        click               # clic izquierdo.
        dblclick            # doble clic.
        mousedown           # cuando se presiona el botón del ratón.
        mouseup             # cuando se suelta.
        mousemove           # cuando se mueve el ratón.
        mouseenter          # entra en un elemento (no burbujea).
        mouseleave          # sale de un elemento (no burbujea).
        mouseover           # pasa por encima (sí burbujea).
        mouseout            # se va de un elemento (sí burbujea).
        contextmenu         # clic derecho.
    
    Eventos de teclado:
      # En estos eventos tienes acceso a la propiedad .key y .code.
        keydown             # al presionar una tecla (antes de soltar).
        keyup               # al soltar la tecla.
        keypress            # (obsoleto, usar keydown).
    
    
    Eventos de formulario
        submit          # cuando se envía un formulario.
        reset           # cuando se resetea.
        focus           # un input recibe foco.
        blur            # un input pierde foco.
        change          # cambia el valor de un input, select o textarea.
        input           # cambia el valor de un input en tiempo real (cada tecla).

    Eventos de ventana/documento:
        load                     # cuando la página ha cargado.
        DOMContentLoaded         # cuando el DOM está listo (sin esperar imágenes).
        resize                   # cuando se cambia el tamaño de la ventana.
        scroll                   # cuando se hace scroll.
        beforeunload             # antes de cerrar o recargar.
        unload                   # al cerrar la página (obsoleto en algunos navegadores).
    
    Eventos de arrastrar y soltar (Drag & Drop):
        dragstart           # empieza a arrastrar un elemento.
        drag                # mientras se arrastra.
        dragend             # termina de arrastrar.
        dragenter           # entra en un área de drop.
        dragover            # se mantiene sobre un área de drop.
        dragleave           # sale de un área de drop.
        drop                # se suelta en el área.
    
    Otros eventos útiles:
        error                   # ocurre un error (en imágenes, scripts…).
        animationstart          # animaciones CSS.
        animationend            # animaciones CSS.
        animationiteration      # animaciones CSS.
        transitionend           # fin de una transición CSS.
        touchstart              # eventos táctiles (móvil).
        touchend                # eventos táctiles (móvil).
        touchmove               # eventos táctiles (móvil).
        wheel                   # movimiento de rueda del ratón.

    


"""
nodos = """ 
# El DOM es la representacion de la memoria de una pagina HTML, como un arbol de nodos. 
  En la que cada elemento es un nodo que forma parte del nodo principal, el document

    Los principares tipos de nodos son:
        - ELEMENT_NODE          # son la etiquetas como div
        - TEXT_NODE             # texto
        - ATTRIBUTE_NODE        # atributos de las etiquetas
        - DOCUMENT_NODE         # el objeto document
        - COMMENT_NODE          # comentarios <!-- ... -->

"""
