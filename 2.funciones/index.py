'''2.1 Desarrollar una funcion convertir que recibe por parametros un valor numerico entero, el cual representa una cantidad expresada en segundos. 
la funcion debera convertir el valor en segundos. la funcion debera convertir el valor en segundos a (dias,horas,minutos y segundos) e imprimirlo como muestra el ejemplo
utilizar la funcion en un programa que solicitara al usuario el ingreso de numeros enteros y naturak, que representa un valor en segundo; 
luego invocar convertir para obtener el resultado como muestra el ejemplo
'''

'''ej: 
    Ingrese tiempo en segundos: 93714
    1 dia(s), 2 horas(s), 1 minuto(s), 54 segundos (s).'''
    
    
x = int(input("Ingrese numero : "))
def convertir (x):
    dias = x // (24*60*60)
    x =x % (24*60*60)
    horas= x //(60*60)
    x =x % (60*60)
    minutos= x//60
    x=x % 60
    return print( '{} dia(s), {} Hora(s), {} minuto(s), {} segundo(s)'.format(dias,horas,minutos,x))

convertir(x)