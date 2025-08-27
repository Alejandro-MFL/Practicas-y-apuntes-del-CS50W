###########################       Apuntes de Funciones       ###########################

# Configuracion global
configuracion = """ 
    git config --global x  
            user.name "tu nombre"
            user.mail "tu mail"
            user.signingkey x       # Establecer x como clave gpg para firmar commits
            color.ui auto           # Activa colores en la terminal para hacer más legibles los comandos de Git
            core.excludesfile ~/.gitignore_global
                # Define un archivo .gitignore que se aplique a todos tus repositorios
            alias.st status         # Crea atajos, git st equivale a git status
        git config --list           # Lista todas las configuraciones activas y su origen
"""

# Inicio de repositorio
InitAndClone = """ 
    git init            # Para iniciar uno nuevo
    git clone URL       # Para clonar uno preexistente
"""

# Ver estado
estado = """ 
    git status          # Muestra archivos modificados, agregados o pendientes de confirmar    
    git diff            # Muestra los cambios en el código que aún no se han confirmado    
"""
historial = """ 
    git log             # Muestra el historial de commits
    git remote -v       # Muestra las URLs de repositorios remotos
"""

# Añadir elementos
adds = """ 
    git add x           # Agrega el elemento x
    git add .           # Agrega todos los elementos    
"""
commits = """ 
    git commit -m "x"   # Realiza una instantanea con la etiqueta x
    git commit -am "x"  # Agrega todo y hace una instantanea con la etiqueta x
"""
stash = """ 
    git stash           # Guarda cambios sin llegar ha hacer commit
    git stash pop       # Recupera los cambios guardados por git stash
"""

# Deshacer cambios
restaurarResetear = """ 
    git restore x       # Quita los elementos no confirmados del archivo x
    git reset x         # Saca el archivo x del area de stanging       
    git reset --hard    # Elimina los cambios no confirmados hasta el ultimo commit
        <commit>        # Se puede añadir un commit concreto o a una version concreta
        origin/main
"""

# Sincronizacion con remoto
pullPushFetch = """
    git pull            # Descarga y combina cambios del repositorio remoto a tu rama local
    git push            # Sube tus commits al repositorio remoto
    git fetch           # Descarga cambios del remoto pero sin fusionarlos
"""

# Ramas
branchs = """ 
    git branch              # Lista de las ramas locales
    git branch x            # Crea una rama con el nombre x
"""
checkout = """ 
    git checkout x          # Cambia a la rama x
    git checkout -b x       # Crea la rama x y cambia a ella
"""
merge = """ 
    git merge x                                 # Combina la rama x con la rama actual

Merge Conflicts:
    Estructura:
        <<<<< HEAD                              # Inicio de conflicto
        b = 2                                   # Mi version
        =====
        b = 0                                   # Version remota
        >>>>> 57656c636f6d6520746f20576562      # Fin del conflicto y hash identificatorio

"""


###########################       Apuntes teoricos       ###########################

# Areas de trabajo
area = """ 
    [Working Directory] -- git add --> [Staging Area] -- git commit -->
        [Repositorio Local] -- git push --> [Repositorio Remoto]
        
    # Ademas puede estar stash entre [Staging Area] -- git commit    
"""
paginaWeb = """ 
    x.github.io     # Para hacer una pagina en github añadir .github.io al nombre del repositorio al crearlo
"""
pestañas = """ 
    - codigo: nos permite ver los archivos y carpetas dentro de nuestro directorio
    - problemas: podemos abrir y cerrar problemas, 
      que son solicitudes de corrección de errores o nuevas funciones
    - Pull request: Solicitudes de quienes desean fusionar código de una rama con otra.
      permite realizar revisiones de código donde se comentan y ofrecen sugerencias antes
      de integrar el código en la rama maestra
    - Acciones de GitHub : esta es la pestaña que usaremos cuando trabajemos en integración
      continua, ya que proporciona registros de las acciones que se han realizado 
      después de cada envío
"""

# GitHub Actions
CI_CD = """
# Son las siglas de Integración Continua y Entrega Continua , es un conjunto de buenas prácticas de desarrollo de software   
    Tiene dos partes:
        -Integración continua:
            Fusiones frecuentes a la rama principal
             # Esto permite afrontar los pequeños conflictos facilmente 
            Pruebas unitarias automatizadas con cada fusión
             # Permite aislar las partes del problema que surgan en las pequeñas fusiones
        -Entrega continua:
            Cronogramas de lanzamiento cortos, lo que significa que se lanzan nuevas versiones de una aplicación con frecuencia.
             # Permite aislar los problemas de cada lanzamiento y que los usuarios se adapten progresivamente a los pequeños cambios
"""
YAML = """ 
# Es un lenguaje configurado que estructura sus datos por clave-valor. 
    Permite anidar claves en claves, mas de un valor en una clave
        ###
            clave1: valor1
            clave2: 
                - valor2
                - valor3
            clave3:
                - clave4 : valor4
                - clave5 : valor5
        ###

    Los archivos YAML acaban en .yml o .yaml

"""
estructura = """
    La estructura de un GitHub Actions es la siguiente:
    ###
        name: Testing                           # Nombre del flujo de trabajo
        on: push                                # Cuando activar el flujo

        jobs:                                   # Trabajo que se activa
        test_project:                           #1
            runs-on: ubuntu-latest              # En que maquina virtual se ejecutara
            steps:                          
            - uses: actions/checkout@v2         # Que accion de GitHub usara
            - name: Run Django unit tests       # Nombre descriptivo
                run: |                          # comandos que se ejecutaran en el servidor
                    pip3 install --user django
                    python3 manage.py test
    ###
        
"""


