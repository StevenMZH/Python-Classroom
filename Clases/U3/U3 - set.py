### Unidad 3 (Estructuras de Datos Basicas) ###

## set (Conjunto)

# Definición
'''
Un set es una colección desordenada de elementos únicos (sin duplicados). Los elementos dentro de un set deben ser inmutables, 
pero el propio set es mutable (puede modificarse).
'''

# Inicialización
conjunto = set()
A = {1, 2, 3}
B = {4, 5, 6}

# Operaciones
''' Unión (La suma de los 2 conjuntos) (A OR B) '''
C = A | B

''' Intersección (Retorna los elementos que están en ambos sets) (A AND B) '''
C = A & B

''' Diferencia (Retorna los valores que están en A y no en B) '''
C = A - B

''' Diferencia Simétrica (Retorna los valores que estén solamente en A o solamente en B) (A XOR B) '''
C = A ^ B

''' Verifica si un valor está en el set, retorna True o False '''
a = 1 in A

# Métodos
'''
    add(x) – Agrega el elemento x al set.
    remove(x) – Elimina el elemento x (lanza un error si no existe).
    discard(x) – Elimina el elemento x si existe (no lanza error si no está presente).
    pop() – Elimina y retorna un elemento arbitrario del set.
    clear() – Elimina todos los elementos del set.
    copy() – Retorna una copia superficial del set.
'''
