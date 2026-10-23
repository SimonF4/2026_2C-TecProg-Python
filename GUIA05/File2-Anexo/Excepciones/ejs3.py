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
    # Manejo con uso de get
    print(colores.get(buscado, "ERROR, no se encontro"))
    colores[buscado]

except KeyError as e:
    print(f"ERROR. No existe la clave {buscado} en el diccionario de colores actual.")
    print(f"La lista de colores solo tiene lo siguiente: {colores}")
    # Metodos de excepcion:
    print("Tipo de error: ", type(e))

else:
    print("Todo ha funcionado correctamente")

# TEST 01: Bien, error catcheado y explicado al usuario.
# ERROR. No existe la clave blanco en el diccionario de colores actual.
# La lista de colores solo tiene lo siguiente: {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
