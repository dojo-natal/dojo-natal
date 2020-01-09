# https://www.hackerrank.com/challenges/common-child/problem

import unittest

from common_child import common_child

class CommonChildTestCase(unittest.TestCase):
    def test_x(self):
        ans = common_child('a', 'a')
        self.assertEqual(ans, 1)

    def test_x_2(self):
        ans = common_child('ab', 'aa')
        self.assertEqual(ans, 1)

    def test_x_3(self):
        ans = common_child('aa', 'ab')
        self.assertEqual(ans, 1)

    def test_x_4(self):
        ans = common_child('aabc', 'abad')
        self.assertEqual(ans, 2)

    def test_x_5(self):
        ans = common_child('harry', 'sally')
        self.assertEqual(ans, 2)

    def test_x_6(self):
        ans = common_child("a"*500, "a"*500)
        self.assertEqual(ans, 500)

if __name__ == '__main__':
    unittest.main()	
