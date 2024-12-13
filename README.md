# PruebaM4_Python2_SistemaControVehiculos
# Diagrama de Clases

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

## Descripción del diagrama de clases
- `Vehiculo`: Clase base que define los atributos comunes como marca, modelo y número de ruedas.
- `Automovil`: Hereda de Vehiculo, añade atributos específicos como velocidad y cilindrada.
- `Bicicleta` y `Motocicleta`: Heredan de Vehiculo, cada una con atributos únicos.
- `CSV`: Maneja la lectura y escritura de datos en archivos CSV.

--------------------------------------------------------------------------------------------------------------------------------------
# Sistema de Control de Vehículos
## Estructura del Proyecto
- `Parte1/`: Base del sistema con clases `Vehiculo` y `Automovil`.
- `Parte2/`: Expande el sistema añadiendo `Bicicleta` y `Motocicleta`.
- `Parte3/`: Implementa funcionalidad de persistencia con CSV.

## Diagrama de Clases
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


