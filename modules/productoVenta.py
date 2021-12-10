
# Clase para almacenar la info de un producto que esta en venta

from producto import *


class ProductoVenta(Producto):
    
    def __init__(self,nom,info, cantidad, precio):   
        
        # Invoca al constructor de clase Producto
        Producto.__init__(self, nom, info)

        self.cantidad = cantidad
        self.precio = precio
        
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    

