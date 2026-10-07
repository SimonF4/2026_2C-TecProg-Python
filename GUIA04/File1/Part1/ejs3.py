# 3) Unión sin duplicados: 
#       dadas dos listas, 
#       unirlas en una tercera 
#           sin repetidos (usar set).

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [2, 4, 6, 8, 10]
lista_3 = []
conjunto = set()

# Mostramos las listas:
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)

# Conversiones con listas
conjunto = set(lista_1)
conjunto = set(lista_2)
lista_3 = list(conjunto)


print("Lista 3 (union de las 2 listas anteriores, sin repetidos):", lista_3)

# TESTEOS:
# test 01:
# Lista 1: [1, 2, 3, 4, 5]
# Lista 2: [2, 4, 6, 8, 10]
# Lista 3 (union de las 2 listas anteriores, sin repetidos): [2, 4, 6, 8, 10]

