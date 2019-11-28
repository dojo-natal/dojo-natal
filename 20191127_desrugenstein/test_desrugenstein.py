import unittest

from desrugenstein import desrugenstein

"""
N S O L
4
|0 1 0 1 (0, 3)| 0 0 1 0 (1, 3) | 0 0 0 1 (2, 3) | 0 1 0 0 (3, 3)
|0 0 0 0 (0, 2)| 1 0 0 1 (1, 2) | 0 0 0 1 (2, 2) | 0 1 0 0 (3, 2)
|1 0 0 0 (0, 1)| 1 0 1 0 (1, 1) | 1 1 0 0 (2, 1) | 0 1 1 0 (3, 1)
|0 0 0 0 (0, 0)| 0 0 1 0 (1, 0) | 0 0 1 0 (2, 0) | 0 0 0 0 (3, 0)

5
x y x y
1 3 0 3
2 3 3 0
2 3 0 0
3 1 3 2
0 3 0 0
0

"""


class DesrugensteinTestCase(unittest.TestCase):
    def test_custo_impossible(self):
        cidade = [
            [[0, 1, 0, 1], [0, 0, 0, 0]],
        ]
        rotas = [
            [[1, 0],[0, 0]],
        ]
        self.assertEqual(desrugenstein(cidade, rotas), "Impossible")

    def test_custo_1(self):
        cidade = [
            [[0, 1, 0, 1], [0, 0, 1, 0]],
        ]
        rotas = [
            [[1, 0], [0, 0]],
        ]
        self.assertEqual(desrugenstein(cidade, rotas), 1)

    def test_custo_2(self):
        cidade = [
            [[0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]],
        ]
        rotas = [
            [[2, 0],[0, 0]], 
        ]
        self.assertEqual(desrugenstein(cidade, rotas), 2)

    def test_custo_3(self):
        cidade = [
            [[0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
        ]
        rotas = [
            [[3, 0],[0, 0]], 
        ]
        self.assertEqual(desrugenstein(cidade, rotas), 3)

    def test_custo_2_no_meio(self):
        cidade = [
            [[0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 1, 0]]
        ]
        rotas = [
            [[1, 0],[2, 0]], 
        ]
        self.assertEqual(desrugenstein(cidade, rotas), 1)


if __name__ == '__main__':
    unittest.main()
