#Prueba de captura de datos del archivo
import pandas as pd
import matplotlib.pyplot as plt

archivo=pd.read_csv('gamesSales.txt')
print(archivo)
print()
#Mostrar encabezados del archivo
print(archivo.head(0))
print()
#Mostrar cola del archivo
print(archivo.tail(5))
print()
#Mostrar estadisticos datos de tendencia central
print(archivo.describe())
print()
#Mostrar datos de columnas especificas
ventasUSA=archivo['NA_Sales']
ventas=round(ventasUSA)
print(ventasUSA)
print(ventas)
#print("Graficos")
x_values=archivo['NA_Sales'].unique()
y_values=archivo['NA_Sales'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.show()
plt.close('all')
#print("Globales")
x_values=archivo['Global_Sales'].unique()
y_values=archivo['Global_Sales'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.show()
plt.close('all')

# Genero principal mas vendido 2017 global
top2017 = archivo[archivo['Year'] == 2017].groupby('Genre')['Global_Sales'].sum().idxmax()
print(top2017)


#  Distribucion de inversion publicitaria x regiones
regionsales = archivo[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()
totalsales = regionsales.sum()
inversion = regionsales / totalsales
print(inversion)