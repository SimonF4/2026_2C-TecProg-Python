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
    

