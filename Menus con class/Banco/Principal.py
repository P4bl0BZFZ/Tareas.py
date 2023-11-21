#Modulo que administra modelo de colaboracion de clases
import ColabBanco
menu="""
    SISTEMA BANCARIO
=====================
1.-INGRESO DE CUENTAS
2.-OPERACIONES
3.-SALIR DE APP.
=====================
"""
sigue=1
while sigue==1:
    print(menu)
    op=int(input("Seleccione opcion :"))
    if op==1:
        nombre=input("Ingrese Nombre del Cliente :")
        monto=int(input("Ingrese monto inicial :"))
        banco=ColabBanco.Banco(nombre,monto)
        print("Registro Ingresado!!!!")
    elif op==2:
        print("DEPOSITO/GIRO EN CUENTA")
        dep=int(input("1:Deposito/2:Giro :"))
        if dep==1:
            monto=int(input("Monto a agregar a cuenta :"))
            banco=ColabBanco.Banco.operar(banco,monto,dep)
        else:
            monto=int(input("Monto a retirar de la cuenta :"))
            banco=ColabBanco.Banco.operar(banco,monto,dep)
        #print("Monto enviado a la cuenta!!!!")
    elif op==3:
        print("Saliendo de Cuentas!!!!")
        sigue=0
    else:    print("Opciones Validas 1/2/3")
print("Proceso Finalizado!!!!!!")
