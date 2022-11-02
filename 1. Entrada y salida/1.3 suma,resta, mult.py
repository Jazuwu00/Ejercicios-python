'''1.3 desarrollar un programa que solicite el ingreso por teclado de dos numeros enteros. luego el programa debera mostrar por pantalla el resultado de sumar,restar, multiplicar y dividir dichos numeros ingresados'''

x = int( input("Ingrese numero 1: "))
z = int( input("Ingrese numero 2: "))

suma= x+z
resta= x-z
multiplicacion= x*z
division=x//z

print("Los resultados para ", x ," y ",z," son: ")
print("La suma: ",suma,"\nLa resta: ",resta,"\nLa multipicacion: ",multiplicacion,"\nLa division: ", division)