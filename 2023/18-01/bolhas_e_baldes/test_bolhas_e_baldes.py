# https://www.beecrowd.com.br/judge/pt/problems/view/1088
import unittest
from unittest import TestCase

from bolhas_e_baldes import bolhas_e_baldes

class BolhasEBaldesTestCase(TestCase):
	def test_5_1(self):
		n = 5
		seq = [1, 5, 3, 4, 2]
		self.assertEqual(bolhas_e_baldes(seq), "Marcelo")

	def test_5_2(self):
		n = 5
		seq = [5, 1, 3, 4, 2]
		self.assertEqual(bolhas_e_baldes(seq), "Carlos")


if __name__ == '__main__':
	unittest.main()