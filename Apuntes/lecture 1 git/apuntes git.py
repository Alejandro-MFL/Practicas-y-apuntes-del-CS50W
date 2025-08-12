### Apuntes de Funciones  ###

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


### Apuntes teoricos ###

# Areas de trabajo
area = """ 
    [Working Directory] -- git add --> [Staging Area] -- git commit -->
        [Repositorio Local] -- git push --> [Repositorio Remoto]
        
    # Ademas puede estar stash entre [Staging Area] -- git commit    
"""
paginaWeb = """ 
    x.github.io     # Para hacer una pagina en github añadir .github.io al nombre del repositorio al crearlo
"""

