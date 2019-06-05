# http://dojopuzzles.com/problemas/exibe/problema-do-miojo/

import unittest
from miojo import miojo

class MiojoTestCase(unittest.TestCase):
    def test_3_5_7(self):
        self.assertTrue(miojo(3, 5, 7))

    def test_3_7_5(self):
        self.assertTrue(miojo(3, 7, 5))

    def test_3_5_5(self):
        self.assertFalse(miojo(3, 5, 5))

    def test_3_3_3(self):
        self.assertTrue(miojo(3, 3, 3))

    def test_3_4_4(self):
    	self.assertFalse(miojo(3, 4, 4))

    def test_3_6_6(self):
    	self.assertFalse(miojo(3, 6, 6))

    def test_3_8_5(self):
    	self.assertTrue(miojo(3, 8, 5))

    def test_3_5_8(self):
    	self.assertTrue(miojo(3, 5, 8))

    def test_3_9_39(self):
    	self.assertTrue(miojo(3, 9, 39))

    def test_3_39_9(self):
    	self.assertTrue(miojo(3, 39, 9))

    def test_3_5_15(self):
    	self.assertFalse(miojo(3, 5, 15))

    def test_3_18_7(self):
    	self.assertTrue(miojo(3, 18, 7))

    def test_6_3_3(self):
    	self.assertTrue(miojo(6, 3, 3))

    def test_9_3_3(self):
    	self.assertTrue(miojo(9, 3, 3))


if __name__ == '__main__':
    unittest.main()	