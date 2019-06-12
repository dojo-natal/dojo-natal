def diamond(l):
    if l == 'A':
        return [[l]]
    if l == 'B':
        return [
            [' ', 'A', ' '],
            ['B', ' ', 'B'],
            [' ', 'A', ' '],
        ]
    if l == 'C':
        return [
            [' ', ' ', 'A', ' ', ' '],
            [' ', 'B', ' ', 'B', ' '],
            ['C', ' ', ' ', ' ', 'C'],
            [' ', 'B', ' ', 'B', ' '],
            [' ', ' ', 'A', ' ', ' '],      
        ]

    inicio = ord("A")
    escolhido = ord(l)
    diferenca = escolhido - inicio
    return diferenca
    # total = escolhido - inicio + 1
    # tamanho = 2*(escolhido-inicio) + 1
    # resultado = []

    # tamanho = 5
    # i = 0

    # for i in total:
    #     linha = []
    #     for j in total:
    #         if ...:
    #             linha.append(' ')
    #         else:


    #     resultado.append(linha)



    # return resultado