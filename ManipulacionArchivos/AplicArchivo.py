#Aplicacion que manipula procesos de almacenamiento de datos
#a traves de menu de control
def crearArchivoDatos():
    nomarch=input("Nombre fisico del archivo :")
    open(nomarch,"w")
    print(nomarch)
    return nomarch

def agregarDatos(nomarch):
    arch=open(nomarch,"a")
    sigue="s"
    while sigue=="s":
        dato=""
        dato=input("Ingrese nombre del producto :")
        dato=dato + "\n"
        arch.write(dato)
        sigue=input("[s/n]Sigue/Detiene carga de Datos :")
    arch.close()
    print("Proceso de carga de datos finalizado")

def listarDatos(nomarch):
    arch=open(nomarch,"r")
    contenido=arch.read()
    print(contenido)
    arch.close()

def contarRegistros(nomarch):
    arch=open(nomarch,"r")
    regs=arch.readlines()
    print("El archivo contiene :",len(regs)," registros")
    arch.close()
   
op=0
arch=""
while(op!=5):
    print("Menu de Control Productos")
    print("=========================")
    print("1.-Crear Archivo Datos...")
    print("2.-Agregar mas Datos.....")
    print("3.-Listar Datos..........")
    print("4.-Contar Registro.......")
    print("5.-Salir de Datos........")
    op=int(input("Seleccione opcion :"))
    if op==1:
        nomarch=crearArchivoDatos()
    elif op==2:
        agregarDatos(nomarch)
    elif op==3:
        listarDatos(nomarch)
    elif op==4:
        contarRegistros(nomarch)
    elif op==5:
        print("Saliendo del menu...")
    else:    print("Opciones validas 1/2/3/4/5...Repita!!")
    
    
