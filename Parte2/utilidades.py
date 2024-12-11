#PARTE2
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
