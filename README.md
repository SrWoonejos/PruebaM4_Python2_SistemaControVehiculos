# PruebaM4_Python2_SistemaControVehiculos

*** 1era PARTE:
# Diagrama de Clases (Descripción en texto)

# Clase Vehiculo
# ----------------
# - Atributos:
#   - marca (str): Marca del vehículo.
#   - modelo (str): Modelo del vehículo.
#   - ruedas (int): Número de ruedas.
#   - velocidad (int): Velocidad máxima en km/h.
#   - cilindraje (int): Cilindraje en cc.
# - Métodos:
#   - __init__: Constructor para inicializar un objeto Vehiculo.
#   - __str__: Devuelve una representación en cadena de los datos del vehículo.

# Relaciones:
# - El módulo "main" utiliza instancias de la clase Vehiculo.
# - El módulo "validadores" asegura que los datos ingresados sean válidos.


*** Diagrama de Clases 2DA PARTE(UML)

Vehiculo
---------
- marca
- modelo
- ruedas
+ __init__()
+ __str__()

  / \
 /   \
/     \
Automovil
---------
- velocidad
- cilindraje
+ __init__()
+ __str__()

  / \
 /   \
/     \
Particular            Carga
---------            --------
- puestos            - peso
+ __init__()          + __init__()
+ __str__()           + __str__()

Bicicleta
---------
- tipo
+ __init__()
+ __str__()

  / \
 /   \
/     \
Motocicleta
-----------
- nro_radios
- cuadro
- motor
+ __init__()
+ __str__()


*** 3ERA PARTE

