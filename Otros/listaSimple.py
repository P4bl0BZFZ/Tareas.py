mayor=1
lista=[1,4.42,8,19,55,15,76,1000.01,1000.1]
for valor in lista:
    if valor>mayor:
        mayor=valor
print("El mayor numero encontrado fue:",mayor)
mayor=2
for i in range(len(lista)):
    if lista[i]>mayor:
        mayor=lista[i]
print("El mayor numero encontrado por indice:",mayor)