def dia_de_pascua(anio):
    #Calculo de residuos
    A = anio % 19
    B = anio % 4
    C = anio % 7
    D = ((19 * A)+ 24) % 30
    E =  ( (2 * B) + (4 * C) + (6 * D) + 5 ) % 7
    Dia = (22 + D + E) 

    if 22 + D + E <= 31:
        Dia = (22 + D + E) 
    else: 
      Dia = (22 + D + E - 31)
      
    return Dia
def calculo(panio):
    a=panio%19
    b=panio%4
    c=panio%7
    d= ( (19 * a) + 24)%30
    e=( (2 * b ) + ( 4 * c ) + ( 6 * d ) + 5 )%7
    mes=( 22 + d + e )
    return mes
def mes_de_pascua(anio):
    mes=calculo(anio)
    if(mes<=31):
        return "Marzo"
    else:
        return "Abril "
def dia_de_pascua(anio):
    dia=calculo(anio)
    if(dia<=31):
        return dia
    else:
        return dia-31
