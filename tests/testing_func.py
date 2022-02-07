# Funciones necesarias para la ejecucion de los tests

import csv
from modules.productoVenta import ProductoVenta

def lee_productos_from_CSV(path):
    with open(path, mode='r') as fichero:
        datos = csv.reader(fichero, delimiter=',')

        """
        Se puede utilizar un set pues el orden no es importante y
        los elementos son únicos. Pero para trabajar mejor accediendo
        a los objetos de ProductVenta es más recomendable usar una tupla además de 
        que resulta más ligero.
        """

        productos = tuple()

        for prod in datos:
            id = prod[0]
            nom = prod[1]
            inf = prod[2]
            cant = prod[3]
            prec = prod[4]
            min = prod[5]
            max = prod[6]

            # Elemento nuevo que alojamos en una tupla para concatenarla con la tupla general de productos
            # La coma del final es necesaria para identificar la tupla con un solo elemento
            prod_nuevo = (ProductoVenta(id, nom, inf, cant, prec, min, max),) 

            productos += (prod_nuevo)
    
    return productos