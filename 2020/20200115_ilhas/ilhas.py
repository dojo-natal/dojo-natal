from collections import defaultdict


def create_bool_matrix(board):
    return [[False for x in range(len(board))] for y in range(len(board))]


def dfs(board, visiteds, x, y):
    if board[x][y] == 1 and not visiteds[x][y]:
        visiteds[x][y] = True
        if x > 0:
            dfs(board, visiteds, x-1, y) # left
        if x < len(board)-1:
            dfs(board, visiteds, x+1, y) # right
        if y > 0:
            dfs(board, visiteds, x, y-1) # up
        if y < len(board)-1:
            dfs(board, visiteds, x, y+1) # down


def ilhas(board):
    count_ilhas = 0
    visiteds = create_bool_matrix(board)
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if not visiteds[x][y] and board[x][y] == 1:
                dfs(board, visiteds, x, y)
                count_ilhas += 1


    return count_ilhas