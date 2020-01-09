def oito_damas(board): 
    # horizontal
    for linha in board:
        qnt_dama_linha = 0
        for item in linha:
            if item == "Q":
                qnt_dama_linha += 1
            if qnt_dama_linha > 1:
                return False

    transposed_board = zip(*board)
    # vertical
    for linha in transposed_board:
        qnt_dama_linha = 0
        for item in linha:
            if item == "Q":
                qnt_dama_linha += 1
            if qnt_dama_linha > 1:
                return False

    # diagonal igual
    tamahno_board = len(board) - 1
    qnt_dama_diagonal = 0
    for x in range(0, tamahno_board):
        for y in range(0, tamahno_board):
            if x == y and board[y][x] == "Q":
                qnt_dama_diagonal += 1
            if qnt_dama_diagonal >= 2:
                return False

    # diagonal perto
    tamahno_board = len(board)
    qnt_dama_diagonal = 0
    dama_list = []
    for x in range(0, tamahno_board):
        for y in range(0, tamahno_board):
            if board[x][y] == "Q":
                dama_list.append([x,y])

    for dama in dama_list:
        if dama[0] == 2 and dama[1] == 0:
            qnt_dama_diagonal+=1
        if dama[0] == 3 and dama[1] == 1:
            qnt_dama_diagonal+=1
        if qnt_dama_diagonal >=2:
            return False

    return True