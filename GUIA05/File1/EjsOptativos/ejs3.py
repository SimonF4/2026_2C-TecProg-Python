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
    fecha_date = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")

    # Pedir fecha:
    fecha_venc_str = input("Ingrese una fecha de vencimiento:")
    fecha_venc_date = datetime.strptime(fecha_venc_str, "%d/%m/%Y")

    print(fecha_date)
    print(fecha_venc_date)
    dias_restantes = fecha_venc_date - fecha_date
    print(dias_restantes)

    

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

