temperaturas=[]
canttemp= 0
smtm=0 #Suma de las temperaturas
tmmbj=float('inf')#Temperatura mas baja
tmmal=float('-inf')#Temperatura mas alta
tmpfdr= 0 #Temperaturas fuera del rango

while True:
    temp=int(input("Ingrese las temperaturas (ingrese 888 al terminar): "))
    if temp==888:
        break
    canttemp+=1
    smtm+=temp
    if temp<tmmbj:
        tmmbj=temp
    if temp>tmmal:
        tmmal=temp
    if temp<50 or temp>80:
        tmpfdr+=1
    temperaturas.append(temp)

promtemp=smtm/canttemp

print("Sus resultados son: ")
print("1.Cantidad de temperaturas ingresadas:",canttemp)
print("2.Promedio de temperaturas:",promtemp,"grados")
print("3.Temperatura más baja:",tmmbj,"grados")
print("4.Temperatura más alta:",tmmal,"grados")
print("5.Cantidad de temperaturas fuera del margen de normalida entre 50 y 80 grados:",tmpfdr)