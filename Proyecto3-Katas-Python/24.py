from functools import reduce

# --- EJERCICIO 24: Diferencia total con reduce ---
# Nota: Calcula la resta acumulada (a - b - c - d...)
# print("\n--- Ejercicio 24: Diferencia total ---")
lista_valores = [100, 10, 5, 2] # 100 - 10 - 5 - 2 = 83
diferencia = reduce(lambda x, y: x - y, lista_valores)
# print(f"Lista {lista_valores} -> Diferencia: {diferencia}")
