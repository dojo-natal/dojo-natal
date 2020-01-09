# https://www.urionlinejudge.com.br/judge/pt/problems/view/1057

import unittest

from chegando_junto import chegando_junto
'''
A – Posição Inicial de Aneed
B – Posição Inicial de Ben
C – Posição Inicial de Cindy
. – Célula vazia
# - Obstáculo
X – Célula alvo
'''

class ChegandoJuntoTestCase(unittest.TestCase):
    def test_um_personagem_1(self):
        board = [
            ['B', 'X', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 1)

    def test_um_personagem_2(self):
        board = [
            ['B', '.', 'X'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 2)

    def test_um_personagem_3(self):
        board = [
            ['B', '.', '.'],
            ['.', '.', 'X'],
            ['.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 3)

    def test_um_personagem_4(self):
        board = [
            ['B', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', 'X'],
        ]
        self.assertEqual(chegando_junto(board), 4)

    def test_um_personagem_1_barreira_4(self):
        board = [
            ['X', '.', '.'],
            ['#', '.', '.'],
            ['B', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 4)    

    def test_um_personagem_1_barreira_2(self):
        board = [
            ['X', '.', '.'],
            ['.', '#', '.'],
            ['B', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 2)    

    def test_um_personagem_uma_barreira_para_quebrar(self):
        board = [
            ['#', 'X', 'B'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 1)

    def test_um_personagem_uma_barreira_para_quebrar2(self):
        board = [
            ['X', 'B', '#'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 1)

    def test_um_personagem_uma_barreira_para_quebrar_mesmo(self):
        board = [
            ['#', 'X', '.', 'B'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]
        self.assertEqual(chegando_junto(board), 2)

if __name__ == '__main__':
    unittest.main()
