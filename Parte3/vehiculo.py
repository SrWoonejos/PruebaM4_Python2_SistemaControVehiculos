#PARTE3 csv
# Clase base para un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

    def to_dict(self): 
        return { 'tipo': 'Vehiculo', 
                'marca': self.marca, 
                'modelo': self.modelo, 
                'nro_ruedas': self.nro_ruedas }