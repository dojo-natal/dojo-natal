# http://dojopuzzles.com/problemas/exibe/diamantes/

import unittest
from diamante import diamond

class DiamanteTestCase(unittest.TestCase):
    def test_simple_diamond(self):
        result = diamond('A')
        expected = [
            ['A']
        ]
        self.assertEqual(result, expected)

    def test_B_diamond(self):
        result = diamond('B')
        expected = [
            [' ', 'A', ' '],
            ['B', ' ', 'B'],
            [' ', 'A', ' ']
        ]
        self.assertEqual(result, expected)

    def test_C_diamond(self):
        result = diamond('C')
        expected = [
            [' ', ' ', 'A', ' ', ' '],
            [' ', 'B', ' ', 'B', ' '],
            ['C', ' ', ' ', ' ', 'C'],
            [' ', 'B', ' ', 'B', ' '],
            [' ', ' ', 'A', ' ', ' '],      
        ]
        self.assertEqual(result, expected)
    
    def test_D_diamond(self):
        result = diamond('D')
        expected = [
            [' ', ' ', ' ', 'A', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', ' '],
            [' ', 'C', ' ', ' ', ' ', 'C', ' '],
            ['D', ' ', ' ', ' ', ' ', ' ', 'D'],
            [' ', 'C', ' ', ' ', ' ', 'C', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', ' '],
            [' ', ' ', ' ', 'A', ' ', ' ', ' '],      
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()	   
