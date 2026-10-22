"""
Ejercicios « Errores y excepciones
Ejercicio 1 (recomendado) ⭐
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

resultado = 10/0

"""

# resultado = 10/0
# RESULTADO: 
# "
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Excepciones\ejs1.py", line 10, in <module>
#     resultado = 10/0
#                 ~~^~
# ZeroDivisionError: division by zero
# "

try:
    a = (int) (input("Ingrese un numero."))
    b = (int) (input("Ingrese el numero por el cual se lo va a dividir (/)."))
    print(f"resultado = { a / b}")

except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número.")

else:
    print("Todo ha funcionado correctamente")

# TESTs:
# TEST 01:
# Ingrese un numero.10
# Ingrese el numero por el cual se lo va a dividir (/).0
# No se puede dividir por cero, prueba otro número.

# TEST 02:
# Ingrese un numero.5
# Ingrese el numero por el cual se lo va a dividir (/).7
# resultado = 0.7142857142857143
# Todo ha funcionado correctamente
