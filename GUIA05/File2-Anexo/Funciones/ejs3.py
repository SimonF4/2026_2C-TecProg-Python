"""
Ejercicio 3
Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
—------
def relacion(a, b):
    resu = 0
    if(a > b):
          resu = 1
    elseif(a < b):
           resu = -1
    else: 
           resu = 0

a = input(“Ingrese un primer numero”)
b = input(“Ingrese un segundo numero”)
print( relacion(a,b) )


"""


def relacion(a, b):
    resu = 0

    if (a > b):
        resu = 1

    elif (a < b):
        resu = -1

    else:
        resu = 0

    print("Resultados:" \
    "\n     +1 = Si el primer número es mayor que el segundo" \
    "\n     -1 = Si el primer número es menor que el segundo" \
    "\n      0 = Si ambos números son iguales")
    return f"El resultado de la relacion es = {resu}"


a = input("Ingrese un primer numero")
b = input("Ingrese un segundo numero")
print(relacion(a, b))

# TESTING:
# TEST 01:
# Ingrese un primer numero1
# Ingrese un segundo numero2
# Resultados:
#      +1 = Si el primer número es mayor que el segundo
#      -1 = Si el primer número es menor que el segundo
#       0 = Si ambos números son iguales
# El resultado de la relacion es = -1

