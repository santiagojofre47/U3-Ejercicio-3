from claseJugador import Jugador

class manejadorJugadores:
    __listaJugadores = None

    def __init__(self):
        self.__listaJugadores = []

    def agregarJugador(self, unJugador):
        if isinstance(unJugador, Jugador):
            self.__listaJugadores.append(unJugador)
            
            