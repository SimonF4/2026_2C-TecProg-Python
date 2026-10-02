# Ejercicios optativos / recomendados
"""
🟩 Ejercicio recomendado 1 – 
Inventario: 
diccionario 
    {producto: {'precio': x, 'stock': y}}. 
Mostrar 
    total del stock 
    y el producto más caro.
"""

diccionario = {}
producto = {}
total_stock = 0
prod_mas_caro = 0
precio = 0
stock = 0

PRECIO_CORTE = -1
STOCK_CORTE = -1

while(precio != PRECIO_CORTE and stock != STOCK_CORTE):
    producto = (input("Ingrese el nombre del producto."))
    precio = float(input("Ingrese el precio (valor) del producto."))
    stock = int(input("Ingrese el stock (cantidad) del producto."))

    # Guardar en los 2 diccionarios.
    # producto ["precio", "stock"] = {precio, stock}
    # diccionario [producto] = producto ["precio", "stock"]
    # En una linea seria: 
    diccionario ["producto"] = {"precio": precio, "stock": stock}

    # "Mostrar total del stock "    
    total_stock += 1

    # "Mostrar el producto más caro"
    if(precio > total_stock):
        prod_mas_caro = producto

print("--- RESULTADOS ---")
print(f"--- total del stock = {prod_mas_caro} ---")
print(f"--- el producto más caro = {total_stock} ---")


# TESTS:
# TEST 01:

# Ingrese el precio (valor) del producto.100
# Ingrese el stock (cantidad) del producto.1
# Traceback (most recent call last):
#   File "c:\Users\Yo\PROYECTOS\CFP11\Python\GUIA04\File1\Part2\ejs1.py", line 28, in <module>
#     diccionario [producto] = producto
#     ~~~~~~~~~~~~^^^^^^^^^^
# TypeError: unhashable type: 'dict'

# TEST 02:
# Ingrese el nombre del producto.papa
# Ingrese el precio (valor) del producto.100
# Ingrese el stock (cantidad) del producto.2
# Ingrese el nombre del producto.batata
# Ingrese el precio (valor) del producto.200
# Ingrese el stock (cantidad) del producto.3
# Ingrese el nombre del producto.fin
# Ingrese el precio (valor) del producto.-1
# Ingrese el stock (cantidad) del producto.-1
# --- RESULTADOS ---
# --- total del stock = batata ---
# --- el producto más caro = 3 ---

# TEST 03:

