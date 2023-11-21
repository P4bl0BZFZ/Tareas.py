import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('Empresas_Eight.csv')

# Convertir las columnas a tipo string
datos['Contratacion'] = datos['Contratacion'].astype(str)
datos['Pais Origen'] = datos['Pais Origen'].astype(str)

# Obtener los datos para el gráfico
x = datos['Contratacion']
y = datos['Pais Origen']
colors = datos['Hijos'].map({'Con hijos': 'blue', 'Sin hijos': 'red'})

# Crear el gráfico de dispersión
plt.scatter(x, y, c=colors)

# Personalizar el gráfico
plt.title("Relación entre el número de personas migradas y si tienen hijos")
plt.xlabel("Contratacion")
plt.ylabel("Pais Origen")

# Mostrar el gráfico
plt.show()
