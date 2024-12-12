# PruebaM4_Python2_SistemaControVehiculos

*** 1era PARTE:
# Diagrama de Clases - Parte1

#PruebaPython2/
Parte1
├── vehiculo.py
├── automovil.py
├── utilidades.py
└── main.py

Parte2/
├── vehiculo.py
├── automovil.py
├── bicicleta.py
├── motocicleta.py
├── utilidades.py
└── main.py

Parte3/
├── vehiculo.py
├── automovil.py
├── bicicleta.py
├── motocicleta.py
├── utilidades.py   #CSV funciones para leer y guardar datos en archivo
└── main.py   # CSV isinstance

--------------------------------------------------------------------------------------------------------------------------------------

@startuml
skinparam style strictuml

package Parte1 {
    class Vehiculo {
        - marca: str
        - modelo: str
        - nro_ruedas: int
        + __str__(): str
    }

    class Automovil {
        - velocidad: int
        - cilindrada: int
        + __str__(): str
    }

    class Utilidades {
        + solicitar_entero(mensaje: str): int
    }

    class Main {
        + main(): void
    }

    Vehiculo <|-- Automovil
}

package Parte2 {
    class Bicicleta {
        - tipo: str
        + __str__(): str
    }

    class Motocicleta {
        - nro_radios: int
        - cuadro: str
        - motor: str
        + __str__(): str
    }

    Vehiculo <|-- Bicicleta
    Bicicleta <|-- Motocicleta
}

package Parte3 {
    class CSV {
        + guardar_vehiculos(vehiculos: list, nombre_archivo: str): void
        + leer_vehiculos(nombre_archivo: str): list
    }

    CSV -[hidden]-> Vehiculo
    CSV -[hidden]-> Automovil
    CSV -[hidden]-> Bicicleta
    CSV -[hidden]-> Motocicleta
}

Automovil <|-- Particular
Automovil <|-- Carga


