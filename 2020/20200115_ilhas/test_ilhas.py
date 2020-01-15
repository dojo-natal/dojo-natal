import unittest

from ilhas import ilhas


class IlhasTestCase(unittest.TestCase):
    def test_0_ilhas(self):
        board = [
            [0]
        ]
        self.assertEqual(ilhas(board), 0)

    def test_1_ilha(self):
        board = [
            [1]
        ]
        self.assertEqual(ilhas(board), 1)

    def test_1_ilha_horizontal(self):
        board = [
            [1, 0],
        ]
        self.assertEqual(ilhas(board), 1)

    def test_1_ilha_quadrado(self):
        board = [
            [1,0,0],
            [1,0,0],
            [1,0,0]
        ]
        self.assertEqual(ilhas(board), 1)

    def test_2_ilha_quadrado(self):
        board = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
        self.assertEqual(ilhas(board), 1)

    def test_2_ilha_quadrado(self):
        board = [
            [1, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(ilhas(board), 4)

if __name__ == '__main__':
    unittest.main()
