# Integración Continua y Despliegue Continuo

Mediante el uso de una GitHub Action implementada en [este archivo](.github/workflows/build_container.yml) se construye el contenedor para pruebas y se sube a DockerHub por cada modificación que suceda sobre los archivos del repositorio que hayan sido especificados y en cualquier rama.

Para poder logearnos correctamente en DockerHub sin necesidad de utilizar nuestra contraseña de usuario hemos hecho uso de un [token de acceso](https://docs.docker.com/docker-hub/access-tokens/) y accedemos a él de forma cómoda en forma de variables de entorno a través de los [secretos cifrados](https://docs.github.com/es/actions/security-guides/encrypted-secrets) que proporciona GitHub. 

## Elección de una platataforma CI
Los requisitos que debe satisfacer la plataforma CI que se elija son los siguientes:
1. Debe ser una plataforma que ofrezca sus servicios en forma de version gratuita y con duración indefinida o bien con un periodo de prueba considerablemente extenso, pues el propósito del proyecto es, hasta ahora, con fines académicos.
2. Debe proporcionar soporte e integración con Docker.
3. Debe ser fácil de instalar y configurar.
4. No requerir de un proceso de verificación de identidad o KYC (Know Your Customer) mediante la acreditación de documentación personal para poder utilizar la plataforma, algo que se ve con asiduidad en este tipo de plataformas. 

## Plataformas candidatas
### [Github Actions](https://github.com/features/actions)
Permite llevar a cabo procesos de CI/CD mediante el uso de flujos de trabajo (workflows) y automatizarlos. Además se puede utilizar la conocida *matrix* para probar distintas versiones del lenguaje.

- El uso de esta plataforma es completamente gratuito.
- Es fácil de utilizar e integrar con GitHub pues ha sido desarrollado por su equipo. Con un archivo YAML ya es suficiente para poder hacer uso de la plataforma, y como se integra bien con Docker ha sido utilizado para la construcción de un contenedor para el objetivo anterior y subirlo a DockerHub.
- Requiere el mismo proceso de registro que para utilizar GitHub, tan solo un correo electrónico y una contraseña. No hay que proporcionar documentación adicional.

    - Puntuación: 4/4
    - Conclusión: ✓

### [Circle CI](https://circleci.com/)
Es una herramienta CI/CD muy conocida y utilizada que al igual que GitHub Actions, ofrecen en el plan gratuito la posibilidad de lanzar construcciones paralelas.

- Ofrece un plan gratuito con un paquete de posibilidades o características más ambicioso que el de la mayoría y 6000 minutos de uso por mes.
- No supone ninguna dificultad utilizarlo y se puede configurar en el repositorio por medio de un archivo `.circleci/config.yml`. Por lo que su [integración con GitHub](https://circleci.com/docs/2.0/gh-bb-integration/) está garantizad, bien documentada y sencilla.
- Tiene soporte para GitHub y Docker.

    - Puntuación: 3.5/4
    - Conclusión: ✗

No se va a considerar para utilizarla en el proyecto porque ha sido una herramienta muy demandada por el resto de compañeros y se trata de evitarla.

### [Travis CI](https://www.travis-ci.com/)
- Ofrece un periodo gratuito en el que podremos utilizar la plataforma, pero una vez finalizado se solicita un pago.
- Se integra con Docker y GitHub.
- Configuración por medio de un archivo YAML, por lo que resulta sencillo.
- Cuando finaliza el periodo de prueba se exigen datos bancarios. 

    - Puntuación: 2/4
    - Conclusión: ✗

### [AppVeyor](https://www.appveyor.com/)
- Posibilidad de ejercer un uso gratuito de la plataforma para proyectos open source, con la particularidad de que solo podremos lanzar un trabajo concurrente.
- Permite utilizar servicios como Docker, que está bien integrado.
- Se configura por medio de un archivo `appveyor.yaml` por lo que resulta bastante sencillo debido a su sintaxis.
- No es necesario proporcionar información bancaria o personal para utilizar la herramienta.

    - Puntuación: 4/4
    - Conclusión: ✓

## Elección final

En genereral, la gran mayoria de plataformas ofrecen una integración con GitHub ya sea como una aplicación externa o mediante llaves de despliegue (deploy key) y soportan Docker. Además de que la configuración por medio de archivos YAML también es un factor común en las opciones propuestas.

GitHub Actions y AppVeyor son las que han alcanzado la puntuación máxima y serán las que se utilizarán para el avance del proyecto.