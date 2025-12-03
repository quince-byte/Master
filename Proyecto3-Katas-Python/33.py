# --- EJERCICIO 33: Lambda suma dos listas ---
# print("\n--- Ejercicio 33: Lambda suma dos listas ---")
l1 = [1, 2, 3]
l2 = [10, 20, 30]
# Usamos map con lambda para sumar elementos correspondientes
suma_listas = list(map(lambda x, y: x + y, l1, l2))
# print(f"{l1} + {l2} = {suma_listas}")
