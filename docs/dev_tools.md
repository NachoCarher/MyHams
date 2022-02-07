# Herramientas utilizadas para el desarrollo

## [Poetry](https://python-poetry.org/)
Para poder garantizar el correcto funcionamiento del proyecto se ha escogido Poetry como gestor de dependencias, que será 
el encargado de instalar las bibliotecas necesarias y así cualquiera podrá ejecutarlo sin problema y fácilmente.
Se ha elegido esta herramienta porque su uso está más simplificado, es intuitiva, resulta fácil eliminar paquetes y 
sus dependencias, algo que suele ser mas difícil de gestionar y funciona como es esperado.

La otra opción más demandada a diferencia de Poetry es Pip:

- [Pip](https://pypi.org/project/pip/)

Es un sistema de gestión de paquetes para instalar y administrar bibliotecas en Python. 
Viene incluido desde la version de Python 2.7.9 y desde la versión 3.4.

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
