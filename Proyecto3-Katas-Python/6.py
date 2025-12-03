# --- EJERCICIO 6 ---
# Factorial de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo de uso:
# print(factorial(5)) # 120
