def sumatoria_i(a, b):
    resultado = 0
    for i in range(a, b+1):
        resultado = resultado + i
    return resultado

def sumatoria_r(a, b):
    if a > b:
        return 0
    else:
        return a + sumatoria_r(a+1, b)
