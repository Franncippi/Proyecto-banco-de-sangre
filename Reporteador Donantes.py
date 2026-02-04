import pandas as pd

archivo_10 = r"C:\Users\Aspire 3\Documents\Proyecto Banco de sangre\Semana 10.txt"

df = pd.read_csv(archivo_10, encoding='latin-1', sep=None, engine='python')


# 2. Ver la "cara" de los datos
print("Primeras filas del banco de sangre:")
print(df.head())

# 3. Información básica de las columnas
print("\nInformación del dataset:")
print(df.info())

# 1. Eliminar columnas que están 100% vacías
df = df.dropna(axis=1, how='all')

# Esto borra automáticamente todas las columnas que no tienen ni un solo dato
df = df.dropna(axis=1, how='all')

# Ahora veamos cuántas columnas nos quedaron
print(f"Ahora el dataset tiene {df.shape[1]} columnas en lugar de 31.")