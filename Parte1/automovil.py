#clase Automovil hereda de Vehiculo

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int):
        super().__init__(marca, modelo, nro_ruedas)