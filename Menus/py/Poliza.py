#Entidad logica que representa una poliza de seguro
class Poliza:
    def ingresarPoliza(self, codigo, tipo, valor, fecha):
        self.codigo = codigo 
        self.tipo = tipo
        self.valor = valor
        self.fecha = fecha
        
    def consultaPoliza(self, codigo):
        if self.codigo == codigo:
            print("Registro encontrado: ", self.codigo)
            print("CODIGO:                    ", self.codigo)
            print("TIPO:                      ", self.tipo)
            print("VALOR:                     ", self.valor)
            print("FECHA DE ACTIVACION:       ", self.fecha)
        else:
            print("Registro NO existe")
            
    def desplegarPoliza(self):
        print("DATOS DE LA POLIZA")
        print("==================")
        print("CODIGO:                    ", self.codigo)
        print("TIPO:                      ", self.tipo)
        print("VALOR:                     ", self.valor)
        print("FECHA DE ACTIVACION:       ", self.fecha)