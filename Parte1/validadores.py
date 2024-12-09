# validadores.py
def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Inténtelo nuevamente.")

def validar_cadena(mensaje):
    while True:
        cadena = input(mensaje).strip()
        if cadena.isalpha():
            return cadena
        print("Error: Solo se permiten letras. Inténtelo nuevamente.")