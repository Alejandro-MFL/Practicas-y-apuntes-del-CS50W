# Definicion de Python

Definicion = """
Python es un  lenguaje de programacion de alto nivel,
 interpretado y multiparadigmatico"""
Estructura = """ 
    imports

    def main():
    definicion de funciones

    main()
"""
 
# Tipos de variables y estructuras de datos basicas
Variables = """
    a = 28          int
    b = 1.5         float 
    c = "Hello!"    str
    d = True        bool
    e = None        NoneType
    f = 3 - 5j      complex # Es un numero que tiene una parte real (3) y la parte imaginaria (-5)
"""
secuencias = """
# Coleccion de elementos secuenciados que son iterables 
    list:       # Ordenadas, mutables, permiten elementos duplicados y de cualquier tipo
        a = [1, 2 ,3]
        a[0] = 1
    
    tuple:      # Ordenadas, inmutables, permiten duplicados
        a = (1, 2)
    
    range:      # Secuencia inmutable de enteros
        a = range(5) # 0, 1, 2, 3, 4
    
    bytes       # Secuencia inmutable de valores entre 0 y 255.
        b = b"hola"

    bytearray   # Secuencia inmutable de valores entre 0 y 255.
        ba = bytearray(b"hola")        
"""
conjuntos = """
# Coleccion de elementos no secuenciados sin duplicaciones
    set:        # Mutable
        a = {2, 5, 3, 1}
    
    frozenset:  # No mutable
        a = {[2, 5, 3, 1]}
"""
mapas = """ 
# Coleciones de pares clave-valor
    dict:       # Mutables, clave única (no duplicada), valor de cualquier tipo
        a = {"nombre": "a", "numero": 0} 
"""


# Operaciones basicas
operaciones = """ 
    +, +=       # Suma
    -, -=       # Resta
    *, *=       # Multiplica
    /, /=       # Division
    //, //=     # Division a entero
    %, %=       # Modulo
    **, **=     # Potencias
"""
operacionesLogicas = """ 
    and
    or
    not
"""
operacionesEspeciales = """ 
    a = f"Hello, {name}"    # Se usa para agregar elementos a un string, es mas seguro que concatenar, hacer con tuplas 
                                #si son con elementos agregados por seguridad
"""


# Estructuras basicas
ifs = """ 
    if n < 0:
        print(a)
    elif n = 0:
        print(b)
    else:
        print(c)
"""
fors = """ 
    for i in x:    # x puede ser una lista, un rango, el elemento que mejor te convenga
        print(i)
     
"""
trys = """ 
    try:
        a = b
    except x:           # x es sustituible por el error que necesites 
        print("nop")      (ValueError, ZeroDivisionError, etc)
"""
whiles = """ 
    i = 0
    while i < 5:
        x
        i +=1
"""
functions = """ 
    def x(parametro):   # No hace falta atributo ni definir previamente el return
        return
"""


# Importar funciones o bibliocas
imports = """ 
    import sys
        y = sys.argv
    from apuntes_git import x
"""


# Clases y tecnicas especiales
classs = """ 
# Creas objetos con parametros y funciones preestablecidas
    class x():
        def __init__(self, x):      # Esta funcion se acciona cada vez que se crea una clase
            self.x = x              # self representa el nuevo de la clase x
"""
decorators = """ 
# Son funciones que tomando una funcion, la modifica y la devuelve
    def decorator1(x):
        def y():
            x()
            print(x ahora es y)
        return y

    @decorator1                 # De esta forma se agrega el decorador para que se llame                 
    def hello():                  automaticamente cuando se llame la funcion hello
        print(h)
"""
lambdas = """ 
# Es un tipo de funcion compacta de un solo uso
    lambda x: x.y               # Esto define una funcion con parametro x y un return de y
    ==
    def f(x):                   # Es el equivalente de un uso de f,  
        return x.y                se usa para dar una key o similares
"""
