# ESTRUCTURAS SELECTIVAS

"""
son sentencias q nos permiten elegir dos o mas opciones, evaluando los criterios
"""
# CONDICIONAL SIMPLE IF
"""se ejecuta si se cumple la condición"""

print("CONDICIONAL SIMPLE IF")
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
if num1 >= num2:
    print("el " , num1 , " es mayor igual a ", num2)


# CONDICIONAL DOBLE IF-ELSE
"""
ejecuta las intrucciones cuando se cumple la condición y otras 
cuando no se cumple
"""
print("CONDICIONAL DOBLE IF-ELSE")
edad = int(input("Ingresa tu edad : "))
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

#CONDICIONAL MULTIPLE
"""Ejecuta multiples condiciones  de forma jerarquica
por ejemplo si no se cumple la primera condición 
se evalúa la siguiente condición y así sucesivamente."""

print("CONDICIONAL MULTIPLE")
edad = int(input("Ingresa tu edad : "))
if edad >= 18:
    print("Eres mayor de edad")
elif edad < 0:
    print("Imposible tener una edad negativa")
else:
    print("Eres menor de edad")

#CONDICIONAL ANIDADA
"""La principal se trata de una estructura condicional compuesta y
la segunda es una estructura condicional simple y está contenida por 
la rama del falso de la primer estructura."""

print("CONDICIONAL ANIDADA")
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

if num1 > num2:
    if num1 > num3:
        print("el numero mayor es", num1)
    else:
        print("el numero mayor es", num3)
else:
    if num2 > num3:
       print("el numero mayor es", num2)
    else:
        print("el numero mayor es",num3)


# ESTRUCTURAS REPETITIVAS
# ESTRUCTURA REPETITIVA WHILE
"""
ejecuta las intrucciones mientras la condición sea verdadera.
"""
print("ESTRUCTURAS REPETITIVAS WHILE")#muestra los numeros mientras j sea menor a 8
j = 1
while j < 8:
  print(j)
  j += 1

# ESTRUCTURA REPETITIVA FOR
"""se usa para iterar sobre una secuencia """
print("ESTRUCTURA REPETITIVA FOR")


num=int(input("Ingrese un numero: "))
for x in range(1,11):
    tabla=num*x
    print(num, "x", x ,"=",tabla)
