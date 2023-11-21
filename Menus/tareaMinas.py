import os#Limpiar codigo
os.system('cls')

menu="""
         SISTEMA DE PLANIFICACIÓN DE LA PRODUCCION
==========================================================
1.- Generar plan de producción
2.- Ingresar datos de producción
3.- Calcular producción total de una faena específica
4.- Calcular producción total de todas las faenas en un día específico
5.- Salir del programa
"""


#Función para generar el plan de producción
def generar_plan():
  faenas=int(input("Ingrese el número de faenas: "))
  dias=int(input("Ingrese el número de días de producción: "))

  plan=[]
  for i in range(faenas):
    fila=[]
    for j in range(dias):
      fila.append(0)
    plan.append(fila)
  print("        PLAN DE PRODUCCIÓN:")
  print("*************************************")
  for i in range(faenas):
    print(f"FAENA {i}", plan[i])
  print("*************************************")
  return plan


#Función para ingresar los datos de producción
def ingresar_datos(plan):
  for i in range(len(plan)):
    for j in range(len(plan[0])):
      toneladas=int(input("Ingrese las toneladas: "))
      plan[i][j]=toneladas
  despliegue_datos(plan)
  return plan


#Función para desplegar los datos antes de los procesos
def despliegue_datos(plan):
  for i in range(len(plan)):
    print(f"FAENA {i}",plan[i])


#Función para calcular la producción total de una faena específica
def produccion_faena(plan):
  faena=int(input("Ingrese el número de la faena: "))
  print(plan[faena])
  prodtotal=sum(plan[faena])
  print(f"La producción total de la faena {faena} es de: {prodtotal}")


#Función para calcular la producción total de todas las faenas en un día específico
def produccion_dia(plan):
  dia=int(input("Ingrese el número del día: "))
  for i in range(len(plan)):
    print(plan[i][dia-1])
  prodtotal=sum([plan[i][dia-1] for i in range(len(plan))])
  print(f"La producción total de todas las faenas en el día {dia} es de:{prodtotal}")


plan=[]
sigue=1
while sigue==1:
  print(menu)
  opcion=int(input("Ingrese su opción: "))
  if opcion==1:
    plan=generar_plan()
  elif opcion==2:
    if plan:
      plan=ingresar_datos(plan)
  elif opcion==3:
    if plan:
      produccion_faena(plan)
  elif opcion==4:
    if plan:
      produccion_dia(plan)
  elif opcion==5:
    print("Saliendo del programa...")
    sigue=0
  else:
    print("!!!Opcion no valida¡¡¡ Por Favor elija 1/2/3/4/5")