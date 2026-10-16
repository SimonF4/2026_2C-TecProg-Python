"""
Ejercicios obligatorios
1) Función palíndromo: 
        escribir una función 
            que retorne 
                True si una palabra/frase es palíndromo 
                    (ignorar espacios y mayúsculas).
"""

palabra = input("Ingrese un texto a evaluar si es palindromo.")

def es_palindromo_solucion1_completa(palabra):
    resultado = True
    # Limpiamos/Normalizamos el ingreso por teclado del usuario.
    palabra_limpia = palabra.replace(" ", "").lower()

    # Una opcion: usar slicer miLista[::-1] con el texto.
    palabra_list = list(palabra_limpia)
    print(palabra_list)         # Resultado = ['t', 'e', 'x', 't', 'o']
    palabra_list_inv = palabra_list[::-1]
    print(palabra_list_inv)     # Resultado = ['o', 't', 'x', 'e', 't']

    # TESTING: len()
    print("Tamanio lista = ", len(palabra_list))               # 5
    tamanio_mitad_de_lista = int(len(palabra_list)/2)
    print("Tamanio lista /2 = ", tamanio_mitad_de_lista)       # 2

    # Para separar en 2 mitades el texto.
    # TESTING: list -> slicing
    # mitad1 = palabra_list[::int(len(palabra_list)/2)] # ['t', 'x', 'o']
    mitad1 = palabra_list[:tamanio_mitad_de_lista]    # ['t', 'e']
    print("1ra mitad = ", mitad1)
    # mitad2 = palabra_list_inv[::int(len(palabra_list_inv)/2)] # ['o', 'x', 't']
    mitad2 = palabra_list_inv[:int(len(palabra_list_inv)/2)]    # ['o', 't']
    print("2da mitad = ", mitad2)

    i = 0
    j = 0
    print("resultado == True: ", resultado == True) # Testing de booleanos en .py.
    # for i in range(0, len(palabra_list)):

    print("Mitad 1, letra media/divisora = ", palabra_list[tamanio_mitad_de_lista])
    print("Mitad 2, letra media/divisora = ", palabra_list_inv[tamanio_mitad_de_lista])
    if( palabra_list[tamanio_mitad_de_lista] == palabra_list_inv[tamanio_mitad_de_lista]):
        while (i < (tamanio_mitad_de_lista)) and (resultado == True):
            print(" Contador i = ", i)
            print(" Contador j = ", j)

            palabra_actual = palabra_list[i]
            print("     Palabra actual = ", palabra_actual)
            palabra_inv_actual = palabra_list_inv[j]
            print("     Palabra actual lectura inversa = ", palabra_inv_actual)

            if( palabra_actual == palabra_inv_actual):
                resultado = True
            else:
                resultado = False

            print("     Resultado de la comparacion = ", resultado)

            # Para poder seguir recorriendo:
            j += 1
            i += 1
    else:
        resultado = False
    
    return resultado

def es_palindromo_solucion1_acortada(palabra):
    resultado = True
    
    palabra_limpia = palabra.replace(" ", "").lower()

    palabra_list = list(palabra_limpia)
    palabra_list_inv = palabra_list[::-1]

    tamanio_mitad_de_lista = int(len(palabra_list)/2)

    i = 0
    j = 0

    if( palabra_list[tamanio_mitad_de_lista] == palabra_list_inv[tamanio_mitad_de_lista]):

        while (i < (tamanio_mitad_de_lista)) and (resultado == True):

            if( palabra_list[i] == palabra_list_inv[j]):
                resultado = True
            else:
                resultado = False

            j += 1
            i += 1
    else:
        resultado = False
    
    return resultado

# Resolucion de vitto en clase (15/10/2026):
def es_palindromo_solucion2_15102026(palabra):
    palabra = palabra.replace(" ", "").lower()
    # Directamente compara las 2 listas enteras si dan el mismo resultado. En vez de ir comparando letra por letra (q es algo q igual debe hacer internamente esto).
    if palabra == palabra[::-1]:
        return True
    else:
        return False

print(f"Es palindromo la palabra '{palabra}'? Resultado = {es_palindromo_solucion1_completa(palabra)}")
print(f"(version metodo acortado) Es palindromo la palabra '{palabra}'? Resultado = {es_palindromo_solucion1_acortada(palabra)}")
print(f"(version 2 del metodo) Es palindromo la palabra '{palabra}'? Resultado = {es_palindromo_solucion2_15102026(palabra)}")

# TESTING:
# TEST 01:
# Ingrese un texto a evaluar si es palindromo.texto
# ['t', 'e', 'x', 't', 'o']
# ['o', 't', 'x', 'e', 't']
# 5
# 2
# ['t', 'e']
# ['o', 't']
# resultado == True:  True
# 0
# 0
# t
# o
# False
# Es palindromo texto? Resultado = False

# TEST 02: con "Neu quen"
# Resultado: loop infinito, pq no cierra el while. Pq se queda atascado i y j en 0. Quedo sin contador pq era un for.

# TEST 03: No mueve i y j al mismo tiempo. + El STRIP no funciono, quedo el espacio vacio. -> Xq??? xq solo borra espacios al inicio y al final del texto. => usar replace()
# Ingrese un texto a evaluar si es palindromo.Neu quen
# ['n', 'e', 'u', ' ', 'q', 'u', 'e', 'n']
# ['n', 'e', 'u', 'q', ' ', 'u', 'e', 'n']
# Tamanio lista =  8
# Tamanio lista /2 =  4
# 1ra mitad =  ['n', 'e', 'u', ' ']
# 2da mitad =  ['n', 'e', 'u', 'q']
# resultado == True:  True
#      Contador i =  0
#      Contador j =  0
#  Palabra actual =  n
#  Palabra actual lectura inversa =  n
# True
#      Contador j =  1
#  Palabra actual =  n
#  Palabra actual lectura inversa =  e
# False
# Es palindromo la palabra 'Neu quen'? Resultado = False

# TEST 04: Bien el resultado. Pero checkeo todas las letras => 1 ciclo innecesario recorrio.
# Ingrese un texto a evaluar si es palindromo.Neu quen
# ['n', 'e', 'u', 'q', 'u', 'e', 'n']
# ['n', 'e', 'u', 'q', 'u', 'e', 'n']
# Tamanio lista =  7
# Tamanio lista /2 =  3
# 1ra mitad =  ['n', 'e', 'u']
# 2da mitad =  ['n', 'e', 'u']
# resultado == True:  True
#  Contador i =  0
#  Contador j =  0
#      Palabra actual =  n
#      Palabra actual lectura inversa =  n
#      Resultado de la comparacion =  True
#  Contador i =  1
#  Contador j =  1
#      Palabra actual =  e
#      Palabra actual lectura inversa =  e
#      Resultado de la comparacion =  True
#  Contador i =  2
#  Contador j =  2
#      Palabra actual =  u
#      Palabra actual lectura inversa =  u
#      Resultado de la comparacion =  True
#  Contador i =  3
#  Contador j =  3
#      Palabra actual =  q
#      Palabra actual lectura inversa =  q
#      Resultado de la comparacion =  True
#  Contador i =  4
#  Contador j =  4
#      Palabra actual =  u
#      Palabra actual lectura inversa =  u
#      Resultado de la comparacion =  True
#  Contador i =  5
#  Contador j =  5
#      Palabra actual =  e
#      Palabra actual lectura inversa =  e
#      Resultado de la comparacion =  True
#  Contador i =  6
#  Contador j =  6
#      Palabra actual =  n
#      Palabra actual lectura inversa =  n
#      Resultado de la comparacion =  True
# Es palindromo la palabra 'Neu quen'? Resultado = True

# TEST 05:
# Ingrese un texto a evaluar si es palindromo.neU quen
# ['n', 'e', 'u', 'q', 'u', 'e', 'n']
# ['n', 'e', 'u', 'q', 'u', 'e', 'n']
# Tamanio lista =  7
# Tamanio lista /2 =  3
# 1ra mitad =  ['n', 'e', 'u']
# 2da mitad =  ['n', 'e', 'u']
# resultado == True:  True
# Mitad 1, letra media/divisora =  q
# Mitad 2, letra media/divisora =  q
#  Contador i =  0
#  Contador j =  0
#      Palabra actual =  n
#      Palabra actual lectura inversa =  n
#      Resultado de la comparacion =  True
#  Contador i =  1
#  Contador j =  1
#      Palabra actual =  e
#      Palabra actual lectura inversa =  e
#      Resultado de la comparacion =  True
#  Contador i =  2
#  Contador j =  2
#      Palabra actual =  u
#      Palabra actual lectura inversa =  u
#      Resultado de la comparacion =  True
# Es palindromo la palabra 'neU quen'? Resultado = True

# TEST 06:
# Anita lava la tina
# Resultado = True
