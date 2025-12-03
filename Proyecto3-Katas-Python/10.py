# --- EJERCICIO 10 ---
# Calcular promedio con excepción personalizada si la lista está vacía.
class ListaVaciaError(Exception):
    pass

def calcular_promedio(numeros):
    try:
        if not numeros:
            raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
        return sum(numeros) / len(numeros)
    except ListaVaciaError as e:
        print(f"Error detectado: {e}")

# calcular_promedio([])
