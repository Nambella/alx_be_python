import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
 
    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(-1, 1), -2)
        self.assertEqual(self.calc.subtraction(-1, -1), 0)

    def test_multiplication(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.multiplication(3, 7), 21)
        self.assertEqual(self.calc.multiplication(-1, 1), -1)
        self.assertEqual(self.calc.multiplication(-1, -1), 1)

    def test_division(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-1, 1), -1)
        self.assertEqual(self.calc.division(-1, -1), 1)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)