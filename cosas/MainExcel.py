import os
import pandas as pd

ruta_excel = os.path.join(os.path.dirname(__file__), 'ventas2.xlsx')

# Leer Excel
df = pd.read_excel(ruta_excel)

print(df.columns.tolist())  # Nombres de columnas
print('---')
print(df)  # Todos los datos
print('---')

# Iterar fila por fila
for index, fila in df.iterrows():
    print(f"ID: {fila['IDENTIFIC']}, Nombre: {fila['NOMBRE']}, Monto: {fila['MONTO']}, Fecha: {fila['FECHA']}")