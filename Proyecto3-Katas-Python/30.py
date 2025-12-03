# --- EJERCICIO 30: Anagramas ---
# print("\n--- Ejercicio 30: Anagramas ---")
def son_anagramas(palabra1, palabra2):
    # Convertimos a minusculas, quitamos espacios, ordenamos y comparamos
    p1 = sorted(palabra1.lower().replace(" ", ""))
    p2 = sorted(palabra2.lower().replace(" ", ""))
    return p1 == p2

# print(f"¿Son anagramas 'Amor' y 'Roma'? {son_anagramas('Amor', 'Roma')}")
