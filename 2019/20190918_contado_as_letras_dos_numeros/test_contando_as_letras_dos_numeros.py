# http://dojopuzzles.com/problemas/exibe/contando-as-letras-dos-numeros/
# https://www.hardware.com.br/comunidade/algoritmo-escrever/1224976/

import unittest

from contando_as_letras_dos_numeros import contando_as_letras_dos_numeros
#from exten import main as tercia
import exten


def tercia_num(n):
    return sum([len(exten.main(numero).replace(' ','')) for numero in range(1, n+1)])

class ContandoAsLetrasDosNumerosTestCase(unittest.TestCase):
    def test_um(self):
        self.assertEqual(contando_as_letras_dos_numeros([1]), 2)

    def test_um_a_dois(self):
        self.assertEqual(contando_as_letras_dos_numeros([1, 2]), 6)

    def test_um_a_tres(self):
        self.assertEqual(contando_as_letras_dos_numeros([1, 2, 3]), 10)

    def test_um_a_cinco(self):
        self.assertEqual(contando_as_letras_dos_numeros(range(1,6)), 21)

    def test_um_a_dez(self):
        self.assertEqual(contando_as_letras_dos_numeros(range(1,11)), 40)

    def test_um_a_vinte(self):
        self.assertEqual(contando_as_letras_dos_numeros(range(1,21)), 105)

    def test_um_a_21(self):
        self.assertEqual(contando_as_letras_dos_numeros(range(1,22)), tercia_num(21))

    def test_um_a_cem(self):
        self.assertEqual(contando_as_letras_dos_numeros(range(1,101)), tercia_num(100))

    # def test_um_a_29(self):
    #     self.assertEqual(contando_as_letras_dos_numeros(range(1,30)), 105 + (6 * 9) + 37)

    # def test_tercia(self):
    #    self.assertEqual(contando_as_letras_dos_numeros(range(1, 1001)), 19759+3)

if __name__ == '__main__':
    unittest.main()
