#PARTE 2 - PRUEBA FINAL PYTHON M4 - FULL STACK PYTHON 2024
# Clase base para representar un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"