#parte 3 csv - main.py
from automovil import Automovil, Particular, Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from utilidades import solicitar_entero, guardar_vehiculos, leer_vehiculos

def menu_vehiculo():
    """Muestra el menú de selección de vehículos."""
    print("\nSeleccione el tipo de vehículo:")
    print("1. Automóvil")
    print("2. Particular")
    print("3. Carga")
    print("4. Bicicleta")
    print("5. Motocicleta")
    print("6. Terminar y guardar")
    return solicitar_entero("Ingrese el número correspondiente al tipo de vehículo: ")

def main():
    vehiculos = []
    while True:
        try:
            tipo_vehiculo = menu_vehiculo()
            if tipo_vehiculo == 'undo':
                print("Operación deshecha.")
                continue

            if tipo_vehiculo == 6:
                guardar_vehiculos(vehiculos, "vehiculos.csv")
                print("Gracias por preferirnos. ¡Hasta la próxima!")
                break

            marca = input("Inserte la marca del vehículo: ")
            modelo = input("Inserte el modelo: ")
            nro_ruedas = solicitar_entero("Inserte el número de ruedas: ")
            if nro_ruedas == 'undo':
                continue

            if tipo_vehiculo in [1, 2, 3]:
                velocidad = solicitar_entero("Inserte la velocidad en km/h: ")
                if velocidad == 'undo':
                    continue
                cilindrada = solicitar_entero("Inserte el cilindraje en cc: ")
                if cilindrada == 'undo':
                    continue

                if tipo_vehiculo == 2:
                    nro_puestos = solicitar_entero("Inserte el número de puestos: ")
                    if nro_puestos == 'undo':
                        continue
                    vehiculo = Particular(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos)
                elif tipo_vehiculo == 3:
                    peso_carga = solicitar_entero("Inserte el peso de la carga en kg: ")
                    if peso_carga == 'undo':
                        continue
                    vehiculo = Carga(marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga)
                else:
                    vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)

            elif tipo_vehiculo == 4:
                tipo_bici = input("Inserte el tipo de Bicicleta (Urbana, Carrera): ").capitalize()
                vehiculo = Bicicleta(marca, modelo, nro_ruedas, tipo_bici)

            elif tipo_vehiculo == 5:
                nro_radios = solicitar_entero("Inserte el número de radios: ")
                if nro_radios == 'undo':
                    continue
                cuadro = input("Inserte el tipo de cuadro: ")
                motor = input("Inserte el tipo de motor: ")
                vehiculo = Motocicleta(marca, modelo, nro_ruedas, nro_radios, cuadro, motor)

            else:
                print("Tipo de vehículo no reconocido.")
                continue

            vehiculos.append(vehiculo)
            print("Vehículo agregado exitosamente.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del vehículo {i}: {vehiculo}")

    vehiculos_leidos = leer_vehiculos("vehiculos.csv")
    for vehiculo in vehiculos_leidos:
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