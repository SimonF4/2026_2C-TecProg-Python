# 3. Promedio de notas: Leer tres notas y calcular el promedio.

# Pedir las 3 notas:
nota1 = float( input("Ingrese la 1er nota:") )
nota2 = float( input("Ingrese la 2da nota:") )
nota3 = float( input("Ingrese la 3er nota:") )
CANT_NOTAS = 3

# Calcular el promedio:
promedio = (nota1+nota2 + nota3) / CANT_NOTAS
# ejemplo division entera:
# promedio = (nota1+nota2 + nota3) // 3

# Mostrar resultado:
print(f"El promedio de {nota1}, {nota2} y {nota3} es = {promedio}")