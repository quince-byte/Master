from functools import reduce
# Lista de dígitos a número entero usando reduce().
def digitos_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

print(digitos_a_numero([5, 7, 2]))
