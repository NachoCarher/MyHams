# Elección de imagen base para el contenedor
Los requisitos que debe cumplir la imagen son:
1. Ser tan ligera como sea posible sin que llegue a comprometer ninguna funcionalidad de la aplicación. Esto evita sobrecargar el contenedor, no desperdiciar espacio y reducir la exposición a vulnerabilidades.
2. Debe contar con las bibliotecas y paquetes estándares necesarios como para proporcionar una estabilidad sólida y que no tenga dependencias extra que puedan ralentizar el desarrollo o propiciar errores.
3. Que disponga de Python instalado o bien ofrezca una forma rápida de realizar su instalación. Es importante una buena compatibilidad con el lenguaje pues es en el que se desarrolla el proyecto.
4. Ser actualizado con asiduidad, de manera se beneficie de los nuevos parches de seguridad y mejoras que salgan para sus dependencias. Si la imagen es oficial o está verificada se tendrá en cuenta, pues es un plus de confianza.

## Imágenes candidatas
Las diferentes imágenes a considerar son [variantes de la imagen oficial de Python](https://hub.docker.com/_/python), están disponibles para distintas versiones de Python y son actualizadas frecuentemente.
Entre ellas se han considerado las versiones `3.8-slim` y `3.8-alpine`.

Existen tambien imágenes basadas en  `Ubuntu` que perfectamente pueden servir para el desarrollo del objetivo, pues realmente consiste en disponer de un entorno Ubuntu completo para el testeo de la aplicación. Sin embargo se descarta por tener paquetes adicionales instalados que no resultan estrictamente necesarios, por ocupar un espacio mucho más considerable que el que exigen las imágenes de Python y no disponer de ninguna versión del lenguaje preinstalada.

### Slim
Deriva de la imagen completa de Python. Esta variante generalmente instala tan sólo los mínimos paquetes requeridos para poder ejecutar Python. Por ende, si tenemos restricciones con respecto al espacio esta imagen resulta mejor opción que la versión completa pues al fin y al cabo ocupa menos.

### Alpine
Estas imágenes están basadas en el [Alpine Linux Project](https://alpinelinux.org/), que es un sistema operativo que fue concebido específicamente para usarse en contenedores y se caracteriza por ser muy liviano. De manera que si el espacio supone un problema, esta variante es una buena opción.

Un aspecto de `Alpine` y que hay que tener en cuenta es que en vez de utilizar `apt-get` para instalar paquetes se usa `apk`. 

## Análisis de las imágenes

Analizamos las variantes de Python y para compararlas entre ellas y seleccionar una se tendrá en cuenta el tamaño de cada imagen y la velocidad de construcción del contenedor para pruebas.

Para estudiar cada candidata se desarrolla un Dockerfile específico para cada una y así poder realizar el montaje y analizar tiempos y tamaño.
No quiere decir que el Dockerfile de la imagen escogida sea el final, será necesario modificarlo para la adaptación total a lo que se solicita en el objetivo.

### Dockerfiles

<details><summary>Dockerfile Python:3.8-alpine</summary>
  
    FROM python:3.8-alpine

    LABEL maintainer="NachoCarher <e.nachoch64@go.ugr.es>" version="1.0" 

    WORKDIR /app/

    RUN apk update && apk add curl gcc libc-dev libffi-dev bash && \
      addgroup -S -g 1000 myhams_test && \
      adduser -S myhams_test -G myhams_test -u 1000 && \
      mkdir -p /home/myhams_test/.local /app && \
      chown -R myhams_test:myhams_test /home/myhams_test /app

    USER myhams_test

    COPY pyproject.toml poetry.lock tasks.py ./


    ENV PATH=$PATH:/home/myhams_test/.local/bin

    RUN curl -sSL https://install.python-poetry.org | python3 - && \
        poetry config virtualenvs.create false && \
        poetry install 

    ENTRYPOINT ["invoke", "test"]
  
</details>
  
<details><summary>Dockerfile Python:3.8-slim</summary>
    
    FROM python:3.8-slim

    LABEL maintainer="NachoCarher <e.nachoch64@go.ugr.es>" version="1.0" 

    WORKDIR /app/

    RUN apt update && apt install -y curl && \
      groupadd -g 1000 -r myhams_test && \
      useradd -u 1000 -r -g myhams_test myhams_test && \
      mkdir -p /home/myhams_test/.local /app && \
      chown -R myhams_test:myhams_test /home/myhams_test /app

    USER myhams_test

    COPY pyproject.toml poetry.lock tasks.py ./


    ENV PATH=$PATH:/home/myhams_test/.local/bin

    RUN curl -sSL https://install.python-poetry.org | python3 - && \
        poetry config virtualenvs.create false && \
        poetry install 

    ENTRYPOINT ["invoke", "test"] 

</details>

Una desventaja de `Alpine` es que no contiene algunos paquetes que son necesarios. Principalmente, utiliza la biblioteca `musl` que es más ligera que `glibc`, de ahí que haya sido necesario especificar su instalación y las de otras dependencias adicionales en el Dockerfile. De no hacerlo y fuese necesario utilizar contenido específico de *libc* (requerida por gran cantidad de programas en C, incluyendo Python) podrían suceder errores, ya que los wheels estándar de Linux no funcionan en Alpine Linux.

Debido a cómo está estructurado `Alpine`, nos fuerza a ejercer una labor de investigación para determinar qué dependencias hay que instalar para que funcione todo correctamente. De ahí que se acaben añadiendo `gcc`, `curl`, `libc-dev`, `libffi-dev` y `bash` y como consecuencia tarde más en construirla.

Una vez diseñados los Dockerfile para cada imagen tan solo queda obtener el tiempo que se tarda en construirlas. Una opción puede ser usando `time`, y una vez completado ese paso listamos las imágenes con `docker images` y obtenemos el espacio ocupado de cada una.
  
```
time docker build --no-cache . -f ./Dockerfile_py_alpine -t hm_alpine
real    0m 47,830s
user    0m 0,046s
sys     0m 0,023s    
```
  
```
time docker build --no-cache . -f ./Dockerfile_py_slim -t hm_slim
real    0m 31,513s
user    0m 0,067s
sys     0m 0,027s  
```
  
| Imagen                    | Tamaño | *Building time* | 
| ------                    | ------ | ------------------------- |
| python:3.8-alpine         | 262MB  | 47,830s                   |
| python:3.8-slim           | 224MB  | 31,513s                   | 
  
  
## Elección final
  
Como podemos observar, la imagen `python:3.8-slim` al tener menos dependencias que instalar es superior aunque la diferencia por tamaño no sea muy exagerada o determinante. Por otro lado, si apreciamos el tiempo que se tardan en construir las imágenes, aquí sí que algo más notable la diferencia con respecto a `python:3.8-alpine`.

Por la implicación de trabajo extra que requiere `Alpine`, su exposición a [bugs en tiempo de ejecución](https://bugs.python.org/issue32307) (aunque éste no cubra Python 3.8) debido a usar otras bibliotecas y sus peores resultados obtenidos nos decantamos por `Slim`.

## Dockerfile del proyecto
Se ha tratado en seguir en todo momento las buenas prácticas de Dockerfile.

- Se utiliza un usuario *myhams* con los privilegios o permisos esenciales, con el objeto de obstruir o dificultar un escalado durante la ejecución del contenedor.
- Organizando todo lo posible bajo la misma capa se consigue incrementar la legibilidad del código y además resulta más sencillo de mantener. De manera que en lugar de utilizar varias instrucciones `RUN` se ha reunido todo en una haciendo uso de los operadores `&&`.
- Proporcionar información útil o metadatos sobre el desarrollador del Dockerfile y la versión utilizada.
- El hecho de no tomar una imagen completa como la de Ubuntu o Python si no una variante como slim en este caso también es una buena práctica. Pues están lo mejor optimizadas posible y son pequeñas.
- Se ha prestado atención a no utilizar instrucciones u ordenes como `ROOT` o `sudo`. Es importante tener en cuenta que una mala gestión de los privilegios puede ocasionar daños o problemas inesperados.