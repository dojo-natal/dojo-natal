# http://dojopuzzles.com/problemas/exibe/numeros-romanos/

import unittest
from numeros_romanos import numeros_romanos


class NumerosRomanosTestCase(unittest.TestCase):
    def test_numero_1(self):
        self.assertEquals(numeros_romanos(1), 'I')

    def test_numero_2(self):
        self.assertEquals(numeros_romanos(2), 'II')

    def test_numero_3(self):
        self.assertEquals(numeros_romanos(3), 'III')

    def test_numero_4(self):
        self.assertEquals(numeros_romanos(4), 'IV')

    def test_numero_5(self):
        self.assertEquals(numeros_romanos(5), 'V')

    def test_numero_6(self):
        self.assertEquals(numeros_romanos(6), 'VI')
    
    def test_numero_7(self):
        self.assertEquals(numeros_romanos(7), 'VII')

    def test_numero_8(self):
        self.assertEquals(numeros_romanos(8), 'VIII')

    def test_numero_10(self):
        self.assertEquals(numeros_romanos(10), 'X')

    def test_numero_20(self):
        self.assertEquals(numeros_romanos(20), 'XX')

    def test_numero_40(self):
        self.assertEquals(numeros_romanos(40), 'XL')

    def test_numero_50(self):
        self.assertEquals(numeros_romanos(50), 'L')

    def test_numero_60(self):
        self.assertEquals(numeros_romanos(60), 'LX')    

    def test_numero_70(self):
        self.assertEquals(numeros_romanos(70), 'LXX')


    def test_numero_80(self):
        self.assertEquals(numeros_romanos(80), 'LXXX')

    def test_numero_90(self):
        self.assertEquals(numeros_romanos(90), 'XC')



if __name__ == '__main__':
    unittest.main()	