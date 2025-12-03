# Función contar palabras
def contar_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for p in palabras:
        p_limpia = p.lower().strip(",.")
        frecuencia[p_limpia] = frecuencia.get(p_limpia, 0) + 1
    return frecuencia

# Función reemplazar palabras
def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

# Función eliminar palabra
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    # Filtro las palabras que no sean la que se quiere eliminar
    filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(filtradas)

# Función para procesar_texto con *args
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        # Esperamos 2 argumentos extra: original y nueva
        if len(args) < 2: return "Error: Faltan argumentos para reemplazar."
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opcion == "eliminar":
        # Esperamos 1 argumento extra: palabra a eliminar
        if len(args) < 1: return "Error: Falta argumento para eliminar."
        return eliminar_palabra(texto, args[0])
    
    else:
        return "Opción no válida."

# CASO DE USO:
texto_prueba = "Hola Antonio, está genial Python, es facil"
print(f"Texto original: '{texto_prueba}'")
print(f"1. Contar: {procesar_texto(texto_prueba, 'contar')}")
print(f"2. Reemplazar 'Python' por 'Java': {procesar_texto(texto_prueba, 'reemplazar', 'Python', 'Java')}")
print(f"3. Eliminar 'genial': {procesar_texto(texto_prueba, 'eliminar', 'genial')}")
