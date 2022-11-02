'''2.2
Desarrollar la funcion producto que recibe por parametro dos numeros enteros y naturales de 3 cifras. la funcion sera utilizada con fines didacticos a fin de mostrar
el metodo para obtener el resultado de un producto de numeros. se pide que la funcion muestre por pantalla los pasos y calculos intermedios de la multipicacion tal como
se hacen sobre una hoja de papel, respetando exactamente las alineaciones y forma para la salida como bien se ilustra en el ejemplo de salida. 
utilizar la funcion en un programa que solicitara al usuario el ingreso de dos numeros enteros y naturales, luego invocar a la funcion producto pasado por parametros 
dichos numeros ingresados.'''


x = int(input("Ingrese el multiplicando : "))
y = int(input("Ingrese el multiplicador : "))

def producto(x, y):
  u=y%10
  d=(y//10)%10
  c=(y//100)%100
  restultado=x * y
  print ("{:10d}".format(x) )
  print ("x{:>9d}".format(y))
  print("{:->10s}".format(""))
  print("{:10d}". format (x*u) )
  print ("{:=#9d}{:->1}". format ((x*d) ,""))
  print ("{:>8d}{:->2}". format ((x*c),""))
  print ("{:->10s}".format(""))
  print ("{:10d}".format(restultado,""))

 

   
     
producto(x,y)
