import os
os.system('cls')#Limpiar consola

def ingresoDatos():
    pacientes={}
    cont="s"
    while cont=="s":
        rut=int(input("Ingrese rut del paciente (sin puntos ni guin): "))
        nombre=input("Ingrese el nombre del paciente: ")
        apellido=input("Ingrese appelido del paciente: ")
        edad=int(input("Ingrese la edad del paciente: "))
        seguro=input("Ingrese seguro del paciente: ")
        pacientes[rut]=(nombre,apellido,edad,seguro)
        cont=input("[s/n] Quiere que siga/pare: ")
    print("Datos cargados correctamente...")
    return pacientes

def desplegarDatos(pacientes):
    print("LISTADO DE PACIENTES GUARDADOS")
    print("-------------------------------")
    for rut in pacientes:
        print(rut,pacientes[rut][0],pacientes[rut][1],pacientes[rut][2],pacientes[rut][3])

def modificarDatos(pacientes,rut):
    print("Modificacion de datos")
    nombre=pacientes[rut][0]
    apellido=pacientes[rut][1]
    edad=pacientes[rut][2]
    seguro=pacientes[rut][3]
    modi=int(input("Modifica: Nombre/1: Apellido/2: Edad/3: Seguro/4: "))
    if modi==1:
        nombre=input("El nombre a sido cambiado a: ")
    elif modi==2:
        apellido=input("El apellido a sido cambiado a: ")
    elif modi==3:
        edad=int(input("La edad a sido cambiada por: "))
    elif modi==4:
        seguro=input("El seguro fue modificado por: ")
    else:   print("!!!Seleccion erronea de numero¡¡¡")
    pacientes[rut]=(nombre,apellido,edad,seguro)
    desplegarDatos(pacientes)

def eliminarDatos(paciente,rut):
    print("Eliminacion de Registro")
    elim=int(input("Eliminar/1: Salvar Datos/2: "))
    if elim==1:
        del paciente[rut]
    else:
        print("Registro salvado, no se elimina!!!!")

def editarDatos(pacientes):
    rut=int(input("Ingrese el rut del paciente para buscar: "))
    if rut in pacientes:
        print(rut)
        print(pacientes[rut][0])
        print(pacientes[rut][1])
        print(pacientes[rut][2])
        print(pacientes[rut][3])
        opc=int(input("1: Modifica/2:Elimina Registro: "))
        if opc==1:
            modificarDatos(pacientes,rut)
        elif opc==2:
            eliminarDatos(pacientes,rut)
        else:    print("Seleccion erronea!!!!")

menu="""
BIENVENIDO AL HOSPITAL NAVAL
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
        pacientes=ingresoDatos()
    elif op==2:
        editarDatos(pacientes)
    elif op==3:
        desplegarDatos(pacientes)
    elif op==4:
        print("Saliendo de app!!!!!")
        sigue=0
    else:    print("Opciones validas 1/2/3/4!!")