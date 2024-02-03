def calcularSegundos(h, m, s):
    h = ((h * 60) * 60)
    m = (m * 60)
    totalsegundos = h + m + s
    return totalsegundos

def calcularHora(s):
    h = (s/60) /60
    m = (s % 3600) / 60
    s = (s % 3600) % 60

    return round(h), round(m), s