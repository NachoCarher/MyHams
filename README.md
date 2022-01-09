# MyHams

## Motivación ✨

Me gustaría que existiese una herramienta software que ayudara al negocio en el que trabaja mi padre a incrementar sus ventas y para ello pienso que una solución es mejorar el sistema de gestión de mercancía y reducir errores en el control de inventario.

## Descripción del problema 🛠️

Desarrollar un sistema encargado de la gestión de un almacén de productos cárnicos y cuyo objetivo es optimizar su organización.

## Puntualizaciones 💡

- Incrementar las ventas:
	- ¿De qué forma?
		Identificación de los pedidos con mayor potencial de venta.
		Por ejemplo, el sistema debería recomendar aumentar el inventario de aquellos productos con ventas
		ocasionales pero que son muy baratos y rentables, y tambien recomendar aquellos que se venden mucho independientemente del precio
		porque acaban aportando un buen beneficio.
		

	- ¿En base a qué información?
		El sistema debe recibir como entrada un histórico o una serie de datos del negocio. 
		Como el precio al por mayor que tienen los productos, la cantidad encargada, la frecuencia con la que se hacen pedidos de un determindado producto,
		porcentaje de existencias vendidas a final de mes, precio de venta.


- Mejorar la gestión:
	- ¿De qué forma?
		Con los datos recabados el sistema reconocerá que productos podrían venderse más y cuáles son prescindibles por su baja rentabilidad.
		Se muestra un pronóstico de la evolución del índice de ventas si se aplicasen las recomendaciones aportadas por la aplicación.
		La gestión se ve favorablemente afectada debido a que con el simple hecho de usar la aplicación ya se está recogiendo el 
		inventario del negocio y está simplificando al usuario final su visualización y control de existencias.

- Reducir errores:
	- ¿Cuáles?
		Considero que es un error el hecho de no saber identificar que productos son los que provocan pérdidas en un negocio. Y a veces puede ser
		difícil reconocerlos puesto a que las pérdidas pueden ser ínfimas u ofrecer un rendimiento muy irregular con altos márgenes positivos y negativos.
		
## Requisitos
- Python **3.8+**

## Dependencias
Gestionadas con el uso de [Poetry](https://python-poetry.org/), consultar [`pyproject.toml`](pyproject.toml).

## Instalación

#### Poetry

Es la herramienta que gestiona e instala todas las dependencias necesarias
para que el proyecto funcione adecuadamente. Para instalarla usar:

```
curl -sSL https://install.python-poetry.org | python3 -
```

#### Este repositorio

[Clonar](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) este repositorio, y para la instalacion de las dependencias con poetry:

```
git clone https://github.com/NachoCarher/MyHams.git;
cd MyHams;
poetry install;
```

## Uso

#### Comprobación de la sintaxis de los fuentes

Para comprobar la sintaxis de los archivos `.py` utilizados, se utiliza la herramienta [invoke](https://www.pyinvoke.org/):

```
poetry shell
inv check
```
## Documentación
Para obtener más información acerca del proyecto puede consultar:
- [Usuarios e historia de usuario](docs/DOCUMENTACION.md)
- [Herramientas de desarrollo](docs/dev_tools.md)
