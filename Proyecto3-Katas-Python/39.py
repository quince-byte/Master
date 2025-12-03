import math
# Función para calcular el área de figuras
def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        return datos[0] * datos[1]
    
    elif figura == "circulo":
        return math.pi * (datos[0] ** 2)
    
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2
    
    else:
        return "Figura desconocida"

print(f"Área Rectángulo (10, 5): {calcular_area('rectangulo', (10, 5))}")
print(f"Área Círculo (r=3): {calcular_area('circulo', (3,))}")
print(f"Área Triángulo (10, 5): {calcular_area('triangulo', (10, 5))}")
