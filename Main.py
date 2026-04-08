from validadores.validar_registro import validar_archivo
from Presentacion import mostrar_entrada_archivo


from logger import Logger


p = mostrar_entrada_archivo()


with open(p, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# Procesar y generar resumen
resumen = validar_archivo(lineas)

# Reportar
Logger.add_to_log("warn", "="*74)
Logger.add_to_log("info", f"Resumen de Filas: {resumen['resumen_filas']['validas']} válidos, {resumen['resumen_filas']['con_problemas']} con problemas de {resumen['resumen_filas']['total']} registros")
Logger.add_to_log("info", f"Resumen de Datos: {resumen['resumen_datos']['total_errores']} errores totales y {resumen['resumen_datos']['total_advertencias']} advertencias totales")
Logger.add_to_log("warn", "="*74)