# motocicleta.py
from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo, motor, chasis, radios):
        super().__init__(marca, modelo, ruedas, tipo)
        self.motor = motor
        self.chasis = chasis
        self.radios = self.validar_entero(radios, "radios")

    def __str__(self):
        return f"{super().__str__()}\nMotor: {self.motor}, Chasis: {self.chasis}, Radios: {self.radios}"