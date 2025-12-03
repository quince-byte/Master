#Filtrar mascotas prohibidas usando filter()
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Mantengo las que no están en prohibidas
    return list(filter(lambda x: x not in prohibidas, lista_mascotas))

print(filtrar_mascotas(["Perro", "Tigre", "Gato", "Oso", "Canario"]))
