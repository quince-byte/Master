# Función que recibe una lista de notas y una nota de corte
def evaluar_clase(notas, nota_aprobado=5):
    if not notas:
        return (0, "suspenso")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)


print(evaluar_clase([6, 7, 4, 8]))
