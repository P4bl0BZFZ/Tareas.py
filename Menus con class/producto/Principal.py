import Producto
menu="""
   MENU PRINCIPAL
===================
1.-INGRESO DE DATOS
2.-EDICION DE DATOS
3.-LISTADO DE DATOS
4.-SALIR
===================
"""
sigue=1
print(menu)
while sigue==1:    
    op=int(input("Seleccione opcion :"))
    if op==1:
        producto=Producto.Producto()#Instanciacion
        codigo=int(input("Ingrese Codigo :"))
        nombre=input("Ingrese Nombre del Producto :")
        precio=int(input("Ingrese precio :"))
        stock=int(input("Ingrese Stock :"))
        producto.ingresarDatos(codigo, nombre,precio,stock)
        print("Registro almacenado!!!")
    elif op==2:
        print("Ingrese codigo para busqueda de registro!!!")
        codigo=int(input("Ingrese Codigo :"))
        producto.editarDatos(codigo)
    elif op==3:
        producto.desplegarDatos()
    elif op==4:
        print("Saliendo de aplicacion!!!!")
        sigue=0
    else:    print("Opciones 1/2/3/4!!!!")
print("Proceso Finalizado!!!")
        
