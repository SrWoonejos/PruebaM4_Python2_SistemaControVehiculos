#clase Automovil hereda de Vehiculo

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, velocidad: float, cilindrada: int):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    #getters
    def get_velocidad(self):
        return self.velocidad
    
    def get_cilindrada(self):
        return self.cilindrada
    
    #setters
    def set_velocidad(self):
        return self.velocidad

    def set_cilindrada(self):
        return self.cilindrada
    
    def __str__(self):
        base_info = super().__str__() 
        return f"{base_info}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"