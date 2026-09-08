# Ejercicios optativos / recomendados
# Ejercicio recomendado 1 – Descuentos por edad:
#           > ingresar edad y precio.
#           > Aplicar 20% si <18 o >65.

edad = int ( input("Ingrese su edad en formato numerico:") )
# PEP8 recomienda usar no usar camelCase y si usar snake_case para el nombre de variables.
precio_ori = float ( input("Ingrese el precio del producto:") )
DESCUENTO = 0.2
# Obligatorio pq sino me queda solo dentro del scope del if esta variable y no la puedo usar fuera como en el print del final.
precio_final = precio_ori

if ( (edad < 18) or (edad > 65) ):
    # es el 100% - valor a descontar
    precio_final = precio_ori - (precio_ori * DESCUENTO)

print(
    f"Para un usuario de edad {edad}, el precio de un producto de valor original {precio_ori} sera {precio_final}")
