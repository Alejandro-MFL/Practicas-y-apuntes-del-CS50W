#Estos apuntes no pertenecen al CS50

# Basico 
Basico=""" 
    Color: -No usar rgba, rgb()

    Texto:  - Si usas fonts que tiene el usuario no las cargas
            - Puedes usar y no solo en texto elementos supletorios 
            ###
                font-family: system-ui, Ubuntu, sans-serif  #Se usan de izquierda a derecha
            ###
                
    Categorias: bloques(cajas) y lineal(letras)

    Bordes:  - Es un elemento de "objeto, aumentarlo aumenta el tamaño
                outline: se puede usar para no tocar el borde
                box-sizing: content-box de base o con border-box
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