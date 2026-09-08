# 2) Mayor de tres: leer tres números y mostrar cuál es el mayor (o si hay empates).
# Ingreso de texto:
num1 = float ( input("Ingrese el 1er numero:") )
num2 = float ( input("Ingrese el 2do numero:") )
num3 = float ( input("Ingrese el 1er numero:") )
mayor = "No existe un mayor."

# PROCESO:
# 1 es el mayor = 1>2 && 1>3
if (num1 > num2) :

    # Concateno con la anterior pregunta:
    if (num1 > num3) :
        mayor = num1
        # Sino = 1>2 && 3>1
    else :
        mayor = num3

# 2 es el mayor = 2>1 && 2>3
elif (num2 > num1) :

    if (num2 > num3) :
        mayor = num2
    else : 
        mayor = num3

# SALIDA:
print("El mayor de los 3 numeros es: ", mayor)
