# vehiculo.py

class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = self.validar_entero(ruedas, "ruedas")

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.ruedas} ruedas"

    @staticmethod
    def validar_entero(valor, nombre_campo):
        try:
            return int(valor)
        except ValueError:
            raise ValueError(f"El campo '{nombre_campo}' debe ser un número entero.")
    