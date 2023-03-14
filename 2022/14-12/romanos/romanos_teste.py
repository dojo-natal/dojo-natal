import unittest
from unittest import TestCase

from romanos import convert_indo_to_romanos, convert_romanos_to_indo

class RomanosTestCase(TestCase):
	def test_convert_indo_to_romanos_1(self):
		self.assertEqual(convert_indo_to_romanos(1), 'I')
		# self.assertEqual(convert_indo_to_romanos('1'), 'I')

	def test_convert_indo_to_romanos_2(self):
		self.assertEqual(convert_indo_to_romanos(2), 'II')
		# self.assertEqual(convert_indo_to_romanos('2'), 'II')

	def test_convert_indo_to_romanos_3(self):
		self.assertEqual(convert_indo_to_romanos(3), 'III')

	def test_convert_indo_to_romanos_4(self):
		self.assertEqual(convert_indo_to_romanos(4), 'IV')

	def test_convert_indo_to_romanos_5(self):
		self.assertEqual(convert_indo_to_romanos(5), 'V')

	def test_convert_indo_to_romanos_6(self):
		self.assertEqual(convert_indo_to_romanos(6), 'VI')

	def test_convert_indo_to_romanos_7(self):
		self.assertEqual(convert_indo_to_romanos(7), 'VII')

	def test_convert_indo_to_romanos_8(self):
		self.assertEqual(convert_indo_to_romanos(8), 'VIII')

	def test_convert_indo_to_romanos_9(self):
		self.assertEqual(convert_indo_to_romanos(9), 'IX')
	
	def test_convert_indo_to_romanos_10(self):
		self.assertEqual(convert_indo_to_romanos(10), 'X')

	def test_convert_indo_to_romanos_400(self):
		self.assertEqual(convert_indo_to_romanos(400), 'CD')

if __name__ == '__main__':
	unittest.main()