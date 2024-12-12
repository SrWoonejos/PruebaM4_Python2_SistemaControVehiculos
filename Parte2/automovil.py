#PARTE 2 - PRUEBA FINAL PYTHON M4 - FULL STACK PYTHON 2024
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

# Clase Particular que hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return (super().__str__() +
                f", {self.nro_puestos} puestos")

# Clase Carga que hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return (super().__str__() +
                f", {self.peso_carga} kg de carga")
