# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/#

import unittest
from telefone import telefone

class TelefoneTestCase(unittest.TestCase):
    def test_MY_LOVE(self):
    	self.assertEqual(telefone("MY LOVE"), "69 5683")

    def test_M(self):
        self.assertEqual(telefone("M"), "6")

    def test_A(self):
        self.assertEqual(telefone("A"), "2")

    def test_MNO(self):
        self.assertEqual(telefone("MNO"), "666")

    def test_10GKZ(self):
        self.assertEqual(telefone("10GKZ"), "10459")

    def test_hifen(self):
        self.assertEqual(telefone("-"), "-")

    def test_1_h_HOME_h_SWEET_h_HOME(self):
        self.assertEqual(telefone("1-HOME-SWEET-HOME"), "1-4663-79338-4663") 

if __name__ == '__main__':
    unittest.main()	