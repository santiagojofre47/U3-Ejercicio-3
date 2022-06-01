import json
from pathlib import Path
from manejadorContrato import manejadorContrato
from claseContrato import Contrato

class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                contratos=d['Contratos']
                dcontrato = contratos[0]
                manejador=class_()
                for i in range(len(contratos)):
                    dcontrato=contratos[i]
                    class_name=dcontrato.pop('__class__')
                    class_=eval(class_name)
                    atributos=dcontrato['__atributos__']
                    unContrato=class_(**atributos)
                    manejador.agregarContrato(unContrato)
                return manejador 

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)        