# https://www.hackerrank.com/challenges/conway
import hy
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

    def test_4x4_keep_alive_with3(self):
        board = [
            [0, 1],
            [0, 1]
        ]
        next_board = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(game_of_life(board), next_board)



if __name__ == "__main__":
    unittest.main()
