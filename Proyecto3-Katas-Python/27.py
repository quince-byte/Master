# Hace el promedio de una lista de números.
def promedio(lista):
    if not lista: return 0
    return sum(lista) / len(lista)

print(f"Promedio de [10, 20, 30]: {promedio([10, 20, 30])}")
