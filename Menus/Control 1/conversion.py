op=0
var1=0
var2=0
result=0
result2=0
while op!=3:
    print("COVERSIONES")
    print("=================================")
    print("1.-Conversion a Celcius")
    print("2.-Conversion a Farenhait")
    print("3.-Salir")
    op=int(input("Seleccione opcion: "))
    if op==1:
        print("Temperatua a convertir")
        print("----------------------")
        var1=int(input("Ingrese los grados Farenhait: "))
        result=(5/9 * (var1 - 32))
        print("La conversion dio ",result,"° Celcius")
    elif op==2:
        print("Temperatua a convertir")
        print("----------------------")
        var2=int(input("Ingrese los grados Celcius: "))
        result2=((9/5 * var2) + 32)
        print("La conversion dio ",result2,"° Farenhait")
    elif op==3:
        print("Saliendo...")
    else:
        print("Elija una de las opciones 1/2/3...")

