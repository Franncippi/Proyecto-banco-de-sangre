import pandas as pd

archivo_10 = r"C:\Users\Aspire 3\Documents\Proyecto Banco de sangre\Semana 10.txt"

df = pd.read_csv(archivo_10, encoding='latin-1', sep=None, engine='python')


# 2. Ver la "cara" de los datos
print("Primeras filas del banco de sangre:")
print(df.head())

# 3. Información básica de las columnas
print("\nInformación del dataset:")
print(df.info())
