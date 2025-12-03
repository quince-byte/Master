from functools import reduce

# --- EJERCICIO 22 ---
# Producto total de una lista numérica usando reduce().
lista_vals = [2, 3, 4] # 2*3*4 = 24
producto_total = reduce(lambda x, y: x * y, lista_vals)

# print(producto_total)
