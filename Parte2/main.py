#PARTE 2 - PRUEBA FINAL PYTHON M4 - FULL STACK PYTHON 2024 - Daniela Miranda
from automovil import Automovil, Particular, Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from utilidades import solicitar_entero

def menu_vehiculo():
    print("\nSeleccione el tipo de vehículo:")
    print("1. Automóvil")
    print("2. Particular")
    print("3. Carga")
    print("4. Bicicleta")
    print("5. Motocicleta")
    return solicitar_entero("Ingrese el número correspondiente al tipo de vehículo: ")

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
        print(f"\nDatos del vehículo {i + 1}")
        tipo_vehiculo = menu_vehiculo()

        marca = input("Inserte la marca del vehículo: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = solicitar_entero("Inserte el número de ruedas: ")
        if nro_ruedas == 'undo':
            break

        if tipo_vehiculo in [1, 2, 3]:  # Automóvil, Particular, Carga
            velocidad = solicitar_entero("Inserte la velocidad en km/h: ")
            if velocidad == 'undo':
                break
            cilindrada = solicitar_entero("Inserte el cilindraje en cc: ")
            if cilindrada == 'undo':
                break

            if tipo_vehiculo == 2:  # Particular
                nro_puestos = solicitar_entero("Inserte el número de puestos: ")
                if nro_puestos == 'undo':
                    break
                vehiculo = Particular(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos)

            elif tipo_vehiculo == 3:  # Carga
                peso_carga = solicitar_entero("Inserte el peso de la carga en kg: ")
                if peso_carga == 'undo':
                    break
                vehiculo = Carga(marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga)

            else:  # Automóvil
                vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)

        elif tipo_vehiculo == 4:  # Bicicleta
            tipo_bici = input("Inserte el tipo de bicicleta (Urbana, Carrera): ").capitalize()
            vehiculo = Bicicleta(marca, modelo, nro_ruedas, tipo_bici)

        elif tipo_vehiculo == 5:  # Motocicleta
            tipo_bici = input("Inserte el tipo de bicicleta (Urbana, Carrera): ").capitalize()
            nro_radios = solicitar_entero("Inserte el número de radios: ")
            if nro_radios == 'undo':
                break
            cuadro = input("Inserte el tipo de cuadro: ")
            motor = input("Inserte el tipo de motor: ")
            vehiculo = Motocicleta(marca, modelo, nro_ruedas, tipo_bici, nro_radios, cuadro, motor)

        else:
            print("Tipo de vehículo no reconocido.")
            continue

        vehiculos.append(vehiculo)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del vehículo {i}: {vehiculo}")

    # Verificar relaciones utilizando isinstance
    for vehiculo in vehiculos:
        if isinstance(vehiculo, Automovil):
            print(f"{vehiculo} es un Automovil")
        if isinstance(vehiculo, Particular):
            print(f"{vehiculo} es un Automovil Particular")
        if isinstance(vehiculo, Carga):
            print(f"{vehiculo} es un Automovil de Carga")
        if isinstance(vehiculo, Bicicleta):
            print(f"{vehiculo} es una Bicicleta")
        if isinstance(vehiculo, Motocicleta):
            print(f"{vehiculo} es una Motocicleta")

if __name__ == "__main__":
    main()
