class Producto:
    def ingresarDatos(self,codigo, nombre,precio,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        print("Objeto almacenado...!")

    def desplegarDatos(self):
        print("DATOS DEL PRODUCTO")
        print("==================")
        print("CODIGO   :",self.codigo)
        print("NOMBRE   :",self.nombre)
        print("PRECIO   :",self.precio)
        print("STOCK    :",self.stock)

    def editarDatos(self,codigo):
        if codigo==self.codigo:
            print("Registro Encontrado!!!")
            print("Registro :",self.codigo," ",self.nombre," ",self.precio," ",self.stock)
        else:    print("REGISTRO NO EXISTE!!!")




        
