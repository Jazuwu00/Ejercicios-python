""" 3.1 . Desarrollar la función operar que reciba como parámetros dos números y un string con alguno de los seis caracteres (+ , / // , ** ) y retorne el resultado de la operación. Desde el programa principal el usuario ingresará los datos que serán pasados como parámetros a la función y mostrará el resultado retornado por la misma."""






def operar(x,y, op):
    res=0
    if(op =="+"):
      res=x + y 
    elif(op=="-"):
      res=x - y 
    elif(op=="/"):
      res=x / y 
    elif(op=="//"):
      res=x // y 
    elif(op=="**"):
      res=x ** y 
    else:
      res= None

    return res

def main():
  x = int(input("Ingrese el primer numero : "))
  y = int(input("Ingrese el segundo numero  : "))
  op= str(input("Ingrese la operacion(+,-,/,//,**): "))
  res=operar(x,y,op)
  if res!=None:
    print(x," ", op," ", y," = ",res)

main()