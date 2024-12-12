#parte 3 csv

import csv

# Función para manejar entradas del usuario con validación
def solicitar_entero(mensaje):
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
        except OSError:
            print("Error de entrada/salida. Verifique el entorno de ejecución.")
            return 0

# Función para guardar datos en un archivo CSV
def guardar_vehiculos(vehiculos, nombre_archivo):
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

# Función para leer datos de un archivo CSV
def leer_vehiculos(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, 'r') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                tipo = fila['tipo']
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
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
    return vehiculos
