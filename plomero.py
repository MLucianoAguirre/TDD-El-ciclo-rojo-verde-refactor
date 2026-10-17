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

def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    zonas_validas = {
        "centrica": 8000,
        "periferica": 12000,
        "fuera_de_la_ciudad": 18000
    }

    if zona not in zonas_validas:
        raise ValueError("Zona no valida")

    if trabajo_mismo_dia:
        return 0

    tarifa = zonas_validas[zona]
    if es_fin_de_semana:
        tarifa *= 1.5

    return int(tarifa)