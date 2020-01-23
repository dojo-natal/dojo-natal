# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

import unittest

from you_can_go_your_own_way import is_possible, you_can_go_your_own_way

class YouCanGoYourOwnWayCase(unittest.TestCase):
    def test_2_x_2_1(self):
        lydia_path = "SE"
        player_path = you_can_go_your_own_way(lydia_path)
        self.assertFalse(is_possible(lydia_path, player_path))


class IsPossibleCase(unittest.TestCase):
    def test_2_x_2_1(self):
        lydia_path = "SE"
        player_path = "ES"
        self.assertTrue(is_possible(lydia_path, player_path))

    def test_2_x_2_false1(self):
        lydia_path = "SE"
        player_path = "S"
        self.assertFalse(is_possible(lydia_path, player_path))

    def test_2_x_2_false2(self):
        lydia_path = "SE"
        player_path = "E"
        self.assertFalse(is_possible(lydia_path, player_path))

    def test_2_x_2_south_two_times_false(self):
        lydia_path = "SE"
        player_path = "SS"
        self.assertFalse(is_possible(lydia_path, player_path))  

    def test_2_x_2_false2(self):
        lydia_path = "SE"
        player_path = "SE"
        self.assertFalse(is_possible(lydia_path, player_path))

    def test_3_x_3_1_false(self):
        lydia_path = "SEES"
        player_path = "EESS"
        self.assertTrue(is_possible(lydia_path, player_path)) 

    def test_3_x_3_2_false(self):
        lydia_path = "SEES"
        player_path = "EE"
        self.assertFalse(is_possible(lydia_path, player_path))

    def test_3_x_3_same_cell_false(self):
        lydia_path = "ESES"
        player_path = "SS"
        self.assertFalse(is_possible(lydia_path, player_path))

    def test_3_x_3_same_cell_in_the_false(self):
        lydia_path = "ESES"
        player_path = "SSEE"
        self.assertTrue(is_possible(lydia_path, player_path))
    




if __name__ == '__main__':
    unittest.main()