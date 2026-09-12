# 🟩 Ejercicio recomendado 2 – Filtro de lista: dada una lista de números, generar otra con solo los pares (for y comprensión de listas).

# "dada una lista de números"
list_numeros = list( range(0, 5, 1) )
# Esta es una forma de crear una listas vacia:
list_resultado = list()

for i in list_numeros:
    print(list_numeros[i])

    # "generar otra con solo los pares"
    if (i % 2 == 0):
        # Para agregar 1 valor a list -> con .append(valor)
        list_resultado.append(i)

    i+=1

print(list_resultado)

# TESTING:
# TEST 01:
# 0
# 1
# 2
# 3
# 4
# [0, 2, 4]
