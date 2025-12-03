from functools import reduce
# Calculo la resta acumulada usando reduce()
lista_valores = [100, 10, 5, 2]
diferencia = reduce(lambda x, y: x - y, lista_valores)
print(f"Lista {lista_valores} -> Diferencia: {diferencia}")