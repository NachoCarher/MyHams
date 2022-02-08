# Metodología [FIRST](https://medium.com/@tasdikrahman/f-i-r-s-t-principles-of-testing-1a497acda8d6)

Es una serie de características y principios que se siguen en la creación de tests.
Cada sigla del nombre de esta metodología hace referencia a una determinada propiedad.

- **Fast**: Los tests deben ejecutarse rápidamente.
- **Isolated/Independent**: Por cada test unitario dado, éste debe ser independiente de los demás. De forma que no pueda ser influenciado por ningún otro factor y se 
pueda ejecutar por separado.
- **Repeteable**: No deben cambiar los valores de los tests dependiendo de su ejecución en diferentes entornos.
- **Self-validating**: Deben de poder validarse por sí mismos sin necesidad de que el usuario compruebe manualmente si pasan o no.
- **Thorough**: Los tests tienen que ser exhaustivos, es decir, tienen que ser capaces de cubrir todos los posibles resultados. Además de que deben ser
escritos primero antes que la implementación de cualquier código.

# Marcos de prueba

Consisten en aquellas funciones que permitan comprobar si los resultados obtenidos de cualquier código son los esperados. Y también son aquellas herramientas
que permiten ejecutar las tareas en un determinado lenguaje de programación para la consecución de los tests. 

Serían unas buenas características de los posibles marcos a elegir para el proyecto que el marco de test seleccionado permitiera el uso de diferentes bibliotecas de 
aserciones y proporcionara salidas fácilmente interpretables. También, al estar tratando de Python, se debería de poder utilizar los objetos que se crean en la 
fase de *setup* de los tests, los denominados *fixtures* y que cuentan con su propia sintaxis.

## Marco de prueba seleccionado

Es marco de prueba que he escogido para la comprobación de los tests de este proyecto es [Pytest](https://github.com/pytest-dev/pytest). Es simple,
lo que facilita la tarea de escribir pequeños tests, pero permite perfectamente el escalado de estos para el desarrollo de pruebas más elaboradas y complejas.
Además, se pueden utilizar los mencionados fixtures, la salida que proporcionan es clara y legible y se pueden utilizar bibliotecas de aserciones.

## Otras opciones

### [Unittest](https://github.com/python/cpython/tree/main/Lib/unittest)

- Se pueden emplear los fixtures.
- Las salidas que maneja no son muy detalladas.
- Se puede testear utilizando bibliotecas de aserciones.

### [Testify](https://github.com/Yelp/Testify)

Tiene como cometido ser sobretodo una gran alternativa a Unittest soportando sus clases e incorporando nuevas características y complementos.
- Permite la utilización de fixtures.
- La salida del *test runner* es intuitiva y sencilla, colorida a diferencia de Unittest.
- Contiene utilidades o herramientas de testeo con el uso de bibliotecas de aserciones entre ellas.

# Bibliotecas de aserciones

Es importante el papel de una biblioteca de aserciones para poder llevar a cabo las pruebas unitarias que se deben testear. Por medio de ésta se puede comprobar 
el resultado esperado con el obtenido y tomar las correspondientes medidas.

[Assertpy](https://github.com/assertpy/assertpy) es una biblioteca de aserciones que funciona correctamente con Pytest y ambos tienen una buena sinergia entre sí, es 
una razón por la que se ha escogido. Pero tambien resulta sencilla de utilizar y muy intuitiva pues el nombre de sus propias sentencias es muy explícito en relación con el comportamiento que van a comprobar.
Soportan una gran cantidad de objetos dentro del ecosistema de Python permitiendo incluso ordenaciones y se pueden realizar aserciones dinámicas de objetos
gracias a que Python se caracteriza por ser un lenguaje de tipado dinámico.

## Otras opciones

### [Verify](https://github.com/dgilland/verify)

- Sintaxis simple buscando una cercanía (quizás algo excesiva) al lenguaje natural.
- Cantidad considerable de validadores.
- Distintos estilos de sintaxis para poder construir cadenas de aserciones más legibles.

### [Grappa](https://github.com/grappa-py/grappa)

- Lenguaje cercano al natural y bastante expresivo.
- Es una biblioteca de aserciones muy ligera.
- Sistema para reportar errores extenso, detallado y fácilmente interpretable.




