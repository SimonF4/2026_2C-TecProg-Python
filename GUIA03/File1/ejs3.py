# 3) Contar positivos: ir pidiendo números hasta ingresar 0; mostrar cuántos fueron positivos.

res = 0
num_ingresado = float(input("Ingrese un numero o 0 para terminar el programa."))

while ( num_ingresado != 0 ) :
    if ( num_ingresado > 0 ):
        res += 1

    num_ingresado = float(input("Ingrese un numero o 0 para terminar el programa."))

print(f"Resultado: Se ingresaron {res} numeros positivos.")

# TEST:
# Ingrese un numero o 0 para terminar el programa.-1
# Ingrese un numero o 0 para terminar el programa.-2
# Ingrese un numero o 0 para terminar el programa.-3
# Ingrese un numero o 0 para terminar el programa.0
# Resultado: Se ingresaron 0 numeros positivos.

# Ingrese un numero o 0 para terminar el programa.-1
# Ingrese un numero o 0 para terminar el programa.1
# Ingrese un numero o 0 para terminar el programa.6
# Ingrese un numero o 0 para terminar el programa.0
# Resultado: Se ingresaron 2 numeros positivos.

