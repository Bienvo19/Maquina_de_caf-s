from src.dispensador_vasos import DispensadorVasos

def test_uso_de_vaso():
    vasos = DispensadorVasos("pequeño", 3, 5)
    assert vasos.usar_vaso() == True
    assert vasos.cantidad == 4

def test_sin_vasos():
    vasos = DispensadorVasos("mediano", 5, 0)
    assert vasos.usar_vaso() == False