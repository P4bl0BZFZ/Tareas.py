import pandas as pd
import matplotlib.pyplot as plt

#Paso 1: Análisis del Archivo de Datos
def analyze_data(filename):
    #Leer el archivo CSV
    data = pd.read_csv(filename)

    #Cambiar valores vacíos en la columna "Pais Residencia" por "SIN DATOS"
    data['Pais Residencia'] = data['Pais Residencia'].fillna('SIN DATOS') #Ocupamos fillna para la ayuda en cambiar los datos

    #Eliminar filas con valores vacíos
    data = data.dropna() #dropna para las filas con valores vacios

    #Eliminar el símbolo "$" de la columna "Salario"
    data['Salario'] = data['Salario'].str.replace('$', '') #replace remplaza los valores que le asignamos

    #Obtener estadísticas resumidas de dos columnas
    stats_col1 = data['Salario'].describe() #describe nos muestra el resumen de las columnas
    stats_col2 = data['Pais Residencia'].describe()

    # Imprimir las estadísticas
    print("Estadísticas:")
    print("=============")
    print(stats_col1)
    print()
    print("Estadísticas:")
    print("=============")
    print(stats_col2)

#Paso 2: Analítica de Datos 1
def has_children(data):
    #Función para determinar si una persona tiene hijos o no
    children = []
    for value in data['Hijos']:
        if value == 'Sí':
            children.append('Sí') 
        else:
            children.append('No')
    return children

def analyze_data_1(filename):
    #Leer el archivo CSV
    data = pd.read_csv(filename)

    # Crear una columna con información sobre si tienen hijos o no y si el número es mayor o igual a 0
    data['Tiene Hijos'] = ['Sí' if tiene_hijos > 0 else 'No' for tiene_hijos in data['Hijos']]

    #Asignar colores a los puntos según si tienen hijos o no
    colors = ['blue' if tiene_hijos == 'Sí' else 'red' for tiene_hijos in data['Tiene Hijos']]
    colors = [str(color) for color in colors]

    #Crear gráfico de dispersión
    plt.scatter(data['Contratacion'].astype(str), data['Pais Origen'].astype(str), c=colors) #usamos astype para convertir los datos 

    #Configurar título y etiquetas de los ejes
    plt.title('Relación entre Migrantes y Tener Hijos')
    plt.xlabel('Año')
    plt.ylabel('Número de Migrantes')

    #Mostrar el gráfico
    plt.show()

    #Imprimir conclusiones
    print("Conclusiones:")
    print("""Podemos sacar en conclusion que tanto en EE.UU, Brazil y 
             costa rica, tenemos una gran media de personas que no emigra con hijos.""")

def analyze_data_2(filename):
    #Leer el archivo CSV
    data = pd.read_csv(filename)

    #Filtrar registros de países de residencia "SIN DATOS" y contratados desde 2016 al 2021
    filtered_data = data[(data['Pais Residencia'] == 'SIN DATOS') & (data['Contratacion'].between(2016, 2021))]

    #Calcular el porcentaje acumulado de sueldos por país
    country_percentage = filtered_data.groupby('Pais Residencia')['Salario'].sum().sort_values(ascending=False).cumsum() / filtered_data['Salario'].sum() # groupby Nos ayuda a agrupar los datos
                                                                                     #sort_values ayuda a los Dataframe en las distintas columnas
    #Obtener los 6 países de mayor sueldo acumulado
    top_countries = country_percentage.head(6)

    # Mostrar dataframe resultante
    print("Dataframe Resultante:")
    print(top_countries)

    #Crear gráfico
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink']  # Colores personalizados
    plt.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%', colors=colors) #auto porcentaje

    #Configurar título y leyenda
    plt.title('Porcentaje de Sueldos Acumulado por País (2016-2021)')
    plt.legend(title='Países', loc='center left', bbox_to_anchor=(1, 0.5)) #Ajustamos en recuadro

    # Guardar el gráfico en un archivo
    plt.savefig('graph.png')

    # Guardar el dataframe resultante en un archivo
    top_countries.to_csv('DF_P3.txt', header=['Porcentaje Acumulado'])

    # Agregar interpretación del gráfico al archivo
    with open('DF_P3.txt', 'a') as file:
        file.write("\n\nInterpretación del gráfico:\n")
        file.write("El gráfico muestra el porcentaje acumulado de sueldos por país\n")
        file.write("para los trabajadores contratados desde 2016 al 2021, donde\n")
        file.write("los países de residencia son 'SIN DATOS'. Se han seleccionado\n")
        file.write("los 6 países con mayor sueldo acumulado para su visualización\n")
        file.write("en el gráfico de pastel. Cada porción del gráfico representa el\n")
        file.write("porcentaje acumulado de sueldos de un país en relación al total.")

# Llamar a la función analyze_data_2 con el nombre de tu archivo CSV
analyze_data_2('Empresas_Eight.csv')



# Menú Principal
def main_menu(filename):
    while True:
        print("         Menú Principal")
        print("=================================")
        print("[1] Análisis del Archivo de Datos")
        print("[2] Analítica de Datos 1")
        print("[3] Analítica de Datos 2")
        print("[4] Salir")
        print("=================================")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            analyze_data(filename)
        elif choice == '2':
            analyze_data_1(filename)
        elif choice == '3':
            analyze_data_2(filename)
        elif choice == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Nombre y apellido de los integrantes
integrantes = ["Matias Cardemil", "Nicolás Urmeneta","Pablo Bórquez"]

# Nombre del archivo de datos
filename = "Empresas_Eight.csv"

# Imprimir nombre y apellido de los integrantes
for integrante in integrantes:
    print(integrante)

# Ejecutar el programa
main_menu(filename)