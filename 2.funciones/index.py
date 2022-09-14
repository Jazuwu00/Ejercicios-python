'''2.1 Desarrollar una funcion convertir que recibe por parametros un valor numerico entero, el cual representa una cantidad expresada en segundos. 
la funcion debera convertir el valor en segundos. la funcion debera convertir el valor en segundos a (dias,horas,minutos y segundos) e imprimirlo como muestra el ejemplo
utilizar la funcion en un programa que solicitara al usuario el ingreso de numeros enteros y naturak, que representa un valor en segundo; 
luego invocar convertir para obtener el resultado como muestra el ejemplo
'''

'''ej: 
    Ingrese tiempo en segundos: 93714
    1 dia(s), 2 horas(s), 1 minuto(s), 54 segundos (s).'''
    
    
# x = int(input("Ingrese numero : "))
# def convertir (x):
#     dias = x // (24*60*60)
#     x =x % (24*60*60)
#     horas= x //(60*60)
#     x =x % (60*60)
#     minutos= x//60
#     x=x % 60
#     return print( '{} dia(s), {} Hora(s), {} minuto(s), {} segundo(s)'.format(dias,horas,minutos,x))

# convertir(x)

'''
2.2
Desarrollar la funcion producto que recibe por parametro dos numeros enteros y naturales de 3 cifras. la funcion sera utilizada con fines didacticos a fin de mostrar
el metodo para obtener el resultado de un producto de numeros. se pide que la funcion muestre por pantalla los pasos y calculos intermedios de la multipicacion tal como
se hacen sobre una hoja de papel, respetando exactamente las alineaciones y forma para la salida como bien se ilustra en el ejemplo de salida. 
utilizar la funcion en un programa que solicitara al usuario el ingreso de dos numeros enteros y naturales, luego invocar a la funcion producto pasado por parametros 
dichos numeros ingresados.'''







from cmath import pi
import math

# x = int(input("Ingrese el multiplicando : "))

# y = int(input("Ingrese el multiplicador : "))


#  while True: 
#      if x>99 and x < 1000 and y> 99 and y < 1000:
#          break;
#      print('Ingrese valores entre 100 y 1000')
#      x = int(input("Ingrese el multiplicando : "))
#      y = int(input("Ingrese el multiplicador : "))



#  def producto(x, y):
#     restultado=x * y
    
#      return print( ' {:8d}'.format(x) ,'\n*{:8d}'.format(y) ,'\n----------\n', '{:8d}'.format(restultado))
     
#  producto(x,y)


""" 2.3.	Programar las funciones areaCirc, areaCuad y areaNegra .
areaCirc recibe como parámetro el radio de un círculo y calcula y retorna el área del mismo. areaCuad recibe como parámetro el lado de un cuadrado y calcula y retorna el área del mismo.
areaNegra recibe como parámetro el lado de un cuadrado de una figura (como la dada a continuación) y calcula y retorna el área negra resultante.
Luego utilizar las funciones en un programa que solicitará al usuario el lado del cuadrado y mostrará por pantalla el valor correspondiente para el área de color negra (Ver figura) y además indicará el porcentaje que éste área representa con respecto al área total del cuadrado. """

def areaCirc (radio):
    return math.pi * (radio * radio)
    
def areaCuad (lado):
    return lado * lado
    
def areaNegra (lado):
    diG= lado *2/3
    diC= lado *1/3
    area= areaCuad(lado)- areaCirc(diG/2)- (2* areaCirc(diC/2))
    return area

print("El area negra es " , areaNegra(12) , "% y es un " ,( ),"% del area total del cuadrado" );