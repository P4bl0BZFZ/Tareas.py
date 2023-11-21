class Persona:
    def __init__(self):
        self.nombre=input("Ingrese Nombre :")
        self.edad=int(input("Ingrese Edad :"))

    def imprimir(self):
        print("Nombre :",self.nombre)
        print("Edad   :",self.edad)

class Empleado(Persona):##Empleado es de tipo Persona
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo :"))

    def imprimir(self):
        super().imprimir()
        print("Sueldo :",self.sueldo)

    def pagarImpuesto(self):
        if self.sueldo > 3000:
            print("El empleado paga impuesto")
        else:
            print("El empleado NO paga impuesto")
#main#
##persona=Persona()
##persona.imprimir()
print("=================")
empleado=Empleado()
empleado.imprimir()
empleado.pagarImpuesto()
            
        
        
                            
