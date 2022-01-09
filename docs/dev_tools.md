# Herramientas utilizadas para el desarrollo

## Lenguaje de programación
### [Python](https://www.python.org/downloads/release/python-380/)
Las razones más significativas por las que se ha elegido Python como lenguaje de programación para el desarrollo del proyecto son:
- Amplia comunidad y con una serie de estándares y principios fuertemente asentados para fomentar la legibilidad del código.
- Lenguaje sencillo y fácil de aprender. Sobretodo favorece un desarrollo rápido.
- Gran cantidad de frameworks, módulos y bibliotecas de gran utilidad enriquecen cualquier proyecto.
- Es multiplataforma, de manera que puede ser utilizado en distintos sistemas operativos.
- Sintaxis limpia y uniforme por lo que es rápido de usar y entender.
- El proyecto tiene como enfoque modelar todo en función a clases y a objetos y Python al ofrecer una programación orientada a objetos nos proporciona
el uso de conceptos como la herencia, abstracción o polimorfismo.

## Gestor de dependencias

Requisitos que debe tener un gestor de dependencias:
- Sintaxis centrada en la limpieza y sencillez.
- Buen soporte por parte de su comunidad, de forma que tenga un mantenimiento relativamente constante.
- Que sea conocido entre la comunidad Python y ampliar el alcance del desarrollo. 

### [Pip](https://pypi.org/project/pip/)

Es un sistema de gestión de paquetes para instalar y administrar bibliotecas en Python. 
Viene incluido desde la version de Python 2.7.9 y desde la versión 3.4.
Cabe a destacar que las actualizaciones de la dependencias se deben realizar manualmente, esta aspecto se opone a su uso en relación a la automatización y 
da lugar a que se descarte como posible herramienta a elegir.

### [Poetry](https://python-poetry.org/)
Poetry es un gestor de dependencias que será el encargado de instalar las bibliotecas necesarias y así cualquiera podrá ejecutarlo sin problema y fácilmente.
Se ha elegido esta herramienta porque es intuitiva y resulta fácil eliminar paquetes y sus dependencias. 
Ésto es algo que suele ser más difícil de gestionar y funciona cómo es esperado.
Además de su velocidad de instalación, cuenta con un buen soporte y trabaja sobre el fichero 'pyproject.toml' que es el archivo oficial de Python
para la gestión de dependencias desde que se introdujo [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format).

### [Pipenv](https://pipenv.pypa.io/en/latest/)

Debido al gran papel que desempeña Python en el mundo de la programación Pipenv aparece como una herramienta implicada en la resolución de las dependencias
con las bibliotecas utilizadas en un proyecto. Una diferencia significativa con respecto a *Poetry* es que éste último, como bien se menciona anteriormente, 
soporta el fichero 'pyproject.toml'.

La herramienta seleccionada para la gestión de dependencias es *Poetry* pues es más rápido en tiempos de instalación que *Pipenv*, utiliza el fichero oficial 'pyproject.toml', tiene buen soporte y es conocido por la comunidad.

## *Task runner*

Requisitos de un gestor de tareas a tener en cuenta:
- Sintaxis centrada en la limpieza y sencillez.
- Buen soporte por parte de su comunidad, de forma que tenga un mantenimiento relativamente constante.
- Que sea conocido entre la comunidad Python y ampliar el alcance del desarrollo. 

### [Celery](https://docs.celeryproject.org/en/stable/index.html)

Es otro task runner simple y sencillo de utilizar, cuenta con una gran comunidad tras él y se basa
en el uso de una cola de tareas para la ejecución de operaciones utilizando las herramientas requeridas, sin embargo, existe un 
gestor llamado *Darq* que parte de la base del uso de colas de tareas de Celery y lo mejora con nuevos aspectos.
  
### [Darq](https://github.com/seedofjoy/darq)

Es un task runner que permite la ejecución asíncrona tomando algunas características de Celery. Permite
organizar las tareas en colas y la finalización de este task runner se lleva a cabo cuando todas las tareas han 
sido ya ejecutadas. Su soporte es constante y frecuentemente actualizado. Pero no tiene la misma popularidad que su predecesor *Celery* y menos desarrolladores lo conocen.
 
### [Poethepoet](https://github.com/nat-n/poethepoet)

Consiste en un task runner que cuenta con una buena sinergia con Poetry y es específico de Python, las tareas se definen en 
el archivo pyproject.toml y se ejecutan con poe, se puede ejecutar tambien con argumentos.
Las tareas pueden ser comandos y pueden ser definidas tambien como una secuencia de otras tareas. Y su comunidad y mantenimiento son activos.
Una característica a considerar en comparación con el resto de alternativas es que su proceso inicial de configuración es más profundo y complejo y tiene otras dependencias.

### [Invoke](https://www.pyinvoke.org/)

Es sido el *task runner* escogido, pues es el gestor de tareas más conocido en Python y específico para proyectos en este lenguaje.
Además de ser potente, limpio, proporcionar un API de alto nivel para ejecutar comandos de shell necesitando un único archivo y tener un mantenimiento continuo.

Con estas caracteristicas demuestra corresponder con los requisitos especificados y ser un *task runner* apto para el proyecto.

