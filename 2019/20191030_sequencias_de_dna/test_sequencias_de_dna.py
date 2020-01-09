# https://www.urionlinejudge.com.br/judge/pt/problems/view/1373

import unittest

from sequencias_de_dna import sequencias_de_dna

class SequenciasDeDnaTestCase(unittest.TestCase):
    def test_nao_existe_subsequencia_comum(self):
        w1 = "lov"
        w2 = "hat"
        k = 1
        self.assertEqual(sequencias_de_dna(w1, w2, k), 0)

    def test_strings_iguais(self):
        w1 = "love"
        w2 = "love"
        k = 1
        self.assertEqual(sequencias_de_dna(w1, w2, k), 4)

    def test_strings_iguais(self):
        w1 = "lovee"
        w2 = "lovee"
        k = 1
        self.assertEqual(sequencias_de_dna(w1, w2, k), 5)

    def test_sub_1(self):
        w1 = "likl"
        w2 = "love"
        k = 1
        self.assertEqual(sequencias_de_dna(w1, w2, k), 1)

    def test_sub_2(self):
        w1 = "lokl"
        w2 = "love"
        k = 2
        self.assertEqual(sequencias_de_dna(w1, w2, k), 2)

    def test_sub_3(self):
        w1 = "lolovk"
        w2 = "love"
        k = 2
        self.assertEqual(sequencias_de_dna(w1, w2, k), 3)

    # def test_x(self):
    #     w1 = "x" * 100
    #     w2 = "x" * 98 + "ll"
    #     k = 100
    #     self.assertEqual(sequencias_de_dna(w1, w2, k), 0)

    def test_x_ll(self):
        w1 = "x" * 100
        w2 = "x" * 98 + "ll"
        k = 98
        self.assertEqual(sequencias_de_dna(w1, w2, k), 98)

    def test_ll_x(self):
        import string
        import random
        def id_generator(size=1, chars=string.ascii_lowercase):
            return ''.join(random.choice(chars) for _ in range(size))
        
        w1_iter_1 = [id_generator() for _ in range(48)]        
        w1_iter_2 = [id_generator() for _ in range(48)]        
        w1 = "".join(w1_iter_1 + list("xyzw") + w1_iter_2)

        w2_iter_1 = [id_generator() for _ in range(48)]        
        w2_iter_2 = [id_generator() for _ in range(48)]        
        w2 = "".join(w2_iter_2 + list("xyzw") + w2_iter_2)

        k = 4
        self.assertEqual(sequencias_de_dna(w1, w2, k), 4)


if __name__ == '__main__':
    unittest.main()	
