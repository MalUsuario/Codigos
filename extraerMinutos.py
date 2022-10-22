def extraerMinutos(hora):
    return hora%100
def extraerHoras(hora):
    return int(hora/100)
def validarHora(hora):
    if(extraerMinutos(hora)<60 and extraerHoras(hora)<25):
        return True
    else:
        return False
def diferenciaHoras(hora1, hora2):
    if(validarHora(hora1) and validarHora(hora2)):
        horas = extraerHoras(hora2) - extraerHoras(hora1)
        minutos = extraerMinutos(hora2) - extraerMinutos(hora1)
        return (horas*60)+minutos
    else:
        return -1
