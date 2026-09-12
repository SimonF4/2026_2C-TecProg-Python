"""🟩 Ejercicio recomendado 1 – Menú de calculadora: sumar, restar, multiplicar y dividir. 
Validar división por cero."""

num1 = float(input("Ingrese el 1er numero: "))
num2 = float(input("Ingrese el 2do numero: "))
operacion = input(
    "Ingrese la operacion a realizar: suma, resta, multiplicacion y division (+, -, *, /)")
resultado = 0

# Para agregarle algo de bucles al ejs.
while ( operacion != "+" ) or ( operacion != "-" ) or ( operacion != "*" ) or( operacion != "/" ):
    operacion = input( 
        "Ingrese la operacion a realizar: suma, resta, multiplicacion y division (+, -, *, /)")


# Tdvia no usamos switch en el curso.
if ( operacion == "+" ):
    resultado = num1 + num2

elif ( operacion == "-" ):
    resultado = num1 - num2

elif ( operacion == "*" ):
    resultado = num1 * num2

# Si o si tuvo q haber ingresado "/" xq lo filtre con el while el ingreso. => Solo valido division por 0.
elif ( num2 != 0 ) :
    resultado = num1 / num2
else:
    print("ERROR, no se puede dividir por 0.")
    resultado = 0

print(f"El resultado de la {operacion} entre {num1} y {num2} es = {resultado}")

# TESTING:
