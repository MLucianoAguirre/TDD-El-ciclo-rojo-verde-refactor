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