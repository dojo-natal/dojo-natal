# https://leetcode.com/problems/jump-game/
import unittest
from unittest import TestCase
from jump_game import jump_game

class JumpGameTestCase(TestCase):
	"""
	constraints:
		1 <= nums.length <= 10^4
		0 <= nums[i] <= 10^5	
	"""
	def test_1_step(self):
		nums = [0]
		self.assertEqual(jump_game(nums), True)

	def test_2_step(self):
		nums = [0,1]
		self.assertEqual(jump_game(nums), False)

	def test_3_step(self):
		nums = [1,1]
		self.assertEqual(jump_game(nums), True)

	def test_4_step(self):
		nums = [1,1,5]
		self.assertEqual(jump_game(nums), True)
	
	def test_5_step(self):
		nums = [3,2,1,0,1,4]
		self.assertEqual(jump_game(nums), False)

	def test_6_step(self):
			nums = [2,3,1,1,4]
			self.assertEqual(jump_game(nums), True)

	def test_7_step(self):
	 	nums = [3,2,1,0,4]
	 	self.assertEqual(jump_game(nums), False)

	def test_8_step(self):
	 	nums = [3,2,2,0,4]
	 	self.assertEqual(jump_game(nums), True)

if __name__ == '__main__':
	unittest.main()
