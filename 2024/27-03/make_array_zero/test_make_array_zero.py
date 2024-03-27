# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
import unittest
from unittest import TestCase
from make_array_zero import make_array_zero

"""
You are given a non-negative integer array nums. In one operation, you must:

- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

"""


class MakeArrayZeroTestCase(TestCase):
	maxDiff = None

	def test_1(self):
		nums = [1, 5, 0, 3, 5]
		self.assertEqual(
			make_array_zero(nums), 3
		)

	def test_2(self):
		nums = [0]
		self.assertEqual(
			make_array_zero(nums), 0
		)

	def test_3(self):
		nums = [0, 4, 2, 4]
		self.assertEqual(
			make_array_zero(nums), 2
		)

	def test_4(self):
		nums = [2,0,2]
		self.assertEqual(
			make_array_zero(nums), 1
		)

if __name__ == '__main__':
	unittest.main()
