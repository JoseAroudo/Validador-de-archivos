from .validar_campos import validar_codigo, validar_nombre, validar_monto, validar_fecha

def validar_registro(campos: list[str], num_fila: int) -> bool:
    """Valida un registro completo y reporta errores"""
    if len(campos) != 4:
        print(f"❌ Fila {num_fila}: Número incorrecto de campos ({len(campos)}, esperados 4)")
        return False
    
    errores = []
    
    # Validar cada campo
    ok, msg = validar_codigo(campos[0])
    if not ok: errores.append(msg)
    
    ok, msg = validar_nombre(campos[1])
    if not ok: errores.append(msg)
    
    ok, msg = validar_monto(campos[2])
    if not ok: errores.append(msg)
    
    ok, msg = validar_fecha(campos[3])
    if not ok: errores.append(msg)
    
    # Reportar resultado
    if errores:
        print(f"\nFila {num_fila}: {campos}")
        print(f"❌ Fila {num_fila}: {len(errores)} error(es)")
        for error in errores:#Primera fila es encabezado y lo valida
            print(f"   • {error}")
        return False
    else:
        print(f"✅ Fila {num_fila}: OK - {campos}")
        return True