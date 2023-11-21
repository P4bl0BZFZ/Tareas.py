import os
os.system('cls')#Limpiar consola
#lista=[]

def ingresoDatos(lista):
    for i in range(5):
        n=int(input("Ingrese datos a la lista: "))
        lista.append(n)
    print(lista)
    return lista

def eliminarDatos(lista):
    #Borrar un dato con "remove"
    borrar=int(input("Ingrese el dato a eliminar: "))
    lista.remove(borrar)
    print(lista)
    #Borrar con "del" buscando la posicion
    borrar2=int(input("Ingrese valor a eliminar :"))
    pos=lista.index(borrar2)
    del lista[pos]
    print(lista)

def despliegueDatos(lista):
    print(lista)


menu="""
1.- Ingreso de datos
2.- Despliegue de datos
3.- Eliminacion  de datos
4.- Salir
"""
lista=[]
sigue=1
while sigue==1:
    op=int(input("Seleccione una opcion 1/2/3/4: "))
    if op==1:
        ingresoDatos(lista)
    elif op==2:
        despliegueDatos(lista)
    elif op==3:
        eliminarDatos(lista)
    elif op==4:
        print("Saliendo...")
        sigue=0
else:
    print("Opcion no valida... por favor elija 1/2/3/4...")