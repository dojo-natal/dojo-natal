# https://www.beecrowd.com.br/judge/pt/problems/view/2458
import unittest
from unittest import TestCase

from setas import setas, get_prox_index, is_fora

class SetasTestCase(TestCase):
	def test_n1(self):
		tabuleiro = [['>']]
		self.assertEqual(setas(tabuleiro), 0)

	def test_n2(self):
		tabuleiro = [
			['V', '>'],
			['>', '<']
		]
		self.assertEqual(setas(tabuleiro), 3)

	def test_n2_loop(self):
		tabuleiro = [
			['>', 'V'],
			['A', '<']
		]
		self.assertEqual(setas(tabuleiro), 4)

class ProxIndexTestCase(TestCase):
	def test_1(self):
		tabuleiro = [['>']]
		self.assertEqual(get_prox_index(tabuleiro, (0,0)), (0,1))
	def test_2(self):
		tabuleiro = [['A']]
		self.assertEqual(get_prox_index(tabuleiro, (0,0)), (-1,0))
	def test_3(self):
		tabuleiro = [['<']]
		self.assertEqual(get_prox_index(tabuleiro, (0,0)), (0,-1))
	def test_4(self):
		tabuleiro = [['V']]
		self.assertEqual(get_prox_index(tabuleiro, (0,0)), (1,0))

class IsForaTestCase(TestCase):
	def test_is_dentro(self):
		tabuleiro = [
			['V', '>'],
			['>', '<']
		]
		self.assertEqual(is_fora(tabuleiro, (0,2)), False)
	
	def test_is_dentro2(self):
		tabuleiro = [
			['V', '>'],
			['>', '<']
		]
		self.assertEqual(is_fora(tabuleiro, (0,0)), True)

if __name__ == '__main__':
	unittest.main()
