# 1. Ejecutar el siguiente código python en el IDE. 
#       - ¿Qué muestra el ejercicio? 
#       - ¿Tiene errores? 
#       - (Si tiene corrígelos)

hdd = "512GB SSD"
cpu = "i10-6700k"
ram = "16GB DDR4"

cabecera = "Procesador\tMemoria\t\tDisco"

print(cabecera)

# Aplicar formato convencional aplicando Format
print("{0}\t{1}\t{2}\n".format(cpu, ram, hdd))
# Aplicar formato nuevo
print(f"{cpu}\t{ram}\t{hdd}\n")

