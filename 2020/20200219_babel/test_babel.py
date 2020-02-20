# https://www.urionlinejudge.com.br/judge/pt/problems/view/1085
import unittest
from babel import babel


class BabelTestCase(unittest.TestCase):
    def test_1_edge_3(self):
        origem = "P"
        destino = "A"
        edges = [
            ("P", "A", "red"),
        ]
        self.assertEqual(babel(origem, destino, edges), 3)

    def test_1_edge_4(self):
        origem = "Q"
        destino = "B"
        edges = [
            ("Q", "B", "red3"),
        ]
        self.assertEqual(babel(origem, destino, edges), 4)

    def test_2_edge_caminhos_iguais(self):
        origem = "A"
        destino = "D"
        edges = [
            ("A", "D", "black"),
            ("A", "D", "red"),
        ]
        self.assertEqual(babel(origem, destino, edges), 3)

    def test_2_edge_caminhos_ao_destino(self):
        origem = "A"
        destino = "C"
        edges = [
            ("A", "B", "black"),
            ("B", "C", "red"),
        ]
        self.assertEqual(babel(origem, destino, edges), 8)

    def test_3_edge_impossivel(self):
        origem = "A"
        destino = "X"
        edges = [
            ("A", "B", "Alack"),
            ("B", "C", "bed"),
            ("C", "D", "red"),
        ]
        self.assertEqual(babel(origem, destino, edges), "impossivel")


if __name__ == "__main__":
    unittest.main()