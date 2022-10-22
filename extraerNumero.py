def extraer(num):
    cont=0
    if(num==0):
        return 0
    else:
        if num<10:
            return (num*11)
        while num!=0:
            if num>10:
                num1=num%10
                num=int(num/10)
                if cont==0:
                    numero=num1
                cont =cont+1
            else:
                if cont>0:				        
                    numero=(num*10)+numero
                    num=numero
                    return num
                else:
                    return num
