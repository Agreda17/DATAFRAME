import pandas as pd

# Definir la lista
lista = [['Juan', 25, 'Estudiante'],
         ['María', 30, 'Profesora'],
         ['Pedro', 35, 'Ingeniero'],
         ['Luisa', 28, 'Abogada']]

# Definir los nombres de las columnas
columnas = ['Nombre', 'Edad', 'Profesión']

# Crear el DataFrame
df = pd.DataFrame(lista, columns=columnas)

# Mostrar el DataFrame
print(df)