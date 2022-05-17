"""

# Condicional IF

SI se_cumple_esta_condicion
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion
    instrucciones
else:
    otras instrucciones

# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores lógicos
and 
or
not

"""

# Ejemplo 1
from typing import TYPE_CHECKING


print("############### EJEMPLO 1 ###############")

color = "verde"

#color = input("¿Adivina cual es mi color favorito?")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto")

# Ejemplo 2
print("############### EJEMPLO 2 ###############")

year = 2020

#year = int(input("¿En que año estamos? "))

if year<2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3
print("############### EJEMPLO 3 ###############")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Europa":
        print(f"El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("############### EJEMPLO 4 ###############")

dia = 1
#dia = int(input("Introduce el numero del día de la semana : "))

"""
if dia==1:
    print("Es Lunes")
else:
    if dia ==2:
        print("Es Martes")
    else:
        if dia ==3:
            print("Es Miércoles")
        else:
            if dia ==4:
                print("Es Jueves")
            else:
                if dia ==5:
                    print("Es viernes")
                else:
                    print("Es fín de semana")
"""

if dia==1:
    print("Es lunes")
elif dia==2:
    print("Es martes")
elif dia ==3:
    print("Es miércoles")
elif dia==4:
    print("Es jueves")
elif dia==5:
    print("Es viernes")
else:
    print("Es fina de semana")

# Ejemplo 5
print("############### EJEMPLO 5 ###############")


edad_minima = 18
edad_maxima =65
#edad_oficial = int(input("¿tienes edad de trabajar Introduce tu edad: "))
edad_oficial = 18

if edad_oficial>= 18 and edad_oficial<=65:
    print("Esta en edad de trabajar !!")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("############### EJEMPLO 6 ###############")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} No es un pais de habla hispana")

# Ejemplo 7
print("############### EJEMPLO 7 ###############")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO un pais de habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")

# Ejemplo 8
print("############### EJEMPLO 8 ###############")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO un pais de habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")


