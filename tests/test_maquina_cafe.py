from src.cafetera import Cafetera
from src.azucarero import Azucarero
from src.dispensador_vasos import DispensadorVasos
from src.maquina_cafe import MaquinaCafe

def test_servir_cafe_exitoso():
    cafetera = Cafetera(10)
    azucarero = Azucarero(5)
    vasos = {
        "pequeño": DispensadorVasos("pequeño", 3, 1)
    }
    maquina = MaquinaCafe(cafetera, azucarero, vasos)
    mensaje = maquina.servir_cafe("pequeño", 2)
    assert mensaje == "Café pequeño con 2 cucharadas de azúcar servido"

def test_sin_vasos():
    cafetera = Cafetera(10)
    azucarero = Azucarero(5)
    vasos = {}
    maquina = MaquinaCafe(cafetera, azucarero, vasos)
    mensaje = maquina.servir_cafe("mediano", 1)
    assert mensaje == "No hay vasos disponibles"