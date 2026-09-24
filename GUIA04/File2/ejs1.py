# EJERCICIO DE LA GUIA ANEXA.
"""
Ejercicio 1:
Tienes una lista de amigos con los nombres ['Pepe', 'Ana', 'Jose', 'Luis']. 
    Imprime cada nombre en una misma línea, 
        separado por un espacio, 
        utilizando un bucle for.

Ejemplo de salida:
Los nombres de mis amigos son: Pepe Ana Jose Luis
"""

amigos = ['Pepe', 'Ana', 'Jose', 'Luis']

for i in range(0, len(amigos)):
    print(amigos[i], end=" ")
# Resultado = "Pepe Ana Jose Luis "

# Otra forma: for i in range(len(amigos)):  # Te lo toma igual pq por default te toma q arranca en 0.

print("\n************************* TESTINGS: ")

print("*** Ejemplo de hacer lo mismo pero con 'join': ***")
print(" - ".join(amigos)) # Resultado = "Pepe - Ana - Jose - Luis"

print("*** TESTs de mostrar nombres con posicionamiento directo: ***")
print(amigos[1]) # Resultado = "Ana"
print(amigos[2]) # Resultado = "Jose"
print(amigos[3]) # Resultado = "Luis"
print(amigos[-1]) # Resultado = "Luis"  -> xq [-1] esto muestra siempre el ultimo.
print(amigos[0]) # Resultado = "Pepe"   -> [0] siempre muestra el 1er item

print("*** Ejemplo de Slicing: ***")
# Slicing: para cortar la lista. Seleccionas inicio(incluye el numero) y fin(no incluye este numero).
print(amigos[1:3]) # rta = ['Ana', 'Jose']

print("*** Ejemplo de agregar/append: ***")
amigos.append("Jessi")  # Devuelve "none" => no se puede meter en un print.
print(amigos[4]) # Resultado = Jessi

print("*** Ejemplo de borrar/remove: ***")
amigos.remove("Pepe")   # Como el metodo anterior. Tmb devuelve none.
print(amigos) # Resultado = "['Ana', 'Jose', 'Luis', 'Jessi']"

print("*** Ejemplo de como invertir una lista: ***")
# Con esto invertis el orden de una lista.
print(amigos[::-1])  # Resultado = "['Jessi', 'Luis', 'Jose', 'Ana']"

print("****** TEST para ver si te hace una copia o te modifica la lista original: **********")
nuevaList = amigos[::-1]
amigos.sort()

print("Lista amigos: ", amigos) # Resultado = "Lista amigos:  ['Ana', 'Jose', 'Luis', 'Jessi']"
print("Lista nueva: ",  nuevaList) # Resultado = "Lista nueva:  ['Jessi', 'Luis', 'Jose', 'Ana']"

# Ejemplo: de como NO acceder a la ultima posicion.
# print(amigos[1200]) # Resultado: ERROR "IndexError: list index out of range"

HOLA = "Hola Mundo"
# Como se imprime la 1er letra: "H_______"
print( HOLA[0:1])   # Resultado = H

# Como se imprime desde: "____ Mundo"
print( HOLA[5:15])  # Resultado = "Mundo"
print("*** Para imprimir desde x valor al ultimo de una lista: ***")
print( HOLA[5:])    # Resultado = "Mundo"

# Como se imprime desde: "____la Mundo"
print( HOLA[2:])    # Resultado = "la Mundo"
