""" 2.4.Programar una función aleatorio que reciba como parámetros 2 números naturales y retorne un número natural al azar comprendido entre estos 2 números (inclusive), pasados por parámetro. Debe asumirse que esta función será invocada de manera que el primer parámetro representa el límite inferior del intervalo y el segundo el límite superior.
En un programa solicitar al usuario el ingreso de los límites del intervalo e invoque a la función aleatorio tres veces de la siguiente manera:
a.	Invocarla con los extremos del intervalo ingresados por el usuario y mostrar en pantalla el valor generado.
b.	Invocarla como en el punto anterior (a), pero usando como extremo inferior el valor generado en el punto anterior (a). c. Invocarla como en el punto anterior (b), pero usando como extremo superior el valor generado en el punto anterior (b). """
from random import randint


x = int(input("Ingrese el limite inferior (numero natural) : "))
y = int(input("Ingrese el limite superior (numero natural) : "))

def aleatorio(x,y):

    return randint(x, y)


def limite(x,y):
    for i in range(3):
       r=aleatorio(x,y)
       print(i+1 ,"-Límite inferior",x,", limite superior ", y, ". Numero generado :",r)
       if i==1 :
        y=r
       else:
        x=r
    
       
       


print (limite(x,y))