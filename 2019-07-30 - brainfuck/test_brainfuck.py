# https://www.urionlinejudge.com.br/judge/pt/problems/view/1456/

import unittest
from brainfuck import brainfuck


class BrainFuckTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(brainfuck("a", ",."), "a")

    def test_aba(self):
        self.assertEqual(brainfuck("aba", ",.,.,."), "aba")

    def test_ab_next_back(self):
        self.assertEqual(brainfuck("aba", ",.>,.<."), "aba")

    def test_a_increment(self):
        self.assertEqual(brainfuck("a", ",+."), "b")

    def test_b_decrement(self):
        self.assertEqual(brainfuck("b", ",-."), "a")

    def test_loop(self):
        self.assertEqual(brainfuck("abab", "[,.>]"), "abab")


if __name__ == '__main__':
    unittest.main()
