#parte 3 csv
from vehiculo import Vehiculo

# Clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (super().__str__() +
                f", {self.velocidad} Km/h, {self.cilindrada} cc")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'Automovil',
            'velocidad': self.velocidad,
            'cilindrada': self.cilindrada
        })
        return data

# Clase Particular que hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return (super().__str__() +
                f", {self.nro_puestos} puestos")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'Particular',
            'nro_puestos': self.nro_puestos
        })
        return data

# Clase Carga que hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return (super().__str__() +
                f", {self.peso_carga} kg de carga")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'Carga',
            'peso_carga': self.peso_carga
        })
        return data
