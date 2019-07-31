# https://www.urionlinejudge.com.br/judge/pt/problems/view/1426

import unittest
from tijolos import tijolos


class TijolosTestCase(unittest.TestCase):
    def test_little_wall(self):
        piramide = [
            [2],
            [None, None],
            [1, None, 1]
        ]
        piramide_que_eu_quero = [
            [2],
            [1,1],
            [1,0,1]
        ]
        self.assertEqual(tijolos(piramide), piramide_que_eu_quero)

    def test_little_big_wall(self):
        piramide = [
            [24],
            [None, None],
            [5, None, 7],
            [None, None, None, None],
            [2, None, 3, None, 4]
        ]
        piramide_que_eu_quero = [
            [24],
            [11, 13],
            [5, 6, 7],
            [2, 3, 3, 4],
            [2, 0, 3, 0, 4]
        ]
        self.assertEqual(tijolos(piramide), piramide_que_eu_quero)

    def test_bigbig_wall(self):
        piramide = [
            [255],
            [None]*2,
            [54, None, 67],
            [None]*4,
            [10, None, 18, None, 13],
            [None]*6,
            [3, None, 3, None, 5, None, 2],
            [None]*8,
            [2,None,  1, None,  2, None,  1, None,  1]
        ]
        piramide_que_eu_quero = [
            [255],
			[121, 134],
			[54, 67, 67],
			[23, 31, 36, 31],
			[10, 13, 18, 18, 13],
			[5, 5, 8, 10, 8, 5],
			[3, 2, 3, 5, 5, 3, 2],
			[2, 1, 1, 2, 3, 2, 1, 1],
			[2, 0, 1, 0, 2, 1, 1, 0, 1],
        ]
        self.assertEqual(tijolos(piramide), piramide_que_eu_quero)

if __name__ == '__main__':
    unittest.main()	
