class Cuenta:
    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto

    def imprimir(self):
        print("Titular :",self.titular)
        print("Monto   :",self.monto)

class Corriente(Cuenta):
    def __init__(self,titular,monto):
        super().__init__(titular,monto)#enviar datos al padre

    def imprimir(self):
        print("Cuenta Corriente")
        super().imprimir()#Solicitar al padre la impresion

class Ahorro(Cuenta):
    def __init__(self,titular,monto,plazo,interes):
        super().__init__(titular,monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("Cuenta de Ahorro a Plazo")
        print("========================")
        super().imprimir()
        print("Plazo en dias :",self.plazo)
        print("Interes       :",self.interes)
        self.aumentoxinteres()

    def aumentoxinteres(self):
        ganancia=self.monto*self.interes/100
        print("Importe del interes pactado :",ganancia)

#Principal
#print("Cuentas Bancarias")
#print("=================")
#corriente=Corriente("Edgardo", 5000)
#corriente.imprimir()
#ahorro=Ahorro("Matilde",10000,30,0.6)
#ahorro.imprimir()















        
