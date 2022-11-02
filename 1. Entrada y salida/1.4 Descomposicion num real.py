'''1.4 Desarrollar un programa que solicite el ingreso de un numero real. Luego el programa debera mostrar la descomposicion del numero real en su parte entera y parte decimal'''


x = float(input("Ingrese numero real: "))
entero=int(x)
decimal= x-int(x)

print("Los resultados para ",x, " son: ")
print("Parte entera: ",entero,"\nParte decimal: ",decimal)
 
 