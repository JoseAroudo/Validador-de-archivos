import re

# Compilar regex una sola vez
REGEX_CODIGO = re.compile(r'^[A-Za-z0-9]{2}$')
REGEX_NOMBRE = re.compile(r'^[A-Za-zÁÉÍÓÚáéíóúÑñÜü .-]+$')
REGEX_FECHA = re.compile(r'^\d{2}-\d{2}-\d{4}$')