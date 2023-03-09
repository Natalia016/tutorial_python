#tuplas :coleccion ordenada e inmutables no se pueden modificar  como las listas
#se describen con parentesism son mas rapidas al ejecutarlas
print ("tupla")
"""Las tuplas se utilizan para almacenar varios elementos en una sola variable."""
numeros =(1,2,3,4,5)
print(numeros)

print("Mostrar elementos pasandole el  indice")
#mostrar un solo elemto de la tupla pasandole el indice
print(numeros[1])

print("Mostrar ultimo elemento de la tupla (-1)")
print(numeros[-1])

print("slicing tupla")
""""Mostrar todos los elemento de la tupla desde la posicion 1 hasta el final"""
print(numeros[1:])

print("BUSQUEDA")
#buscar
"si el numero 2 esta en la tupla"
print(2 in numeros)

#index
""""buscamos el elemnto en la tupla que corresponda a la posición """
print("INDEX")
print(numeros.index(4))

#COUNT
""""Retorna el valor de las coincidencias en la tupla """
print("COUNT")
print(numeros.count(3))

#LEN
print("LEN")
"""nos permite sabver cuantos elementos tiene la tupla"""
print(len(numeros))


#covertir tuplas a listas
print("LIST")
tupla_v = ('a','e','i','o')
lista_t = list(tupla_v)
print(lista_t)


#covertir listas en tuplas
print("TUPLE")
lista_num =[1,2,3,4]
tupla_num = tuple(lista_num)
print(tupla_num)

#unir tuplas
print("UNIR DOS LISTAS +")
"""se emplea el operador + para unir 2 listas"""

tupla_1 = ['A','B','C']
tupla_2 = ['a','e','i']
tupla_3 = tupla_1 + tupla_2
print(tupla_3)