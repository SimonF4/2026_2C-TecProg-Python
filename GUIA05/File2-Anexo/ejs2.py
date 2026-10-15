"""
Ejercicios de Funciones

Ejercicio 1
    Realiza una función llamada area_rectangulo(base, altura) 
        que devuelva 
            el área del rectángulo 
        a partir de 
            una base 
            y una altura. 
        Calcula 
            el área de un rectángulo de 15 de base y 10 de altura:
    
    Recordatorio
    El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""

def area_rectangulo(base, altura):
    return base * altura

base = 15
altura = 10
print(f"El area de un rectangulo de base {base} y altura {altura} es = {area_rectangulo(base, altura)}")

# TESTING:
# TEST 01: bien.
# El area de un rectangulo de base 15 y altura 10 es = 150
