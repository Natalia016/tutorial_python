#DICCIONARIO
""" es una colección ordenada, modificable y que no admite duplicados. ,  
se utilizan para almacenar valores de datos en pares clave:valor. corchetes"""

#crear diccionario
diccionario_vehi = { "marca" : "ford" , "modelo" :"2020", "color" : "rojo"}
print(diccionario_vehi)

# mostrar un elemento del diccionario
print("MOSTRAR ELEMENTO POR CLAVE")
print(diccionario_vehi["marca"])

#COPIAR
""""""
print("COPY")
dic_copia=diccionario_vehi.copy()
print(dic_copia)

#COPIAR con dict
""""""
print("DICT PARA COPIAR EL DICCIONARIO")
dic_copia=dict(diccionario_vehi)
print(dic_copia)

#KEYS
#AGREGAR UNA CLAVE AL DICCIONARIO
print("KEYS-AGREGAR ELEMNTO AL DICCIONARIO")
x = diccionario_vehi.keys()
print(x) #antes del cambio
diccionario_vehi["km"]= 20000
print(x) #despues de agredar cambio

#MOSTRAR TODAS LAS CLAVES  DEL DICCIONARIO
print("KEYS- MOSTRAR TODAS LAS CLAVES")
print(diccionario_vehi.keys())

#VALUES
print("VALUES-MODIFICAR EL VALOR A  ELEMENTO DEL DICCIONARIO ")

x = diccionario_vehi.values()
print(x) #antes del cambio
diccionario_vehi["color"]= "azul"
print(x) #despues de agredar cambio

#UPDATE
print("UPDATE")
diccionario_vehi.update({"color": "violeta"})
print(diccionario_vehi)

#pop
""""elimina clave del diccionario"""
print("POP")
vehi = { "marca" : "twingo" , "modelo" :"2000", "color" : "rojo"}
print(vehi)
vehi.pop("modelo")
print(vehi)

#MOSTRAR TODAS LAS CLAVES  DEL DICCIONARIO
print("VALUES- MOSTRAR TODOS LOS VALORES")
print(diccionario_vehi.values())
#ITEMS
"""El items() método devolverá cada elemento en un diccionario, como tuplas en una lista."""
print("ITEMS")
x = diccionario_vehi.items()
print(x) #antes del cambio
diccionario_vehi["color"]= "negro"
print(x) #despues de agregar cambio

#del
print("DEL - ELIMINAR CLAVE")
"""eliminar elementos del diccionario"""
del (diccionario_vehi["modelo"])
print(diccionario_vehi)

#GET
"""permite mostrar los elementos del valor que pertence a la clave
si no existe dentro del diccionario aparece mensaje no error"""

print("GET")
print(diccionario_vehi.get("motor","no existe motor del vehiculo"))

#BUSQUEDA DIRECTA DENTRO DEL DICCIONARIO
print("IN")
print("motor" in diccionario_vehi)

#VACIAR EL DICCIONARIO
print("CLEAR")
diccionario_vehi.clear()
print(diccionario_vehi)

#diccionario anidado
print("DICCIONARIO ANIDADO")
dic_vehiculos = {
  "carro1" : {
    "marca" : "ford",
    "modelo" : 2022,
    "color": "blanco"
  },
  "carro2" : {
    "marca" : "chevrolet",
    "modelo" : 2004,
    "color": "verde"
  },
  "carro3" : {
      "marca": "twingo",
      "modelo": 2000,
      "color": "azul"
  }

}
print(dic_vehiculos)