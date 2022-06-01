from datetime import datetime

class Jugador:
    __Nombre = None
    __DNI = None
    __Ciudad_Natal = None
    __Pais_Origen = None
    __Fecha_Nacimiento = None

    def __init__(self, nombre = None, dni = None, ciudad = None, pais = None, fecha = None):
        if isinstance(fecha,datetime):
            self.__Nombre = nombre
            self.__DNI = dni
            self.__Ciudad_Natal = ciudad
            self.__Pais_Origen = pais
            self.__Fecha_Nacimiento = fecha

    def getDNI(self):
        return self.__DNI    

    def getNombre(self):
        return self.__Nombre    

    def __str__(self):
        return 'Nombre: {} DNI: {}' .format(self.__Nombre,self.__DNI)