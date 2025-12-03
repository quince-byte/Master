from functools import reduce
# Producto de una lista de números usando reduce().
lista_vals = [2, 3, 4]
producto_total = reduce(lambda x, y: x * y, lista_vals)
print(producto_total)
