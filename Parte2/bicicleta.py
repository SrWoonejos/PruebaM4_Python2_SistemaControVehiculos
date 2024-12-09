# bicicleta.py
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}\nTipo: {self.tipo}"
