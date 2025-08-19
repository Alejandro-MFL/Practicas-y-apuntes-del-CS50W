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
static = """ 
    Para usar un elementos de static has de poner en la primera linea {% load static %}
        CSS : <link href="{% static 'direccion/styles.css' %}" rel="stylesheet">
"""
models = """ 
#Es donde se definen los modelos que son las clases a traves de las cuales
    se manipula la base de datos.
En el apartado SQL modelos y migraciones estan desarrollados
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




