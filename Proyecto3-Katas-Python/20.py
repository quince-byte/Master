# Filtro solo valores int de una lista mixta (int y string) usando filter().
lista_mixta = [1, "hola", 20, "mundo", 5]
solo_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))

print(solo_enteros)
