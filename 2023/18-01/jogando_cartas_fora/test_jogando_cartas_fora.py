# https://www.beecrowd.com.br/judge/pt/problems/view/1110
import unittest
from unittest import TestCase

from jogando_cartas_fora import jogando_cartas_fora

class JogandoCartasForaTestCase(TestCase):
	def test_7(self):
		self.assertEqual(jogando_cartas_fora(7), ([1, 3, 5, 7, 4, 2], 6))


if __name__ == '__main__':
	unittest.main()