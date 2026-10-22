"""
Ejercicio 3
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee 
    y además explica en un mensaje al usuario la causa y/o solución:

Codigo:
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']
"""

# colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
# colores['blanco']
# RESULTADO:
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Excepciones\ejs3.py", line 13, in <module>
#     colores['blanco']
#     ~~~~~~~^^^^^^^^^^
# KeyError: 'blanco'

try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
    buscado = 'blanco'
    colores[buscado]

except KeyError:
    print(f"ERROR. No existe la clave {buscado} en el diccionario de colores actual.")
    print(f"La lista de colores solo tiene lo siguiente: {colores}")

else:
    print("Todo ha funcionado correctamente")

# TEST 01: Bien, error catcheado y explicado al usuario.
# ERROR. No existe la clave blanco en el diccionario de colores actual.
# La lista de colores solo tiene lo siguiente: {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
