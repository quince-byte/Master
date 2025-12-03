from functools import reduce

# --- EJERCICIO 17 ---
# Lista de dígitos a número entero usando reduce().
# Ejemplo: [5, 7, 2] -> 5*10+7 = 57 -> 57*10+2 = 572
def digitos_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

# print(digitos_a_numero([5, 7, 2]))
