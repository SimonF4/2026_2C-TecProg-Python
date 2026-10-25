"""
Ejercicio 7 (recomendado) ⭐
Escribe una función llamada fizz_buzz 
    que reciba un número entero como entrada. 

La función debe seguir las siguientes reglas:
    Si el número es divisible solo por 5, debe retornar el string "Buzz".
    Si el número es divisible solo por 3, debe retornar el string "Fizz".
    Si el número es divisible por 3 y por 5 simultáneamente, debe retornar el string "FizzBuzz".
    Si no cumple ninguna de las condiciones anteriores, debe retornar el número recibido como entrada.
    Agregar DocString de la función.
//(Docstring: lo vemos la clase que viene.)

"""

def fizz_buzz (a):
    """ Docstring: Metodo fizz_buzz, recibe un número entero como entrada. """

    resu = 0

    if ( (a % 5 == 0) and (a % 3 == 0) ):
        resu = "FizzBuzz"
    elif (a % 5 == 0):
        resu = "Buzz"
    elif (a % 3 == 0):
        resu = "Fizz"
    else:
        resu = a

    return resu

a = input("Escriba un número a evaluar.")
print( fizz_buzz(a) )


# Opcion2:
a = input("Escriba un número a evaluar.")

def fizz_buzz_v2 (a):
    """ Docstring: fizz_buzz version 2. Se elimino la repeticion del codigo en las validaciones."""

    resu  = a
    div_5 = (a % 5 == 0)
    div_3 = (a % 3 == 0)

    if ( div_5 and div_3 ):
        resu = "FizzBuzz"
    elif div_5:
        resu = "Buzz"
    elif div_3: 
        resu = "Fizz"
    else:
        resu = a

    return resu

print( fizz_buzz_v2(a) )

# TESTING:
# TEST 01: Fallo pq puse mal el input.
# Escriba un número a evaluar.7
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Funciones\ejs7.py", line 33, in <module>
#     print( fizz_buzz(a) )
#            ~~~~~~~~~^^^
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA05\File2-Anexo\Funciones\ejs7.py", line 21, in fizz_buzz
#     if ( (a % 5 == 0) and (a % 3 == 0) ):
#           ~~^~~
# TypeError: not all arguments converted during string formatting

# TEST 02:

