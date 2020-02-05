# http://crbonilha.com/2014/03/22/o-problema-do-troco
import unittest

from problema_do_troco import problema_do_troco


class ProblemaDoTrocoTestCase(unittest.TestCase):
    def test_1_tipo_1_N(self):
        tipos_de_moedas = [1]
        qt_de_troco = 1
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 1)

    def test_2_tipo_1_N(self):
        tipos_de_moedas = [1]
        qt_de_troco = 2
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 2)

    def test_3_tipo_2_1_N(self):
        tipos_de_moedas = [2, 1]
        qt_de_troco = 3 
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 2)

    def test_5_tipo_2_1_N(self):
        tipos_de_moedas = [2, 1]
        qt_de_troco = 5
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 3)

    def test_6_tipo_2_1_N(self):
        tipos_de_moedas = [2, 1]
        qt_de_troco = 6
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 3)

    def test_9_tipo_5_4_2_N(self):
        tipos_de_moedas = [1, 2, 8, 14, 25]
        qt_de_troco = 28
        self.assertEqual(problema_do_troco(qt_de_troco, tipos_de_moedas), 2)


if __name__ == '__main__':
    unittest.main()
