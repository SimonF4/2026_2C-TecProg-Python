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





print(f"El resultado de la {operacion} entre {num1} y {num2} es = {resultado}")