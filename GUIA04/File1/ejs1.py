"""
1) Lista de alumnos: 
    cargar nombres, #{ingreso por teclado}  
    mostrar cantidad 
    y el primero/último. 
    Luego ordenar 
        y mostrar.
"""

nombres = []
nombre = None

while (nombre != "FIN"):
    nombre = input( "Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos." )
    nombres.append(nombre)
    
print(f"Cantidad de alumnos ingresados = {len(nombres)}")
print(f"Primer alumno ingresado = {nombres[0]}")
print(f"Ultimo alumno ingresado = {nombres[-1]}")

# Ordenar = sort
nombres.sort()
print(f"Lista de alumnos ordenada = {nombres}")

# TESTING:
# TEST 01:
# ERROR pequenio: Habia puesto mal el nombre de la variable nomas.

# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.A
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.B
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.C
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.D
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.FIN
# Cantidad de alumnos ingresados = 5
# Primer alumno ingresado = A
# Ultimo alumno ingresado = FIN
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA04\File1\ejs1.py", line 23, in <module>
#     print(f"Lista de alumnos ordenada = {amigos}")
#                                          ^^^^^^
# NameError: name 'amigos' is not defined

# TEST 02:
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.a
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.b
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.c
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.d
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.fin
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.FIN
# Cantidad de alumnos ingresados = 6
# Primer alumno ingresado = a
# Ultimo alumno ingresado = FIN
# Lista de alumnos ordenada = ['FIN', 'a', 'b', 'c', 'd', 'fin']

