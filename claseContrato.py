from datetime import datetime
from claseEquipo import Equipo
from claseJugador import Jugador

class Contrato:
    __fechaInicio =  None
    __fechaFin = None
    __pago_mensual = None
    __jugador = None
    __equipo = None
    
    def __init__(self, fecha_inicio = None, fecha_fin = None, pago = None, jugador = None, equipo = None):
        if isinstance(jugador, Jugador) and isinstance(equipo, Equipo):
            self.__fechaInicio = fecha_inicio
            self.__fechaFin = fecha_fin
            self.__pago_mensual = pago
            self.__jugador = jugador
            self.__equipo = equipo

    def __str__(self):
        s = 'Fecha de inicio: {}/{}/{} Fecha fin: {}/{}/{} Pago:{}\n'.format(self.__fechaInicio.year, self.__fechaInicio.month, self.__fechaInicio.day,self.__fechaFin.year,self.__fechaFin.month,self.__fechaFin.day,self.__pago_mensual)
        s+=str(self.__equipo)+'\n'+str(self.__jugador)+'\n'
        return s

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo       

    def getFechaInicio(self):
        return self.__fechaInicio     

    def getFechaFin(self):
        return self.__fechaFin    

    def getPagoMensual(self):
        return self.__pago_mensual

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        __atributos__ = dict(fecha_inicio = str(self.__fechaInicio), fecha_fin = str(self.__fechaFin), pago = self.__pago_mensual, dni = self.__jugador.getDNI(), nombre_equipo = self.__equipo.getNombre())
        )
        return d

