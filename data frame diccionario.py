import pandas as pd

# Definir el diccionario
diccionario = {
    'Nombre': ['lucas', 'fernanda', 'Pedro', 'Luis'],
    'Edad': [28, 35, 40, 30],
    'Profesión': ['Estudiante', 'Profesora', 'Padre ', 'Albañil']
}

# Crear el DataFrame
df = pd.DataFrame(diccionario)

# Mostrar el DataFrame
print(df)
