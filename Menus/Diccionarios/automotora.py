import os
os.system('cls')#Limpiar consola

def ingresarDatos():
    vehiculo={}
    cont="s"
    while cont=="s":
        patente=input("Ingrese patente :")#clave del registro
        marca=input("Ingrese marca: ")
        tipo=input("Ingrese modelo: ")
        valor=int(input("Ingrese valor: "))
        vehiculo[patente]=(marca,tipo,valor)
        cont=input("[s/n] Quiere que siga/pare: ")
    print("Diccionario cargados con registros...!")
    return vehiculo

def desplegarDatos(vehiculo):
    print("LISTADO DE VEHICULOS")
    print("$$$$$$$$$$$$$$$$$$$$")
    for patente in vehiculo:
        print(patente,vehiculo[patente][0],vehiculo[patente][1],vehiculo[patente][2])
        
def modificarDatos(vehiculo,patente):
    print("Modificacion de datos")
    marca=vehiculo[patente][0]
    tipo=vehiculo[patente][1]
    precio=vehiculo[patente][2]
    modi=int(input("Modifica: Marca/1:Tipo/2:Valor/3: "))
    if modi==1:
        marca=input("Nueva Marca: ")
    elif modi==2:
        tipo=input("Nuevo Tipo: ")
    elif modi==3:
        valor=int(input("Ingrese Nuevo Valor: "))
    else:    print("Seleccion erronea de variable!!!!")
    vehiculo[patente]=(marca,tipo,valor)
    desplegarDatos(vehiculo)

def eliminarDatos(vehiculo,patente):
    print("Eliminacion de Registro")
    elim=int(input("Eliminar/1: Salvar Datos/2: "))
    if elim==1:
        del vehiculo[patente] #Eliminar por la patente
    else:
        print("Registro salvado, no se elimina!!!!")
    
def editarDatos(vehiculo):
    patente=input("Ingrese patente para busqueda: ")
    if patente in vehiculo:
        print(patente)
        print(vehiculo[patente][0])
        print(vehiculo[patente][1])
        print(vehiculo[patente][2])
        opc=int(input("1: Modifica/2:Elimina Registro: "))
        if opc==1:
            modificarDatos(vehiculo,patente)
        elif opc==2:
            eliminarDatos(vehiculo,patente)
        else:    print("Seleccion erronea!!!!")
    
menu="""
MENU DE CONTROL AUTOMOTORA
==========================
[1]Ingresar Datos
[2]Edicion de Datos 
[3]Despliegue de Datos
[4]Salir de App
"""
sigue=1
while sigue==1:
    print(menu)
    op=int(input("Seleccione opcion: "))
    if op==1:
        vehiculo=ingresarDatos()
    elif op==2:
        editarDatos(vehiculo)
    elif op==3:
        desplegarDatos(vehiculo)
    elif op==4:
        print("Saliendo de app!!!!!")
        sigue=0
    else:    print("Opciones validas 1/2/3/4!!")
