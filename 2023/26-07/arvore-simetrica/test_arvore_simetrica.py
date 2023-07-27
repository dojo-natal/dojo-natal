# https://www.beecrowd.com.br/judge/pt/problems/view/2800
import unittest
from unittest import TestCase

from arvore_simetrica import isSymetric


class Node(object):
		def __init__(self, val=0, left=None, right=None):
				self.val = val
				self.left = left
				self.right = right


class ArvoreSimetricaTestCase(TestCase):
	# def test_01(self):
	# 	arvore = Node(val=2, left=None, right=None)
	# 	self.assertTrue(isSymetric(arvore))

	def test_02(self):
		arvore = Node(val=1, left=Node(val=2, left=None, right=None), right=None)
		self.assertFalse(isSymetric(arvore))

	# def test_03(self):
	# 	arvore = Node(
	# 		val=1,
	# 		left=Node(val=2, left=None, right=None), 
	# 		right=Node(val=2, left=None, right=None)
	# 	)
	# 	self.assertTrue(isSymetric(arvore))

	# def test_04(self):
	# 	arvore = Node(
	# 		val=1,
	# 		left=Node(
	# 			val=2, 
	# 			left=Node(val=3, left=None, right=None), 
	# 			right=Node(val=4, left=None, right=None)
	# 		), 
	# 		right=Node(
	# 			val=2, 
	# 			left=Node(val=3, left=None, right=None), 
	# 			right=Node(val=4, left=None, right=None)
	# 		)
	# 	)
		self.assertTrue(isSymetric(arvore))



if __name__ == '__main__':
	unittest.main()