"""
Ejercicio3. Escribir un programa que muestre los cuadrados
(un numero multipicado por si mismo) de los 60 primeros numeros 
naturales. Resolverlo con for y con while

"""

# WHILE

contador=0
while contador<=60:
    print(f"El cuadrado de {contador} es {contador*contador}")
    contador +=1
else:
    print("Se termino")

# FOR

for numero in range(0,61):
    print(f"El cuadrado de {numero} es {numero*numero}")
else:
    print("Se termino")
