import Poliza
menu = """
MENU DE CONTROL
===============
[1] Ingreso de poliza
[2] Consulta de poliza
[3] Despliegue de poliza
[4] Salir
"""
sigue = 1
while sigue == 1:
    print(menu)
    op = int(input("Seleccione opcion: "))
    if op == 1:
        poliza = Poliza.Poliza() #Instanciacion de Clase
        codigo = int(input("Ingrese codigo: "))
        tipo = input("Tipo de poliza: ")
        valor = int(input("Ingrese valor de la poliza: "))
        fecha = input("Fecha de activacion: ")
        #Objeto punto metodo
        poliza.ingresarPoliza(codigo, tipo, valor, fecha)
        print("DATOS ENVIADOS A LA RAM !!!")
    elif op == 2:
        codigo = int(input("Ingrese codigo de busqueda: "))
        poliza.consultaPoliza(codigo)
    elif op == 3:
        poliza.desplegarPoliza()
    elif op == 4:
        print("Saliendo...")
        sigue = 0
    else:
        print("Seleccione opcion valida...")