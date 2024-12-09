# main.py
from vehiculo import Vehiculo
from validadores import validar_entero, validar_cadena

def main():
    print("Programa de registro de vehículos para peaje")

    vehiculos = []
    cantidad = validar_entero("¿Cuántos Vehículos desea insertar?: ")

    for i in range(1, cantidad + 1):
        print(f"\nDatos del automóvil {i}")
        marca = validar_cadena("Inserte la marca del automóvil: ")
        modelo = validar_cadena("Inserte el modelo: ")
        ruedas = validar_entero("Inserte el número de ruedas: ")
        velocidad = validar_entero("Inserte la velocidad en km/h: ")
        cilindraje = validar_entero("Inserte el cilindraje en cc: ")

        vehiculo = Vehiculo(marca, modelo, ruedas, velocidad, cilindraje)
        vehiculos.append(vehiculo)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i}: {vehiculo}")

if __name__ == "__main__":
    main()