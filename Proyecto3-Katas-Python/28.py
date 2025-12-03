# --- EJERCICIO 28: Primer elemento duplicado ---
# print("\n--- Ejercicio 28: Primer duplicado ---")
def encontrar_primer_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None # Si no hay duplicados

lista_dup = [1, 2, 3, 4, 2, 5]
# print(f"En {lista_dup}, el primer duplicado es: {encontrar_primer_duplicado(lista_dup)}")
