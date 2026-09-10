# Ejercicios obligatorios
# 1) Suma de los primeros N números: implementar con for y con while.

# inicio
i = 0
# fin
n = 2
suma = 0

# Con for:
# Pensaba q era asi pero no: for (i, n, 1) :
for i in range(i, n+1, 1) :
    print(i)
    suma += i
    # el range() ya te salta de 1 en 1.

print (f"Suma de los primeros {n} numeros, con for: {suma}")

i = 0
suma = 0
# Con while:
# Con (i < 0), como en el ejemplo de la guia, da bucle infinito.
while ( i < n+1 ) :
    print(i)
    suma += i
    i += 1
    # i++: No lo toma, tira error.

print (f"Suma de los primeros {n} numeros, con while: {suma}")

# TEST 01:
# Suma de los primeros 6 numeros, con for: 15
# Suma de los primeros 6 numeros, con while: 20

# TEST 02:
# 0
# 1
# 2
# Suma de los primeros 2 numeros, con for: 3
# 2
# Suma de los primeros 2 numeros, con while: 5

# TEST 03:
# 0
# 1
# 2
# Suma de los primeros 2 numeros, con for: 3
# 0
# 1
# 2
# Suma de los primeros 2 numeros, con while: 6

# TEST 04:
# 0
# 1
# 2
# Suma de los primeros 2 numeros, con for: 3
# 0
# 1
# 2
# Suma de los primeros 2 numeros, con while: 3
