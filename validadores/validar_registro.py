from logger import Logger

from .validar_campos import validar_NIU, validar_cod_conexion,validar_comercializador, validar_conex_red, validar_consu_act, validar_id_mercado,validar_nivel_tension_sec,validar_nivel_tension_prim,validar_cargo_inversion,validar_tipo_conexion, validar_consistencias_tension_y_cargo

def validar_registro(campos: list[str], num_fila: int) -> bool:
    """Valida un registro completo y reporta errores"""
    if len(campos) != 10:
        Logger.add_to_log("error", f"❌ Fila {num_fila}: Número incorrecto de campos ({len(campos)}, esperados 10)")
        #print(f"❌ Fila {num_fila}: Número incorrecto de campos ({len(campos)}, esperados 10)")
        return False
    
    errores = []
    advertencias = []
    
    # Validar cada campo
    ok, msg = validar_NIU(campos[0])
    if not ok: errores.append(msg)
    if ok == 2: advertencias.append(msg)
    
    ok, msg = validar_comercializador(campos[1])
    if not ok: errores.append(msg)
    
    ok, msg = validar_nivel_tension_sec(campos[2])
    if not ok: errores.append(msg)
    
    ok, msg = validar_nivel_tension_prim(campos[3])
    if not ok: errores.append(msg)
    
    ok, msg = validar_cargo_inversion(campos[4])
    if not ok: errores.append(msg)
    
    ok, msg = validar_tipo_conexion(campos[5])
    if not ok: errores.append(msg)
    
    ok, msg = validar_cod_conexion(campos[6])
    if not ok: errores.append(msg)
    
    ok, msg = validar_conex_red(campos[7])
    if not ok: errores.append(msg)
    
    ok, msg = validar_consu_act(campos[8])
    if not ok: errores.append(msg)

    ok, msg = validar_id_mercado(campos[9])
    if not ok: errores.append(msg)
    
    advertencias.extend(
        validar_consistencias_tension_y_cargo(
            campos[2],
            campos[3],
            campos[4],
        )
    )



    # Reportar resultado
    if errores:
        #print(f"\nFila {num_fila}: {campos}")
        #print(f"❌ Fila {num_fila}: {len(errores)} error(es)")
        #for...
        ##print(f"   • {error}")
    #else:
    ##print(f"✅ Fila {num_fila}: OK - {campos}")#Muestra los campos que están correctos, pero no es necesario


        Logger.add_to_log("info", f"Fila {num_fila}: {campos}")
        Logger.add_to_log("error", f"❌ Fila {num_fila}: {len(errores)} error(es)")

        for error in errores:
            Logger.add_to_log("error", f"   • {error}")
        return False
    elif advertencias:
        Logger.add_to_log("info", f"⚠️ Fila {num_fila}: {len(advertencias)} advertencia(s)")
        for advertencia in advertencias:
            Logger.add_to_log("warn", f"   • {advertencia}")
        return True