from src.cafetera import Cafetera

def test_uso_de_cafe():
    cafetera = Cafetera(10)
    assert cafetera.usar_cafe(5) == True
    assert cafetera.cantidad_cafe == 5

def test_cafe_insuficiente():
    cafetera = Cafetera(3)
    assert cafetera.usar_cafe(5) == False