class Equipo:
    __Nombre = None
    __Ciudad = None

    def __init__(self, nombre = None, ciudad = None):
        self.__Nombre = nombre
        self.__Ciudad = ciudad
        
    def getNombre(self):
        return self.__Nombre    

    def __str__(self):
        return 'Nombre: {} Ciudad: {}' .format(self.__Nombre, self.__Ciudad)

