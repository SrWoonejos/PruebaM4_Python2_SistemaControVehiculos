#clase vehiculo

class Vehiculo:
    def __init__(self, marca: str, modelo: str, nro_ruedas: int):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

#getters
def get_marca(self):
    return self.marca

def get_modelo(self):
    return self.modelo

def get_nro_ruedas(self):
    return self.nro_ruedas

#setters
def set_marca(self, marca):
    self.marca = marca

def set_modelo(self, modelo):
    self.modelo = modelo

def set_nro_ruedas(self, nro_ruedas):
    self.nro_ruedas = nro_ruedas


def __str__(self):
    return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro. de ruedas: {self.nro_ruedas}"


