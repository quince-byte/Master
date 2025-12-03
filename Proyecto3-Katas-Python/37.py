# Función para determinar el momento del día
def momento_dia(hora):
    if 6 <= hora < 13:
        return "Es por la mañana."
    elif 13 <= hora < 20:
        return "Es por la tarde."
    elif (20 <= hora <= 24) or (0 <= hora < 6):
        return "Es por la noche."
    else:
        return "Hora no válida."


hora_test = 15
print(f"Hora {hora_test}: {momento_dia(hora_test)}")
