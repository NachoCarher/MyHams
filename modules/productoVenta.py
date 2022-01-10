# Clase para almacenar la info de un producto que esta en venta

from producto import *


class ProductoVenta(Producto):
    """
    Clase que representa un producto a la venta.

    Parametros
    ----------
    nom : str, default=''
        Nombre del producto.
    info : str, default=''
        Información sobre las características del producto.
    cantidad : int, default=0
        Cantidad de el producto disponible en stock.
    precio : float, default=0.0
        El precio del producto.
    min : int, default=0
        Mínimo de unidades de un producto que deber de haber en stock.
    max : int, default=0
        Máximo de unidades de un producto que deber de haber en stock.
    """

    def __init__(self, nom='', info='', cantidad=0, precio=0.0, min=0, max=0):   
        
        # Invoca al constructor de clase Producto
        Producto.__init__(self, nom, info)

        self.cantidad = cantidad
        self.precio = precio
        self.min = min
        self.max = max
        
    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad

    def get_cantidad_minima(self):
        return self.min

    def get_cantidad_maxima(self):
        return self.max
