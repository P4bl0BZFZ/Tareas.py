print("|============================|")
print("| BIENVENIDO A PIZZAS JUANAS |")
print("|============================|")
print(" ")
print("Valor base de la pizza: $1000")
base=1000
supertt=0
ingre=0
i=0
c=0
stt=0
cant=int(input("Cantidad de Pizzas que desea: "))
while i<cant:
    c=0
    stt=0
    menu="""
    Ingredientes:
    1.-Tomate   $300
    2.-Carne    $800
    3.-Pepperoni   $400
    4.-Aceitunas  $600
    """
    print(menu)
    ingr=int(input("Ingrese la cantidad de ingredientes: "))
    while ingr<=4:
        sel=int(input("Ingrese ingrediente: "))
        if sel==1:
            in1=sel
            print("Tomate $300")
            stt=stt + 300
        elif sel==2:
            in2=sel
            print("Carne $800")
            stt=stt + 800
        elif sel==3:
            in3=sel
            print("Peperoni $400")
            stt=stt + 400
        elif sel==4:
            in4=sel
            print("Aceitunas $600")
            stt=stt + 600
        c=c + 1
        print("Subtotal: ",stt)
        print("Valor de ingrediente: ",ingr)
        print("Valor de c: ",c)
        if c==ingr:
            print("Pizzas solicitadas ",cant)
            print("Ingredientes ",ingr)
            ingre=ingre + ingr
            total=base + stt
            print("Total ",total)
            break
    print("Total de ingredientes ",ingre)
    supertt=supertt + total
    print("Total general ",supertt)
    i=i + 1