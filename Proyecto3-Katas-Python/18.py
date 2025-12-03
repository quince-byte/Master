# Filtro estudiantes con calificación >= 90 de una lista de diccionarios.
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 95},
    {"nombre": "Maria", "edad": 21, "calificacion": 90}
]

estudiantes_destacados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))
print(estudiantes_destacados)
