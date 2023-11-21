
def ingresarDatos():
    productos=[]
    n=int(input("Ingrese cantidad de muestra: "))
    for i in range(n):
        codigo=int(input("Ingrese codigo de la muestra: "))
        nombre=input("Ingrese descripcion de la muestra: ")
        precio=int(input("Ingrese valor de la muestra: "))
        productos.append((codigo,nombre,precio))
    print("MUESTRAS CARGADAS CORRECTAMENTE...")
    return productos

def busquedaDatos(productos):
    enc=0
    pos=-1
    cont=-1
    cod=int(input("Ingresar codigo a buscar: "))
    for codigo,nombre,precio in productos:
        if(codigo==cod):
            enc=1
            pos=cont
            print(codigo," ",nombre," ",precio)
    if enc==0:
        print("!!!REGISTRO NO EXISTENTE¡¡¡ REINTENTE CON OTRO...")
    return pos  

def eliminarDatos(productos, pos):
    productos.pop(pos)
    print("Ingrese codigo a eliminar: ")
    n=n-1

def presentarDatos(productos):
    print("CODIGO  MUESTRA  PRECIO")
    for codigo,nombre,precio in productos:
        print(codigo," ",nombre," ",precio)


menu="""
MENU DE CONTROL
===============
1.-INGRESO DE DATOS
2.-CONSULTA DE DATOS
3.-ELIMINAR DATOS
4.-DESPLEGAR DATOS
5.-SALIR
"""
sigue=1
n=0
pos=-1
while sigue==1:
    print(menu)
    op=int(input("Seleccione opcion: "))
    if op==1:
        print("AlMACENAMENTO DE DATOS")
        productos=ingresarDatos()
    elif op==2:
        print("BUSQUEDA DE DATOS POR CODIGO")
        pos=busquedaDatos(productos)
    elif op==3:
        print("ELIMINAR DATOS POR CODIGO")
        pos=busquedaDatos(productos, pos)
        if pos>=0:
            eliminarDatos(productos.pos)
            n=n-1
    elif op==4:
        print("ESTADO DE LAS MUESTRAS")
        print("======================")
        presentarDatos(productos)
    elif op==5:
        print("Saliendo de la aplicacion...")
        sigue=0
    else:
        print("!!!OPCION NO ENCONTRADA¡¡¡ PORFAVOR ELIJA LAS SIGUIENTES OPCIONES 1/2/3/4/5....")
print("     PROCESO FINALIZADO")