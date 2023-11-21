empl=int(input("Ingrese su cantidad de empleadores: "))#Solicitamos datos
anu=int(input("Indique su cantidad de ingreso anual: "))
if empl>=2:#Realizamos las operaciones debidas, con sus resultados
    if anu<=7481646:
        impu= 0
        print("Usted queda exento de pagar impuestos.")
    elif anu>=7481647 and anu<=16625880:
        impu=0.04 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>=16625881 and anu<=27709800:
        impu=0.08 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>=27709801 and anu<=38793720:
        impu=0.135 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>=38793721 and anu<=49877640:
        impu=0.23 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>=49877641 and anu<=66503520:
        impu=0.304 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>=66503521 and anu<=83129400:
        impu=0.355 * anu/100
        print("Su impuesto a pagar es de: $",impu)
    elif anu>83129401:
        impu=0.4 * anu/100
        print("Su impuesto a pagar es de: $",impu)
else:
    print("Cantidad de empleadores inválida. Por favor, ingrese un valor válido.")
