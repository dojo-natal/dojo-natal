# https://pt.wikipedia.org/wiki/Problema_das_oito_damas
# https://www.geeksforgeeks.org/8-queen-problem/

import unittest

from oito_damas import oito_damas

# 8
# 8x8

class OitoDamasTestCase(unittest.TestCase):
    def test_3_4_x_4(self):
        board = [
            [None, None, None, None],
            [None, "Q", None, None],
            [None, None, None, "Q"],
            ["Q", None, None, None],
            
        ]
        self.assertTrue(oito_damas(board))

    def test_3_4_x_4_false(self):
        board = [
            [None, None, None, None],
            [None, "Q", None, None],
            [None, None, None, "Q"],
            [None, "Q", None, None]
        ]
        self.assertFalse(oito_damas(board))

    def test_3_4_x_4_linha_false(self):
        board = [
            [None, None, None, None],
            [None, "Q", "Q", None],
            [None, None, None, "Q"],
            [None, None, None, None]
        ]
        self.assertFalse(oito_damas(board))        

    def test_3_4_quebrando_roubado(self):
        board = [
            [None, None, None, None],
            ["Q", None, None, None],
            [None, None, None, "Q"],
            ["Q", None, None, None]
        ]
        self.assertFalse(oito_damas(board))

    def test_diagonal_first_x_y_igual(self):
        board = [
            [None, None, None, "Q"],
            [None, "Q", None, None],
            [None, None, "Q", None],
            [None, None, None, None],
        ]
        self.assertFalse(oito_damas(board))

    def test_diagonal_first_x_y_perto(self):
        board = [
            [None, None, None, "Q"],
            [None, None, None, None],
            ["Q", None, None, None],
            [None, "Q", None, None],
        ]
        self.assertFalse(oito_damas(board))

    def test_diagonal_first_x_y_perto_2(self):
        board = [
            [None, None, None, None],
            ["Q", None, None, None],
            [None, None, None, None],
            [None, None, "Q", None],
        ]
        self.assertFalse(oito_damas(board))

if __name__ == '__main__':
    unittest.main()
