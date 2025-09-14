#Estos apuntes no pertenecen al CS50

# Basico 
Bordes=""" 
    De serie afecta al tamaño del objeto, como el padding, para poder evitarlo puedes cambiar "box-sizing"
        box-sizing: content-box     # Aumenta el tamaño basico
        box-sizing: border-box      # Fuerza a que el tamaño total englobe el borde

    outline: Otra opcion es usar "outline" es un borde dentro del objeto, antes del borde y no afecta al tamaño del objeto                 
"""
Desbordamiento= """ 
#Cuando el contenido es mas grande que el continente se desborda
    Soluciones:
        -overflow: x; x = ...
            visible         # Desborda
            hidden          # Corta el contenido sobrante
            scroll          # Corta el contenido pero siempre agrega barras para desplazarte por el contenido, aunque no desborde
            auto            # Dependiendo del navegador y si hay desbordamiento usa un metodo para navegar por el contenido(normalmente barras)
       
        -text-overflow: x; x = ...
            ellipsis        # Corta el texto y añade puntos suspensivos
            clip            # El predeterminado
"""
Posicionamiento=""" 
# El posicionamiento de serie es estatico
    position: x; x = ...
        absolute        # Fuerza su espacio de forma absoluta respecto al primer elemento de referencia
        relative        # Crea un elemento de referencia para los hijos
        fixed           # Da una posicion fija respecto a la pantalla
        sticky          # hace que se desplace por el contenedor
"""
Profundidad=""" 
# Se usa un sistema de capas para dar profundidad, estas se puedes tocar a traves de:
    z-indez: y;     y = cualquier numero
"""
BloquesTipo=""" 
    Categorias: bloques(cajas) y lineal(letras). Se pueden alterar por
        -display: x; x= ...
            inline      
            block
            flex    # Esto afecta a como almacena a sus descendientes, forma flexible
            grid    # Esto afecta a como almacena a sus descendientes, forma cuadricula
    
"""
Texto= """ 
    - Si usas fonts que tiene el usuario no las cargas
    - Puedes usar elementos supletorios 
    ###
        font-family: system-ui, Ubuntu, sans-serif  #Se usan de izquierda a derecha
    ###
"""
Seudoclases= """ 
# Sirven para seleccionar elementos en un estado concreto (:y)
  y = ...
    :hover                          # cuando el puntero está sobre un elemento
    :active                         # cuando se hace clic y se mantiene pulsado
    :focus                          # cuando un input o botón está seleccionado/activo
    :visited                        # enlaces que ya se visitaron
    :first-child / :last-child      # primer o último hijo dentro de un contenedor
    :nth-child(n)                   # selecciona un hijo en la posición n
    :not(selector)                  # selecciona todos los elementos excepto los que coinciden
    :checked                        # inputs tipo checkbox o radio marcados
    :disabled / :enabled            # elementos de formulario deshabilitados/habilitados
    :required / :optional           # inputs obligatorios u opcionales
"""
SeudoElementos=""" 
# Permiten acceder a partes específicas de un elemento (::y)
  y = ...
    ::before             # inserta contenido antes de un elemento
    ::after              # inserta contenido después
    ::first-line         # primera línea de un texto
    ::first-letter       # primera letra de un bloque de texto
    ::selection          # la parte seleccionada con el ratón
    ::placeholder        # el texto placeholder de inputs
"""
SectoresCombinados = """ 
    a, b    eleccion multiple
    a b     seleccion descendente (selecciona descendientes tipo b que esten en un tipo a)
    a > b   seleccion de hijo (selecciona solo los hijos directos tipo b en a)
    a + b   seleccion de hermanos adyacentes (selecciona el elemento tipo b que este justo despues del tipo a)
    [a=b]   seleccion de atributos (selecciona elementos que tengan el mismo valor b en el atributo a. Ejemplo: input[type="text"])
    a:b     seleccion de pseudoclase (selecciona elementos a en el estado especial b. Ejemplo: a:focus o a:hover)
    a::b    seleccion de pseudoelemento (selecciona un subelemento b en el elemento a. Ejemplo a::first-letter )
"""
Prioridad = """ 
  Orden de prioridad al aplizar estilo:
        1. inline
        2. id
        3. class
        4. type  

"""
ResponsiveDesign=""" 
#Hace referencia a la escabilidad para diferentes formatos.
    Se puede añadir que el ancho cambie automaticamente con el ancho de la pagina
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    Se pueden añadir media queries, se añade un @
        @media (max-width: a) {...}
        @media (min-width: b) {...}


"""

# Fexbox
DireccionFlex=""" 
    Se puede organizar por linea o columna y siempre de forma unidireccional
    - flex-direction: x; x = ...
        row         # Fila
        column      # Columna 
        x-reverse   # Para row y column empieza de final a principio
    
    - El contenido se puede alterar con reverse o con:
        writing-mode: vertical-lr esto gira los objetos 90 grados
        direction: rtl esto coloca de derecha a izquierda
        # Esto es relevante para paginas nacionales, donde el orden de lectura puede variar
    # Esto tambien se puede cambiar el orden desde los hijos con "orden: 1"

        

    # flex direction como flex wrap puede tocarse a la vez desde "flex-flow"
"""
ContenidoFlex=""" 
    - Desbordamiento
        Como maneja el contenido y lo organiza de distintos modos 
            flex-wrap: x; x = ...
                nowrap      # Es el por defecto, fuerza el tamaño de los hijos para que entre
                wrap        # Altera el tamaño del continente para que entre el contenido

        # flex direction como flex wrap puede tocarse a la vez desde "flex-flow"

    - Modificacion especifica de los elementos desde 3 opciones desde el los hijos 
        - flex-grow: x; x = ...
            0           # Puede aumentar su tamaña base(flex-basis) es el valor por defecto
        - flex-shrink: x; x = ...
            1           # Puede reducir su tamaña base(flex-basis) es el valor por defecto
        - flex-basis: x; x = ...
            auto        # Tiene un tamaño base automatico

    - Pueds modificar los anteriores 3 por:   
        - flex: auto    # para que se ajuste automaticamente si tocar los otros tres
        - flex: 1       # enciende grow y shrink y da a una proporcion respecto al padre
        - flex: 2       # enciende grow y shrink y da el doble de espacio que los que tienen 1 y asi sucesivamente

"""
Aliniar=""" 

 """


# Herramientas 
Bootstrap= """ 
    Bootstrap.com: es una biblioteca de estilos CSS
"""
Sass="""
# Haciendo archivos .scss, nos brinda nuevas opciones como añadir variables, anidar elementos, heredar caracteristicas.
        requiere que se compile antes ya que los navegadores no lo aceptan, con:
        sass x.scss:x.css
        Lo puede hacer automaticamente con:
        sass --watch x.scss:x.css    
"""
Codilink= """ 
# Es una pagina para hacer pruebas con ejemplo visual    
    https://codi.link/
"""
Info=""" 
    https://web.dev/learn/css?hl=es Contiene mucha informacion y ejemplos Mas fiable
    https://lenguajecss.com/ Contiene mucha informacion y ejemplos
    https://developer.mozilla.org/es/docs/Web/CSS Ultimas novedades

"""