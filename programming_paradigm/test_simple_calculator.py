import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.sub(3, 2), 1)
        self.assertEqual(self.calc.sub(1,1), 0)
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.div(4, 2), 2)
        self.assertEqual(self.calc.div(4, 1), 1)
    def test_multiplication(self):
        self.assertEqual(self.calc.mult(2, 2), 4)
        self.assertEqual(self.calc.mult(2, 1), 2)    
