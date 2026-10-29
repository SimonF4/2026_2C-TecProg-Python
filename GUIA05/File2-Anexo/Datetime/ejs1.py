"""
Ejercicios « Módulo Datetime
Ejercicio 1 - Formateo de Fechas
Crea un programa que:
    Muestra la fecha y hora actual en el siguiente formato:
        "Domingo 13 de Octubre del 2024 - 22:30"
    Usa locale para configurar el idioma en español.

Pista: Usa strftime para aplicar el formato.

"""

from datetime import datetime
import locale
# Seteamos el local siempre al inicio.
locale.setlocale(locale.LC_ALL, 'es-ES')

dt_actual = datetime.now()    # Fecha y hora actual
print(dt_actual)  # Resultado = 2026-10-28 20:34:58.270186

# strftime = Formateo manual (inglés por defecto):
dt_actual_formateado = dt_actual.strftime(
    "%A %d de %B del %Y - %I:%M")  # Ejemplo: Saturday 18 June 2024 09:37
print(dt_actual_formateado)

# Idioma "es-ES" (código para el español de España)
# Setear a esta altura del codigo el locale no modifica el resultado, tiene que ser siempre las primeras lineas de codigo.
# locale.setlocale(locale.LC_ALL, 'es-ES')
# print(dt_actual_formateado)


# TESTS:
# TEST 01: setLocale() abajo de todo el codigo.
# 2026-10-28 20:40:21.106186
# Wednesday 28 October 2026 08:40
# Wednesday 28 October 2026 08:40

# TEST 02: setLocale() arriba de todo.
# 2026-10-28 20:40:09.359882
# miércoles 28 octubre 2026 08:40
# miércoles 28 octubre 2026 08:40

# TEST 03: BIEN. Texto ahora si bien formateado como pide el ejs.
# 2026-10-28 20:50:12.348427
# miércoles 28 de octubre del 2026 - 08:50
