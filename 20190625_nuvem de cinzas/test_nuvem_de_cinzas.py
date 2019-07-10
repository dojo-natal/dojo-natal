# http://dojopuzzles.com/problemas/exibe/nuvem-de-cinzas/

import unittest
from nuvem_de_cinzas import nuvem_de_cinzas

class TenisTestCase(unittest.TestCase):
    def test_1_x_2(self):
        mapa = [
            ['*', 'A'],
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 1)

    def test_2_x_2(self):
        mapa = [
            ['*', '.'],
            ['.', 'A'],
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 2)

    def test_3_x_2(self):
        mapa = [
            ['*', '.'],
            ['.', '.'],
            ['.', 'A']
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 3)

    def test_3_x_2_2(self):
        mapa = [
            ['.', '.'],
            ['*', '.'],
            ['.', 'A']
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 2)

    def test_3_x_2_3(self):
        mapa = [
            ['.', '.'],
            ['.', '.'],
            ['*', 'A']
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 1)


    def test_fim(self):
        mapa = [
            ['.', '.', '.', '.', '*'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'A'],
            ['.', '.', '.', '.', '.'],
            ['A', '.', '.', '.', '.'],
        ]
        self.assertEqual(nuvem_de_cinzas(mapa), 8)


if __name__ == '__main__':
    unittest.main()
