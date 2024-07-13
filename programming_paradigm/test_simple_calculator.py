import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
     calc = SimpleCalculator()
     self.assertEqual(calc.add(2, 3), 5)
     self.assertEqual(calc.add(-1, 1), 0)
     self.assertEqual(calc.add(-1, -1), -2)
    def test_subtract(self):
     calc = SimpleCalculator()
     self.assertEqual(calc.subtract(10, 5), 5)
     self.assertEqual(calc.subtract(-1, 1), -2)
     self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self):
     calc = SimpleCalculator()
     self.assertEqual(calc.multiply(3, 7), 21)
     self.assertEqual(calc.multiply(-1, 1), -1)
     self.assertEqual(calc.multiply(-1, -1), 1)
    def test_divide(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.divide(10, 2), 5)
    self.assertEqual(calc.divide(-1, 1), -1)
    self.assertEqual(calc.divide(-1, -1), 1)
    with self.assertRaises(ValueError):
        calc.divide(10, 0)