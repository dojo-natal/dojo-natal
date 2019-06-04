import unittest
from problem import foo

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(foo())


if __name__ == '__main__':
    unittest.main()
