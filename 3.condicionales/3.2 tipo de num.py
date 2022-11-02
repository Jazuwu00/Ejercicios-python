""" 3.2. Desarrollar una función que reciba un número real como parámetro y que retorne un mensaje si el número es "positivo", "negativo" o "cero". Adicionalmente deberá desarrollar otra función, que retorne otro mensaje, si el número recibido es "entero natural", "entero" o "real". El programa principal deberá efectuar el ingreso de un número real e imprimir por pantalla los mensajes retornados por las funciones."""


x = int(input("Ingrese un numero : "))


def num(x):
    res=""
    if(x>0):
      res= "Positivo"
    elif(x<0):
      res= "Negativo"
    else:
      res= "Cero"

    return res

def tipo(x):
    if x==int(x) :
      if x>0:
        res="entero natural"
      else:
        res="entero"
    else:
      res= "real"

    return res
    
print("el numero ",x, " es ",num(x), " y ",tipo(x))