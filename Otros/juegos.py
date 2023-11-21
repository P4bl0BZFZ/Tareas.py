import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo=pd.read_csv('games_sales.txt')

# Mostrar los datos del archivo
print(archivo)
print()

# Mostrar encabezados del archivo
print(archivo.head(0))
print()

# Mostrar cola del archivo
print(archivo.tail(5))
print()

# Mostrar estadísticos de datos de tendencia central
print(archivo.describe())
print()

# Mostrar datos de columnas específicas
ventasUSA=archivo['NA_Sales']
ventas=round(ventasUSA)
print(ventasUSA)
print(ventas)
print()

# Gráfico de ventas en América del Norte
x_values=archivo['NA_Sales'].unique()
y_values=archivo['NA_Sales'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('Ventas en América del Norte')
plt.xlabel('Ventas (millones)')
plt.ylabel('Frecuencia')
plt.show()
plt.close('all')

# Gráfico de ventas globales
x_values = archivo['Global_Sales'].unique()
y_values = archivo['Global_Sales'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('Ventas Globales')
plt.xlabel('Ventas (millones)')
plt.ylabel('Frecuencia')
plt.show()
plt.close('all')

# Punto 1: Género principal más vendido en 2017 a nivel global
top_genre_2017=archivo[archivo['Year']==2017].groupby('Genre')['Global_Sales'].sum().idxmax()

# Punto 2: Subgénero en el quinto lugar de ventas en 2020 en Europa
subgenre_2020_eu=archivo[archivo['Year']==2020].sort_values('EU_Sales', ascending=False)['Genre'].iloc[4]

# Punto 3: Distribución de la inversión publicitaria por regiones
region_sales=['NA_Sales', 'EU_Sales', 'JP_Sales']
region_total_sales = archivo[region_sales].sum()
ad_investment=region_total_sales / region_total_sales.sum()

# Gráfico 1: Ventas por género en 2017 a nivel global
genre_sales_2017=archivo[archivo['Year']==2017].groupby('Genre')['Global_Sales'].sum()
plt.figure(figsize=(10, 6))
genre_sales_2017.plot(kind='bar')
plt.title('Ventas por Género en 2017 (Global)')
plt.xlabel('Género')
plt.ylabel('Ventas (millones)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_2017.png')
plt.close()

# Gráfico 2: Ventas por subgénero en 2020 en Europa
subgenre_sales_2020_eu=archivo[archivo['Year']==2020].groupby('Genre')['EU_Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
subgenre_sales_2020_eu.plot(kind='bar')
plt.title('Ventas por Subgénero en 2020 (Europa)')
plt.xlabel('Subgénero')
plt.ylabel('Ventas (millones)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_2020_europa.png')
plt.close()

# Gráfico 3: Distribución de la inversión publicitaria por regiones
plt.figure(figsize=(8, 8))
ad_investment.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Distribución de la Inversión Publicitaria por Regiones')
plt.ylabel('')
plt.tight_layout()
plt.savefig('inversion_publicitaria.png')
plt.close()

# Imprimir respuestas y confirmación de generación de gráficos
print("Respuestas:")
print("1. Género principal más vendido en 2017 a nivel global:", top_genre_2017)
print("2. Subgénero en el quinto lugar de ventas en 2020 en Europa:", subgenre_2020_eu)
print("3. Distribución de la inversión publicitaria por regiones:")
print(ad_investment)

print("Los gráficos se han generado correctamente.")