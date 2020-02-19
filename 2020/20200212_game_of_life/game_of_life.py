from copy import copy


def game_of_life(board):
    newboard = copy(board)
    tamanho_do_board = len(board)
    # cont_vivas = 0
   
    # Get a quantidade de vivos
    for y in range(tamanho_do_board):
        for x in range(tamanho_do_board):
            cell_situation = board[x][y]
            cont_vivas = 0
           
            try:
                cont_vivas += board[x-1][y]
            except:
                pass
            try:
                cont_vivas += board[x-1][y-1]
            except:
                pass
            try:
                cont_vivas += board[x][y-1]
            except:
                pass
            try:
                cont_vivas += board[x+1][y-1]
            except:
                pass
            try:
                cont_vivas += board[x+1][y]
            except:
                pass
            try:
                cont_vivas += board[x+1][y+1]
            except:
                pass
            try:
                cont_vivas += board[x][y+1]
            except:
                pass
            try:
                cont_vivas += board[x-1][y+1]
            except:
                pass

            '''
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            '''
            if cell_situation == 0 and cont_vivas == 3:
                newboard[x][y] = 1
            if cont_vivas < 2:
                newboard[x][y] = 0
            if cell_situation == 1 and cont_vivas == 2 or cont_vivas == 3:
                newboard[x][y] = 1
            if cont_vivas > 3:
                newboard[x][y] = 0

    return newboard     