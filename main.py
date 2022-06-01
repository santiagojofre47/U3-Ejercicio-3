from manejadorContrato import manejadorContrato
from manejadorEquipos import manejadorEquipos
from manejadorJugadores import manejadorJugadores
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu

if __name__ == '__main__':
    UnManejadorEquipo = manejadorEquipos()
    UnManejadorJugador = manejadorJugadores()
    UnManejadorContrato = manejadorContrato()
    unObjetoEncoder = ObjectEncoder()
    UnManejadorEquipo.leerArchivo()
    objetoMenu = Menu()
    print(' === LISTA DE EQUIPOS ===')
    print(UnManejadorEquipo)
    objetoMenu.mostrarMenu(UnManejadorContrato, UnManejadorEquipo, UnManejadorJugador,unObjetoEncoder)