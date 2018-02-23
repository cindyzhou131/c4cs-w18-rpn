import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate("1 1 -")
        self.assertEqual(0, result)
    def test_mult(self):
        result = rpn.calculate("1 1 *")
        self.assertEqual(1, result)
    def test_div(self):
        result = rpn.calculate("1 1 /")
        self.assertEqual(1, result)
    def test_exp(self):
        result = rpn.calculate("1 1 ^")
        self.assertEqual(1, result)
    def test_sin(self):
        result = rpn.calculate("0 sin")
        self.assertEqual(0, result)
    def test_cos(self):
        result = rpn.calculate("0 cos")
        self.assertEqual(1, result)
    def test_exp(self):
        result = rpn.calculate("1 1 ^")
        self.assertEqual(1, result)
    def test_summation(self):
        result = rpn.calculate("1 1 1 1 1 4 sum_all")
        self.assertEqual(9, result)
