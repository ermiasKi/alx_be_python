import unittest
from simple_calculator import SimpleCalculator

class test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(0,0),0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,4),1)
        self.assertEqual(self.calc.subtract(3,7),-4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,4),20)
        self.assertEqual(self.calc.multiply(0,4),0)
    def test_division(self):
        self.assertEqual(self.calc.devide(20,4),5)
        self.assertEqual(self.calc.devide(5,0),ZeroDivisionError)
