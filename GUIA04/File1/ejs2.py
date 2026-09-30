"""
2) Agenda simple: 
    diccionario {nombre: teléfono}. 
    Permitir 
        agregar 
        y consultar 
        por nombre.
"""

diccionario = {}
print(type(diccionario)) # Para testear.
nombre = input("Ingrese su nombre")
# i = 0


while (nombre.upper() != "FIN"):
    # Sin validación de número de teléfono 
    numero = input("Ingrese número de teléfono")
    # agregar al diccionario = usar la definición y guardarle un valor.
    diccionario[nombre] = numero
    nombre = input("Ingrese su nombre")


for nombre in diccionario:
    print(nombre, diccionario[nombre])

print( diccionario ) # Para test nomás.

# TESTING:
# TEST01:
    # <class 'dict'>
    # Ingrese su nombrea
    # Ingrese número de teléfono123
    # Ingrese su nombreb
    # Ingrese número de teléfono345
    # Ingrese su nombrefin
    # a 123
    # b 345
    # {'a': '123', 'b': '345'}

