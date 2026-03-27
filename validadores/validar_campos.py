from .regex_patterns import Alfanum11,Alfanum12, Alfanum15,num11,num6

def validar_NIU(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Código vacío"
    if valor == "MINIPAK" or valor == "MINSUP" or valor == "PAVSUP":
        return 2, "Advertencia : Código NIU con valor especial (MINIPAK, MINSUP o PAVSUP)"
    if not Alfanum12.match(valor):
        return False, f"Código NIU inválido: '{valor}' (debe ser de hasta 12 caracteres [numeros o letras] y comenzar con Frt)"
    return True, ""

def validar_comercializador(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":#Lo más probable es que quite la validación,y deje con regex apenas
        return False, "Código de comercializador vacío"#Dejar más explicito los campos a los que se esta refiriendo o el campo
    if not num6.match(valor):
        return False, f"Codigo de comercializador inválido: '{valor}' (debe ser de hasta 6 digitos)"
    return True, ""

def validar_nivel_tension_sec(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Nivel de tensión vacío"
    if not valor in ("0","1","2","3","4"):
        return False, f"Nivel de tensión inválido: '{valor}' (debe ser numérico, 0 o 1 o 2 o 3 o 4)"
    return True, ""

def validar_nivel_tension_prim(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Nivel de tensión vacío"
    if not valor in ("0","2","3"):
        return False, f"Nivel de tensión inválido: '{valor}' (debe ser numérico 0, 2 o 3)"
    return True, ""
#
# Mirar terminología de los campos de tension
#

def validar_cargo_inversion(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Cargo de inversión vacío"
    if not valor in ("0","50","100"):
        return False, f"Cargo de inversión inválido: '{valor}' (debe ser numérico 0, 50 o 100)"
    return True, ""


def validar_tipo_conexion(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Tipo de conexión vacío"
    if not valor in ("1","2"):
        return False, f"Tipo de conexión inválido: '{valor}' (debe ser numérico entre 1 o 2)"
    return True, ""


def validar_cod_conexion(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Código de conexión vacío"
    if not Alfanum15.match(valor):
        return False, f"Código de conexión inválido: '{valor}' (debe ser de hasta 15 caracteres [numeros o letras])"
    return True, ""


def validar_conex_red(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Código de conexión vacío"
    if not valor in ("1","2"):
        return False, f"Código de conexión inválido: '{valor}' (debe ser numérico entre 1 o 2)"
    return True, ""


def validar_consu_act(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "Consumo energía activa vacío"
    if not num11.match(valor):
        return False, f"Consumo energía activa inválido: '{valor}' (debe ser de hasta 11 digitos)"
    return True, ""

def validar_id_mercado(valor: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, "ID de mercado vacío"
    if not valor in ("176"):
        return False, f"ID de mercado inválido: '{valor}' (debe ser 176)"
    return True, ""


def validar_consistencias_tension_y_cargo(nivel_sec: str, nivel_prim: str, cargo_inv: str) -> list[str]:
    advertencias = []

    # Regla: para tensión secundaria 1, primaria solo puede ser 2 o 3.
    if nivel_sec == "1":
        if nivel_prim not in ("2", "3"):
            advertencias.append(
                f"Advertencia: Si nivel tensión secundaria es 1, tensión primaria debe ser 2 o 3, pero es '{nivel_prim}'"
            )
    else:
        if nivel_prim != "0":
            advertencias.append(
                f"Advertencia: Si nivel tensión secundaria es {nivel_sec}, tensión primaria debe ser 0, pero es '{nivel_prim}'"
            )

    # Regla: para tensión secundaria distinta de 1, el cargo de inversión debe ser 0.
    if nivel_sec != "1" and cargo_inv != "0":
        advertencias.append(
            f"Advertencia: Si nivel tensión secundaria es {nivel_sec}, cargo de inversión debe ser 0, pero es '{cargo_inv}'"
        )

    return advertencias