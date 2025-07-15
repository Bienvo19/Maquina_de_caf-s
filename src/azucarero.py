class Azucarero:
    def __init__(self, cantidad_azucar):
        self.cantidad_azucar = cantidad_azucar

    def tiene_azucar(self, cantidad):
        return self.cantidad_azucar >= cantidad

    def usar_azucar(self, cantidad):
        if self.tiene_azucar(cantidad):
            self.cantidad_azucar -= cantidad
            return True
        return False