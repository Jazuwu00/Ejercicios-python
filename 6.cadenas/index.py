# Desarrollar un programa que permita realizar las operaciones de unién, interseccién y
# diferencia entre conjuntos. Los conjuntos estardn representados por listas. El programa
# deberd presentar un menu como se detalla a continuacién y al ingresar el valor, se
# ejecutard la opcién elegida.

# Ej: de presentacién de menti en pantalla
# 1. CARGAR CONJUNTOS
# 2. UNION
# 3. INTERSECCION
# 4. DIFERENCIA
# 5. DIFERENCIA SIMETRICA
# 6. SALIR

def cargarLstA(ls):
    ls.append(1)
    ls.append(3)
    ls.append(2)
    ls.append(5)
    ls.append(6)
    ls.append(7)

def cargarLstB(ls):
    ls.append(2)
    ls.append(4)
    ls.append(6)
    ls.append(8)
    ls.append(11)


def inter(lsA,lsB):
    res=[]
    for i in lsA:
        if i in lsB:
            res.append(i)

    return res

def union(lsA,lsB):
    res=[]+lsA
    for i in lsB:
        if i not in res:
            res.append(i)
    return res


def dif(lsA,lsB):
    res=[]+lsA
    for i in lsB:
        if i in res: 
            res.remove(i)
    return res



def difsim(lsA,lsB):
    res=[]

    

    return res 




def main():
    lsA=[]
    lsB=[]
    cargarLstA(lsA)
    cargarLstB(lsB)
    print("A:",lsA)
    print("B:",lsB)
    print("Interseccion:",inter(lsA,lsB))
    print("union:",union(lsA,lsB))
    print("DIF A-B",dif(lsA,lsB))
    print("DIF B-A",dif(lsB,lsA))
    print("DIF SIMETRICA",difsim(lsA,lsB))




main()