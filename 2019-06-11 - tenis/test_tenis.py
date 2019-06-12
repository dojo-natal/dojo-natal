# http://dojopuzzles.com/problemas/exibe/partida-de-tenis/

import unittest
from tenis import play_tenis

class TenisTestCase(unittest.TestCase):
    def test_partida_em_branco(self):
        lances = []
        resultado = play_tenis(lances)
        self.assertEqual(resultado, 'D')

    def test_partida_jogador_1_ganha(self):
        lances = [1]
        resultado = play_tenis(lances)
        self.assertEqual(resultado, 1)

    def test_partida_jogador_2_ganha(self):
        lances = [1, 2, 2]
        resultado = play_tenis(lances)
        self.assertEqual(resultado, 2)

    def test_deuce(self):
        lances = [1, 1, 1, 2, 2, 2]
        resultado = play_tenis(lances)
        self.assertEqual(resultado, 'D')

if __name__ == '__main__':
    unittest.main()	    