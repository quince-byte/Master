


def encontrar_palabras(lista_palabras: list[str], palabra_objetivo: str)-> list:
    lista_con_objetivo = []
    # Para cada palabra que contenga la palabra objetivo la añado a la nueva lista
    # Ignoro si está en mayúsculas o en minúsculas
    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            lista_con_objetivo.append(palabra)
    return lista_con_objetivo


lista_palabras = ["Terrícola", "pepsicOla","colador","verde", "ciruela"]
palabra_objetivo = "cola"

print(encontrar_palabras(lista_palabras,palabra_objetivo))