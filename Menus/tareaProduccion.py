import os
os.system('cls')#Limpiar consola

menu="""
         SISTEMA DE PLANIFICACIÓN DE LA PRODUCCION
==========================================================
1.- Generar plan de producción
2.- Ingresar datos de producción
3.- Calcular producción total de una faena específica
4.- Calcular producción total de todas las faenas en un día específico
5.- Salir del programa
"""
def generarPlan():
    plan=[]
    minas=int(input("Ingrese numero de faenas: "))
    prod=int(input("Ingrese numero de días de producción: "))
    for i in range(minas):
        faenas=[]
        for j in range(prod):
            faenas.append(0)
        plan.append(faenas)
    print("PLAN DE PRODUCCION")
    print("==================")
    for i in range(minas):
        print(plan[i])
    return plan

sigue=1
while sigue==1:
    print(menu)
    op=int(input("Seleccione opción: "))
    if op==1:
        plan=generarPlan()
    elif op==5:
        print("Saliendo del sistema...")
        sigue=0
    else: print("Opcion invalida!!! Por favor elija 1/2/3/4/5... ")
print(menu)


