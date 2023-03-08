# datos de entrada
base = 7
altura = 8

#procedimiento
""""se usan verbos en infinitivo"""
def calcularAreaTriangulo(b,h):
    area =(b * h) / 2
    return  area

#salida
"""la variable resultado guarda el valor que retorna la funcion"""
resultado = calcularAreaTriangulo(base, altura)
print("el area del triangulo es :", resultado)

"""
mismo ejercicio insertandole datos 
"""

# datos de entrada
base = float(input("ingrese la base :"))
altura = float(input("ingrese la altura :"))

#procedimiento
""""se usan verbos en infinitivo"""
def calcularAreaTriangulo(b,h):
    area =(b * h) / 2
    return  area

#salida
"""la variable resultado guarda el valor que retorna la funcion"""
resultado = calcularAreaTriangulo(base, altura)
print("el area del triangulo es :", resultado)


#FUNCION CON ARGUMENTOS POR DEFECTO
def mostrarPais(pais = "Colombia"):
    print("Yo soy de :" + pais)
mostrarPais("suiza")

#FUNCION CON ARGUMENTOS POR DEFECTO
"""
EJEMPLO 2
"""
def mostrarPais(pais = "Colombia"):
    print("Yo soy de :" + pais)
mostrarPais("suiza")
mostrarPais("Ecuador")
mostrarPais("")
mostrarPais("Brazil")