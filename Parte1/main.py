#main.py 1era parte

from automovil import Automovil
from utilidades import solicitar_entero

def main():
    vehiculos = []

    while True:
        nro_vehiculos = solicitar_entero("Cuantos Vehiculos desea insertar: ")
        if nro_vehiculos == 'undo':
            break
        if nro_vehiculos > 0:
            break
        else:
            print("Por favor, ingrese un número mayor a cero.")

    for i in range(nro_vehiculos):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = solicitar_entero("Inserte el número de ruedas: ")
        if nro_ruedas == 'undo':
            break
        velocidad = solicitar_entero("Inserte la velocidad en km/h: ")
        if velocidad == 'undo':
            break
        cilindrada = solicitar_entero("Inserte el cilindraje en cc: ")
        if cilindrada == 'undo':
            break

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i}: {vehiculo}")

if __name__ == "__main__":
    main()