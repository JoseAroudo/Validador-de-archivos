import os

ruta_archivo = os.path.join(os.path.dirname(__file__), 'ventas1.txt')

# Leer archivo
with open(ruta_archivo, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# Separar encabezados y datos
encabezados = lineas[0].rstrip('\n').split('\t')  # Primera línea = columnas
filas_datos = []

for linea in lineas[1:]:  # Resto de líneas = datos
    columnas = linea.rstrip('\n').split('\t')
    filas_datos.append(columnas)

# Imprimir
print(f'Columnas: {encabezados}')
print('---')
for i, fila in enumerate(filas_datos, 1):
    print(f'Respuesta {fila[0]}: {fila}')