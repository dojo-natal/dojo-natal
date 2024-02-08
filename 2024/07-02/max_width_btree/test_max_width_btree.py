# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
import unittest
from unittest import TestCase
from max_width_btree import max_width_btree

class MaxWidthBTreeTestCase(TestCase):
	def test_1(self):
		root = [1,3,2,5,]
		self.assertEqual(max_width_btree(root), 2)

	def test_2(self):
		root = [1,3,2,5,None,None,9,6,None,7]
		self.assertEqual(max_width_btree(root), 7)

if __name__ == '__main__':
	unittest.main()
