''''1.2. Desarrollar un programa que solicite por teclado dos lados de un rectangulo. luego calcular el perimetro y area del mismo. mostrar los resultados de la siguiente forma:
    Ingresar lado 1 : 20 
    ingresar lado 2 : 10
    
    area: 200
    perimetro:60 '''
    
x = int( input("Ingrese lado 1: "))
z = int( input("Ingrese lado 2: "))

area = x * z

perimetro = x*2 + z*2

print("Area : ",area  ,"\nPerimetro : ",perimetro )