""" 2.3.	Programar las funciones areaCirc, areaCuad y areaNegra .
areaCirc recibe como parámetro el radio de un círculo y calcula y retorna el área del mismo. areaCuad recibe como parámetro el lado de un cuadrado y calcula y retorna el área del mismo.
areaNegra recibe como parámetro el lado de un cuadrado de una figura (como la dada a continuación) y calcula y retorna el área negra resultante.
Luego utilizar las funciones en un programa que solicitará al usuario el lado del cuadrado y mostrará por pantalla el valor correspondiente para el área de color negra (Ver figura) y además indicará el porcentaje que éste área representa con respecto al área total del cuadrado. """

import math


x = float(input("Ingrese numero : "))

def areaCirc (radio):
    return math.pi * (radio * radio)
    
def areaCuad (lado):
    return lado * lado

def areaBlanca(lado):
    radioChi= (lado/3)/2
    radioG= ((lado/3)*2)/2
    aCir= 2*(areaCirc(radioChi))+areaCirc(radioG)
    return aCir
    
def areaNegra (lado):
    diG= lado *2/3
    diC= lado *1/3
    area= areaCuad(lado)- areaCirc(diG/2)- (2* areaCirc(diC/2))
    return area

aNegra = areaNegra(x)
aBlanca = areaBlanca(x)
aNegraPorc = (aNegra/(aBlanca+aNegra))*100

aNegraStr = "{:.2f}".format (aNegra)
aNegraPorcStr = "{:.2f}". format (aNegraPorc)
print("")

print("El area negra es ", aNegraStr, end="")
print(" y es un " + aNegraPorcStr +
"% del area total del cuadrado",end="")

 


