from manejadorContrato import manejadorContrato
from manejadorEquipos import manejadorEquipos
from manejadorJugadores import manejadorJugadores
from claseObjectEncoder import ObjectEncoder
class Menu:
    __opcion = None

    def mostrarMenu(self, UnManejadorContrato, UnManejadorEquipo, unManejadorJugadores, unObjetoEncoder):
        if isinstance(UnManejadorContrato, manejadorContrato) and isinstance(UnManejadorEquipo, manejadorEquipos) and isinstance(unManejadorJugadores, manejadorJugadores) and isinstance(unObjetoEncoder, ObjectEncoder):
            salir = False
            while not salir:
                print('1- Crear un contrato para un jugador')
                print('2- Consultar jugador contratado')
                print('3- Consultar contratos')
                print('4- Obtener importe de contratos')
                print('5- Guardar archivo')
                print('6- Salir')
                self.__opcion = int(input('Ingrese una opcion: '))

                if self.__opcion == 1:
                    UnManejadorContrato.contratarJugador(UnManejadorEquipo,unManejadorJugadores)

                elif self.__opcion == 2:
                    dni = (input('Ingrese el DNI de un jugador: '))
                    UnManejadorContrato.buscarJugador(dni)

                elif self.__opcion == 3:
                    nombre_equipo = input('Ingres el nombre de un equipo: ')
                    UnManejadorContrato.mostrarJugadores(nombre_equipo)   

                elif self.__opcion == 4:
                    nombre_equipo = input('Ingres el nombre de un equipo: ')
                    ImporteTotal = UnManejadorContrato.getImporteTotal(nombre_equipo) 
                    print('El importe que se debe pagar por los jugadores del equipo {} es: {}' .format(nombre_equipo,ImporteTotal))
                elif self.__opcion == 5:
                    d = UnManejadorContrato.toJSON()
                    unObjetoEncoder.guardarJSONArchivo(d,'Contratos.json')
                    print('Archivo guardado con exito!')

                elif self.__opcion == 6:
                    salir = True
                    print('Cerrando menu...')    

                else:
                    print('ERROR: Opcion ingresada incorrecta!')



