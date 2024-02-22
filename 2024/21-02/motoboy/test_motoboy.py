# https://judge.beecrowd.com/pt/problems/view/1286
import unittest
from unittest import TestCase
from motoboy import motoboy
#from solucao_dp import motoboy

class MotoboyTestCase(TestCase):
	maxDiff = None

	def test_1(self):
		n_pedidos = 6
		n_max_pizzas_podem_ser_entregues_por_roberto = 10
		pedidos = [
			(15, 5),
			(23, 4),
			(21, 2),
			(16, 4),
			(19, 5),
			(18, 2)
		]
		self.assertEqual(
			motoboy(
				n_pedidos,
				n_max_pizzas_podem_ser_entregues_por_roberto,
				pedidos
			), 
			62
		)
	def test_2(self):
		n_pedidos = 2
		n_max_pizzas_podem_ser_entregues_por_roberto = 15
		pedidos = [
			(47, 12),
			(39, 4)
		]

		self.assertEqual(
			motoboy(
				n_pedidos,
				n_max_pizzas_podem_ser_entregues_por_roberto,
				pedidos
			), 
			47
			)

	def test_3(self):
		n_pedidos = 5
		n_max_pizzas_podem_ser_entregues_por_roberto = 23
		pedidos = [
			(43, 9),
			(4, 1),
			(17, 2),
			(13, 5),
			(54, 17)
		]

		self.assertEqual(
			motoboy(
				n_pedidos,
				n_max_pizzas_podem_ser_entregues_por_roberto,
				pedidos
			), 
			77
		)
	def test_4(self):
		n_pedidos = 6
		n_max_pizzas_podem_ser_entregues_por_roberto = 7
		pedidos = [
			(14,4),
			(21,2),
			(26,7),
			(18,4),
			(30,13),
			(10,2)
		]
		self.assertEqual(
			motoboy(
				n_pedidos,
				n_max_pizzas_podem_ser_entregues_por_roberto,
				pedidos
			), 
			39
		)



if __name__ == '__main__':
	unittest.main()
