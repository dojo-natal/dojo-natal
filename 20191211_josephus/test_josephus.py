# https://www.urionlinejudge.com.br/judge/pt/problems/view/1030

import unittest

from josephus import josephus


class JosephusTestCase(unittest.TestCase):
    def test_quem_comeca_morre(self):
        n_pessoas = 2
        salto = 1
        self.assertEqual(josephus(n_pessoas, salto), 2)

    def test_com_salto_dois(self):
        n_pessoas = 2
        salto = 2
        self.assertEqual(josephus(n_pessoas, salto), 1)

    def test_com_salto_tres(self):
        n_pessoas = 2
        salto = 3
        self.assertEqual(josephus(n_pessoas, salto), 2)
    
    def test_tres_com_salto_1(self):
        n_pessoas = 3
        salto = 1
        self.assertEqual(josephus(n_pessoas, salto), 3)

    def test_tres_com_salto_2(self):
        n_pessoas = 3
        salto = 2
        self.assertEqual(josephus(n_pessoas, salto), 3)

    def test_tres_com_salto_3(self):
        n_pessoas = 3
        salto = 3
        self.assertEqual(josephus(n_pessoas, salto), 2)

    def test_tres_com_salto_4(self):
        n_pessoas = 3
        salto = 4
        self.assertEqual(josephus(n_pessoas, salto), 2)

    def test_tres_com_salto_5(self):
        n_pessoas = 3
        salto = 5
        self.assertEqual(josephus(n_pessoas, salto), 1)

    def test_tres_com_salto_6(self):
        n_pessoas = 3
        salto = 6
        self.assertEqual(josephus(n_pessoas, salto), 1)

    def test_final(self):
        n_pessoas = 1234
        salto = 233
        self.assertEqual(josephus(n_pessoas, salto), 25)

if __name__ == '__main__':
    unittest.main()
