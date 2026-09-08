# Mini Calculadora
# Ingresar dos números y una operación (+, -, *, /). Mostrar el resultado. Validar división por cero.

num1 = float ( input("Ingrese el 1er numero:") )
num2 = float ( input("Ingrese el 2do numero:") )
operacion = input("Ingrese el char de operacion: ")
# Instanciar res previo al uso dentro de los condicionales.
res = 0

# OPERACION: Condicionales.
if operacion == "+" :
    res = num1 + num2
elif operacion == "-" :
    res = num1 - num2
elif operacion == "*" :
    res = num1 * num2
elif operacion == "/" :
    # Para la division por 0:
    if ( num2 != 0 ):
        res = num1 / num2
    else:
        print("ERROR, no se puede dividir por 0")
else:
    print("Error, valor invalido de operacion.")


# Mostrar por pantalla: validar previamente division por 0.
# En Python el and se pone con "and" y no con "&&"
if ( operacion == "/" ) and ( num2 == 0 ):
    print("ERROR, no se puede dividir por 0")
else:
    print(f"La {operacion} de {num1} y {num2} es = {res}")