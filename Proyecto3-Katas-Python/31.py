# Busco nombre con excepción propia en caso de error
class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre_usuario():
    try:
        entrada_nombres = "Juan,Ana,Pedro"
        lista_nombres = [n.strip() for n in entrada_nombres.split(',')]
        objetivo = input("¿A quién buscas?: ")
        print(f"Lista: {lista_nombres} | Buscando a: {objetivo}")
        # Si el nombre no está en la lista, lanzo la excepción
        if objetivo in lista_nombres:
            print(f"¡Éxito! {objetivo} está en la lista.")
        else:
            raise NombreNoEncontradoError(f"El nombre '{objetivo}' no se encuentra en la lista.")
            
    except NombreNoEncontradoError as e:
        print(f"Excepción capturada: {e}")

buscar_nombre_usuario()
