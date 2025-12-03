# Convierto una lista de tuplas a lista de strings usando map().
lista_tuplas = [("Hola", "Mundo"), ("Python", "Genial"), ("Map", "Function")]
# Uno los elementos de la tupla con un espacio
lista_strings = list(map(lambda t: f"{t[0]} {t[1]}", lista_tuplas))

print(lista_strings)
