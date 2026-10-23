"""
Ejercicio 2
Localiza el error en el siguiente bloque de código. 
    Crea una excepción para evitar que el programa se bloquee 
    y además explica en un mensaje al usuario la causa y/o solución:

Codigo:
lista = [1, 2, 3, 4, 5]
lista[10]

"""
# EJERCICIO DE EXCEPCIONES: Excepcion "IndexError".

# lista = [1, 2, 3, 4, 5]
# lista[10]
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Excepciones\ejs2.py", line 12, in <module>
#     lista[10]
#     ~~~~~^^^^
# IndexError: list index out of range

try: 
    lista = [1, 2, 3, 4, 5]
    lista[10]

except IndexError: 
    print("ERROR, se intentó acceder a un valor inexistente de la lista.")
else:
    print("Todo ha funcionado correctamente")

# TESTs:
# TEST 01:
# ERROR, se intentó acceder a un valor inexistente de la lista.
