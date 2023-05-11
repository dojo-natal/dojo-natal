# https://www.beecrowd.com.br/judge/pt/problems/view/2458
import unittest
from unittest import TestCase

from problema_facil import facil

class ProblemaFacilTestCase(TestCase):
	def test_01(self):
		vetor = [1, 3, 2, 2, 4, 3, 2, 1]
		consulta = [
			[1, 3],
			[2, 4],
			[3, 2],
			[4, 2],
		] 
		indeces_vetor = [2, 0, 7, 0]
		self.assertEqual(facil(vetor, consulta), indeces_vetor)

	def test_02(self):
		vetor = [1, 3, 2, 2, 4, 3, 2, 1]
		consulta = [
			[1, 3],
			[2, 4],
			[3, 2],
			[4, 2],
		] 
		indeces_vetor = [2, 0, 7, 0]
		self.assertEqual(facil(vetor, consulta), indeces_vetor)



if __name__ == '__main__':
	unittest.main()