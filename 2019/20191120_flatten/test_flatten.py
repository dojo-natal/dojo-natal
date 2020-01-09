import unittest

from flatten import flatten

# [1, 2, [3, 4, [5, 6, [1]]]] => [1, 2, 3, 4, 5, 6, 1]

class FlattenTestCase(unittest.TestCase):
    def test_flat_list(self):
        self.assertEqual(flatten([1]), [1])

    def test_list_nested_two_level(self):
        self.assertEqual(flatten([[1]]), [1])

    def test_list_nested_three_levels(self):
        self.assertEqual(flatten([[[1]]]), [1])

    def test_list_nested_two_levels_two_elements(self):
        self.assertEqual(flatten([[[1, 1]]]), [1, 1])

    def test_quebra(self):
        self.assertEqual(
            flatten([[[1, 1], 1], 1]), [1, 1, 1, 1]
        )



if __name__ == '__main__':
    unittest.main()
