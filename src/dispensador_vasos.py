class DispensadorVasos:
    def __init__(self, tipo_vaso, capacidad_vaso, cantidad):
        self.tipo_vaso = tipo_vaso
        self.capacidad_vaso = capacidad_vaso
        self.cantidad = cantidad

    def tiene_vasos(self):
        return self.cantidad > 0

    def usar_vaso(self):
        if self.tiene_vasos():
            self.cantidad -= 1
            return True
        return False