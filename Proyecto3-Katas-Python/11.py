# Pide edad y maneja excepciones
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad está fuera del rango esperado (0-120).")
        print(f"Edad registrada: {edad}")
    except ValueError as e:
        print(f"Entrada inválida: {e}")

pedir_edad()

