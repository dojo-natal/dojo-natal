# https://www.urionlinejudge.com.br/judge/pt/problems/view/2249

import unittest

from numero_de_erdos import numero_de_erdos
 

class NumeroDeErdosTestCase(unittest.TestCase):
    def test_um_artigo_infinito(self):
        input_data = [
            ["a"]
        ]
        output_data = {
            "a": "infinito",
        }
        self.assertEqual(numero_de_erdos(input_data), output_data)

    def test_uma_pessoa_trabalha_diretamente_com_erdos(self):
        input_data = [
            ["erdos", "a"]
        ]
        output_data = {
            "a": 1,
        }
        self.assertEqual(numero_de_erdos(input_data), output_data)

    def test_mais_de_uma_pessoa_com_erdos(self):
        input_data = [
          ["erdos", "J. Silva", "M. Souza"],
        ]
        output_data = {
            "J. Silva": 1,
            "M. Souza": 1,
        }
        self.assertEqual(numero_de_erdos(input_data), output_data)

    def test_relacionamento_nivel_2(self):
        input_data = [
          ["erdos", "J. Silva", "M. Souza"],
          ["Genilson", "M. Souza"]
        ]
        output_data = {
            "J. Silva": 1,
            "M. Souza": 1,
            "Genilson": 2,
        }
        self.assertEqual(numero_de_erdos(input_data), output_data)
if __name__ == '__main__':
    unittest.main()
