dic = { 
    1:len('um'), 
    2:len('dois'), 
    3:len('tres'), 
    4:len('quatro'), 
    5:len('cinco'),
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 3,
    11: 4,
    12: 4,
    13: 5,
    14: len('quatorze'),
    15: len('quinze'),
    16: len('dezesseis'),
    17: len('dezessete'),
    18: len('dezoito'),
    19: len('dezenove'),
    20: len('vinte'),
    30: len('trinta'),
    40: len('quarenta'),
    50: len('cinquenta'),
    60: len('sesseenta'),
    70: len('setenta'),
    80: len('oitenta'),
    90: len('oventa'),
    100: len('cem'),
    200: len('duzentos'),
    300: len('trezetos'),
    400: len('quatrocentros'),
    500: len('quinhentos'),
    600: len('seiscentos'),
    700: len('setecentos'),
    800: len('oitocentos'),
    900: len('novecentos'),
    1000: len('mil'),
}


def contando_as_letras_dos_numeros(numeros):
    acc = 0
    for numero in numeros:
        if numero <= 20:
            acc += dic[numero]
        elif numero <= 100:
            dec = numero // 10
            dec *= 10
            resto = numero % 10
            acc += dic[resto] + 1 + dic[dec]
        
    return acc