# Implemento una clase Árbol con métodos para gestionar su crecimiento y ramas.

class Arbol:
    # Inicializa el árbol
    def __init__(self):
        self.tronco = 1
        self.ramas = [] # Lista vacía de ramas
    
    # Crecer el tronco
    def crecer_tronco(self):
        self.tronco += 1
        print(f"-> Tronco creció. Ahora mide: {self.tronco}")

    # Nueva rama
    def nueva_rama(self):
        self.ramas.append(1) # Agrega rama longitud 1
        print("-> Nueva rama agregada.")

    # Crecer ramas
    def crecer_ramas(self):
        # Actualiza cada rama sumándole 1
        self.ramas = [r + 1 for r in self.ramas]
        print("-> Todas las ramas crecieron 1 unidad.")

    # Quitar rama específica
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            eliminada = self.ramas.pop(posicion)
            print(f"-> Rama en posición {posicion} (longitud {eliminada}) eliminada.")
        else:
            print(f"-> Error: No existe rama en la posición {posicion}.")

    # Info árbol
    def info_arbol(self):
        return {
            "Longitud Tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitud de ramas": self.ramas
        }

mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)
info_final = mi_arbol.info_arbol()

