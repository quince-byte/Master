# Enmascara un texto
def enmascarar(texto):
    cadena = str(texto)
    longitud = len(cadena)
    if longitud <= 4:
        return cadena
    # Multiplica '#' por la longitud menos 4 y concatena los últimos 4
    return '#' * (longitud - 4) + cadena[-4:]

print(f"Tarjeta: {enmascarar('123456781234')}")
