''''1.1 Desarrollar un programa que solicite por pantalla (consola) el ingreso de un número entero. Luego el programa debe mostrar por pantalla (consola) el número ingresado.'''

#x = int( input("Ingrese un numero: "))

#print("El numero que ingreso fue :", x)


''''1.2. Desarrollar un programa que solicite por teclado dos lados de un rectangulo. luego calcular el perimetro y area del mismo. mostrar los resultados de la siguiente forma:
    Ingresar lado 1 : 20 
    ingresar lado 2 : 10
    
    area: 200
    perimetro:60 '''
    
# x = int( input("Ingrese lado 1: "))
# z = int( input("Ingrese lado 2: "))

# area = x * z

# perimetro = x*2 + z*2

# print("Area : ",area  ,"\nPerimetro : ",perimetro )

'''1.3 desarrollar un programa que solicite el ingreso por teclado de dos numeros enteros. luego el programa debera mostrar por pantalla el resultado de sumar,restar, multiplicar y dividir dichos numeros ingresados'''

# x = int( input("Ingrese numero 1: "))
# z = int( input("Ingrese numero 2: "))

# suma= x+z
# resta= x-z
# multiplicacion= x*z
# division=x//z

# print("Los resultados para ", x ," y ",z," son: ")
# print("La suma: ",suma,"\nLa resta: ",resta,"\nLa multipicacion: ",multiplicacion,"\nLa division: ", division)

'''1.4 Desarrollar un programa que solicite el ingreso de un numero real. Luego el programa debera mostrar la descomposicion del numero real en su parte entera y parte decimal'''

""" 
x = float(input("Ingrese numero : "))
entero=int(x)
decimal= x-int(x)

print("Los resultados para ",x, " son: ")
print("Parte entera: ",entero,"\nParte decimal: ",decimal)
 """
 




import random
def saludo(val):
    msjA="Hola"
    msjB="Chau"
    res= msjA*(val)+ msjB*(1-val)
    return res

def main():
    ale=random.randint(0,1)
    print(saludo(ale))
main()