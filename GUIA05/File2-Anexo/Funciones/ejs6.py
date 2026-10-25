"""
Ejercicio 6 (recomendado) ⭐
Realiza una función separar(lista) 
que tome
      una lista de números enteros
      y devuelva dos listas ordenadas.
               La primera con los números pares 
               y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]
[1, 5, 7]
Sugerencia
Para ordenar una lista automáticamente puedes utilizar el método .sort().

"""

# EJS DE LA CLASE 31 - 20/10/26.

def separar(lista):
    """ Docstring: Metodo para separar una lista ingresada. Devuelve 2 listas: pares e impares."""
    list_pares = []
    list_impares = []

    # PROCESO:
    # Sin usar .sort(): Xq ese metodo no te sirve para separar en pares e impares.
    for num in lista:
        if (num % 2 == 0):
            list_pares.append(num)
        else:
            list_impares.append(num)

    # OPCION 2:
    #           Hacerlo en 1 linea.
    # pares = [n for n in numeros if n % 2 == 0]
    # impares = [n for n in numeros if n % 2 != 0]

    # .sort() aca si nos sirve: Para ordenar las listas resultantes.
    list_pares.sort()
    list_impares.sort()

    return list_pares, list_impares

pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)

# TESTING:
# TEST 01: Bien.
# [2, 6]
# [1, 5, 7]
