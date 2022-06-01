import numpy as np
from datetime import datetime
from manejadorEquipos import manejadorEquipos
from manejadorJugadores import manejadorJugadores
from claseContrato import Contrato
from claseJugador import Jugador
from claseEquipo import Equipo

class manejadorContrato:
    __dimension = None
    __incremento = None
    __cantidad = None
    __Contratos = None


    def __init__(self, dimension = 10, incremento = 5):
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
        self.__Contratos = np.empty(self.__dimension,dtype=Contrato)

    def agregarContrato(self,unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Contratos.resize(self.__dimension)
        self.__Contratos[self.__cantidad] = unContrato
        self.__cantidad+=1    

    def contratarJugador(self, unManejador, unMaejadorJugadores):
        if isinstance(unManejador, manejadorEquipos):
            nombre = input('Ingrese el nombre del jugador: ')
            dni = input('Ingrese su DNI: ')
            ciudad = input('Ingrese la ciudad natal: ')
            pais = input('Ingrese el pais de origen: ')
            dia = int(input('Ingrese el dia de nacimiento: '))
            mes = int(input('Ingrese el mes de nacimiento: '))
            year = int(input('Ingrese el anio de nacimiento: '))
            fecha_nacimiento = datetime(year,mes,dia)
            unJugador = Jugador(nombre,dni,ciudad,pais,fecha_nacimiento)
            unMaejadorJugadores.agregarJugador(unJugador)
            print('=== LISTA DE EQUIPOS ===')
            print(unManejador)
            nombre_equipo = input('Ingrese el nombre de un equipo: ')
            equipo = unManejador.obtenerEquipo(nombre_equipo)
            if type(equipo) != Equipo:
                print('ERROR: equipo no encontrado!')    
            else:
                inicio = datetime.now()
                fin = datetime(inicio.year+1,inicio.month,inicio.day)
                pago = input('Ingrese el pago mensual: ')
                unContrato = Contrato(inicio,fin,float(pago),unJugador,equipo)
                self.agregarContrato(unContrato)

    def buscarJugador(self, dni):
        i = 0
        encontro = False
        jugador = None
        equipo = None
        fecha = None
        while i < self.__cantidad and not encontro:
            jugador = self.__Contratos[i].getJugador()
            if jugador.getDNI() == dni:
                equipo = self.__Contratos[i].getEquipo()
                fecha = self.__Contratos[i].getFechaFin()
                encontro = True
                print('Nombre del jugador: {} equipo al que juega: {} expiracion del contrato: {}/{}/{}'.format(jugador.getNombre(),equipo.getNombre(),fecha.day,fecha.month,fecha.year))
            else:
                i+=1
        if not encontro:
            print('ERROR: Jugador no encontrado!')        

    def mostrarJugadores(self, nombre_equipo):
        i = 0
        encontro = False
        while i < self.__cantidad:
            if self.__Contratos[i].getEquipo().getNombre().lower() == nombre_equipo.lower():
                fecha_inicio = self.__Contratos[i].getFechaInicio()
                fecha_fin = self.__Contratos[i].getFechaFin()
                dif = fecha_fin - fecha_inicio
                if dif.days == 183:
                    print(self.__Contratos[i].getJugador())
                    i+=1
                    encontro = True
                else:
                    i+=1
            else:
                i+=1
        if not encontro:
            print('ERROR: Equipo no encontrado!')         

    def getImporteTotal(self, nombre_equipo):
        i = 0
        importeTotal = 0
        while i < self.__cantidad:
            if self.__Contratos[i].getEquipo().getNombre().lower() == nombre_equipo.lower():
                importeTotal+=float(self.__Contratos[i].getPagoMensual())
                i+=1
            else:
                i+=1       
        return importeTotal            

    def toJSON(self):
        d = []
        i = 0
        while i < self.__cantidad:
            d.append(self.__Contratos[i].toJSON())
            i+=1      
        return d
