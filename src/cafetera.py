class Cafetera:
    def __init__(self, cantidad_cafe):
        self.cantidad_cafe = cantidad_cafe

    def tiene_cafe(self, cantidad):
        return self.cantidad_cafe >= cantidad

    def usar_cafe(self, cantidad):
        if self.tiene_cafe(cantidad):
            self.cantidad_cafe -= cantidad
            return True
        return False