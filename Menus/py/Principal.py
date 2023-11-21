#Bloque monolitico de Colaboracion Bancaria
#Clase colaboradora
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
        
    def depositar(self, monto):
        self.monto = self.monto + monto 
        
    def girar(self, monto):
        self.monto = self.monto - monto
         
    def consultar(self):
        return self.monto
    
    def desplegar(self):
        print(self.nombre, "Tiene depositado: ", self.monto)
        
#Clase Banco
class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juanito")
        self.cliente2 = Cliente("Cecilia")
        self.cliente3 = Cliente("Fernanda")
        
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(3000)
        self.cliente3.depositar(6000)
        self.cliente3.girar(330)
        
    def reporteOperaciones(self):
        total = self.cliente1.consultar() + self.cliente2.consultar() + self.cliente3.consultar()
        print("Monto de todos los depositos: ", total)
        self.cliente1.desplegar()
        self.cliente2.desplegar()
        self.cliente3.desplegar()
        
#Bloque main
banco = Banco()
banco.operar()
banco.reporteOperaciones()