import pandas as pd

archivo_10 = r"C:\Users\Aspire 3\Documents\Proyecto Banco de sangre\2025-vih.txt"

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

# Elegimos las columnas que parecen más útiles según tu df.info()
columnas_interes = [
    'FECHAALTA', 
    'SEXO', 
    'EDADORDEN', 
    'ESTUDIODESCRIPCION', 
    'VARIABLEDESCRIPCION', 
    'RESULTADO'
]

# Creamos el nuevo DataFrame con esa selección
df_reducido = df[columnas_interes].copy()

# Comprobamos cómo quedó
print("Nuevo DataFrame creado con éxito:")
print(df_reducido.head())

# Verificamos la nueva información
print("\nInformación de tu nuevo dataset:")
print(df_reducido.info())

print("Formas en que están escritos los resultados:")
print(df['RESULTADO'].unique())

# 1. Convertir la columna RESULTADO a números
# 'errors=coerce' transforma automáticamente las palabras en NaN (nulos)
df['RESULTADO_NUMERICO'] = pd.to_numeric(df['RESULTADO'], errors='coerce')

# 2. Crear un nuevo DataFrame que solo contenga las filas que tienen números
# Usamos dropna en la columna que acabamos de crear
df_solo_numeros = df.dropna(subset=['RESULTADO_NUMERICO']).copy()

# 3. (Opcional) Borrar la columna vieja de texto si ya no la necesitás
# df_solo_numeros = df_solo_numeros.drop(columns=['RESULTADO'])

# 4. Ver los resultados
print("Ahora tenés un dataset puramente numérico:")
print(df_solo_numeros[['ESTUDIODESCRIPCION', 'RESULTADO_NUMERICO']].head(10))

# 5. Estadísticas rápidas de tus resultados numéricos
print("\nResumen estadístico de los valores:")
print(df_solo_numeros['RESULTADO_NUMERICO'].describe())