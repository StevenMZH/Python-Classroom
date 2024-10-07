### Unidad 3 (Estructuras de Datos Basicas) ###

## list (Lista)
        
#Definicion
'''
Una lista en Python, es una colección ordenada de elementos (matriz), de cualquier dimension, que pueden ser modificada y redimensionada.             
Los elementos pueden repetirse y pueden ser de cualquier tipo de datos. 
'''
        
#Inicializacion

lista = list()
lista = [1,2,5.4,'s',"._."]
        

# Operaciones

''' Acceso por indice '''
i1 = lista[0]

'''Obtener una sublista'''
subLista = lista[2:5]

'''Concatenacion de Listas'''
lista2 = lista + [4,5,9,'hola']

'''Obtener la longitud de una lista'''
longitud = len(lista)

'''duplicacion del contendo'''
lista3 = lista*2

'''Verifica si un valor esta en la lista, retorna True o False'''
a = 1 in lista

# Metodos
'''
append(x) – Agrega un elemento al final de la lista.
insert(i, x) – Inserta un elemento en una posición específica.
            
remove(x) – Elimina la primera aparición del elemento especificado.
pop(i) – Elimina y retorna el elemento en la posición especificada (por defecto el último).
clear() – Elimina todos los elementos de la lista.
            
index(x) – Retorna el índice del primer elemento igual a x.
count(x) – Retorna la cantidad de veces que x aparece en la lista.
sort() – Ordena la lista en su lugar.
reverse() – Invierte el orden de los elementos en la lista.
copy() – Retorna una copia superficial de la lista.
'''
