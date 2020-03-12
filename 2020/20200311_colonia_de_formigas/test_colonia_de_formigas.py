# https://www.urionlinejudge.com.br/judge/pt/problems/view/1135
from colonia_de_formigas import colonia_de_formigas
import unittest


class ColoniaDeFormigasTestCase(unittest.TestCase):
    def test_simples(self):
        tuneis = [
            (1, 0, 2),
        ]
        queries = [
            (1, 0),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 2)

    def test_simples_ainda(self):
        tuneis = [
            (1, 0, 3),
        ]
        queries = [
            (1, 0),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 3)

    def test_dois_tuneis(self):
        tuneis = [
            (1, 0, 3),
            (0, 2, 5),
        ]
        queries = [
            (1, 2),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 8)

    def test_dois_tuneis(self):
        tuneis = [
            (1, 0, 3),
            (0, 2, 5),
        ]
        queries = [
            (1, 2),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 8)

    def test_tres_tuneis(self):
        tuneis = [
            (1, 2, 2),
            (1, 0, 3),
            (0, 3, 5),
            
        ]
        queries = [
            (1, 2),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 8)

    def test_sample_tuneis(self):
        tuneis = [
            (1, 0, 1000000000),
            (2, 1, 1000000000),
            (3, 2, 1000000000),
            (4, 3, 1000000000),
            (5, 4, 1000000000),            
        ]   
        queries = [
            (5, 0),
        ]
        self.assertEqual(
            colonia_de_formigas(tuneis, queries), 5000000000)


if __name__ == "__main__":
    unittest.main()