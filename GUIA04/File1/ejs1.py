"""
1) Lista de alumnos: 
    cargar nombres, #{ingreso por teclado}  
    mostrar cantidad 
    y el primero/último. 
    Luego ordenar 
        y mostrar.
"""
# No incluye validaciones por 0.

nombres = []
nombre = input( "Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos." )

# .upper() = detalle para q tome tmb "fin" en minuscula.
while (nombre.upper() != "FIN"):
    nombres.append(nombre)
    nombre = input( "Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos." )
    #if (nombre != "FIN"): #Era para q no me sume el ultimo (FIN) a la lista. No es necesario si pongo el append() primero y un input fuera del bucle.
    
print(f"Cantidad de alumnos ingresados = {len(nombres)}")
print(f"Primer alumno ingresado = {nombres[0]}")
print(f"Ultimo alumno ingresado = {nombres[-1]}")

# Ordenar = sort
nombres.sort()
print(f"Lista de alumnos ordenada = {nombres}")



# ************** MISMO EJS PERO CON FOR Y INGRESO DE CANTIDAD:  **************
print("******************* CON FOR Y INGRESO DE CANTIDAD: *******************")
nombres2 = []
cantidad = int(input( "Ingrese la cantidad de alumnos (en numero)." ))

for i in range(cantidad):
    nombre = input( "Ingrese los nombres.")
    nombres2.append(nombre)

print(f"Cantidad de alumnos ingresados = {len(nombres2)}")
print(f"Primer alumno ingresado = {nombres2[0]}")
print(f"Ultimo alumno ingresado = {nombres2[-1]}")

# Ordenar = sort
nombres2.sort()
print(f"Lista de alumnos ordenada = {nombres2}")

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

# TEST 03:
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.a
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.b
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.c
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.d
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.FIN
# Cantidad de alumnos ingresados = 4
# Primer alumno ingresado = a
# Ultimo alumno ingresado = d
# Lista de alumnos ordenada = ['a', 'b', 'c', 'd']
# ******************* CON FOR Y INGRESO DE CANTIDAD: *******************
# Ingrese la cantidad de alumnos (en numero).4
# Ingrese los nombres.a
# Ingrese los nombres.b
# Ingrese los nombres.c
# Ingrese los nombres.d
# Cantidad de alumnos ingresados = 4
# Primer alumno ingresado = a
# Ultimo alumno ingresado = d
# Lista de alumnos ordenada = ['a', 'b', 'c', 'd']

# TEST 04:
# ERROR. Por no validar cuando sean listas tamanio 0.
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.a
# Ingrese los nombres. Ingrese FIN para dejar de ingresar alumnos.fin
# Cantidad de alumnos ingresados = 1
# Primer alumno ingresado = a
# Ultimo alumno ingresado = a
# Lista de alumnos ordenada = ['a']
# ******************* CON FOR Y INGRESO DE CANTIDAD: *******************
# Ingrese la cantidad de alumnos (en numero).0
# Cantidad de alumnos ingresados = 0
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA04\File1\ejs1.py", line 38, in <module>
#     print(f"Primer alumno ingresado = {nombres2[0]}")
#                                        ~~~~~~~~^^^
# IndexError: list index out of range
