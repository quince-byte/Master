# Función para ejecutar la tienda
def ejecutar_tienda():
    print("--- Bienvenido a la tienda ---")
    try:
        # Solicitar precio original
        precio_str = input("Ingrese el precio del artículo: ")
        precio_original = float(precio_str)
        
        # Preguntar por cupón
        tiene_cupon = input("¿Tiene cupón de descuento? (si/no): ").lower()
        
        precio_final = precio_original
        
        if tiene_cupon == "si":
            # Solicitar valor del cupón
            valor_cupon = float(input("Ingrese el valor del descuento: "))
            
            # Validar y aplicar descuento
            if valor_cupon > 0:
                # Validar que el descuento no sea mayor al precio
                descuento_real = min(valor_cupon, precio_original)
                precio_final = precio_original - descuento_real
                print(f"Descuento de {descuento_real} aplicado.")
            else:
                print("El cupón no es válido (debe ser mayor a 0).")
        
        # Mostrar precio final
        print(f"El precio final a pagar es: {precio_final}")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

ejecutar_tienda()
