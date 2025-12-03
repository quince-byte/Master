import math

# --- EJERCICIO 39: ÁREA DE FIGURAS ---
print("\n--- Ejercicio 39: Área de figuras ---")
def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        # datos = (base, altura)
        return datos[0] * datos[1]
    
    elif figura == "circulo":
        # datos = (radio, )
        return math.pi * (datos[0] ** 2)
    
    elif figura == "triangulo":
        # datos = (base, altura)
        return (datos[0] * datos[1]) / 2
    
    else:
        return "Figura desconocida"

print(f"Área Rectángulo (10, 5): {calcular_area('rectangulo', (10, 5))}")
print(f"Área Círculo (r=3): {calcular_area('circulo', (3,))}")
print(f"Área Triángulo (10, 5): {calcular_area('triangulo', (10, 5))}")
