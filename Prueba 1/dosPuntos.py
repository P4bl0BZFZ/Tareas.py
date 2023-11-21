import math #importamos math para la raiz

#Solicitamos al usuario los datos
pnt1x=float(input("Ingrese primer punto de X: "))
pnt1y=float(input("Ingrese primer punto de Y: "))
pnt2x=float(input("Ingrese segundo punto de X: "))
pnt2y=float(input("Ingrese segundo punto de Y: "))
#Realizamos la operacion
ptx=(pnt2x - pnt1x)**2
pty=(pnt2y - pnt1y)**2
resultXY=ptx + pty
dst=math.sqrt(resultXY)
#Damos el resultado
print("La distancia entre los dos puntos es de: ",dst)