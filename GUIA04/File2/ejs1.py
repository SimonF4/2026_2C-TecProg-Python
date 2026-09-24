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

# Otra forma: for i in range(len(amigos)):  # Te lo toma igual pq por default te toma q arranca en 0.

# Resultado: Pepe Ana Jose Luis 
print("\n************************* TESTINGS: ")
print(" - ".join(amigos))

print(amigos[1])
print(amigos[2])
print(amigos[3])
print(amigos[-1])
print(amigos[0])
print(amigos[1:3]) # rta = ['Ana', 'Jose']
amigos.append("Jessi")
print(amigos[4])
amigos.remove("Pepe")
print(amigos)
print(amigos[::-1])

# nuevaList = amigos[::-1]
amigos.sort()

print("Lista amigos: ", amigos)
# print("Lista nueva: ",  nuevaList)

# print(amigos[1200])

HOLA = "Hola Mundo"
print( HOLA[0:1])
print( HOLA[5:15])
print( HOLA[5:]) # Para imprimir desde x al ultimo.
print( HOLA[2:])
