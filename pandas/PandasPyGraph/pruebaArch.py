#Prueba de captura de datos del archivo
import pandas as pd
import matplotlib.pyplot as plt

arch=pd.read_csv('juegos.txt')
print(arch)
print()
#Mostrar encabezados del archivo
print(arch.head(0))
print()
#Mostrar cola del archivo
print(arch.tail(5))
print()
#Mostrar estadisticos datos de tendencia central
print(arch.describe())
print()
#Mostrar datos de columnas especificas
ventasUSA=arch['NA_Sales']
ventas=round(ventasUSA)
print(ventasUSA)
print(ventas)
print("Graficos")
x_values=arch['NA_Sales'].unique()
y_values=arch['NA_Sales'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.show()
plt.close('all')


