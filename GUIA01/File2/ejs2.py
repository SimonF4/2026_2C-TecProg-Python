# 2. ¿Cuál es la sintaxis en Python para extraer los primeros tres caracteres de una cadena?

"""
a) str.substr(0, 3) = error
b) str.Substring(0, 3) = error
c) str[0:3] = Funciona: resultado da "Hol"
d) str.slice(0, 3) = error
Mi rta = d) parece ser. En principio pensaba q seria lo de substring pero tira error.
rta final = c) str[0:3].
"""

# Testing:
STR = "Hola soy un String"

print( STR[0:3]  )
