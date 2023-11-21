menu="""

            Chilandis - Tours
                                
1.-Torres del Paine        $500000
2.-Campos de Hielo         $350000
3.-Vale de la Luna         $400000 
4.-2 Tours              15% Descuento
5.-Todos los Tours      25% Descuento
6.-Salir
"""
edad=0
precio=0
stotal=0 #Subtotal
desc=0 #Descuento
total=0
print(menu)
op=int(input("Seleccione opcion: "))
if op==1:
    print("Usted selecciono Torres del Paine con un costo base de $500000")
    precio=500000
    cant=int(input("Ingrese cantidad de personas: "))
    edad=int(input("Ingrese 1: Si son todas de tercera edad/Ingrese 0: Si NO lo son: "))
    if edad==1:
        stotal=cant * 500000
        desc=stotal * 0.25
        total=stotal - desc
        print("Total parcial del Tour: ",stotal)
        print("Se le aplicara un descuento de: ",desc)
        print("Costo final del Tour: ",total)
    else:
        stotal=cant * 500000
        total=stotal
        print("Total parcial del Tour: ",stotal)
        print("Costo final del Tour: ",total)
if op==2:
    print("Usted selecciono Campos de Hielo con un costo base de $350000")
    precio=350000
    cant=int(input("Ingrese cantidad de personas: "))
    edad=int(input("Ingrese 1: Si son todas de tercera edad/Ingrese 0: Si NO lo son: "))
    if edad==1:
        stotal=cant * 350000
        desc=stotal * 0.25
        total=stotal - desc
        print("Total parcial del Tour: ",stotal)
        print("Se le aplicara un descuento de: ",desc)
        print("Costo final del Tour: ",total)
    else:
        stotal=cant * 350000
        total=stotal
        print("Total parcial del Tour: ",stotal)
        print("Costo final del Tour: ",total)
elif op==3:
    print("Usted selecciono Vale de la Luna con un costo base de $400000")
    precio=400000
    cant=int(input("Ingrese cantidad de personas: "))
    edad=int(input("Ingrese 1: Si son todas de tercera edad/Ingrese 0: Si NO lo son: "))
    if edad==1:
        stotal=cant * 400000
        desc=stotal * 0.25
        total=stotal - desc
        print("Total parcial del Tour: ",stotal)
        print("Se le aplicara un descuento de: ",desc)
        print("Costo final del Tour: ", total)
    else:
        stotal=cant * 400000
        total=stotal
        print("Total parcial del Tour: ",stotal)
        print("Costo final del Tour: ",total)
if op == 4:
    t1=int(input("Ingrese primer tour 1/2/3: "))
    t2=int(input("Ingrese segundo tour 1/2/3: "))
    if t1==1 and t2 == 2:
        stotal=500000 + 350000
    elif t1==1 and t2 == 3:
        stotal=500000 + 400000
    else:
        stotal=350000 + 400000
    desc=stotal * 0.15
    total=stotal - desc
    print("Total parcial de los Tours: ",stotal)
    print("Se le aplicara un descuento de: ",desc)
    print("Costo final de los Tours: ",total)
elif op==5:
    print("Usted selecciono Todos los Tours con un descuento del 25%")
    stotal=1250000
    desc=stotal * 0.25
    total=stotal - desc
    print("Total parcial de los Tours: ",stotal)
    print("Se le aplicara un descuento de: ",desc)
    print("Costo final de los Tours: ",total)
elif op==6:
    print("Gracias por visitar Chilandis - Tours. ¡Hasta pronto!")
else:
    print("Opcion invalida. Intente de nuevo.")
