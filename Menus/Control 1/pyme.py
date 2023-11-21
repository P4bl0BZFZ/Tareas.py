menu="""
|====================|
| BIENVENIDO A  NAUI |
|====================|
"""

menu2="""
    |=====================|
    | Catalogo de la ropa |
    |=====================|


    ID    PRODUCTOS       PRECIO BASE |
 -------------------------------------|       
    1    Pantalones      $12000       |
    2    Camisas         $9000        |
    3    Chaquetas       $45000       |
    4    Poleras         $6000        | 
--------------------------------------|
        Tallas Disponibles            |  
--------------------------------------|                
                S                     |  
                M                     |  
                L                     |  
                XL                    | 
--------------------------------------|
"""

menu3="""
1.-Pantalones   $12000
2.-Camisas      $9000
3.-Chaquetas    $45000
4.-Poleras      $6000
"""
menu4="""
    Tallas
       S
       M
       L
       XL 
"""
menu5="""
    Tipo de envío
Local
Envio Ciudad
Fuera Ciudad
"""

prod=0
sigue=1
op=0
i=0
preto=0#Precio total
def añadirRopa():
    cant=int(input("Ingrese cantidad de carritos a crear: "))
    i=0
    preto=0 #preto de precio total
    while i<cant:
        productos = []
        c=0 #c de cantidad
        pre=0 #pre de precio
        prod=int(input("Ingrese cantidad de productos a añadir: "))
        while c<prod:
            print(menu3)
            precio = 0
            sel=int(input("Ingrese producto: "))
            if sel==1:
                print("Pantalón $12000")
                pre += 12000
            elif sel == 2:
                print("Camisa $9000")
                pre += 9000
            elif sel == 3:
                print("Chaqueta $45000")
                pre += 45000
            elif sel == 4:
                print("Polera $6000")
                pre += 6000
            tallas={"S": 0.1, "M": 0.15, "L": 0.2, "XL": 0.25}
            print(menu4)
            t=input("Ingrese talla: ")
            if t in tallas.keys():
                pre *= (1 + tallas[t])
            else:
                print("Talla inválida. No se aplicará descuento.")
            envios={"Local": 0, "Envío Ciudad": 0.05, "Fuera Ciudad": 0.1} 
            print(menu5)
            e = input("Ingrese tipo de envío: ")
            if e in envios.keys():
                pre *= (1 + envios[e])
            else:
                print("Tipo de envío inválido. No se aplicará descuento.")
            c += 1
            print("ID de producto:", c)
            print("Subtotal:", pre)
            productos.append(pre)
        print("Productos seleccionados:", productos)
        total = sum(productos) * 1.19
        print("Total a pagar + IVA:", total)
        preto += total
        i += 1
    print("Precio total:", preto)

print(menu)
while op!=5:
    print("|=======================|")
    print("| CATALOGO DE LA TIENDA |")
    print("|=======================|")
    print(" ")
    print("1.-Catalogo de la tienda")
    print("2.-Añadir productos al carrito")
    op=int(input("Seleccione opcion: "))
    if op==1:
        print(menu2)
    elif op==2:
        print("Ingrese ID del producto a añadir: ")
        compra=añadirRopa()
    else:
        print("!!OPCION NO VALIDA¡¡¡ Seleccione una de las siguientes 1/2/...")