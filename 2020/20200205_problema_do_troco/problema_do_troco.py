def problema_do_troco(quantidade, tipos):
    moedas_usadas = 0
    tipos = sorted(tipos)
    max_tipo = tipos.pop()
    
    while quantidade != 0:
        if quantidade - max_tipo < 0:
            max_tipo = tipos.pop()
            moedas_usadas += 1
            break
        else:    
            quantidade -= max_tipo
            moedas_usadas += 1
    return moedas_usadas

