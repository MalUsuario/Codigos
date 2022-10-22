def calcular_costo_ninos(cantidad):
    costo_ninos = 0
    if cantidad <= 2:
        costo_ninos = (cantidad) * 6000
    else:
        costo_ninos = (cantidad) * 6000 * 0.85
    return costo_ninos

def calcular_costo_adultos(cantidad):
    costo_adultos = 0
    if cantidad == 4:
        costo_adultos = (cantidad - 1) * 10000
    else:
        costo_adultos = (cantidad) * 10000
    return costo_adultos

def calcular_dos_uno(cantidad_adultos):
    costo_dos_uno = 0
    if cantidad_adultos == 2:
        costo_dos_uno = (cantidad_adultos - 1) * 10000
    else:
        costo_dos_uno = (cantidad_adultos) * 10000
    return costo_dos_uno

def tu_cine(dia, cantidad_ninos, cantidad_adultos):
    costo_total = 0
    if dia == 3:
        costo_total = float((calcular_dos_uno(cantidad_adultos) + calcular_costo_ninos(cantidad_ninos)))
    else:
        costo_total = float(calcular_costo_ninos(cantidad_ninos) + calcular_costo_adultos(cantidad_adultos))
    return costo_total
