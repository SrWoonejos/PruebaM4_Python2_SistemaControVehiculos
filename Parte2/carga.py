# carga.py
from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.carga = self.validar_entero(carga, "carga")

    def __str__(self):
        return f"{super().__str__()}\nCarga: {self.carga} Kg"