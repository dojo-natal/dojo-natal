import typing as t


def get_prox_index(tabuleiro, index_atual: t.Tuple[int, int]) ->  t.Tuple[int, int]:
    x, y = index_atual
    simbolo = tabuleiro[x][y]
    if simbolo == "V":
      prox = (x + 1), y
    elif simbolo == "A":
      prox = (x - 1), y
    elif simbolo == "<":
      prox = x, (y - 1)
    elif simbolo == ">":
      prox = x, (y + 1)
    
    return prox

def is_fora(tabuleiro, index_atual) -> bool:
  row, column = index_atual
  try:
    tabuleiro[row][column]
    return True
  except IndexError:
    return False


def setas(tabuleiro):
  N = len(tabuleiro)
  safe = [[False for n in range(N)] for n in range(N)]
  visited = [[False for n in range(N)] for n in range(N)]
  count_safe = 0
  # ‘V’ Aponta para a célula da linha abaixo, na mesma coluna 
  # ‘<’ (sinal menor-que) aponta para a célula à esquerda, na mesma linha 
  # ‘>’ (sinal maior-que) aponta para a célula à direita, na mesma linha 
  # ‘A’ Aponta para a célula da linha acima, na mesma coluna 

  caminhoAtual = []
  invalidos = []

  def percorrer(tabuleiro, pos_inicial, invalidos):
    # retorna True se for seguro
    caminhoAtual = [pos_inicial]
    x, y = pos_inicial
    visited[x][y] = True
    prox_index = get_prox_index(tabuleiro, pos_inicial)
    if is_fora(tabuleiro, prox_index) or prox_index in invalidos: # NAO EH SEGURO
      invalidos = invalidos + caminhoAtual + [prox_index]
      px, py = prox_index
      visited[px][py] = True
      caminhoAtual = []
      return False
    if prox_index in caminhoAtual:
      count_safe += len(caminhoAtual)
      return True
  
    percorrer(tabuleiro, prox_index, invalidos)

  count_seguro = 0
  for x in range(N):
    for y in range(N):
      if percorrer(tabuleiro, pos_inicial=(x, y), invalidos=[]):
        count_seguro += 1
  
  return count_seguro

