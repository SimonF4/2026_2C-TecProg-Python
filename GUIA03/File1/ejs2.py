# 2) Tabla de multiplicar: pedir un número y mostrar su tabla del 1 al 10.

num = int(input( "Ingrese un numero:" ))

i = 1
FIN = 10

for i in range( i, (FIN+1)) :
    multActual = num * i

    print(f"{num} * {i} = {multActual}")

print("Fin del Programa.")

# Test 01:
# Ingrese un numero:3
# 3 * 1 = 3
# 3 * 2 = 33
# 3 * 3 = 333
# 3 * 4 = 3333
# 3 * 5 = 33333
# 3 * 6 = 333333
# 3 * 7 = 3333333
# 3 * 8 = 33333333
# 3 * 9 = 333333333
# 3 * 10 = 3333333333
# Fin del Programa.

# rta: andaba mal pq me comi el casteo del ingreso en la 1er linea.

# Test 02:
# Ingrese un numero:1
# 1
# 1 * 1 = 1
# 2
# 1 * 2 = 2
# 3
# 1 * 3 = 3
# 4
# 1 * 4 = 4
# 5
# 1 * 5 = 5
# 6
# 1 * 6 = 6
# 7
# 1 * 7 = 7
# 8
# 1 * 8 = 8
# 9
# 1 * 9 = 9
# 10
# 1 * 10 = 10
# Fin del Programa.
