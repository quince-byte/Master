lista1 = [3,35,45,4,65,456,34,3,4,645,6,45,43,2]
lista2 = [664,54,32435,574,3453,3452,3543,345,54,54,45,32,25,45]

def hacer_diferencia(lista1: list[str], lista2: list[str]):
    # Resto cada valor de una lista al de la otra
    lista_diferencia = list(map(lambda x,y: y - x,lista1,lista2))
    return lista_diferencia


print(hacer_diferencia(lista1,lista2))