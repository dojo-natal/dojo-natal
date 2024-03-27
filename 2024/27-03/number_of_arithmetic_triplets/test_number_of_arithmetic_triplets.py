# https://leetcode.com/problems/number-of-arithmetic-triplets/submissions/1215863647/
import unittest
from unittest import TestCase
from number_of_arithmetic_triplets import number_of_arithmetic_triplets

"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
"""


class MakeArrayZeroTestCase(TestCase):
	maxDiff = None

	def test_1(self):
		nums = [0,1,4,6,7,10]
		diff = 3
		self.assertEqual(
			number_of_arithmetic_triplets(nums, diff), 2
		)

	def test_2(self):
		nums = [4,5,6,7,8,9]
		diff = 2
		self.assertEqual(
			number_of_arithmetic_triplets(nums, diff), 2
		)

if __name__ == '__main__':
	unittest.main()
