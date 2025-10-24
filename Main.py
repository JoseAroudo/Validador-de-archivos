import os

from validadores.validar_registro import validar_registro

    
# Main
p = os.path.join(os.path.dirname(__file__), 'ventas1.txt')

with open(p, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

print(f"Procesando {len(lineas)} líneas...\n")

validos = 0
invalidos = 0

for i, linea in enumerate(lineas, start=1):
    campos = linea.rstrip('\n').split('\t')
    if validar_registro(campos, i):
        validos += 1
    else:
        invalidos += 1

print(f"\n{'='*50}")
print(f"Resumen: {validos} válidos, {invalidos} inválidos de {len(lineas)} total")