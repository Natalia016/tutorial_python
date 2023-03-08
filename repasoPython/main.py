#TIPOS DE DATOS PRIMITIVOS
#NUMEROS ENTEROS

numero1:int =57
print(numero1)

numero2 = 24
print(numero2)

#NUMEROS REALES
numero3:float = 4.9
print(numero3)

numero4 =5.0
print(numero4)

#BOOLEANOS

esColombiano: bool = True
esArgentino = False
print(esColombiano)

#CARACTER Y CADENA DE CARACTERES
mensaje = "cadena con una comilla simple ',una comilla doble \" y una diagonal invertida\\"
print (mensaje)

#OPERADORES
#ARITMETICOS

numero5 = 9
numero6 = 12
suma = numero5 + numero6
multiplicacion = numero5 * numero6
resta = numero5 - numero6
division = numero5 / numero6
modulo = numero5 % numero6
print("la suma es : " , suma )
print("la multiplicación es :" , multiplicacion)
print("la resta es :" , resta)
print("la división es :" , division)
print("la modulo es :" , modulo)

#OPERADOR DE ASIGNACIÓN
x = 7
y = 8
z = 2
print(x)

#OPERADOR LOGICOS
#AND (Y)
q = 5
print(q > 4 and q < 9)

#OR (O)
p = 4
print(p > 5 or p < 10)

#NOT
print(not(p > 2 and q < 7))

#OPERADOR RELACIONALES
valor1 = 7
valor2 = 9

print(valor1 == valor2) #igualdad
print(valor1 > valor2) #mayor q
print(valor1 >= valor2) # mayor igual q
print(valor1 <= valor2) #menor igual q
print(valor1 != valor2) #no igual

#FUNCIONES
"""
Bloque de codigo que retornan un valor y solo se ejecutan
cuando se llaman
"""

def mi_funcion():
    print("hola Nata")
mi_funcion() #invocar la funcion

def mensaje(nombre): # se pueden pasar varios argumentso separado de coma y espacio
    print("Hola "+ nombre)

mensaje(" Natalia")

