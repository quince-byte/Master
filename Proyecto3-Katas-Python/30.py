# Devuelve True si dos palabras son anagramas.
def son_anagramas(palabra1, palabra2):
    # Convierto a minusculas, quito espacios, ordeno las letras y comparo si es la misma
    p1 = sorted(palabra1.lower().replace(" ", ""))
    p2 = sorted(palabra2.lower().replace(" ", ""))
    return p1 == p2

print(f"¿Son anagramas 'Amor' y 'Roma'? {son_anagramas('Amor', 'Roma')}")
