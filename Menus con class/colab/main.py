import colaboracion
menu="""
   MENU PRINCIPAL
===================
1.-INGRESO DE DATOS
2.-OPERACION DE DATOS
3.-LISTADO DE DATOS
4.-SALIR
===================
"""
sigue=1
print(menu)
while sigue==1:    
    op=int(input("Seleccione opcion :"))
    if op==1:
        banco=colaboracion.Banco()#Instanciacion
        nombre=input("Ingrese Nombre del Cliente :")
        monto=int(input("Ingrese Monto Inicial :"))
        banco.colaboracion.Banco(nombre,monto)
        print("Registro almacenado!!!")
    elif op==2:
        colaboracion.Banco.banco.operar()
    elif op==3:
        colaboracion.Banco.reporteDeposito()
    elif op==4:
        print("Saliendo de aplicacion!!!!")
        sigue=0
    else:    print("Opciones 1/2/3/4!!!!")
print("Proceso Finalizado!!!")
        
