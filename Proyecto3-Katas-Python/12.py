# Devuelve la longitud de cada palabra en una frase usando map().
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

print(longitud_palabras("Hola mundo python"))
