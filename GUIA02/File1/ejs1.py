# 1) Par o impar: leer un número entero y mostrar si es par o impar.
# Lectura
num1 = int(input("Ingrese el 1er numero:"))
res = ""

# OPERACION:
if (num1 % 2 == 0):
    res = "Par"
else:
    res = "Impar"

# Mostrar resultado
print(f"El numero {num1} es {res}")
