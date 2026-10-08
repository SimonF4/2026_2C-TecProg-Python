# 3) Unión sin duplicados: 
#       dadas dos listas, 
#       unirlas en una tercera 
#           sin repetidos (usar set).

lista_1 = [1, 2, 3, 4, 5]
conjunto_1 = set()
lista_2 = [2, 4, 6, 8, 10]
conjunto_2 = set()
lista_3 = []
conjunto_3 = set()

# Mostramos las listas:
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)

# Conversiones con listas
conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)
# Usamos el metodo union() de conjuntos (no es de listas => hay q convertirlos a conjuntos)
conjunto_3 = conjunto_1.union(conjunto_2)
# Lo convertimos de nuevo a lista.
lista_3 = list(conjunto_3)


print("Lista 3 (union de las 2 listas anteriores, sin repetidos):", lista_3)

# TESTEOS:
# Test 01: Fallaba pq no use el metodo "union()"
# Lista 1: [1, 2, 3, 4, 5]
# Lista 2: [2, 4, 6, 8, 10]
# Lista 3 (union de las 2 listas anteriores, sin repetidos): [2, 4, 6, 8, 10]

# TEST 02: Anda bien.
# Lista 1: [1, 2, 3, 4, 5]
# Lista 2: [2, 4, 6, 8, 10]
# Lista 3 (union de las 2 listas anteriores, sin repetidos): [1, 2, 3, 4, 5, 6, 8, 10]
