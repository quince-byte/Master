# --- EJERCICIO 31: Buscar nombre con excepción (Interactivo) ---
# print("\n--- Ejercicio 31: Buscar nombre (Try/Except) ---")
class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre_usuario():
    try:
        # Simulamos la entrada para que corra en bloque sin input real
        # Para probarlo interactivo, descomenta las líneas 'input' y comenta las fijas
        
        # entrada_nombres = input("Ingresa nombres separados por coma: ")
        entrada_nombres = "Juan,Ana,Pedro" # Valor fijo para el ejemplo
        
        lista_nombres = [n.strip() for n in entrada_nombres.split(',')]
        
        # objetivo = input("¿A quién buscas?: ")
        objetivo = "Luis" # Valor fijo (Luis no está, saltará error)
        
        print(f"Lista: {lista_nombres} | Buscando a: {objetivo}")
        
        if objetivo in lista_nombres:
            print(f"¡Éxito! {objetivo} está en la lista.")
        else:
            raise NombreNoEncontradoError(f"El nombre '{objetivo}' no se encuentra.")
            
    except NombreNoEncontradoError as e:
        print(f"Excepción capturada: {e}")

# buscar_nombre_usuario()
