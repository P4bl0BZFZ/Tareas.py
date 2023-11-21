itth=int(input("Ingresos total de la familia: "))
cttp=int(input("Cantidad de pesonas en el hogar: "))
te=int(input("Cantidad de terera edad: "))

inpc=itth/cttp
print("Ingreso por capita",inpc)
if(te>=2):
    print("Usted pertenece a el tramo C3")
else:
    print("Usted pertenece a cualquier tramo C1, C2, C3 o AB")
    if cttp <=4:
        if inpc<=60000:
            print("Su grupo familiar pertenece a el tramo C3")
        elif inpc>60000 and inpc<=100000:
            print("Su grupo familiar pertenece a el tramo C2")
        elif inpc>100000 and inpc<=300000:
            print("Su grupo familiar pertenece a el tramo C1")
        elif inpc>300000:
            print("Su grupo familiar pertenece a el tramo AB")

    elif cttp>=5:
        if inpc<=40000:
            print("Su grupo familiar pertenece a el tramo C3")
        elif inpc>40000 and inpc<=80000:
            print("Su grupo familiar pertenece a el tramo C2")
        elif inpc>80000 and inpc<=250000:
            print("Su grupo familiar pertenece a el tramo C1")
        elif inpc>250000:
            print("Su grupo familiar pertenece a el tramo AB")
sigue=int(input("1:Sigue/2:Parar proceso: "))
