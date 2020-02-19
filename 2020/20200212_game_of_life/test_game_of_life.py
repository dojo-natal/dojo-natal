# https://leetcode.com/problems/game-of-life/
from game_of_life import game_of_life
import unittest

class GameOfLifeTestCase(unittest.TestCase):
    def test_4x4_bringing_dead_alive(self):
        board = [
            [0, 1],
            [1, 1]
        ]
        next_board = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(game_of_life(board), next_board)

    def test_4x4_everybody_dies(self):
        board = [
            [0, 0],
            [1, 1]
        ]
        next_board = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(game_of_life(board), next_board)

    def test_4x4_todos_morrem_vive_um(self):
        board = [
            [1, 0],
            [1, 1]
        ]
        next_board = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(game_of_life(board), next_board)


if __name__ == "__main__":
    unittest.main()