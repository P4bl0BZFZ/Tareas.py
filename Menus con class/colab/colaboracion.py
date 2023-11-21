class Cliente:
    def __init__(self,nombre):#Constructor
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def girar(self,monto):
        self.monto=self.monto-monto

    def consultar(self):
        return self.monto

    def desplegar(self):
        print(self.nombre," Tiene depostado :",self.monto)
#---------------------------------------------------------
class Banco:
    def __init__(self):#Constructor
        self.cliente=Cliente(self,nombre,monto)

    def operar(self):
        self.cliente.depositar(10000)

    def reporteDeposito(self):
        self.cliente.desplegar()
