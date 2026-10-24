"""
Ejercicio 2 (recomendado) ⭐
Realiza una función llamada area_circulo(radio) 
    que devuelva 
        el área de un círculo 
            a partir de un radio. 

Calcula el área de un círculo de 5 de radio:

Recordatorio
El área de un círculo se obtiene al
     elevar el radio a dos y multiplicando el resultado por el número pi. 
        Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:
            import math

            print(math.pi)
            3.141592653589793
"""
import math

def area_circulo(radio):
    # Potencia/exponente en Python es con: "**". Ej: "5**2".
    return (radio ** 2) * math.pi



radio = 5
print(math.pi)
print(f"El area de un circulo de radio {radio} es = {area_circulo(radio)}")

# TESTING:
# TEST 01:
# El area de un circulo de radio 5 es = 78.53981633974483