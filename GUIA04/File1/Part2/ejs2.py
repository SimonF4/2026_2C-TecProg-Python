# 🟩 Ejercicio recomendado 2 
# – Normalizador de datos: 
# a partir de 
#   una lista con
#        nombres repetidos 
#        y espacios extra, 
#   generar una lista 
#       limpia 
#       y única (strip, title, set).
# (strip, title, set):
# Strip = eliminar espacios vacíos.
# Title = para poner mayúscula en la letra.
# set = para hacerlo un Conjunto => elimina repetidos.

lista_1 = ["     nombre1", " nombre1      ", " nombre2 ", "nombre2 ", "nombre3"]
lista_limpia = []
conjunto = set()

for nombre in lista_1:
    print(nombre)
    # --- Normalizacion de los nombres: ---
    nombre_strip = nombre.strip()
    print("nombreLimpio:", nombre_strip)
    # Corregimos con title el nombre ya limpio:
    nombre_limpio = nombre_strip.title()
    print("nombre en forma title:", nombre_limpio)
    # Se puede hacer todo eso en 1 linea:
    # nombre_1_liner = nombre.strip().title()
    # print("nombre limpio en 1 liner", nombre_1_liner)

    # Eliminamos repetidos al guardarlos en un set/conjunto.
    conjunto.add(nombre_limpio)

print(conjunto)
lista_limpia = list(conjunto)
# sorted() para ordenar la lista pq sino me quedaba desordenada.
lista_limpia = sorted(lista_limpia)

print("Lista limpia resultante = ", lista_limpia)

# TESTEOs:
# TEST 01: Bien, pero no ordena por letra y numero. En el medio el conjunto lo desordeno.
#      nombre1
# nombreLimpio: nombre1
# nombre en forma title: Nombre1
#  nombre1      
# nombreLimpio: nombre1
# nombre en forma title: Nombre1
#  nombre2 
# nombreLimpio: nombre2
# nombre en forma title: Nombre2
# nombre2 
# nombreLimpio: nombre2
# nombre en forma title: Nombre2
# nombre3
# nombreLimpio: nombre3
# nombre en forma title: Nombre3
# {'Nombre1', 'Nombre3', 'Nombre2'}
# Lista limpia resultante =  ['Nombre1', 'Nombre3', 'Nombre2']

# TEST 02:
#     nombre1
# nombreLimpio: nombre1
# nombre en forma title: Nombre1
#  nombre1      
# nombreLimpio: nombre1
# nombre en forma title: Nombre1
#  nombre2 
# nombreLimpio: nombre2
# nombre en forma title: Nombre2
# nombre2 
# nombreLimpio: nombre2
# nombre en forma title: Nombre2
# nombre3
# nombreLimpio: nombre3
# nombre en forma title: Nombre3
# {'Nombre2', 'Nombre3', 'Nombre1'}
# Lista limpia resultante =  ['Nombre1', 'Nombre2', 'Nombre3']
