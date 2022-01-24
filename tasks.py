from invoke import task, run

@task
def installdeps(c):
    """
    Instala todas las dependencias necesarias para el proyecto.
    """
    run("poetry install")

@task
def lint(c):
    """
    Tarea para comprobar la sintaxis de los ficheros fuente. 
    Utilizando el verificador Pylint.
    """
    print("Combrobando codigos fuente...")
    
    # Verifica los códigos del directorio modules
    run("pylint -E modules")

@task
def test(c):
    '''
    Lanza los tests creados para el proyecto
    '''
    run ('python3 -m pytest')
