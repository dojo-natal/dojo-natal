class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for lin in range(len(grid)):
          for col in range(len(grid[lin])):  
            if grid[lin][col] == '1':
                # Percorrer todos as celulas adjacents
                # Precisa olhar pra direita, esquerda, cima e baixo
                # Encontrou Terra na celula adjacente adiciona a fila
                # Nao achou mais nada, afunda a fila
                count += 1 #conta a a quantidade de ilhas
                lin_atual = lin
                col_atual = col
                fila = []
                fila.append((lin_atual, col_atual))

                #pecorrendo toda a lista e zerando as posi
                while(len(fila) != 0):
                    [lin_atual,col_atual] = fila[0]
                    grid[lin_atual][col_atual] = "0"
                    if (col_atual+1 < len(grid[lin])): #direita
                        if grid[lin_atual][col_atual+1] == '1':
                            fila.append((lin_atual, col_atual + 1))

                    if (lin_atual+1 < len(grid)): #baixo
                        if grid[lin_atual+1][col_atual] == '1':
                            fila.append((lin_atual+1, col_atual))
                    
                    if (col_atual-1 >= 0): #esquerda
                        if grid[lin_atual][col_atual - 1] == '1':
                            fila.append((lin_atual, col_atual - 1))
                    
                    if (lin_atual-1 >= 0): #cima
                        if grid[lin_atual-1][col_atual] == '1':
                            fila.append((lin_atual-1, col_atual))
                    fila.pop(0)

        return count
             
