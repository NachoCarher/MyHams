from invoke import task, run

@task
def installdeps(c):
    """
    Instala todas las dependencias necesarias para el proyecto.
    """
    run("poetry install")

@task
def check(c):
    """
    Tarea para comprobar la sintaxis de los ficheros fuente. 
    Utilizando el modulo de compilacion de fuentes de python 'py_compile'.
    """
    print("Combrobando codigos fuente...")
    
    # Verifica los códigos del directorio modules
    run("python -m py_compile modules/*.py")
