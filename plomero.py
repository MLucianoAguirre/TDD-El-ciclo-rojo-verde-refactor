def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if zona == "periferica":
        return 12000
    return 8000

def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if zona == "periferica":
        return 12000
    elif zona == "fuera_de_la_ciudad":
        return 18000
    return 8000

def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if trabajo_mismo_dia:
        return 0

    if zona == "periferica":
        return 12000
    elif zona == "fuera_de_la_ciudad":
        return 18000
    return 8000

def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if trabajo_mismo_dia:
        return 0

    if zona == "periferica":
        tarifa_base = 12000
    elif zona == "fuera_de_la_ciudad":
        tarifa_base = 18000
    else:
        tarifa_base = 8000

    if es_fin_de_semana:
        tarifa_base *= 1.5

    return int(tarifa_base)