
class UsuarioBanco:
    #Inicializar
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"-> {self.nombre} retiró {cantidad}. Nuevo saldo: {self.saldo}")

    # Agregar dinero
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"-> {self.nombre} ingresó {cantidad}. Nuevo saldo: {self.saldo}")

    # Transferir dinero
    def transferir_dinero(self, otro_usuario, cantidad):
        print(f"--- Intentando transferir {cantidad} de {self.nombre} a {otro_usuario.nombre} ---")
        try:
            # Primero intentamos retirar; si falla, saltará el error y no se agregará al otro usuario
            self.retirar_dinero(cantidad) 
            otro_usuario.agregar_dinero(cantidad)
            print("-> Transferencia exitosa.")
        except ValueError as e:
            print(f"-> Error en transferencia: {e}")

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print(f"\nEstado Final -> Alicia: {alicia.saldo}, Bob: {bob.saldo}")
