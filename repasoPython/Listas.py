#LISTAS
"""se utilizan para almacenar varios elementos en una sola variable."""

print("LISTA")

animales = ["perro", "gato", "caballo"]
print(animales[2])
#len
print("LEN")
"determina cuantos elementos tiene la lista"
print("cantidad de elementos que tiene la lista : ", len(animales))

#append
print("APPEND")
"""agrega un elemento al final de la lista
"""
animales.append("oveja")
print(animales)

#INSERT
print("INSERT")
"""inserta un elemento a la lista en determinado indice """
list_numeros = [1,2,4,5]
list_numeros.insert(2,3)
print(list_numeros)

#EXTEND
print("EXTEND")
"""Agregar varios elementos a la lista"""
list_num = [1,2,3]
list_num.extend([4,5,6])
print(list_num)

#CONCATENAR 2 LISTAS
print("CONCATENAR 2 LISTAS")
"""permite concatenar 2 listas """
lista1 = [1,2,3]
lista2 = [4,5,6]

lista3 = lista1+lista2
print(lista3)

print("IN")
"""consultar si determinado elemento pertenece a la lista true o false"""
lista = [1,2,3,"nata"]
print(3 in lista)

#INDICE DE UN ELEMTO
print("INDEX")
"""consultar el indice del elemento a consultar"""
print
#CONTAR
print("COUNT")
"""las listas permiten elemntos repetidos , count nos cuenta cuantas veces esta el elemento en la lista"""
lista = [1,2,3,2,2,3,"nata"]
print(lista.count(2))

#ELIMINAR ELEMNTOS DE LA LISTA
print("POP")
"""ELIMINA EL ULTIMO ELEMNTO DE LA LISTA SI DENTRO DE LOS PARENTESIS NO TIENE PARAMETRO
O TAMBIEN SE LE PUEDE PASAR COMO PARAMETRO LA POSICION DEL ELEMENTO
"""
lista.pop()
"PASANDOLE EL INDICE A ELIMINAR"
lista.pop(2)
print(lista)

#REMOVE
"""REMOVE- permite eliminar el elemento sin necesidad de saber el index"""
print("REMOVE")
lista.remove(1) #se le pasa el valor a eliminar
print(lista)

#CLEAR
print("CLEAR")
"""CLEAR - ELIMINA TODOS LOS ELEMENTOS DE LA LISTA"""
lista.clear()
print(lista)

#SORT
print("SORT")
"permite ordenar una lista de enteros desordenada de forma ascendente"
list_num_desorden = [2,3,4,6,1,5]
list_num_desorden.sort()
print(list_num_desorden)

"""ordenar de forma descendente"""
list_num_desorden = [2,3,4,6,1,5]
list_num_desorden.sort(reverse=True)
print(list_num_desorden)

#copy
"""para hacer una copia de la lista se puede mediante el metodo copy o list"""
print("COPY")
lista_copia = list_num_desorden.copy()
print(lista_copia)

#unir listas
print("UNIR DOS LISTAS +")
"""se emplea el operador + para unir 2 listas"""

lista_1 = ['A','B','C']
lista_2 = ['a','e','i']

lista_3 = lista_1+lista_2
print(lista_3)