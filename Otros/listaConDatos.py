#Creacion de lista con ingreso de datos
lista=[]
for i in range(5):
    n=int(input("Ingreso datos a la lista: "))
    lista.append(n)
print(lista)

lista2=[]
for i in range(5):
    n=int(input("Ingreso datos de lista: "))
    lista2=lista2+[n]
print(lista2)

#Lista directa
lista3=[0 for i  in range(5)]
for i in range(5):
    n=int(input("Ingrese datos a la lista: "))
    lista3[i]=n
print(lista3)