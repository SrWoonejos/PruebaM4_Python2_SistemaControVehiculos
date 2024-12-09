# automovil.py
from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, ruedas)
        self.velocidad = self.validar_entero(velocidad, "velocidad")
        self.cilindrada = self.validar_entero(cilindrada, "cilindrada")

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"
