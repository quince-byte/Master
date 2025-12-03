# --- EJERCICIO 8 ---
# Programa que pide dos números y maneja excepciones (no numérico y división por cero).
def dividir_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"La división fue exitosa. Resultado: {resultado}")
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        
# dividir_numeros() (Descomentar para probar interactividad)
