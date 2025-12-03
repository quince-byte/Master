# --- EJERCICIO 40: TIENDA EN LÍNEA (INTERACTIVO) ---
print("\n--- Ejercicio 40: Tienda con descuentos ---")

def ejecutar_tienda():
    print("--- Bienvenido a la tienda ---")
    try:
        # a. Solicitar precio original
        precio_str = input("Ingrese el precio del artículo: ")
        precio_original = float(precio_str)
        
        # b. Preguntar por cupón
        tiene_cupon = input("¿Tiene cupón de descuento? (si/no): ").lower()
        
        precio_final = precio_original
        
        if tiene_cupon == "si":
            # c. Solicitar valor del cupón
            valor_cupon = float(input("Ingrese el valor del descuento: "))
            
            # d. Validar y aplicar descuento
            if valor_cupon > 0:
                # Opcional: Validar que el descuento no sea mayor al precio
                descuento_real = min(valor_cupon, precio_original)
                precio_final = precio_original - descuento_real
                print(f"Descuento de {descuento_real} aplicado.")
            else:
                print("El cupón no es válido (debe ser mayor a 0).")
        
        # e. Mostrar precio final
        print(f"El precio final a pagar es: {precio_final}")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

# NOTA PARA COLAB:
# La función ejecutar_tienda() contiene inputs. 
# Si la descomentas abajo, el script se pausará esperando que escribas.
# ejecutar_tienda()
