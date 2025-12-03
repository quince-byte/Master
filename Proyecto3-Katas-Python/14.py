# --- EJERCICIO 14 ---
# Retornar palabras que comiencen con una letra específica usando filter().
def filtrar_por_inicial(lista_palabras, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista_palabras))

# print(filtrar_por_inicial(["Manzana", "Banana", "Melón", "Pera"], "M"))
