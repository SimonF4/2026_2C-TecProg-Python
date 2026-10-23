"""
Ejercicio 4
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee 
    y además explica en un mensaje al usuario la causa y/o solución:

Codigo:
resultado = 15 + "20"
"""

# resultado = 15 + "20"
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Excepciones\ejs4.py", line 11, in <module>
#     resultado = 15 + "20"
#                 ~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    # Como seria para que no tire error:
    resultado = "20" + "20"
    print("suma de texto: ", resultado)
    resultado = 15 + 15
    print("suma de ints: ", resultado)

    resultado = 15 + "20"

except TypeError as e:
    print(f"Error de tipo de dato: no se puede sumar un entero y un String.")
    print(f"Mas detalles: {e.__doc__}")

else:
    print("Todo ha funcionado correctamente")

# TEST 01: 
# suma de texto:  2020
# suma de ints:  30
# Error de tipo de dato: no se puede sumar un entero y un String.
# Mas detalles: Inappropriate argument type.
