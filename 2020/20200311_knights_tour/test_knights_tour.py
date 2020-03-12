# https://pt.wikipedia.org/wiki/Problema_do_cavalo
import hy
from knights_tour import knights_tour
import unittest

"""
[
3  [][f][]
2  [][][] 
1 [i][][]
   A  B  C 
]
"""

class KnightsTourTestCase(unittest.TestCase):
    def test_2x2_impossivel(self):
        self.assertFalse(
            knights_tour(lado=2, x=1, y=1))

    def test_3x3_(self):
        self.assertFalse(
            knights_tour(lado=2, x=1, y=1))


if __name__ == "__main__":
    unittest.main()
