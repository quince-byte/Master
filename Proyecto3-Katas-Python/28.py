# Encuentra el primer elemento duplicado en una lista.
def encontrar_primer_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None

lista_dup = [1, 2, 3, 4, 2, 5]
print(f"En {lista_dup}, el primer duplicado es: {encontrar_primer_duplicado(lista_dup)}")
