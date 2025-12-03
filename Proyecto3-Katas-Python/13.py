# --- EJERCICIO 13 ---
# Devolver tuplas (MAYUS, minus) de un conjunto de caracteres usando map().
def tuplas_mayus_minus(caracteres):
    # map itera sobre el conjunto
    return list(map(lambda c: (c.upper(), c.lower()), caracteres))

# print(tuplas_mayus_minus({'a', 'b', 'c'}))
