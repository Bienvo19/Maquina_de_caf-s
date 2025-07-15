from src.azucarero import Azucarero

def test_uso_de_azucar():
    azucarero = Azucarero(10)
    assert azucarero.usar_azucar(3) == True
    assert azucarero.cantidad_azucar == 7

def test_azucar_insuficiente():
    azucarero = Azucarero(2)
    assert azucarero.usar_azucar(5) == False