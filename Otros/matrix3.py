#Arreglo de datos que almacenan productos
#Uno de funcion->def

def ingresaDatos():
    productos=[]
    n=int(input("Ingrese el tamaño del vector: "))
    for i in range(n): 
        codigo=int(input("Ingrese codigo: "))
        nombre=input("Ingrese nombre: ")
        precio=int(input("Ingrese valor: "))
        productos.append((codigo, nombre, precio))
    return productos

def presentarDatos(productos):
    print("DATOS DE LOS PRODUCTOS")
    print("CODIGO  NOMBRE  PRECIO")
    for codigo,nombre,precio in productos:
        print(codigo," ",nombre," ",precio," ")


productos=ingresaDatos()
presentarDatos(productos)