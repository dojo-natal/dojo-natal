# https://www.beecrowd.com.br/judge/pt/problems/view/2800
import unittest
from unittest import TestCase

from brincando_de_consultas import consultar

class BrincandoDeConsultasTestCase(TestCase):
	def test_01(self):
		vetor = [1, 2, 3, 4]
		consultas = [
			[2, 1, 2, 2],
			[2, 1, 2, 3],
			[1, 2, 1],
			[2, 1, 2, 2]
		] 
		indeces_vetor = [1, 2, 2]
		self.assertEqual(consultar(vetor, consultas), indeces_vetor)


if __name__ == '__main__':
	unittest.main()