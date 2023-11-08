# https://leetcode.com/problems/jump-game/
import unittest
from unittest import TestCase
from search_suggestions_system import search_suggestion

class SearchSuggestionsSystemTestCase(TestCase):
	def test_1(self):
		products = ["a","aab","aabb","acb","baa"]
		searchword = "aab"
		result = search_suggestion(products, searchword)
		self.assertEquals(
			result, 
			[
				["a", "aab", "aabb"], 
				["aab", "aabb"],
				["aab", "aabb"]
			],
		)

if __name__ == '__main__':
	unittest.main()
