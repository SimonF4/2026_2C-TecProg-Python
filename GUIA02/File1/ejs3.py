# 3) Promedio y condición: 
#       leer tres notas, 
#       calcular el promedio 
#       y mostrar “Aprobado/Recupera/Desaprobado”.

# LECTURA:
num1 = float ( input("Ingrese el 1er numero:") )
num2 = float ( input("Ingrese el 2do numero:") )
num3 = float ( input("Ingrese el 3er numero:") )
promedio = 0
CANT_NUM = 3
res = ""

# PROCESO:
promedio = ( num1+num2+num3 ) / CANT_NUM

if (promedio > 7) : 
    res = "APROBADO :D"
elif ( promedio > 4 ) :
    res = "RECUPERA :/"
else:
    res = "DESAPROBADO :("

# SALIDA:
print(f"El promedio fue {promedio}. El alumno esta {res}")
