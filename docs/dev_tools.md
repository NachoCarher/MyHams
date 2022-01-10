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
Cabe a destacar que las actualizaciones de la dependencias se deben realizar manualmente, esta aspecto se opone a su uso en relación a la automatización.

Es sencillo, tiene un soporte contínuo y es conocido, pero la última característica comentada se puede considerar como una desventaja y como consecuencia no
es suficiente como para elegirlo.

- Puntuación: 2.5/3
- Conclusión: ✗


### [Poetry](https://python-poetry.org/)

Poetry es un gestor de dependencias que será el encargado de instalar las bibliotecas necesarias y así cualquiera podrá ejecutarlo sin problema y fácilmente.
Ésto es algo que suele ser más difícil de gestionar y funciona como es esperado. Es intuitiva y resulta fácil eliminar paquetes y sus dependencias.
Además de su velocidad de instalación, cuenta con un buen soporte y trabaja sobre el fichero 'pyproject.toml' que es el archivo oficial de Python
para la gestión de dependencias desde que se introdujo [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format).

- Puntuación: 3/3
- Conclusión: ✓


### [Pipenv](https://pipenv.pypa.io/en/latest/)

Debido al gran papel que desempeña Python en el mundo de la programación Pipenv aparece como una herramienta implicada en la resolución de las dependencias
con las bibliotecas utilizadas en un proyecto. El una herramienta popular y el soporte que tiene es realmente activo, suele haber respuestas a sus *issues* con
notable inmediatez.

- Puntuación: 3/3
- Conclusión: ✓

### Decisión

Existe un empate entre *Poetry* y *Pipenv* y ambos son buenos recursos y se adaptan a los criterios descritos, sin embargo, un factor que inclina la 
balanza a favor de *Poetry* es que éste soporta el fichero 'pyproject.toml'. De manera que se escoge *Poetry* como gestor de dependencias.

## *Task runner*

Requisitos de un gestor de tareas a tener en cuenta:
- Sintaxis centrada en la limpieza y sencillez.
- Buen soporte por parte de su comunidad, de forma que tenga un mantenimiento relativamente constante.
- Que sea conocido entre la comunidad Python y ampliar el alcance del desarrollo.
- Configuración en un fichero independiente.

### [Celery](https://docs.celeryproject.org/en/stable/index.html)

Es un *task runner* simple y sencillo de utilizar.
Cuenta con una gran comunidad tras él proporcionándole un mantenimiento periódico.
Se basa en el uso de una cola de tareas para la ejecución de operaciones utilizando las herramientas requeridas.
Un inconveniente es que necesita utilizar un *broker* como por ejemplo [RabbitMQ](https://www.rabbitmq.com/) para enviar y recibir mensajes, por lo que incluye dependencias y no cumple un requisito.
  
- Puntuación: 3/4
- Conclusión: ✗
 
### [Darq](https://github.com/seedofjoy/darq)

Es un *task runner* que permite la ejecución asíncrona tomando algunas características de *Celery* e imponiéndose por encima.
Permite organizar las tareas en colas y la finalización de este task runner se lleva a cabo cuando todas las tareas han sido ya ejecutadas. 
Su soporte es constante y frecuentemente actualizado. 
Sin embargo no tiene la misma popularidad que su predecesor *Celery* y menos desarrolladores lo conocen.

- Puntuación: 3.5/4
- Conclusión: ✗
 
### [Poethepoet](https://github.com/nat-n/poethepoet)

Consiste en un task runner que cuenta con una buena sinergia con Poetry y es específico de Python.
Las tareas se definen en el archivo pyproject.toml y se ejecutan con poe, se puede ejecutar tambien con argumentos. Por este motivo no cumple con el requisito
de que configure en un archivo aparte (tasks.py).

Las tareas pueden ser comandos y pueden ser definidas tambien como una secuencia de otras tareas.

Su comunidad es amplia y su mantenimiento frecuente.

Otra desventaja comparación con el resto de alternativas es que su proceso inicial de configuración es más profundo y complejo y tiene otras dependencias.

- Puntuación: 2/4
- Conclusión: ✗

### [Invoke](https://www.pyinvoke.org/)

Es el gestor de tareas más conocido en Python, específico para proyectos en este lenguaje y de sencilla sintaxis.
No tiene dependencias más que la suya propia.
Y además es potente, limpio, proporciona un API de alto nivel para ejecutar comandos de shell necesitando un único archivo y tiene un mantenimiento continuo.

- Puntuación: 4/4
- Conclusión: ✓

### Decisión

Tras esta comparación, se puede determinar que *Invoke*, con una puntuación de 4/4 demuestra satisfacer los criterios descritos y se escoge como *task runner*.
