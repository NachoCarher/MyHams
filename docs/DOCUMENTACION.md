# MyHams

Aquí se encuentra la información adicional del proyecto con una extensión más detallada.

## Tipos de usuarios 

La aplicación va destinada a un tipo de usuario concreto:

- Empresario: dueño del negocio que busca una mejora en la gestión del inventario, datos estadísticos sobre sus ventas y recomendaciones de cómo incrementarlas basándose en los propios datos.

La aplicación recoge los datos de los usuarios que interactúan con ella para así poder diferenciarlos y tener a sus disposición dos plataformas de pago distintas, 
en la que el costo de los productos para los usuarios de tipo empresario será más reducido dada una cantidad mínima de compra. 

La aplicación recoge los datos de los usuarios que interactúan con ella para así poder generar nuevas recomendaciones de mejora y ponerlas a disposición de ellos.
Por ejemplo, hay 30 negocios en el sistema que venden el 100% de totalidad de sus existencias de un determinado producto. En consecuencia, lo que el sistema va a hacer es
que cuando haya un usuario que no venda dicho producto porque sencillamente no lo tiene a la venta o nunca lo ha tenido, la apliación le recomendará que lo 
compre pues está suponiendo un producto exitoso para otros empresarios.

## Descripción de los usuarios: 

- Miguel (Empresario): hombre de 33 años, nivel de estudios superior (graduado), habituado con frecuencia a usar el ordenador y el smartphone, quiere emprender su negocio de supermercados. No es del todo bueno organizando el inventario y las ventas de un negocio y necesita de un sistema que le guiara con la gestión.

## User-journey

"Como Miguel García (dueño de una carnicería en un pueblo de Granada), querría tener ayuda a la hora de organizar el inventario de mi negocio. Considero que una 
visualización de datos estadísticos sobre las ventas de la carnicería sería una guía de gran importancia para saber cuáles son los productos que se venden mejor 
y cuáles son aquellos que me están suponiendo un lastre y siendo poco rentables. Es algo que agradecería mucho, pues en el sector alimentario los productos que no se venden se acaban caducando, 
eso se traduce en pérdidas y supone una cantidad de dinero que al final no puedo recuperar."

## Historias de usuario

- [HU1](https://github.com/NachoCarher/MyHams/issues/6) -> Como empresario, quiero que el sistema me proporcione información como para poder decidir sobre qué productos de los que tengo en mi inventario son los que debería seguir vendiendo o aumentar su stock y cuáles son aquellos que no me están siendo rentables y debería retirar.
- [HU2](https://github.com/NachoCarher/MyHams/issues/7) -> Como empresario, una cosa que se debe de manejar bien en el sector alimentario es saber detectar a la perfección cuáles son aquellos productos que generan pérdidas o bien porque se venden poco o bien porque a pesar de que no se vendan tan mal, el hecho de mantenerlos a cierta temperatura (mantenimiento) supone un gasto notable. Por eso en este negocio es importante disponer de productos que se vendan lo antes posible, pues al ser alimentos, disponen de fecha de caducidad y una vez pasada ésta no se podrán vender.
- [HU3](https://github.com/NachoCarher/MyHams/issues/11) -> Como empresario, me gustaría poder registrar en la aplicación los distintos tipos de productos que venderé en mi negocio con su respectiva información para poder organizar más intuitivamente el stock.

## Milestones

| **Milestone** | **Contenido** |
| ------------- | --------------- 
| [M0 - Sistema de gestión de productos](https://github.com/NachoCarher/MyHams/milestone/1) | Desarrollar una entidad en la que se puedan almacenar los productos disponibles y cada uno con su información correspondiente. |
| [M1 - Sistema de gestión de inventario](https://github.com/NachoCarher/MyHams/milestone/5) | Se pretende desarrollar software que permita al cliente registrar los productos que tiene intención de vender (stock) así como los datos de ventas de cada uno. |
| [M2 - Programa estadístico](https://github.com/NachoCarher/MyHams/milestone/4) | Se requiere una función que calcule y devuelva en base al número de ventas, precio de compra y P.V.P (precio de venta al público) de un producto un índice de rentabilidad asociado a él. |
