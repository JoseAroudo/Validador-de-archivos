from typing import Pattern

from .regex_patterns import Alfanum12, Alfanum15, num11, num6

ESTADOS_NIU_ESPECIALES = {"MINIPAK", "MINSUP", "PAVSUP"}
NIVELES_TENSION_SEC = {"0", "1", "2", "3", "4"}
NIVELES_TENSION_PRIM = {"0", "2", "3"}
CARGOS_INVERSION = {"0", "50", "100"}
TIPOS_CONEXION = {"1", "2"}
ID_MERCADO_VALIDO = "176"


def _validar_requerido(valor: str, mensaje_vacio: str) -> tuple[bool, str]:
    if valor.strip() == "":
        return False, mensaje_vacio
    return True, ""


def _validar_con_regex(
    valor: str,
    patron: Pattern[str],
    mensaje_vacio: str,
    mensaje_invalido: str,
) -> tuple[bool, str]:
    ok, msg = _validar_requerido(valor, mensaje_vacio)
    if not ok:
        return ok, msg
    if not patron.match(valor):
        return False, mensaje_invalido
    return True, ""


def _validar_en_conjunto(
    valor: str,
    valores_validos: set[str],
    mensaje_vacio: str,
    mensaje_invalido: str,
) -> tuple[bool, str]:
    ok, msg = _validar_requerido(valor, mensaje_vacio)
    if not ok:
        return ok, msg
    if valor not in valores_validos:
        return False, mensaje_invalido
    return True, ""


def validar_NIU(valor: str) -> tuple[bool | int, str]:
    ok, msg = _validar_requerido(valor, "Código vacío")
    if not ok:
        return ok, msg

    if valor in ESTADOS_NIU_ESPECIALES:
        return 2, "Código NIU con valor especial (MINIPAK, MINSUP o PAVSUP)"

    if not Alfanum12.match(valor):
        return False, f"Código NIU inválido: '{valor}' (debe ser de hasta 12 caracteres [numeros o letras] y comenzar con Frt)"
    return True, ""


def validar_comercializador(valor: str) -> tuple[bool, str]:
    return _validar_con_regex(
        valor,
        num6,
        "Código de comercializador vacío",
        f"Codigo de comercializador inválido: '{valor}' (debe ser de hasta 6 digitos)",
    )


def validar_nivel_tension_sec(valor: str) -> tuple[bool, str]:
    return _validar_en_conjunto(
        valor,
        NIVELES_TENSION_SEC,
        "Nivel de tensión vacío",
        f"Nivel de tensión inválido: '{valor}' (debe ser numérico, 0 o 1 o 2 o 3 o 4)",
    )


def validar_nivel_tension_prim(valor: str) -> tuple[bool, str]:
    return _validar_en_conjunto(
        valor,
        NIVELES_TENSION_PRIM,
        "Nivel de tensión vacío",
        f"Nivel de tensión inválido: '{valor}' (debe ser numérico 0, 2 o 3)",
    )


def validar_cargo_inversion(valor: str) -> tuple[bool, str]:
    return _validar_en_conjunto(
        valor,
        CARGOS_INVERSION,
        "Cargo de inversión vacío",
        f"Cargo de inversión inválido: '{valor}' (debe ser numérico 0, 50 o 100)",
    )


def validar_tipo_conexion(valor: str) -> tuple[bool, str]:
    return _validar_en_conjunto(
        valor,
        TIPOS_CONEXION,
        "Tipo de conexión vacío",
        f"Tipo de conexión inválido: '{valor}' (debe ser numérico entre 1 o 2)",
    )


def validar_cod_conexion(valor: str) -> tuple[bool, str]:
    return _validar_con_regex(
        valor,
        Alfanum15,
        "Código de conexión vacío",
        f"Código de conexión inválido: '{valor}' (debe ser de hasta 15 caracteres [numeros o letras])",
    )


def validar_conex_red(valor: str) -> tuple[bool, str]:
    return _validar_en_conjunto(
        valor,
        TIPOS_CONEXION,
        "Código de conexión vacío",
        f"Código de conexión inválido: '{valor}' (debe ser numérico entre 1 o 2)",
    )


def validar_consu_act(valor: str) -> tuple[bool, str]:
    return _validar_con_regex(
        valor,
        num11,
        "Consumo energía activa vacío",
        f"Consumo energía activa inválido: '{valor}' (debe ser de hasta 11 digitos)",
    )


def validar_id_mercado(valor: str) -> tuple[bool, str]:
    ok, msg = _validar_requerido(valor, "ID de mercado vacío")
    if not ok:
        return ok, msg
    if valor != ID_MERCADO_VALIDO:
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