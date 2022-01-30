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

## *Task runner*

Requisitos de un gestor de tareas a tener en cuenta:
- Sintaxis centrada en la limpieza y sencillez.
- Buen soporte por parte de su comunidad, de forma que tenga un mantenimiento relativamente constante.
- Que sea conocido entre la comunidad Python y ampliar el alcance del desarrollo.
- Configuración en un fichero independiente.

### [Make](https://www.gnu.org/software/make/manual/make.html)
La herramienta make basa su funcionamiento en la estructura de un único archivo Makefile y se puede considerar una opción apta para
ser analizada y determinar si podría ser útil para usarla en el proyecto.

Se caracteriza por no tener una sintaxis excesivamente difícil o compleja y tampoco resulta arduo iniciarse a la herramienta.

A día de hoy sigue estando respaldada por los desarrolladores y actualizándose.

En concreto es muy utilizada en los sistemas operativos tipo Unix/Linux, pues es un comando normalmente utilizado para la compilación de una gran cantidad
de programas y el task runner por excelencia. Pero por parte de la comunidad de Python no se llega a considerar como específico del lenguaje.

- Puntuación: 3/4
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
