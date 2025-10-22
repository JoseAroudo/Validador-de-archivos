# Validador de Archivos

Un validador de archivos en Python que revisa datos de archivos locales, detecta errores de formato o contenido y genera un log detallado con los fallos encontrados.

## 📋 Descripción

Este proyecto proporciona una herramienta de validación de archivos que permite verificar la integridad y el formato de datos en archivos locales. El sistema analiza el contenido del archivo según reglas de validación predefinidas y genera un registro completo de todos los errores encontrados durante el proceso de verificación.

## ✨ Características

- **Validación de datos**: Verifica la integridad y formato de los datos en archivos locales
- **Detección de errores**: Identifica errores de formato, contenido y estructura
- **Generación de logs**: Crea registros detallados con todos los errores encontrados
- **Múltiples formatos**: Soporte para diversos tipos de archivos (CSV, JSON, TXT, etc.)
- **Informes detallados**: Proporciona información específica sobre cada error detectado

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clona el repositorio:
```bash
git clone https://github.com/JoseAroudo/Validador-de-archivos.git
cd Validador-de-archivos
```

2. (Opcional) Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Uso básico

```python
from validador import ValidadorArchivos

# Crear una instancia del validador
validador = ValidadorArchivos('ruta/al/archivo.csv')

# Ejecutar la validación
resultados = validador.validar()

# Generar el log de errores
validador.generar_log('errores.log')
```

### Ejemplo con configuración personalizada

```python
from validador import ValidadorArchivos

# Configurar reglas de validación
reglas = {
    'formato': 'csv',
    'delimitador': ',',
    'encoding': 'utf-8',
    'columnas_requeridas': ['nombre', 'email', 'edad']
}

# Crear validador con configuración
validador = ValidadorArchivos('datos.csv', reglas=reglas)

# Validar y obtener resultados
if validador.validar():
    print("Archivo válido")
else:
    print(f"Se encontraron {validador.total_errores()} errores")
    validador.generar_log('log_errores.log')
```

## 📝 Formato del Log

El log de errores generado incluye la siguiente información:

```
[FECHA Y HORA] - ERROR - Tipo de error: [TIPO]
Línea: [NÚMERO DE LÍNEA]
Descripción: [DESCRIPCIÓN DETALLADA DEL ERROR]
Valor encontrado: [VALOR]
Valor esperado: [VALOR ESPERADO]
---
```

### Ejemplo de log:

```
2025-10-22 13:00:00 - ERROR - Tipo de error: FORMATO_INVALIDO
Línea: 15
Descripción: El formato del email no es válido
Valor encontrado: usuario@email
Valor esperado: formato_email_valido@dominio.com
---

2025-10-22 13:00:01 - ERROR - Tipo de error: CAMPO_REQUERIDO
Línea: 23
Descripción: Falta el campo obligatorio 'edad'
Valor encontrado: None
Valor esperado: Valor numérico
---
```

## 🔍 Tipos de Errores Detectados

El validador puede detectar diversos tipos de errores:

| Tipo de Error | Descripción |
|---------------|-------------|
| `FORMATO_INVALIDO` | El formato del dato no cumple con las especificaciones |
| `CAMPO_REQUERIDO` | Falta un campo obligatorio en el archivo |
| `TIPO_DATO_INCORRECTO` | El tipo de dato no coincide con el esperado |
| `VALOR_FUERA_RANGO` | El valor está fuera del rango permitido |
| `ENCODING_ERROR` | Error en la codificación del archivo |
| `ESTRUCTURA_INVALIDA` | La estructura del archivo no es correcta |
| `DUPLICADO` | Se encontraron valores duplicados donde no se permiten |

## ⚙️ Configuración

### Archivo de configuración

Puedes crear un archivo `config.json` para definir las reglas de validación:

```json
{
  "formato": "csv",
  "delimitador": ",",
  "encoding": "utf-8",
  "validaciones": {
    "columnas_requeridas": ["id", "nombre", "email"],
    "tipos_datos": {
      "id": "int",
      "nombre": "string",
      "email": "email"
    },
    "rangos": {
      "edad": {"min": 0, "max": 120}
    }
  },
  "log": {
    "ruta": "logs/errores.log",
    "nivel": "ERROR",
    "formato": "detallado"
  }
}
```

## 📊 Ejemplos

### Validar un archivo CSV

```python
validador = ValidadorArchivos('datos.csv')
validador.validar()
validador.generar_log('errores_csv.log')
```

### Validar un archivo JSON

```python
validador = ValidadorArchivos('datos.json', formato='json')
validador.validar()
validador.generar_log('errores_json.log')
```

### Obtener estadísticas de errores

```python
validador = ValidadorArchivos('datos.csv')
validador.validar()

stats = validador.obtener_estadisticas()
print(f"Total de errores: {stats['total']}")
print(f"Errores de formato: {stats['formato']}")
print(f"Campos faltantes: {stats['campos_faltantes']}")
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Jose Aroudo**

- GitHub: [@JoseAroudo](https://github.com/JoseAroudo)

## 📞 Soporte

Si encuentras algún problema o tienes alguna pregunta, por favor abre un [issue](https://github.com/JoseAroudo/Validador-de-archivos/issues) en GitHub.

## 🗺️ Roadmap

- [ ] Soporte para validación de archivos XML
- [ ] Interfaz gráfica de usuario (GUI)
- [ ] Generación de reportes en PDF
- [ ] Validación en tiempo real
- [ ] API REST para validación remota
- [ ] Integración con bases de datos

---

⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub
