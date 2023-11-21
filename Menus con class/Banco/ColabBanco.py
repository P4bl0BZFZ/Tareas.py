#Colaboracion Banco Cliente
class Cliente:    #clase colaboradora
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto

    def depositar(self,monto):
        self.monto=self.monto+monto

    def girar(self,monto):
        self.monto=self.monto-monto

    def consultar(self):
        return self.monto

    def desplegar(self):
        print(self.nombre," Tiene en su cuenta depositado :",self.monto)

class Banco:  #clase master
    
    def __init__(self,nombre,monto):
        self.cliente=Cliente(nombre,monto)

    def operar(self,monto,dep):
        if dep==1:
            self.cliente.depositar(monto)
        else:
            self.cliente.girar(monto)
        print("Monto actualizado :",self.cliente.consultar())
        self.cliente.desplegar()

        
        
