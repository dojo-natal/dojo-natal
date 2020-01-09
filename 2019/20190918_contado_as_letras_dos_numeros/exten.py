#!/urb/bin/env python
# _*_ coding: utf-8 _*_


unidades = ["zero", "um", "dois", "tres", "quatro",
            "cinco", "seis", "sete", "oito", "nove"]

teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

tens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"]

def tercia(num):
    numero=str(num)
    numero.zfill(3)
    a=int(numero[0])
    b=int(numero[1])
    c=int(numero[2])
    if a == 0:
        if b == 0:
            resultado=unidades[c]
            return resultado
        elif b == 1:
            if c >= 0 and c <= 9:
                resultado = teens[c]
                return resultado
        elif b == 2:
            if c == 0:
                resultado = 'vinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='vinte e '+unidades[c]
                return resultado
        elif b >=3 and b <= 9:
            if c == 0:
                resultado = tens[b-1]
                return resultado
            if c >= 1 and c <= 9:
                resultado = tens[b-1]+' e '+unidades[c]
                return resultado
    if a == 1:
        if b == 0:
            if c == 0:
                resultado = 'cem'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='cento e '+unidades[c]
                return resultado
        elif  b == 1:
            if c >= 0 and c <= 9:
                resultado = 'cento e '+teens[c]
                return resultado
        elif b == 2:
            if c == 0:
                resultado = 'cento e vinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado ='cento e vinte e '+unidades[c]
                return resultado
        elif b >= 3 and b <= 9:
            if c == 0:
                resultado = 'cento e '+tens[b-1]
                return resultado
            elif c > 0 and c <= 9:
                resultado = 'cento e '+tens[b-1]+ ' e '+unidades[c]
                return resultado

    elif a >= 2 and a <= 9:
        if a == 2 and b ==0 and c == 0:
            prefix='duzentos'
        elif a ==2:
            prefix='duzentos e '

        if a == 3 and b ==0 and c == 0:
            prefix='trezentos'
        elif a == 3:
            prefix='trezentos e '
        if a == 4 and b ==0 and c == 0:
            prefix='quatrocentos'
        elif a == 4:
            prefix='quatrocentos e '
        if a == 5 and b ==0 and c == 0:
            prefix='quinhentos'
        elif a == 5:
            prefix='quinhentos e '
        if a == 6 and b ==0 and c == 0:
            prefix='seiscentos'
        elif a == 6:
            prefix='seiscentos e '

        if a == 7 and b ==0 and c == 0:
            prefix='setecentos'
           
        elif a == 7:
            prefix='setecentos e '
        if a == 8 and b ==0 and c == 0:
            prefix='oitocentos'
        elif a == 8:
            prefix='oitocentos e '
        if a == 9 and b ==0 and c == 0:
            prefix='novecentos'
        elif a == 9:
            prefix='novecentos e '

        if b == 0:
            if c == 0:
                resultado = prefix
                return resultado
            elif c > 0 and c <= 9:
                resultado = prefix+unidades[c]
                return resultado
        elif b == 1:
            if c >= 0 and c <= 9:
                resultado = prefix+teens[c]
                return resultado
            #elif c >= 6 and c <= 9:
                #resultado = prefix+tens[b-1]+' e '+unidades[c]
                return resultado
        elif b == 2:
            if c == 0:
                resultado = prefix+'vinte'
                return resultado
            elif c > 0 and c <= 9:
                resultado = prefix+'vinte e '+unidades[c]
                return resultado
        elif b >= 3 and b <= 9:
            if c == 0:
                resultado = prefix+tens[b-1]
                return resultado
            elif c > 0 and c <= 9:
                resultado = prefix+tens[b-1]+' e '+unidades[c]
                return resultado
def main(num):
    result=''
    numero=str(num)
    numero=numero.zfill(9)+numero
    posicion=1
    for i in [0,3,6]:
        var=numero[i]+numero[i+1]+numero[i+2]
        if int(var) != 0:
            res=tercia(var)
            if i == 0:
                result=res+" milhões "
            elif i == 3:
                result=result+res+" mil "
            elif i == 6:
                result=result+res
    return result