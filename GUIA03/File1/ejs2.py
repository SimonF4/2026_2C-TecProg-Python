# 2) Tabla de multiplicar: pedir un número y mostrar su tabla del 1 al 10.

num = input( "Ingrese un numero:" )

i = 1
fin = 10

for i in range( i, fin+1) :
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

# Test 02:
