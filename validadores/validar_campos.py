from .regex_patterns import REGEX_CODIGO, REGEX_NOMBRE, REGEX_FECHA

def validar_codigo(valor: str) -> tuple[bool, str]:
    if not REGEX_CODIGO.match(valor):
        return False, f"Código inválido: '{valor}' (debe ser 2 caracteres alfanuméricos)"
    return True, ""

def validar_nombre(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Nombre vacío"
    if len(valor) > 50:
        return False, f"Nombre muy largo: {len(valor)} caracteres (máx 50)"
    if not REGEX_NOMBRE.match(valor):
        return False, f"Nombre contiene caracteres inválidos: '{valor}'"
    if not valor.isupper():
        return False, f"Nombre debe estar en mayúsculas: '{valor}'"
    return True, ""

def validar_monto(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Monto vacío"
    if len(valor) > 10:
        return False, f"Monto muy largo: {len(valor)} dígitos (máx 10)"
    if not valor.isdigit():
        return False, f"Monto debe ser numérico: '{valor}'"
    return True, ""

def validar_fecha(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Fecha vacía"
    if len(valor) != 10:
        return False, f"Fecha con longitud incorrecta: '{valor}' (debe ser DD/MM/YYYY)"
    if valor.count('-') != 2:
        return False, f"Fecha sin separadores correctos: '{valor}'"
    if not REGEX_FECHA.match(valor):
        return False, f"Formato de fecha inválido: '{valor}' (use DD/MM/YYYY)"
    return True, ""