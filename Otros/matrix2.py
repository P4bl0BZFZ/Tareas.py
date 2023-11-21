#Matrix de datos que almacena productos
#Se desea almacenar codigo, nombre y precio seleccionado en consola

producto=[[] , [] , []]
tam=int(input("Ingrese datos a almacenar: "))

for i in range(tam):
    codigo=int(input("Ingrese el codigo del producto: "))
    nombre=input("Descripcion del proucto: ")
    precio=float(input("Valor del producto: ")) 
    producto[0].append(codigo)
    producto[1].append(nombre)
    producto[2].append(precio)
print("Registros almacenados en la matrix...\n")
#A
print("DATOS ALMACENADOS EN LA ESTRUCTURA\n")
for i in range(len(producto)):
    for j in range(len(producto[i])):
        print(producto[i][j])

print("CODIGO   NOMBRE   PRECIO")
for i in range(len(producto)):
    for j in range(len(producto[i])):
        print(producto[j][i],end=" ")
        if(j==2):
            print()