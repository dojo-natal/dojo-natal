# https://www.urionlinejudge.com.br/judge/pt/problems/view/1372
import unittest

# Cada caixa terá inicialmente pelo menos 1 e no máximo 103 doces.
# M(linhas) e N(colunas) (1 ≤ M ≤ 10^5) x (1 ≤ N ≤ 10^5),
# Cada caixa terá inicialmente pelo menos 1 e no máximo 10^3 doces.


"""
board = [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 8, 1, 1],
  [1, 1, 1, 1, 1],
]
board = [
  [1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, x, 0, 1],
  [0, 0, 0, 0, 0],
]
"""

def zerar_envolta(board, x, y):
    new_board = board[:]

    try:
      new_board[y][x-1] = 0
    except:
      pass

    try:
      new_board[y][x + 1] = 0
    except:
      pass

    return new_board

def pega_e_zera(board, x, y):
    new_board = board[:]
    v = new_board[y][x] # peguei
    new_board[y][x] = 0 # zerei
    new_board = zerar_envolta(board, x, y) # zero envolta
    return None, v


def next(board, max_doces):
  linha = board[0]
  max_element = max(linha)
  max_element_x = linha.index(max_element)
  _, v = pega_e_zera(board, x=max_element_x, y=0)
  max_doces += v
  return board, max_doces

def doces(board):
  max_doces = 0
  board, max_doces = next(board, max_doces)
  board, max_doces = next(board, max_doces)
  return max_doces


class DocesTestCase(unittest.TestCase):
  def test_1_linha_1_colunas(self):
      board = [
        [1],
      ]
      self.assertEqual(doces(board), 1)

  def test_1_linha_1_colunas_2_doces(self):
        board = [
          [2],
        ]
        self.assertEqual(doces(board), 2)

  def test_1_linha_2_colunas(self):
        board = [
          [0, 1],
        ]
        self.assertEqual(doces(board), 1)

  def test_1_linha_3_colunas(self):
        board = [
          [0, 1, 2]
        ]
        self.assertEqual(doces(board), 2)

  def test_1_linha_4_colunas_aplicando_regra(self):
        board = [
          [0, 1, 2, 3]
        ]
        self.assertEqual(doces(board), 4)


if __name__ == "__main__":
  unittest.main()
