# particular.py
from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.puestos = self.validar_entero(puestos, "puestos")

    def __str__(self):
        return f"{super().__str__()}\nPuestos: {self.puestos}"