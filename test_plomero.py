from plomero import calcular_visita

def test_zona_centrica_dia_semana_sin_trabajo():
    assert calcular_visita("centrica", False, False) == 8000