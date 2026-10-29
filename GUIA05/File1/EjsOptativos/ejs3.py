"""
🟩 Ejercicio recomendado 3 – 

Control de vencimientos (datetime):
Crear una función parse_fecha(fecha_str) 
    que convierta 'DD/MM/AAAA' 
                    a date. 
    Luego pedir al usuario una fecha de vencimiento 
        y calcular cuántos días faltan desde hoy. 
    
    Si ya venció, informar cuántos días pasaron.
"""
from datetime import datetime


def parse_fecha(fecha_str):
    """ Docstring: Ingreso = string en formato 'DD/MM/AAAA'. Return = dias faltantes o si vencio."""
    resultado = ""

    # Conversion:
    fecha_date = datetime.strptime(fecha_str, "%d/%m/%Y")

    # Pedir fecha:
    fecha_venc_str = input("Ingrese una fecha de vencimiento:")
    fecha_venc_date = datetime.strptime(fecha_venc_str, "%d/%m/%Y")

    print(fecha_date)
    print(fecha_venc_date)
    dias_restantes = fecha_venc_date - fecha_date
    print(dias_restantes)

    # Se podria pasar a parte de este metodo, por exceso de funcionalidades. Pero el enunciado lo pide hacer todo en el mismo metodo.
    # "Si ya venció, informar cuántos días pasaron."
    resultado = evaluar_vencimiento(dias_restantes)

    return resultado

def evaluar_vencimiento(dias_restantes):
    if(dias_restantes.days < 0):
        resultado = f"CUIDADO!!! Producto ya vencido hace {dias_restantes}."     # Resultado = te pone por ej.: "-67 days".
    else:
        resultado = f"El producto vencera dentro de {dias_restantes.days} dias." # Resultado = con .days te da solo el numero.

    return resultado

print(parse_fecha("01/01/2027"))

# TESTINGs:
# TEST 01: ERROR. Motivo: me sobraba H y M en el formato, pq no le puso hora y mins cuando llame al metodo => no coincide => error.
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File1\EjsOptativos\ejs3.py", line 38, in <module>
#     parse_fecha("01/01/2027")
#     ~~~~~~~~~~~^^^^^^^^^^^^^^
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File1\EjsOptativos\ejs3.py", line 21, in parse_fecha
#     fecha_date = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
#   File "C:\Users\Yo\AppData\Local\Programs\Python\Python313\Lib\_strptime.py", line 789, in _strptime_datetime
#     tt, fraction, gmtoff_fraction = _strptime(data_string, format)
#                                     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Yo\AppData\Local\Programs\Python\Python313\Lib\_strptime.py", line 555, in _strptime
#     raise ValueError("time data %r does not match format %r" %
#                      (data_string, format))
# ValueError: time data '01/01/2027' does not match format '%d/%m/%Y %H:%M'

# TEST 02: ERROR. Motivo: 
# Ingrese una fecha de vencimiento:27/10/2026
# 2027-01-01 00:00:00
# 2026-10-27 00:00:00
# -66 days, 0:00:00
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File1\EjsOptativos\ejs3.py", line 41, in <module>
#     parse_fecha("01/01/2027")
#     ~~~~~~~~~~~^^^^^^^^^^^^^^
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File1\EjsOptativos\ejs3.py", line 32, in parse_fecha
#     if(dias_restantes < 0):
#        ^^^^^^^^^^^^^^^^^^
# TypeError: '<' not supported between instances of 'datetime.timedelta' and 'int'

# TEST 03: BIEN.
# Ingrese una fecha de vencimiento:26/10/2026
# 2027-01-01 00:00:00
# 2026-10-26 00:00:00
# -67 days, 0:00:00
# Producto ya vencido -67 days, 0:00:00 por dias.

# TEST 04:
# Ingrese una fecha de vencimiento:01/02/2030
# 2027-01-01 00:00:00
# 2030-02-01 00:00:00
# 1127 days, 0:00:00
# El producto vencera dentro de 1127 dias.
