"""Desarrollar una función booleana que reciba como parámetros tres números enteros positivos que representan el día, el mes y el año de una fecha. La función deberá ret|nar True si la fecha es válida caso contrario deberá ret|nar False.
Desde el programa principal ingresar p| teclado el día, mes y año p| separado, invocar a la función y mostrar p| pantalla un mensaje indicando si "la fecha es c|recta" o "la fecha es inc|recta, dependiendo del caso.
Ayuda: Un año es bisiesto si es múltiplo de 4 y no de 100, o es múltiplo de 400. P| ejemplo el año 2000 es bisiesto pero el 1800 no lo es.
"""

d = int(input("Ingrese el día:"))
m = int(input("Ingrese el mes:"))
a = int(input("Ingrese el anio:"))


def fecha(d,m,a):


    res=False

    if m==2 :
        if  d>0 and d<=28:
             res=True
        elif d==29 and (a%4==0 and a%100!=0 or a%400==0):
             res= True
        else:
             res=False


    if m == 1 | m == 3 | m == 5 | m == 7 | m == 8 | m == 10 | m == 12 and( d>=1 and d<=31):
        res=True
    
     
    if m==4 | m==6 | m==9 | m==11  and( d>0 and d<=30):
         res=True
 

    return res



def main():
    if fecha(d,m,a):
        print(d ,"/",m,"/",a, " es corecta")
    else:
        print(d ,"/",m,"/",a, " es incorrecta")

main()