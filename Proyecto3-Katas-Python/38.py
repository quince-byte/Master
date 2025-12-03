# --- EJERCICIO 38: CALIFICACIÓN ALUMNO ---
print("\n--- Ejercicio 38: Calificación Texto ---")
def obtener_calificacion_texto(nota):
    if 0 <= nota <= 69: return "Insuficiente"
    elif 70 <= nota <= 79: return "Bien"
    elif 80 <= nota <= 89: return "Muy bien"
    elif 90 <= nota <= 100: return "Excelente"
    else: return "Nota fuera de rango"

print(f"Nota 85: {obtener_calificacion_texto(85)}")
print(f"Nota 60: {obtener_calificacion_texto(60)}")
