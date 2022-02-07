# Clase para almacenar la info de un producto

class Producto:
    def __init__(self, id='', nom='', info=''):
        """
        Clase que representa un producto de un catálogo.

        Parámetros
        ----------
        id : str, default=''
            Identificador del producto.
        nom : str, default=''
            Nombre del producto.
        info : str, default=''
            Información sobre las características del producto.
        """

        self.id = id
        self.nombre = nom    
        self.informacion = info

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_informacion(self):
        return self.informacion
