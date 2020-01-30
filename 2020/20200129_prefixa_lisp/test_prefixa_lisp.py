import unittest

from prefixa_lisp import prefixa_lisp


class PrefixaLispUmaExpreTestCase(unittest.TestCase):
    def test_uma_expressao_soma(self):
        expr = "(+ 1 2)"
        self.assertEqual(prefixa_lisp(expr), 3)

    def test_uma_expressao_soma_float(self):
        expr = "(+ 1.6 2)"
        self.assertEqual(prefixa_lisp(expr), 3.6)

    def test_uma_expressao_soma_2(self):
        expr = "(+ 2 2)"
        self.assertEqual(prefixa_lisp(expr), 4)

    def test_uma_expressao_soma_3(self):
        expr = "(+ 2 3)"
        self.assertEqual(prefixa_lisp(expr), 5)

    def test_uma_expressao_sub_1(self):
        expr = "(- 3 2)"
        self.assertEqual(prefixa_lisp(expr), 1)

    def test_uma_expressao_sub_1(self):
        expr = "(- 3 2)"
        self.assertEqual(prefixa_lisp(expr), 1)

    def test_uma_expressao_sub_1_float(self):
        expr = "(- 3.6 2)"
        self.assertEqual(prefixa_lisp(expr), 1.6)

    def test_uma_expressao_div(self):
        expr = "(/ 3 3)"
        self.assertEqual(prefixa_lisp(expr), 1)

    def test_uma_expressao_div_float(self):
        expr = "(/ 3.0 2)"
        self.assertEqual(prefixa_lisp(expr), 1.5)

    def test_uma_expressao_mult(self):
        expr = "(* 3 3)"
        self.assertEqual(prefixa_lisp(expr), 9)

    def test_uma_expressao_mult_float(self):
        expr = "(* 3.3 3.0)"
        self.assertEqual(prefixa_lisp(expr), 9.899999999999999)


class PrefixaLispDuasExpreTestCase(unittest.TestCase):
    def test_soma_de_somas(self):
        expr = "(+ (+ 2 3) 4)"
        self.assertEqual(prefixa_lisp(expr), 9)

#class PrefixaLispTresExpreTestCase(unittest.TestCase):
    #def test_soma_de_somas(self):
    #    expr = "(+ (+ 2 3) (+ 2 3))"
    #    self.assertEqual(prefixa_lisp(expr), 10)



if __name__ == '__main__':
    unittest.main()
