### Unidad 3 (Estructuras de Datos Basicas) ###

## tuple (Tupla)

# Definición
'''
Una tupla es una colección ordenada de elementos (matriz), de cualquier dimensión, que no puede ser modificada ni redimensionada. 
Los elementos pueden repetirse y pueden ser de cualquier tipo de datos. Es, en efecto, práctica una lista no modificable.
'''

# Inicialización
tupla = tuple(2, 3, '3f', "uwu")

# Operaciones
''' Acceso por índice '''
i1 = tupla[0]

''' Obtener una subtupla '''
subTupla = tupla[2:5]

''' Concatenación de tuplas '''
tupla2 = tupla + (4, 5, 9, 'hola')

''' Obtener la longitud de una tupla '''
longitud = len(tupla)

''' Duplicación del contenido '''
tupla3 = tupla * 2

''' Verifica si un valor está en la tupla, retorna True o False '''
a = 1 in tupla

# Métodos
'''
Las tuplas tienen menos métodos que las listas debido a su inmutabilidad.

index(x) – Retorna el índice del primer elemento igual a x.
count(x) – Retorna la cantidad de veces que x aparece en la tupla.
'''
