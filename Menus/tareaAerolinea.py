
def ingresoDatos():
    print("Informacion de Usuario")
    id=int(input("Ingrese una ID: "))
    nombres=input("Ingrese nombre y apellido del Usuario: ")
    edad=int(input("Ingrese edad del Usuario: "))
    klmrec=int(input("Ingrese Kilometros a recorrer: "))
    print("Informacion guardada con exito...")
    pasajeros.append([id, nombres, edad, klmrec])
    return pasajeros

def consultaDatos():
    print("Informacion de Usuarios")
    print("-----------------------")
    idConsulta=int(input("Ingrese la ID a consultar: "))
    enc=0
    for id, nombres, edad, klmrec in pasajeros:
        if idConsulta==id:
            enc=1
            print("Informacion de los Usuarios")
            print("---------------------------")
            print("ID  NOMBRE  EDAD  KILOMETROS")
            print("ID encontrada como: ",id," ",nombres," ",edad," ",klmrec,"Km")
    if enc==0:      
        print("!!!La ID que solicito no se encuentra¡¡¡")  

def despliegueDatos():
    print("Usuarios registrados")
    print("ID  NOMBRE  EDAD  KILOMETROS")
    for id, nombres, edad, klmrec in pasajeros:
        print(id," ",nombres," ",edad," ",klmrec,"Km")

def eliminacionDatos():
    idBorrar=int(input("Ingrese ID a eliminar: "))
    for i in range(len(pasajeros)):
        if pasajeros[1][0]==idBorrar:
            pasajeros.pop(i)
            print("Informacion eliminada con exito.")
            return True
    print("No se encontro el registro...")
    return False

def salir():
    print("Hasta luego, vuelva pronto...")

pasajeros=[]
id=0
nombres=str
edad=0
klmrec=0
op=0

while op!=5:
    print("  |======================|")
    print("  | AEROLINEAS AIRPLANET |")
    print("  |======================|")
    print("1.-Ingresar datos de Usuario")
    print("2.-Consultar informacion del Usuario")
    print("3.-Informacion general")
    print("4.-Eliminacion de Usuario")
    print("5.-Salir")
    op=int(input("Seleccione una opcion: "))
    if op==1:
        ingresoDatos()
    elif op==2:
        consultaDatos()
    elif op==3:
        despliegueDatos()
    elif op==4:
        eliminacionDatos()
    elif op==5:
        salir()
    else:
        print("La opcion selecionada no es valida... !!Elija opcion 1/2/3/4/5¡¡")