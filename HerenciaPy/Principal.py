from CuentasBancarias import Corriente,Ahorro
class Vista:
    def __init__(self):
        print("Cuentas Bancarias")
        print("=================")
        corriente=Corriente("Edgardo", 5000)
        corriente.imprimir()
        ahorro=Ahorro("Matilde",10000,30,0.6)
        ahorro.imprimir()   
#Inicializacion
vista=Vista()

