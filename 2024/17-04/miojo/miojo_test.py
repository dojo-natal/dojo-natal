# https://cncodingdojo.wordpress.com/2010/10/06/kata-9-miojo/
import unittest
from unittest import TestCase
from miojo import miojo

class Miojo(TestCase):
  def test_1(self):
    a = 5
    b = 7
    t = 3
    self.assertEqual(miojo(a,b,t), 10)

  def test_2(self):
    a = 22
    b = 15
    t = 14
    self.assertEqual(miojo(a,b,t), 44)

  def test_3(self):
    a = 22
    b = 15
    t = 14
    self.assertEqual(miojo(a,b,t), 45)


if __name__ == '__main__':
  unittest.main()
