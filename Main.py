from validadores.validar_registro import validar_registro
from Presentacion import mostrar_entrada_archivo


from logger import Logger


p = mostrar_entrada_archivo()


with open(p, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

#print(f"Procesando {len(lineas)-1} líneas...\n")

validos = 0
invalidos = 0
advertencias = 0

for i, linea in enumerate(lineas[1:], start=1):
    campos = linea.rstrip('\n').split(';')
    if validar_registro(campos, i):
        validos += 1
    elif not validar_registro(campos, i):
        invalidos += 1
    else:
        advertencias += 1
        Logger.add_to_log("warn", f"⚠️ Fila {i}: Advertencia al validar")


Logger.add_to_log("warn", "="*74)
Logger.add_to_log("info", f"Resumen: {validos} válidos, {invalidos} inválidos y {advertencias} advertencias de {len(lineas)-1} total")
Logger.add_to_log("warn", "="*74)