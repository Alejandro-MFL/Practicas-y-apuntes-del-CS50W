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

"""
urls = """
# Aqui se colocan las rutas propias, las de el proyecto y las de la aplicacion
Ejemplo:
    -App:
    ###
        from django.urls import path
        from . import views   # Importamos las vistas de la misma app

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


# Funciones basicas
migraciones = """ 
    Una migración en Django es un archivo de instrucciones que describe cómo debe transformarse
    la base de datos para reflejar los cambios que hiciste en tus modelos
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