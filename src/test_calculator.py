import unittest
import random
import datetime
from src.simple_calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.randint(-1000, 1000))

    @classmethod
    def setUpClass(cls):
        print("Start:", datetime.datetime.today().strftime("%H:%M:%S.%f"))

    @classmethod
    def tearDownClass(cls):
        print("Stop: ", datetime.datetime.today().strftime("%H:%M:%S.%f"))

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_multiply(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_subtract(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.subtract(100, 5).value, calc_value - 105)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(4, 2).value, (calc_value ** 4) ** 2)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2, 8).value, ((calc_value ** (1/2)) ** (1/8)))

    def test_kek1(self):
        calc_value = self.calculator.value
        self.assertNotEqual(self.calculator.root(25).divide(3.14, 16).add(1, 41, 4).multiply(2.999999).value,
                            calc_value ** (1/2))

    def test_kek2(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2).divide(3.14, 15).add(1, 41, 4).multiply(2.71828).value,
                         ((calc_value ** (1/2)) / 3.14 / 15 + (1 + 41 + 4)) * 2.71828)

    def test_kek3(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(99).subtract(1234.9876).root(985).multiply(33).value,
                         (((calc_value ** 99) - 1234.9876) ** (1 / 985)) * 33)

    def test_kek4(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(11, 3, 5, 1).add(123.3456789, 9999.99999).power(2)
                               .root(123).value,
                               round(((calc_value * 11 * 3 * 5 * 1 + 123.3456789 + 9999.99999) ** 2) ** (1 / 123), 7))

    def test_kek5(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.multiply(11, 3, 5, 1).add(123.3456789, 9999.99999).power(2)
                               .root(123, 11).power(2, 2, 1).value,
                               round(((((((calc_value * 11 * 3 * 5 * 1 + 123.3456789 + 9999.99999) ** 2)
                                         ** (1 / 123)) ** (1 / 11)) ** 2) ** 2) ** 1, 7))

    def test_magic_1(self):
        # calc_value = self.calculator.value
        self.assertEqual(3 ** 3, Calculator(3) ** 3)


if __name__ == '__main__':
    unittest.main()
