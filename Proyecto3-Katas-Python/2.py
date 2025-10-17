mylist = [2,3,54,3,5,7,56,7,8,5,5,7,8,4,3,3,23]
# Utilizo la función map con lambda para multiplicar por 2 todos los elementos de la lista
mapped = list(map(lambda x: x*2, mylist))
print(mapped)