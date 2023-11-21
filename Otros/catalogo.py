menu="""
MENU DE CONTROL CATALOGO
[1]INGESO DE PRODUCTO
[2]ELIMINAR PRODUCTO
[3]CATALOGO
[4]COMPRAR PRODUCTO
[5]SALIR
"""
sigue=1
codigo=[]
nombre=[]
precio=[]
stock=[]
n=int(input("Ingrese el tamaño de carrito de compra: "))

while(sigue==1):
    print(menu)
    op=int(input("Seleccione opcion:"))
    if op==1:
        print("Ingreso de producto")
        for i in range(n):
            cod=int(input("Codigo: "))
            codigo.append(cod)
            nom=input("Nombre del producto: ")
            nombre.append(nom)
            pre=int(input("Precio: "))
            precio.append(pre)
            stc=int(input("Disponibilidada: "))
            stock.append(stc)
        print("Catalogo cargado correctamente.")
    elif op==2:
        print("Eliminacion de producto")
        pos=int(input("Ingrese posicion menor a n: "))
        codigo.pop(pos)
        nombre.pop(pos)
        precio.pop(pos)
        stock.pop(pos)
        print("Registro eliminado...")
        n=n-1
    elif op==3:
        print("Despliegue de catalogo")
        for i in range(n):
            print(codigo[i]," ",nombre[i]," ""$",precio[i]," ",stock[i])
    elif op==4:
        print("Ejecutar compra")
        pos=int(input("Ingrese posicion del producto: "))
        print(codigo[pos]," ",nombre[pos]," ","$",precio[pos]," ",stock[pos])
        cant=int(input("Ingrese cantidad solicitada: "))
        total=precio[pos]*cant
        iva=total*0.19
        compra=total+iva
        stock[pos]=stock[pos]-cant
        print("Valor de la compra parcial:  $",total)
        print("Valor de la compra total:   $",compra)
        print("Tock actualizado: ",stock[pos])
    elif op==5:
        print("Saliendo de la App...")
        sigue=0
    else:
        print("Opciones 1/2/3/4/5, repita el proceso!!!") 
print("Compra finalizada, vuelva pronto :D")
        
