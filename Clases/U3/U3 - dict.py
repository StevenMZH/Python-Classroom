### Unidad 3 (Estructuras de Datos Basicas) ###

## dict (Diccionario/Tablas Hash)

# Definición
'''
Un diccionario es una colección desordenada de pares clave-valor. Las claves deben ser inmutables y únicas, 
mientras que los valores pueden ser de cualquier tipo.
'''

# Inicialización
diccionario = dict()
diccionario = {"key1": "value1", "key2": "value2"}

# Operaciones
''' Acceso de un valor por su clave '''
a = diccionario["key1"]

''' Modificación del valor de una clave '''
diccionario["key1"] = 23

''' Eliminar un key:value '''
del diccionario["key1"]

''' Verificar si existe una clave, retorna True o False '''
a = "key1" in diccionario

# Métodos
'''
    get(key) – Retorna el valor asociado a la clave key (retorna None si la clave no existe).
    keys() – Retorna un objeto con todas las claves del diccionario.
    values() – Retorna un objeto con todos los valores del diccionario.
    items() – Retorna una lista de pares clave-valor (tuplas).
    clear() – Elimina todos los elementos del diccionario.
    copy() – Retorna una copia superficial del diccionario.
''' 
