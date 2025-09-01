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
tests = """ 
# Es un archivo con TestCase importado, se usa para probar una aplicacion, funciona similar a unittest
  desarrollado mas en # Test djangoTest
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
limiteDeVelocidad = """ 
    Limita la cantidad de solicitudes que un usuario puede realizar en un periodo de tiempo determinado.
    Esto ayuda a proteger contra ataques de denegación de servicio (DOS) , 
    en los que un usuario malintencionado realiza tantas llamadas a la API que esta se bloquea.
"""

# Test
asserts = """ 
# asserts es un metodo de afirmacion, de tal forma que si no fuera asi da un mensaje
  de error, un AssertionError
        ###
            def square(x):
                return x + x

            assert square(10) == 100        
        ###
            daria el siguiente mensaje Output:
                Traceback (most recent call last):
                File "assert.py", line 4, in <module>
                    assert square(10) == 100
                AssertionError
    
    En django, se expande los metodos de assert
        - Logicas
            assertTrue(x) 
            assertFalse(x)
        - Igualdad
            assertIs(x, y) 
            assertIsNot(x, y)
            assertIsNone(x) 
            assertIsNotNone(x) 
        - Comparacion
            assertGreater(x, z) 
            assertGreaterEqual(x, z) 
            assertLess(x, z) 
            assertLessEqual(x, z) 
        - Pertenencia y tipo
            assertIn(x, y) 
            assertNotIn(x, y) 
            assertIsInstance(obj, cls) 
            assertNotIsInstance(obj, cls) 
        - Excepciones
            assertRaises(exc, func, *args, **kwargs) 
             # pasa si func lanza excepción exc                     
            assertRaisesRegex(exc, regex, func, ...) 
             # igual pero comprobando el mensaje de error
        - Advertencias
            assertWarns(warning, func, ...)
            assertWarnsRegex(warning, regex, func, ...)
        - Regex     # Son cadenas de texto especiales que describe un patrón de búsqueda
            assertRegex(text, regex) → pasa si text hace match con regex
            assertNotRegex(text, regex) → pasa si no hace match      
        - Coleccion
            assertCountEqual(x, z) 
             # pasa si x y z tienen los mismos elementos (sin importar orden)
"""
testMultiples = """ 
# Hay distintas formas, bastante similares

    - Archivos x.sh:
    # Son archivos acabados en .sh, en los que puedes hacer pruebas en termi
      es mejor que hacerlo a mano pero no muy rapido
        ###
            python3 -c "from tests0 import test_prime; test_prime(1, False)"
            python3 -c "from tests0 import test_prime; test_prime(2, True)"
            python3 -c "from tests0 import test_prime; test_prime(8, False)"
            python3 -c "from tests0 import test_prime; test_prime(11, True)"
            python3 -c "from tests0 import test_prime; test_prime(25, False)"
        ###
        requiere un archivo de pruebas, en este caso tests0, en el que agreges una prueba a fallo

    - Archivo.py con unittest:
    # Es una importacion de una biblioteca de py, chequeas funciones directamente
      tiene la ventaja de añadir un codestring que explica la prueba y usa menos archivos q un x.sh
        ###
            # importar unittest y las funciones a testear
            import unittest
            from prime import is_prime

            # una clase con las funciones a testear
            class Tests(unittest.TestCase):

                def test_1(self):
                    ***Check that 1 is not prime.***
                    self.assertFalse(is_prime(1))

                def test_2(self):
                    ***Check that 2 is prime.***
                    self.assertTrue(is_prime(2))

                def test_8(self):
                    ***Check that 8 is not prime.***
                    self.assertFalse(is_prime(8))

                def test_11(self):
                    ***Check that 11 is prime.***
                    self.assertTrue(is_prime(11))

            # ejecutar cada prueba
            if __name__ == "__main__":
                unittest.main()
                    ###
"""
djangoTest = """ 
# Es un sistema muy similar a unittest, funciona con un db de prueba que tienes que crear previamente
puedes trabajar con una copia importada o con la real, pero esto no es aconsejable.

    - Respecto a la db, se crea y migra un db temporal que se limpiara y vaciara con cada prueba
      para asegurar repetibilidad y q no se ensucia la db
    - Ejemplo de formato, es muy similar a unittest:    
    ###
        class FlightTestCase(TestCase):

            def setUp(self):

                # creas los distintos elementos de la db que usaras en las pruebas

                a1 = Airport.objects.create(code="AAA", city="City A")
                a2 = Airport.objects.create(code="BBB", city="City B")

                Flight.objects.create(origin=a1, destination=a2, duration=100)
                Flight.objects.create(origin=a1, destination=a1, duration=200)
                Flight.objects.create(origin=a1, destination=a2, duration=-100)

                # Despues las funciones de prueba

                def test_departures_count(self):
                    a = Airport.objects.get(code="AAA")
                    self.assertEqual(a.departures.count(), 3)
                
                def test_valid_flight(self):
                    a1 = Airport.objects.get(code="AAA")
                    a2 = Airport.objects.get(code="BBB")
                    f = Flight.objects.get(origin=a1, destination=a2, duration=100)
                    self.assertTrue(f.is_valid_flight())

                def test_invalid_flight_duration(self):
                    a1 = Airport.objects.get(code="AAA")
                    a2 = Airport.objects.get(code="BBB")
                    f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
                    self.assertFalse(f.is_valid_flight())

                def test_index(self):                   #1

                    # Se crea un cliente
                    c = Client()                    
                    response = c.get("/flights/")
                    # Se revisa el codigo devuelto
                    self.assertEqual(response.status_code, 200)

                    # Se hace una prueba de un elemento
                    self.assertEqual(response.context["flights"].count(), 3)
                
                def test_invalid_flight_page(self):     #2 
                    max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

                    c = Client()
                    response = c.get(f"/flights/{max_id + 1}")
                    self.assertEqual(response.status_code, 404)
    ###
    #1 La penultima prueba es un ejemplo de pruebas de cliente, django simula el acceso de
     un cliente a la pagina, crea el cliente, revisa el codigo y aplica la prueba x
    #2 En la ultima, utiliza el comando Max, para usarlo requiere que se agrege el import: 
     from django.db.models import Max. Con max_id se agrega el total de ids
"""
selenio = """ 
# Aunque django ya pueda implementar pruebas de cliente, el framework de selenio nos facilita esto de forma visual
    Requiere una configuracion basica:
     ###
        import os
        import pathlib
        import unittest

        from selenium import webdriver

        def file_uri(filename):
            return pathlib.Path(os.path.abspath(filename)).as_uri()

        driver = webdriver.Chrome()
     ###
  
    Despues puedes establecer las pruebas correspondientes que tu uses, siguiendo el metodo de
     unittest
    ###
        class WebpageTests(unittest.TestCase):

            def test_title(self):
                ***Make sure title is correct***
                driver.get(file_uri("counter.html"))
                self.assertEqual(driver.title, "Counter")

            def test_increase(self):
                ***Make sure header updated to 1 after 1 click of increase button***
                driver.get(file_uri("counter.html"))
                increase = driver.find_element_by_id("increase")
                increase.click()
                self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

            def test_decrease(self):
                ***Make sure header updated to -1 after 1 click of decrease button***
                driver.get(file_uri("counter.html"))
                decrease = driver.find_element_by_id("decrease")
                decrease.click()
                self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

            def test_multiple_increase(self):
                ***Make sure header updated to 3 after 3 clicks of increase button***
                driver.get(file_uri("counter.html"))
                increase = driver.find_element_by_id("increase")
                for i in range(3):
                    increase.click()
                self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")

        if __name__ == "__main__":
            unittest.main()
    ###


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

    Funciones en cicloMigracion
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
# Escalabilidad
servidores = """
    Localizacion nube/fisico:
        - En la nuve es mas sencillo, con una inversion inicial menor y 
         con mayor adaptabilidad
        - En cambio en fisico-propios el costo es menor a largo plazo y tienes mas 
         personalizacion y flexibilidad

    Escalabilidad:
        - Vertical, es el aumento de las capacidades del servidor,
          sustituirlo por uno mas grande
        - Horizontal, agregar mas servidores es mas eficiente y evitas que un fallo en un servidor 
         bloque la web
    
    Equilibrio de la carga:
        # Al tener multiples servidores, el reparto de la carga respecto a los distintos servidores es importante
        hay tres tipos de distribucion:
            - Aleatorio
            - Round-Robin, va alternando cada servidor
            - Por menos carga
        Todas las opciones tienen pros y contras entre rendimiento y velocidad de respuesta
    
    Almacenamiento de sesiones
        # Las sesiones de los usuarios y donde se registran es un asunto relevante:
            - Si las sesiones son persistentes en el servidor que se alojo, 
             ese usuario siempre tendra que ser enviado a ese servidor, dependiendo completamente de este
            - Si las seiones de datos se almacenan en una base de datos a la que todos los servidores tengan
             acceso, el contra es que leer y escribir en base de datos requerira mas procesamiento
            - Si las sesiones estan en el cliente, por cookies, es lo mejor salvo por el pequeño detalle de
             que respecto a la seguridad es bastante fragil

"""
BaseDeDatos = """ 
    Particionado de tabla       
        - Vertical: se fragmenta la tabla por columnas
        - Horizontal: Se fragmenta en varias tablas con las mismas columnas, 
         normalmente en fucion de una columna, en libros seria subdibidar una biblioteca por cada genero

    Replicacion de bases de datos:      # Finalidad de que un fallo no elimine toda la base de datos
        - Replicación Primaria Única, una es la operativa, el resto son copias de seguridad que se actualizan 
         en funcion de la primera
        - Replicacion multiprimaria, todas son operables, todas se actualizan entre todas. 
        Que solo una sea operativa nos sigue exponiendo a que cuando falle colapse, 
         que todas sean operables añade mucha complejidad al haber procesos y actualizaciones simultaneas
         
# Toda la base de datos no puede estar almacenada en un unico servidor por punto unico de fallo
"""
cache = """ 
# La memoria cache es una memoria temporal, que puede estar desde el cliente o desde el servidor,
 se usa para sin tener un gran coste, no tener que cargar elementos que recientemente se han cargado
    Django proporciona su propio framework de caché
        - Almacenamiento en caché por vista
        - Almacenamiento en caché de fragmentos de plantilla
        - API de caché de bajo nivel

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
ejemplos ="""
# Ejemplos de funciones que por relevancia o por cuestianes didacticas son interesantes

    document.addEventListener("DOMContentLoaded", () => {                                #1
        document.querySelectorAll("button").forEach(button => {                          #2
            button.onclick = () => {                                                     #3
                document.querySelector("#hello").style.color = button.dataset.color;
            }
        });
    });

    #1 Esta es una importante funcion que obliga a esperar que se haya cargado por completo el DOM
    para ejecutar el codigo, es util para evitar errores
    #2 Un simple ejemplo de la conbinacion de sellecionar todos los elementos(querySelectorAll), 
       recorrerlos (forEach) y les asigna una funcion
    #3 cada botton tiene una funcion onclick, pero es mas optimo usar button.addEventListener("click",)
"""

# Basicos
arrowFunction = """ 
# Es un tipo de funcion sin nombre muy usada en js, es una abreviacion:
    - sin variables
        const x = () => console.log("Hola x");
    - con una variable
        const x = n => n * n;
    - con varias variables:
        const x = (m, n) => m + b;
"""
tiempoJS = """ 
# Hay dos funciones principalmente pare el manejo de tiempo, ambas se rigen por milisegundos:
    - setTimeout(), ejecuta una funcion una vez despues de un tiempo x:
        setTimeout(() => {
        console.log("paso un segundo")}, 1000);
    - setIntervals(), ejecuta una funcion cada x tiempo:
        setInterval(() => {
            console.log("Esto se muestra cada segundo");
        }, 1000);  # cada 1 segundo
    
    # Ambas se pueden parar con clearInterval() y clearTimeout () aunq para ello deberas ligarlas a una variable

"""

# Django
AlmacenamientoLocal = """ 
    - localStorage es un almacen clave-valor en el navegador, persistente y ligado al dominio 
        Condiciones:
            -liga el almacenimiento al dominio, sin configurarlo especialmente ni subdominios
            - Capacidad variable dependiendo del navegador (5 a 10 mb)
            - Acceso sincrono
            - Solo strings por lo que requiere serializar
            - Inseguro
            - No expira automaticamente
            - no envia al servidor
            - API JS sencilla

        Metodos principales:
            localStorage.setItem("usuario", "Ana");         # Guardar un valor
            let user = localStorage.getItem("usuario");     # Recuperar un valor
            localStorage.removeItem("usuario");             # Eliminar un valor
            localStorage.clear();                           # Vaciar todo       
            let total = localStorage.length;                # Número de elementos guardados        
            let clave = localStorage.key(0);                # Acceso por índice (poco usado)
    
    - sessionStorage es un almacen muy similar a local, pero esta ligado a la pestaña y los datos son eliminados cuando esta se cierra
"""
APIs = """ 

    -AJAX nos permite acceder a informacion de paginas externas, a trabes de la funcion fetch(), puedes
    solicitar informacion y recibir una promise, es una respuesta no instantane. Se usa cuando la promesa se cumple o se deniega
    ###
        document.addEventListener('DOMContentLoaded', function() {
            fetch('https:#api.exchangeratesapi.io/latest?base=USD')
            .then(response => response.json())    # Espera a la respuesta y hace una promesa de dato convertido en json
            .then(data => {                       # Cuando el dato llega lo gestiona 
                console.log(data);
            });
            .catch(error => {                     #
                console.log('Error:', error);
        });
    ###
    La parte interesante es que fetch en realidad no es el AJAx perse, es una peticion de HTTP desde el navegador,
    la respuesta son siempre promesas de llegar un dato en algun momento, algunas veces un no, al ser datos asincronos,
    no pueden guardarse normal sin un trato especial
    La respuesta se puede convertir en:
        response.text()             # devuelve una promesa con el cuerpo como string.
        response.json()             # devuelve una promesa que parsea el cuerpo como JSON.
        response.blob()             # devuelve un Blob (para archivos).
        response.formData()         # devuelve un FormData.
        response.arrayBuffer()      # devuelve datos binarios.
       
    
"""

########################             IU             ########################    

# divs
paginas = """ 
    Un ejemplo de cambio de elementos de una pagina
    ###
        
        window.onpopstate = function(event) {                                           #1
            console.log(event.state.section);
            showSection(event.state.section);
        }

        function showSection(section) {                                                 #2
            fetch(`/sections/${section}`)
            .then(response => response.text())
            .then(text => {
                console.log(text);
                document.querySelector('#content').innerHTML = text;
            });

        }

        document.addEventListener('DOMContentLoaded', function() {                      #3
            document.querySelectorAll('button').forEach(button => {
                button.onclick = function() {
                    const section = this.dataset.section;

                    history.pushState({section: section}, "", `section${section}`);     #4
                    showSection(section);
                };
            }); 
        });
    ###

    #1. window.onpopstate Establece que hara el navegador cuando den atras
    #2. hace una api al servidor para saber que section acceder
    #3. da a cada boton la funcion de establecer la seccion y llamar la funcion #2
    #4. history.pushState modifica el historial de navegacion

"""
ventana = """ 
    window.innerWidth               # Ancho de la ventana en píxeles
    window.innerHeight              # Altura de la ventana en píxeles
    window.scrollY:                 # cuantos píxeles hemos recorrido desde la parte superior
    document.body.offsetHeight:     # La altura en píxeles de todo el documento
"""
animaciones = """ 
    - Establecemos las fases de la animacion
        1º Opcion:
        ###
            @keyframes animation_name {
                from {
                    /* Some styling for the start */
                }

                to {
                    /* Some styling for the end */
                }
            }
        ###
        2º Opcion:
        ###
            @keyframes animation_name {
                0% {
                    /* Some styling for the start */
                }

                75% {
                    /* Some styling after 3/4 of animation */
                }

                100% {
                    /* Some styling for the end */
                }
            }
        ###
    
    - en <style> aplicas a un elemento
        animation-name: x;
        animation-duration: 1s;
        animation-fill-mode: y;         # 1
        position: relative;             # Si quieres modificar su posicion

        #1. y puede tomar los siguientes valores :
            none        # Solo se ven los cambios mientras dura la animación
            forwards    # El elemento se queda con el estilo del último keyframe al terminar
            backwards   # El elemento adopta el estilo del primer keyframe hasta que empiece la animacion
            both        # Combina forwards + backwards



"""  

# REACT
crudo = """ 
# Añades las bibliotecas de REACT, util pedagogicamente, para proyectos se instala
    Ejemplo de inicio de REACT:
        ###
            <!DOCTYPE html>
            <html lang="en">
                <head>                                                              #1
                    <script src="https:#unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
                    <script src="https:#unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
                    <script src="https:#unpkg.com/babel-standalone@6/babel.min.js"></script>
                    <title>Hello</title>
                </head>
                <body>
                    <div id="app"></div>                                            #2

                    <script type="text/babel">                                      #3
                        function App() {                                            #4
                            return (
                                <div>
                                    Hello!
                                </div>
                            );
                        }

                        ReactDOM.render(<App />, document.querySelector("#app"));   #5
                    </script>
                </body>
            </html>
        ###

        #1. Son la conexion con React, 
            - React: Define los componentes y su comportamiento.
            - ReactDOM:Toma componentes de React y los inserta en el DOM
            - Babel: Traduce de JSX , el lenguaje en el que escribiremos en React,
            
        #2. El div vacio en el que rellenaremos desde codigo
        #3. Añadimos la etiqueta de que ha de traducirse con babel
        #4. Creamos el componente app, que en react pueden ser funciones
        #5. Renderiza la funcion con dos argumentos:
            - El componente a renderizar 
            - El elemento del DOM donde se representa el componente    
"""
instalacionR = """ 

Esquema de carpetas:
    Base:
        frontend/
        │
        ├── .env                
        ├── index.html
        ├── package.json
        ├── vite.config.js
        ├── node_modules/         # dependencias instaladas (no se toca)
        ├── public/               # archivos estáticos públicos 
        └── src/                  # aquí vive tu código React
            ├── App.jsx           # componente principal de la aplicación
            ├── App.css           # componentes concretos de css de App.jpx
            ├── main.jsx          # punto de entrada: monta React en index.html, no tocar por ahora
            ├── index.css         # componentes generales de css de toda la pagina
            └── assets/           # imágenes, estilos, etc.

        -.env variable de entorno expuesta en el cliente
        - index.html Es el HTML principal, esta vacio, salvo por un <div id="root"></div>, que es donde 
        se inyectara el codigo
        - package.json Lista las dependencias (React, Vite, etc.) y scripts (npm run dev, npm run build, npm run preview).
        - vite.config.js Configuración del bundler Vite (rutas, plugins, etc). Normalmente no lo tocas mucho al inicio.
        - node_modules/ Carpeta donde npm instala las librerias, no tocar
        - public/ Contenedor de los archivos estaticos
        - src/ Carpeta que contiene la aplicacion de REACT
        - main.jsx primer archivo que se ejecuta; monta <App /> dentro del div id="root" del index.html.
        - assets/ es un contenedor como public, pero para los elementos que pasan por Vite 
        (las empaqueta, optimiza y les pone hash para cache busting)

    estructurado de src:
      src/
        main.jsx
        App.jsx                 # En el convergen todos los elementos
        styles/                 # Donde estan los elementos esteticos, incluido index.css
        components/             # piezas reutilizables (Button, Modal, Card...)
        pages/                  # pantallas enrutables
            Login/
            Login.jsx
            Login.module.css
            Dashboard/
            Dashboard.jsx
            Weekend/
            Weekend.jsx
            PlanCard.jsx
        features/               # lógica + UI de dominios concretos
            auth/
            api.js              # login, refresh, me
            useAuth.js          # hook de sesión
            weekends/
            api.js              # GET/POST weekends
            hooks.js            # hooks específicos (useWeekend)
            plans/
            api.js              # CRUD de planes
        lib/
            http.js               # fetch con baseURL y token
        assets/
        index.css  

"""

sistaxisR = """ 
    Encender servidor:
        npm run dev

    argumentos:
        function Hello(props) {
            return (
                <h1>Hello, {props.name}!</h1>
            );
        }


        <Hello name="Ron" />

    
"""
