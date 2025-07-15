from .cafetera import Cafetera
from .azucarero import Azucarero
from .dispensador_vasos import DispensadorVasos

class MaquinaCafe:
    def __init__(self, cafetera, azucarero, vasos):
        self.cafetera = cafetera
        self.azucarero = azucarero
        self.vasos = vasos

    def servir_cafe(self, tipo_vaso, cantidad_azucar):
        dispensador = self.vasos.get(tipo_vaso)
        if not dispensador or not dispensador.tiene_vasos():
            return "No hay vasos disponibles"
        if not self.cafetera.tiene_cafe(dispensador.capacidad_vaso):
            return "No hay café disponible"
        if not self.azucarero.tiene_azucar(cantidad_azucar):
            return "No hay azúcar disponible"

        dispensador.usar_vaso()
        self.cafetera.usar_cafe(dispensador.capacidad_vaso)
        self.azucarero.usar_azucar(cantidad_azucar)
        return f"Café {tipo_vaso} con {cantidad_azucar} cucharadas de azúcar servido"