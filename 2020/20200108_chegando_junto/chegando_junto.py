def get_index(board, v):
    for i, linha in enumerate(board):
        for j, elemento in enumerate(linha):
            if elemento == v:
                return i, j
    return None

def barreira_entre_alvo(board):
    target_index = get_index(board, 'X')
    target_index_B = get_index(board, 'B')
    target_index_obstaculo = get_index(board, '#')
    
    if mesma_coluna(target_index_B,target_index, target_index_obstaculo):
        if target_index_obstaculo[1] < target_index[1] and target_index_alvo[1] < target_index_obstaculo[1]:
            return True
        if target_index_obstaculo[1] > target_index[1] and target_index[1] > target_index_B[1]:
            return True
    elif  mesma_linha(target_index_B,target_index, target_index_obstaculo):
        if target_index_obstaculo[0] < target_index[0] and target_index_alvo[0] < target_index_obstaculo[0]:
            return True
        if target_index_obstaculo[0] > target_index[0] and target_index[0] > target_index_B[0]:
            return True
    return False 

def mesma_linha(index_pessoa, index_alvo, index_obstaculo):
    return index_pessoa[0] == index_alvo[0] and index_obstaculo[0] == index_pessoa[0]

    def mesma_coluna(index_pessoa, index_alvo, index_obstaculo):
    return index_pessoa[1] == index_alvo[1] and index_obstaculo[1] == index_pessoa[1]

def chegando_junto(board):
    target_index = get_index(board, 'X')
    target_index_B = get_index(board, 'B')
    target_index_obstaculo = get_index(board, '#')
    abs_x = abs(target_index[0] - target_index_B[0])
    abs_y = abs(target_index[1] - target_index_B[1])
    dist_min = abs_x + abs_y
    if target_index_obstaculo:

        if barreira_entre_alvo(board):
        
            return dist_min + 2

    return dist_min
        
   