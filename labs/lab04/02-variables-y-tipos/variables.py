"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tengaa un dato distinto
"""

texto = "Máster en Python"
#texto = 1

texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------------------------")

numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("----------------------------------------")

#Concatenación
nombre = "Víctor"
apellidos = "Robles"
web = "victorrobles.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)