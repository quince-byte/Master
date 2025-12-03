print("--- INICIO DE LOS EJERCICIOS (35 al 40) ---")

# --- EJERCICIO 35: CLASE USUARIO BANCO ---
print("\n--- Ejercicio 35: Clase UsuarioBanco ---")

class UsuarioBanco:
    # a. Inicializar
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # b. Retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"-> {self.nombre} retiró {cantidad}. Nuevo saldo: {self.saldo}")

    # d. Agregar dinero
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"-> {self.nombre} ingresó {cantidad}. Nuevo saldo: {self.saldo}")

    # c. Transferir dinero (de self a otro_usuario)
    def transferir_dinero(self, otro_usuario, cantidad):
        print(f"--- Intentando transferir {cantidad} de {self.nombre} a {otro_usuario.nombre} ---")
        try:
            # Primero intentamos retirar; si falla, saltará el error y no se agregará al otro
            self.retirar_dinero(cantidad) 
            otro_usuario.agregar_dinero(cantidad)
            print("-> Transferencia exitosa.")
        except ValueError as e:
            print(f"-> Error en transferencia: {e}")

# CASO DE USO:
print("\n... Ejecutando Caso de Uso Banco ...")

# a. Crear dos usuarios: Alicia (100) y Bob (50)
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# b. Agregar 20 unidades al saldo de Bob (50 + 20 = 70)
bob.agregar_dinero(20)

# c. Transferir 80 unidades de Bob a Alicia
# Bob tiene 70. Quiere transferir 80. Esto debería fallar.
bob.transferir_dinero(alicia, 80)

# d. Retirar 50 unidades del saldo de Alicia
alicia.retirar_dinero(50)

# Estado final
print(f"\nEstado Final -> Alicia: {alicia.saldo}, Bob: {bob.saldo}")
