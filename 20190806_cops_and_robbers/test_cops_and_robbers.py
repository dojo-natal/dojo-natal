# https://www.urionlinejudge.com.br/judge/pt/problems/view/1905

import unittest

from cops_and_robbers import cops_and_robbers


class CopsAndRobbersTestCase(unittest.TestCase):
    def test_one_single_free_space(self):
        board = [
            [0]
        ]
        self.assertEqual(cops_and_robbers(board), 'cops')

    def test_non_free_space(self):
        board = [
            [1]
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_2x2_last_space_busy(self):
        board = [
            [0, 0],
            [0, 1]
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')
    
    def test_2x2_without_way_to_robbers(self):
        board = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_2x2_without_way_to_robbers_on_first_line(self):
        board = [
            [1, 0],
            [0, 0]
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_3x3_second_line_blocked(self):
        board = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_3x3_second_column_blocked(self):
        board = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_3x3_diagonal_blocked(self):
        board = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_3x3_with_random_walls(self):
        board = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

    def test_5x5_with_random_walls_cops_U(self):
        board = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'cops')

    def test_cops_from_uri(self):
        board = [
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0],
        ]
        self.assertEqual(cops_and_robbers(board), 'cops')

    def test_robbers_from_uri(self):
        board = [
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0]
        ]
        self.assertEqual(cops_and_robbers(board), 'robbers')

if __name__ == '__main__':
    unittest.main()
