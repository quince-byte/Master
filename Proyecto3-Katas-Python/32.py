# --- EJERCICIO 32: Buscar empleado y puesto ---
# print("\n--- Ejercicio 32: Buscar Empleado ---")
def buscar_empleado(nombre_completo, lista_empleados):
    # lista_empleados es una lista de diccionarios
    for emp in lista_empleados:
        if emp['nombre'] == nombre_completo:
            return emp['puesto']
    return "Esta persona no trabaja aquí."

empleados_db = [
    {"nombre": "Juan Perez", "puesto": "Gerente"},
    {"nombre": "Ana Garcia", "puesto": "Desarrolladora"}
]
# print(f"Puesto de Ana Garcia: {buscar_empleado('Ana Garcia', empleados_db)}")
# print(f"Puesto de Pepe: {buscar_empleado('Pepe', empleados_db)}")
