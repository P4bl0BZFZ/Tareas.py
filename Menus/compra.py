var1=0
var2=0
resul=0
nombre=""
op=0
while op!=5:
    print("MENU DE CONTROL")
    print("===============")
    print("1.-Ingreso de Dato")
    print("2.-Efectuar operacion")
    print("3.-Presentar resultados")
    print("4.-Otra opcion")
    print("5.-Salir")
    op=int(input("Selecione opcion: "))
    if op==1:
        print("Ingresos")
        print("--------")
        nombre=input("Ingrese su nombre: ")
        var1=int(input("Ingrese primera variable: "))
        var2=int(input("Ingrese segunda variable: "))
        print("Datos ingresados correctamente")
        print("==============================")
    elif op==2:
        print("Ejecuciones")
        print("-----------")
        resul=var1 + var2
        print("Resultado de la suma: ",resul)
        resul=var1 - var2
        print("Resultado de la resta: ",resul)
        resul=var1 * var2
        print("Resultado de la mul: ",resul)
        resul=var1 / var2
        print("Resultado de la div: ",resul)
    elif op==3:
        print("Despliegue")
        print("----------")
        print("Variable de entrada 1: ",var1)
        print("Variable de entrada 2: ",var2)
        print("Ultima operacion realiada dio como resultado: ",resul)
    elif op==4:
        modulo=var1 % var2
        print("El modulo de la entrada es: ",modulo)
    elif op==5:
        print("Saliendo....")
        print("Usuario,",nombre, "acaba de abandonar el sistema")
    else:
        print("Opciones 1/2/3/4/5...")
        