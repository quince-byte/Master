# Devuelve tuplas en mayúsculas y minúsculas de un conjunto de caracteres usando map().
def tuplas_mayus_minus(caracteres):
    return list(map(lambda c: (c.upper(), c.lower()), caracteres))

print(tuplas_mayus_minus({'a', 'b', 'c'}))
