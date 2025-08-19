# Base
valores = """ 
# Guardados:
    NULL = Ausencia de valor
    INTEGER = numeros enteros de entre 1 a 8 bytes
    REAL = numeros decimales 8 bytes
    TEXT = texto almacenado como UTF-8 o 16
    BOLB = datos en binario sin interpretar
"""
inicio = """ 
    # Para importar elementos de un csv, es necesario primero ".mode csv", si se hace manualmente creando las tablas, 
      la primera linea sera usada como elemento de la tabla

    .mode csv
    .import clientes.csv clientes
    
"""

# Manipulacion de tablas
crear = """ 
     Crear tablas
    CREATE TABLE clientes (
        id INTEGER,
        nombre TEXT,
        tiempo NUMERIC,
        correo TEXT,
        PRIMARY KEY (ID)
    ); 
    #Se pueden vincular tablas con PRYMARY y FOREIGN(PRIMARY KEY se puede usar sirectamente)
"""
ver = """ 
# Para ver todas las tablas de una base
    .tables

# Para ver la informacion de una tabla 
    PRAGMA table_info(clientes);
    # Describe una tabla con los siguientes elementos
        Columna	    Significado
        cid	        Índice de la columna (0, 1, 2...)
        name	        Nombre de la columna
        type	        Tipo de dato (TEXT, INTEGER, etc.)
        notnull	    ¿Puede ser nulo? (1 = NO, 0 = sí)
        dflt_value	    Valor por defecto (si tiene alguno)
        pk	            ¿Es clave primaria? (1 = sí, 0 = no)

        
# Para ver la estructura de una tabla
    .schema nombreTabla

# Para acceder a la informacion de una tabla
    SELECT * FROM clientes WHERE ciudad = 'Madrid' AND id < 70;

    SELECT * FROM clientes WHERE (ciudad = 'Madrid' or ciudad = 'Barcelona') AND correo LIKE '%gmail.com';
    
    SELECT ciudad, COUNT(*) AS n FROM clientes GROUP BY ciudad ORDER BY n DESC LIMIT 4;
        #DESC descendiente ASC ascendente


    # Se pueden vincular tablas con PRYMARY y FOREIGN(PRIMARY KEY se puede usar ade una)
        Con JOIN pueden unirse para que salgan juntas:
            #SELECT * FROM clientes JOIN consumidores ON clientes.id = consumidores.show_id;
        los muestra una al lado de la otra
        
        JOIN / INNER JOIN
            Devuelve solo las filas donde existe coincidencia en ambas tablas
        LEFT OUTER JOIN
            Devuelve todas las filas de la tabla izquierda , y las coincidencias con la derecha 
        RIGHT OUTER JOIN
            Devuelve todas las filas de la tabla derecha , y las coincidencias con la izquierda 
        FULL OUTER JOIN
            Devuelve todas las filas de ambas tablas
"""
eliminar = """ 
#Para eliminar una tabla:
    DROP TABLE IF EXISTS clientes;

#Ejemplo de eleminar datos
    DELETE FROM clientes WHERE ciudad IS NOT NULL;
"""
añadir = """ 
#insercion de datos:
    INSERT INTO clientes(nombre, correo) VALUES
    ('Ana García', 'ana@example.com'),
    ('Luis Pérez', 'luis@example.com');    
    #Las columnas no rellenas tendran el valor de NULL

# Modificacion de datos con UPDATE:
    UPDATE clientes SET correo = 'nuevo@email.com' WHERE nombre = 'Ana García';

"""
indexar = """ 
# Sirve para mejorar la eficiencia de procesamiento a costa del espacio, 
  crea una lista de pointers con estructura apta para busqueda binaria.
  Esto es muy efectivo pero aumenta enormemente el espacio ocupado

    CREATE INDEX title_index ON clientes (correo);
        CREATE UNIQUE INDEX para que no se dubliquen 

# Implicaciones: crea un indice dentro del archivo con forma de binaria para busquedas mas rapidas,
    - Contras: un mayor gasto de espacio en el archivo(relativamente alto), con un mayor costo al modificar las listas 
        INSERT, UPDATE o DELETE
    - Pros: Al permitir busquedas binarias todas las queries son exponencialmente mas eficientes respecto al tamaño
                #WHERE, JOIN, ORDER BY, o GROUP BY

"""

# Funciones
agregacion = """ 
    COUNT(x)	                # Cuenta filas (o no nulas si se pasa columna)	
        SELECT COUNT(*) FROM clientes;
    SUM(x)	                    # Suma valores	
        SELECT SUM(edad) FROM clientes;
    AVG(x)	                    # Promedio	
        SELECT AVG(edad) FROM clientes;
    MIN(x)	                    # Valor mínimo	
        SELECT MIN(edad) FROM clientes;
    MAX(x)	                    # Valor máximo	
        SELECT MAX(edad) FROM clientes;
    TOTAL(x)	                # Como SUM, pero siempre REAL	
        SELECT TOTAL(sueldo) FROM empleados;
    GROUP_CONCAT(x, ',')	    # Une valores en un string	
        SELECT GROUP_CONCAT(nombre, ', ') FROM clientes;
"""
texto = """ 
    UPPER(x)	                # Convierte a mayúsculas	
        SELECT UPPER(nombre) FROM clientes;
    LOWER(x)	                # Convierte a minúsculas	
        SELECT LOWER(nombre) FROM clientes;
    LENGTH(x)	                # Longitud de la cadena	
        SELECT LENGTH(nombre) FROM clientes;
    TRIM(x)	                    # Quita espacios ambos lados	
        SELECT TRIM(' hola '); → 'hola'
    LTRIM(x)	                # Quita espacios a la izquierda	
        SELECT LTRIM(' hola');
    RTRIM(x)	                # Quita espacios a la derecha	
        SELECT RTRIM('hola ');
    SUBSTR(x,inicio,long)	    # Subcadena	
        SELECT SUBSTR(nombre,1,3) FROM clientes;
    REPLACE(x,ant,nuevo)	    # Reemplaza texto	
        SELECT REPLACE(nombre,'a','@');
    INSTR(x,y)	                # Posición de y en x	
        SELECT INSTR('barcelona','cel'); → 4
"""
matematicas = """ 
    ABS(x)	                    # Valor absoluto	
        SELECT ABS(-42); → 42
    ROUND(x,d)	                # Redondea a d decimales	
        SELECT ROUND(3.14159,2); → 3.14
    SIGN(x)	                    # Signo: -1, 0, 1	
        SELECT SIGN(-5); → -1
    RANDOM()	                # Aleatorio entero	
        SELECT RANDOM();
    RANDOM()%n	                # Aleatorio 0-n	
        SELECT RANDOM()%100;
"""
fechaYHora = """ 
    date(timestring,mod)	    # Devuelve fecha	
        SELECT date('now'); → 2025-08-19
    time(timestring,mod)	    # Devuelve hora	
        SELECT time('now');
    datetime(timestring,mod)	# Fecha + hora	
        SELECT datetime('now','+1 day');
    julianday(timestring)	    # Días julianos	
        SELECT julianday('now');
    strftime(fmt,time)	        # Formato personalizado	
        SELECT strftime('%Y-%m-%d', 'now');
"""
control = """
    COALESCE(x,y,...)	        # Primer valor no nulo	
        SELECT COALESCE(email,'sin email') FROM clientes;
    IFNULL(x,y)	                # y si x es NULL	
        SELECT IFNULL(telefono,'N/A') FROM clientes;
    NULLIF(x,y)	                # NULL si x=y	
        SELECT NULLIF(5,5); → NULL
    TYPEOF(x)	                # Tipo real del valor	
        SELECT TYPEOF(42); → integer
    HEX(x)	                    # Convierte a hexadecimal	
        SELECT HEX('abc'); → 616263
    QUOTE(x)	                # Devuelve cadena SQL escapada	
        SELECT QUOTE("O'Reilly"); → 'O''Reilly'
    ZEROBLOB(n)	                # BLOB de n bytes en 0	
        SELECT ZEROBLOB(4);


"""


