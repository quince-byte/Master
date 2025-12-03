# --- EJERCICIO 16 ---
# Palabras más largas que 'n' de un texto usando filter().
def palabras_largas(texto, n):
    lista_palabras = texto.split()
    return list(filter(lambda p: len(p) > n, lista_palabras))

# print(palabras_largas("El veloz murciélago comía feliz", 5))
