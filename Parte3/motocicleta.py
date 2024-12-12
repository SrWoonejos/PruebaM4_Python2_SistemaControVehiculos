#PARTE 3 CSV
from bicicleta import Bicicleta

# Clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return (super().__str__() +
                f", {self.nro_radios} radios, Cuadro: {self.cuadro}, Motor: {self.motor}")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'Motocicleta',
            'nro_radios': self.nro_radios,
            'cuadro': self.cuadro,
            'motor': self.motor
        })
        return data
