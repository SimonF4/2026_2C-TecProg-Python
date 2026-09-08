# Ejercicios optativos / recomendados
# Ejercicio recomendado 2 – Validador de operación:
#       > pedir una operación (+, -, *, /).
#       > Si no es válida, mostrar mensaje.

operacion = input(
    "Elija y escriba uno de los siguientes operadores matematicos (+, -, *, /) :")
msg = "ERROR. Operacion invalida."

if (operacion == "+") :
    msg = "+"

elif (operacion == "-") :
    msg = "-"

elif (operacion == "*") :
    msg = "*"

elif (operacion == "/") :
    msg = "/"


print(f"Operacion seleccionada: {msg}")
