import numpy as np
import csv
from claseEquipo import Equipo

class manejadorEquipos:
    __dimension = None
    __incremento = None
    __cantidad = None
    __Equipos = None

    def __init__(self, incremento = 5):
        self.__incremento = incremento
        self.__cantidad = 0
        
    def agregarEquipo(self, unEquipo):  
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Equipos.resize(self.__dimension)
        self.__Equipos[self.__cantidad] = unEquipo
        self.__cantidad+=1

    def obtenerEquipo(self, nombre):
        i = 0
        encontro = False
        equipo = None
        while i < self.__cantidad and not encontro:
            if self.__Equipos[i].getNombre().lower() == nombre.lower():
                equipo = self.__Equipos[i]
                encontro = True
            else:
                i+=1   
        return equipo         

    def leerArchivo(self):
        archivo = open('equipos.csv') 
        reader = csv.reader(archivo, delimiter = ',')  
        band = False       
        for fila in reader:
            if not band:
                band = True
                #Incializar arreglo con dimension n contenida en el archivo csv
                self.__dimension = int(fila[0])
                self.__Equipos = np.empty(self.__dimension,dtype = Equipo)
            else:
                unEquipo = Equipo(fila[0],fila[1])
                self.agregarEquipo(unEquipo)

    def __str__(self):
        i  = 0
        s=''
        while i < self.__cantidad:
            s+=str(self.__Equipos[i])+'\n'
            i+=1
        return s    