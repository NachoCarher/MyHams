# Tests para el archivo productoVenta.py

from assertpy import assert_that
from testing_func import *

archivo_datos = "tests/data.txt"

def test_archivo_datos_valido():
    """
    Comprobamos que existe el archivo con los datos necesarios para
    poder ejecutar el resto de tests.
    """
    assert_that(archivo_datos).exists()


def test_respeta_nivel_maximo():
    # Cargamos los productos
    productos = lee_productos_from_CSV(archivo_datos)

    # Comprobamos que lo cargado no está vacío
    assert_that(productos).is_not_empty()
    
    """
    Utilizando is_not_empty() a parte de comprobar que contiene objetos
    verifica que es iterable
    
    assert_that(productos).is_iterable()
    """

    for prod in productos:
        # Comprobamos que cada elemento de productos es de la clase esperada y el estado de la lectura es correcto
        assert_that(prod, description = "Producto mal cargado").is_instance_of(ProductoVenta)

        cantidad_max = int(prod.get_cantidad_maxima())
        cantidad_actual = int(prod.get_cantidad())
        error = "El producto \"" + str(prod.get_nombre()) + "\" excede el nivel maximo de stock"

        assert_that(cantidad_actual, description = error).is_less_than_or_equal_to(cantidad_max)


def test_respeta_nivel_minimo():
    # Cargamos los productos
    productos = lee_productos_from_CSV(archivo_datos)

    # Comprobamos que lo cargado no está vacío
    assert_that(productos).is_not_empty()

    for prod in productos:
        # Comprobamos que cada elemento de productos es de la clase esperada y el estado de la lectura es correcto
        assert_that(prod, description = "Producto mal cargado").is_instance_of(ProductoVenta)

        cantidad_min = int(prod.get_cantidad_minima())
        cantidad_actual = int(prod.get_cantidad())
        error = "El producto \"" + str(prod.get_nombre()) + "\" es inferior al nivel minimo de stock"

        assert_that(cantidad_actual, description = error).is_greater_than_or_equal_to(cantidad_min)
