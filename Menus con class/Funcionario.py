class Funcionario:
    def __init__(self):
        self.rut=input("Ingrese rut :")
        self.nombre=input("Ingrese nombre :")
        self.sueldo=int(input("Ingree sueldo :"))
    def imprimir(self):
        print("RUT    :",self.rut)
        print("NOMBRE :",self.nombre)
        print("SUELDO :",self.sueldo)

class Medico(Funcionario):
    def __init__(self):
        super().__init__()
        self.espec=input("Ingrese Especialidad :")
    def imprimir(self):
        super().imprimir()
        print("ESPECIALIDAD :",self.espec)
        
class Enfermera(Funcionario):
    def __init__(self):
        super().__init__()
        self.turno=input("Ingrese Turno: DIA/TARDE/NOCHE :")
    def imprimir(self):
        super().imprimir()
        print("TURNO :",self.turno)        

class Tens(Funcionario):
    def __init__(self):
        super().__init__()
        self.especie=input("Ingrese Especialidad: TAC/EMERGENCIA/AMBULATORIO :")
    def imprimir(self):
        super().imprimir()
        print("ESPECIALIDAD :",self.especie)
        
medico=Medico()
medico.imprimir()
enfermera=Enfermera()
enfermera.imprimir()
tens=Tens()
tens.imprimir()
