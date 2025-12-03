# --- EJERCICIO 11 ---
# Pedir edad y manejar excepciones (no numérico y rango inválido).
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad está fuera del rango esperado (0-120).")
        print(f"Edad registrada: {edad}")
    except ValueError as e:
        # Esto captura tanto el error de int() si escriben letras, como nuestro raise manual
        print(f"Entrada inválida: {e}")

# pedir_edad() (Descomentar para probar)
