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







x = int(input("Ingrese el multiplicando : "))

y = int(input("Ingrese el multiplicador : "))


while x < 99  :
    while y < 99:
        print('Ingrese valores entre 100 y 1000')
        x = int(input("Ingrese el multiplicando : "))
        y = int(input("Ingrese el multiplicador : "))



def producto(x, y):
    restultado=x * y
    
    return print( ' {:8d}'.format(x) ,'\n*{:8d}'.format(y) ,'\n----------\n', '{:8d}'.format(restultado))
     
producto(x,y)