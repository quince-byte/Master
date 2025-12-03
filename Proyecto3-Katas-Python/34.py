# --- EJERCICIO 34: CLASE ARBOL ---
# print("\n--- Ejercicio 34: Clase Árbol ---")

class Arbol:
    # a. Inicializar árbol
    def __init__(self):
        self.tronco = 1
        self.ramas = [] # Lista vacía de ramas
    
    # b. Crecer tronco
    def crecer_tronco(self):
        self.tronco += 1
        print(f"-> Tronco creció. Ahora mide: {self.tronco}")

    # c. Nueva rama
    def nueva_rama(self):
        self.ramas.append(1) # Agrega rama longitud 1
        print("-> Nueva rama agregada.")

    # d. Crecer ramas (aumentar longitud de todas)
    def crecer_ramas(self):
        # Actualizamos cada rama sumándole 1
        self.ramas = [r + 1 for r in self.ramas]
        print("-> Todas las ramas crecieron 1 unidad.")

    # e. Quitar rama específica
    def quitar_rama(self, posicion):
        # Manejo básico de índice para evitar errores
        if 0 <= posicion < len(self.ramas):
            eliminada = self.ramas.pop(posicion)
            print(f"-> Rama en posición {posicion} (longitud {eliminada}) eliminada.")
        else:
            print(f"-> Error: No existe rama en la posición {posicion}.")

    # f. Info árbol
    def info_arbol(self):
        return {
            "Longitud Tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitud de ramas": self.ramas
        }

# --- EJECUCIÓN DEL CASO DE USO (a - g) ---
# print("\n... Ejecutando Caso de Uso del Árbol ...")

# a. Crear un árbol
mi_arbol = Arbol()

# b. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# c. Añadir una nueva rama
mi_arbol.nueva_rama()

# d. Hacer crecer todas las ramas una unidad
mi_arbol.crecer_ramas()

# e. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# Estado actual antes de borrar:
# Tenemos 3 ramas: La primera creció (ahora mide 2), las nuevas miden 1.
# Ramas esperadas: [2, 1, 1]
# print(f"Estado antes de borrar: {mi_arbol.info_arbol()}")

# f. Retirar la rama situada en la posición 2 
# (Posición 2 es el índice 2, o sea, la tercera rama)
mi_arbol.quitar_rama(2)

# g. Obtener información sobre el árbol
info_final = mi_arbol.info_arbol()
# print(f"INFORMACIÓN FINAL: {info_final}")
