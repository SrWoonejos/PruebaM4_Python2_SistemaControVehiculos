# vehiculo.py
class Vehiculo:
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas, "
                f"{self.velocidad} Km/h, {self.cilindraje} cc")