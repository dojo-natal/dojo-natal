# http://dojopuzzles.com/problemas/exibe/quebra-de-linha/

import unittest
from quebra_linha import quebra_linha

class QuebraLinhaTestCase(unittest.TestCase):

    def test_uma_linha(self):
        frase = 'banana'
        self.assertEqual(quebra_linha(frase), ['banana'])

    def test_uma_linha_20_caracteres(self):
        frase = 'banana banana banana'
        self.assertEqual(quebra_linha(frase), ['banana banana banana'])

    def test_duas_linhas(self):
        frase = 'uma minhoca muito bonita'
        self.assertEqual(quebra_linha(frase), ['uma minhoca muito', 'bonita'])

    def teste_palavra_grande(self):
        frase = 'pneumoultramicroscopicosilicovulcanoconiotico'
        


if __name__ == '__main__':
    unittest.main()	