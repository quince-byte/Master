from functools import reduce
# Concateno una lista de palabras usando reduce().
palabras_para_unir = ["Python", "es", "muy", "poderoso"]
frase_unida = reduce(lambda x, y: x + " " + y, palabras_para_unir)
print(frase_unida)
