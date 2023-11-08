# https://leetcode.com/problems/jump-game/
import unittest
from unittest import TestCase
from merge_two_sorted_lists import solution

class MergeTwoSortedListsTestCase(TestCase):
	def test_1_step(self):
		output = solution([1, 2, 4], [1, 3, 4])

		assert output == [1, 1, 2, 3, 4, 4]

if __name__ == '__main__':
	unittest.main()
