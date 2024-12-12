#parte 3 csv
from automovil import Automovil, Particular, Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
import csv

def solicitar_entero(mensaje):
    """Solicita un entero al usuario con validación de errores."""
    while True:
        try:
            valor = input(mensaje)
            if valor.lower() == 'undo':
                return 'undo'
            valor = int(valor)
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

def guardar_vehiculos(vehiculos, nombre_archivo):
    """Guarda una lista de vehículos en un archivo CSV."""
    if not vehiculos:
        print("No hay vehículos para guardar.")
        return

    try:
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            campos = list(vehiculos[0].to_dict().keys())
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()
            for vehiculo in vehiculos:
                writer.writerow(vehiculo.to_dict())
        print(f"Datos guardados en {nombre_archivo} correctamente.")
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")

def leer_vehiculos(nombre_archivo):
    """Lee vehículos desde un archivo CSV."""
    vehiculos = []
    try:
        with open(nombre_archivo, 'r') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                tipo = fila.get('tipo')
                if tipo == 'Automovil':
                    vehiculo = Automovil(fila['marca'], fila['modelo'], int(fila['nro_ruedas']), int(fila['velocidad']), int(fila['cilindrada']))
                elif tipo == 'Particular':
                    vehiculo = Particular(fila['marca'], fila['modelo'], int(fila['nro_ruedas']), int(fila['velocidad']), int(fila['cilindrada']), int(fila['nro_puestos']))
                elif tipo == 'Carga':
                    vehiculo = Carga(fila['marca'], fila['modelo'], int(fila['nro_ruedas']), int(fila['velocidad']), int(fila['cilindrada']), int(fila['peso_carga']))
                elif tipo == 'Bicicleta':
                    vehiculo = Bicicleta(fila['marca'], fila['modelo'], int(fila['nro_ruedas']), fila['tipo_bici'])
                elif tipo == 'Motocicleta':
                    vehiculo = Motocicleta(fila['marca'], fila['modelo'], int(fila['nro_ruedas']), fila['tipo_bici'], int(fila['nro_radios']), fila['cuadro'], fila['motor'])
                else:
                    continue
                vehiculos.append(vehiculo)
        print(f"Datos leídos de {nombre_archivo} correctamente.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
    return vehiculos