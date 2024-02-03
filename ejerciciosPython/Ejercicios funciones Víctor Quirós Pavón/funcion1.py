def escribir_centrado(texto):
    huecos = " " * (40 - len(texto) // 2)
    print(huecos + texto,"\n")