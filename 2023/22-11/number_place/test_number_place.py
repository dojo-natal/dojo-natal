# https://atcoder.jp/contests/abc327/tasks/abc327_c
import unittest
from unittest import TestCase
from number_place import number_place_9x9, number_place_3x3


class NumberPlaceTestCase(TestCase):
	"""
	constraints:
		For each row of A, the nine cells in that row contain 
			each integer from 1 to 9 exactly once.
		For each column of A, the nine cells in that column contain 
			each integer from 1 to 9 exactly once.
		Divide the rows of A into three groups, each of three rows, 
			from top to bottom, and similarly divide the columns into 
			three groups, each of three columns, from left to right. 
			Each 3×3 grid obtained from A in this way contains 
			each integer from 1 to 9 exactly once.

	"""
	def test_1_step(self):
		nums = [
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[4, 5, 6, 7, 8, 9, 1, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), True)


	def test_2_step(self):
		nums = [
			[1, 1, 3, 4, 5, 6, 7, 8, 9],
			[4, 5, 6, 7, 8, 9, 1, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), False)

	def test_3_step(self):
		nums = [
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 5, 6, 7, 8, 9, 4, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), False)

	def test_4_step(self):
		nums = [
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[2, 1, 6, 7, 8, 9, 4, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), False)

	def test_5_step(self):
		nums = [
			[1, 2, 3, 4, 5, 6, 1, 8, 9],
			[4, 5, 6, 7, 8, 9, 7, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), False)

	def test_6_step(self):
		nums = [
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[4, 5, 6, 7, 8, 9, 1, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[1, 9, 2, 3, 4, 5, 6, 7, 8]
		]
		self.assertEqual(number_place_9x9(nums), False)

	def test_final_step(self):
		nums = [
			[4, 9, 1, 7, 8, 2, 3, 6, 5],
			[3, 2, 6, 5, 9, 4, 1, 8, 7],
			[7, 5, 8, 3, 1, 6, 4, 2, 9],
			[1, 3, 7, 8, 6, 5, 9, 4, 2],
			[2, 6, 5, 4, 7, 9, 8, 1, 3],
			[8, 4, 9, 1, 2, 3, 7, 5, 6],
			[6, 8, 2, 9, 4, 7, 5, 3, 1],
			[9, 1, 3, 6, 5, 8, 2, 7, 4],
			[5, 7, 4, 2, 3, 1, 6, 9, 8]
		]
		self.assertEqual(number_place_9x9(nums), True)


class NumberPlace3x3TestCase(TestCase):
	def test_3x3_1(self):
		nums = [
			[1, 2, 3],
			[1, 4, 6],
			[7, 8, 9],
		]
		self.assertEqual(number_place_3x3(nums), False)

	def test_3x3_2(self):
		nums = [
			[1, 2, 3],
			[5, 4, 6],
			[7, 8, 9],
		]
		self.assertEqual(number_place_3x3(nums), True)

if __name__ == '__main__':
	unittest.main()
