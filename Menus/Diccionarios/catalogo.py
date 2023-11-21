import os 
os.system('cls')
#Uso de diccionario para crear un catalogo de productos
def ingresarDatos():
    producto={}
    sigue="s"
    while sigue=="s":
        codigo=int(input("Ingrese Codigo :"))
        descrip=input("Descripcion del producto :")
        precio=float(input("Ingrese Precio :"))
        stock=int(input("Ingrese Stock :"))
        producto[codigo]=(descrip,precio,stock)
        sigue=input("Quiere que siga/pare[s/n] ?")
    print("Carga de diccionario ejecutada!!!")
    return producto

def imprimirDatos(producto):
    print("Listado de productos")
    for codigo in producto:
        print(codigo,producto[codigo][0],producto[codigo][1],producto[codigo][2])

def consultarDatos(producto):
    print("BUSQUEDA DE PRODUCTO POR CODIGO")
    print("*******************************")
    codigo=int(input("Ingrese codigo :"))
    if codigo in producto:
        print(codigo, producto[codigo][0], producto[codigo][1],producto[codigo][2])
    else:
        print("Codigo NO existe....")    
#main
producto=ingresarDatos()
imprimirDatos(producto)
consultarDatos(producto)
print("Proceso terminado!!!!")
