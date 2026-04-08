from logger import Logger

from .validar_campos import validar_NIU, validar_cod_conexion,validar_comercializador, validar_conex_red, validar_consu_act, validar_id_mercado,validar_nivel_tension_sec,validar_nivel_tension_prim,validar_cargo_inversion,validar_tipo_conexion, validar_consistencias_tension_y_cargo

def validar_registro(campos: list[str], num_fila: int) -> tuple[str, int, int]:
    """Valida un registro completo y reporta errores.
    
    Retorna: (estado, num_errores, num_advertencias)
    """
    if len(campos) != 10:
        Logger.add_to_log("error", f"❌ Fila {num_fila}: Número incorrecto de campos ({len(campos)}, esperados 10)")
        return "error", 1, 0
    
    errores = []
    advertencias = []
    
    # Validar cada campo usando tabla de validadores
    validadores = [
        (validar_NIU, campos[0], "NIU"),
        (validar_comercializador, campos[1], "comercializador"),
        (validar_nivel_tension_sec, campos[2], "nivel_tension_sec"),
        (validar_nivel_tension_prim, campos[3], "nivel_tension_prim"),
        (validar_cargo_inversion, campos[4], "cargo_inversion"),
        (validar_tipo_conexion, campos[5], "tipo_conexion"),
        (validar_cod_conexion, campos[6], "cod_conexion"),
        (validar_conex_red, campos[7], "conex_red"),
        (validar_consu_act, campos[8], "consu_act"),
        (validar_id_mercado, campos[9], "id_mercado"),
    ]
    
    for validador, valor, _ in validadores:
        ok, msg = validador(valor)
        if ok == 2:  # Caso especial: NIU con valor especial
            advertencias.append(msg)
        elif not ok:
            errores.append(msg)
    
    # Validar consistencias entre campos
    advertencias.extend(
        validar_consistencias_tension_y_cargo(
            campos[2],
            campos[3],
            campos[4],
        )
    )
    
    # Reportar resultado
    estado = "ok"
    if errores:
        Logger.add_to_log("info", f"\n\nFila {num_fila}: {campos}")
        Logger.add_to_log("error", f"❌ Fila {num_fila}: {len(errores)} error(es)")

        if advertencias:
            Logger.add_to_log("info", f"⚠️ Fila {num_fila}: {len(advertencias)} advertencia(s)")
            for advertencia in advertencias:
                Logger.add_to_log("warn", f"   • {advertencia}")

        for error in errores:
            Logger.add_to_log("error", f"   • {error}")
        
        estado = "error_warning" if advertencias else "error"
    elif advertencias:
        Logger.add_to_log("info", f"⚠️ Fila {num_fila}: {len(advertencias)} advertencia(s)")
        for advertencia in advertencias:
            Logger.add_to_log("warn", f"   • {advertencia}")
        estado = "warning"
    
    return estado, len(errores), len(advertencias)


def validar_archivo(lineas: list[str]) -> dict:
    """Procesa todos los registros del archivo y genera dos tipos de resumen.
    
    Args:
        lineas: Lista de líneas del archivo (incluyendo encabezado)
    
    Retorna: Dict con resumen de filas y resumen de errores/advertencias totales
    """
    filas_validas = 0
    filas_con_problemas = 0
    total_errores = 0
    total_advertencias = 0
    
    # Procesar cada fila (saltar encabezado en índice 0)
    for i, linea in enumerate(lineas[1:], start=1):
        campos = linea.rstrip('\n').split(';')
        _, errores_fila, advertencias_fila = validar_registro(campos, i)
        
        total_errores += errores_fila
        total_advertencias += advertencias_fila
        
        if errores_fila == 0 and advertencias_fila == 0:
            filas_validas += 1
        else:
            filas_con_problemas += 1
    
    return {
        "resumen_filas": {
            "validas": filas_validas,
            "con_problemas": filas_con_problemas,
            "total": len(lineas) - 1,
        },
        "resumen_datos": {
            "total_errores": total_errores,
            "total_advertencias": total_advertencias,
            "total_registros": len(lineas) - 1,
        },
    }
