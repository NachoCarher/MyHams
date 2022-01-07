# Herramientas utilizadas para el desarrollo

## [Python](https://www.python.org/downloads/release/python-380/)
Se ha elegido Python como lenguaje de programación para el desarrollo del proyecto pues su comunidad es muy amplia y se ejerce hincapié en algo tan fundamental
como la legibilidad del código. Es fácil, rápido y ameno de aprender, es un lenguaje multiplataforma, dinámico e interpretado y cuenta con una enorme variedad 
de bibliotecas con soporte constante y open-source que pueden mejorar mucho el funcionamiento y desarrollo de este proyecto.


## [Poetry](https://python-poetry.org/)
Para poder garantizar el correcto funcionamiento del proyecto se ha escogido Poetry como gestor de dependencias, que será 
el encargado de instalar las bibliotecas necesarias y así cualquiera podrá ejecutarlo sin problema y fácilmente.
Se ha elegido esta herramienta porque su uso está más simplificado, es intuitiva, resulta fácil eliminar paquetes y 
sus dependencias. Ésto es algo que suele ser mas difícil de gestionar y funciona cómo es esperado. Además de su velocidad 
de instalación, cuenta con un buen soporte y trabaja sobre el fichero 'pyproject.toml' que es el archivo oficial de Python
para la gestión de dependencias desde que se introdujo [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format).

Las otras opciones más demandadas a diferencia de Poetry son Pip y Pipenv:

- [Pip](https://pypi.org/project/pip/)

Es un sistema de gestión de paquetes para instalar y administrar bibliotecas en Python. 
Viene incluido desde la version de Python 2.7.9 y desde la versión 3.4.

- [Pipenv](https://pipenv.pypa.io/en/latest/)

Debido al gran papel que desempeña Python en el mundo de la programación Pipenv aparece como una herramienta implicada en la resolución de las dependencias
con las bibliotecas utilizadas en un proyecto. Y proporciona a los desarrolladores de las aplicaciones un buen método para organizar el entorno de trabajo.

## [Invoke](https://www.pyinvoke.org/)
Es el gestor de tareas más conocido en Python, es potente, limpio y proporciona un API de alto
nivel para ejecutar comandos de shell necesitando un único archivo.

Otras alternativa a invoke son: 

- [Celery](https://docs.celeryproject.org/en/stable/index.html)

Es otro task runner simple y sencillo de utilizar, cuenta con una gran comunidad tras él y se basa
en el uso de una cola de tareas para la ejecución de operaciones utilizando las herramientas requeridas.
  
- [Poethepoet](https://github.com/nat-n/poethepoet)

Consiste en un task runner que cuenta con una buena sinergia con Poetry, las tareas se definen en 
el archivo pyproject.toml y se ejecutan con poe, se puede ejecutar tambien con argumentos.
Las tareas pueden ser comandos y pueden ser definidas tambien como una secuencia de otras tareas.

  
- [Darq](https://github.com/seedofjoy/darq)

Es un task runner que permite la ejecución asíncrona tomando algunas características de Celery. Permite
organizar las tareas en colas y la finalización de este task runner se lleva a cabo cuando todas las tareas han 
sido ya ejecutadas.
