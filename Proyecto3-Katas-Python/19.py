# Lambda que filtra números impares.
numeros = [1, 2, 3, 4, 5, 6]
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)
