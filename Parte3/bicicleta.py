#parte 3 csv
from vehiculo import Vehiculo

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return (super().__str__() +
                f", Tipo: {self.tipo}")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'Bicicleta',
            'tipo_bici': self.tipo
        })
        return data