import unittest
from store import coupon_calculations as cc

"""
Program: test_coupon_calculations.py
Author: Kelly Klein
Last date modified: 6/10/2020
This program will use variables to test a program that takes user input for price, a cash coupon, and a percent coupon
    and output those totals plus tax, shipping and a grand total
"""


class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon):
    def test_price_under_10(self):
        value_under_10 = 7.99
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 5), 2.84, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 10), 2.69, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 15), 2.54, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 10, 5), -1.91, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 10, 10), -1.81, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 10, 15), -1.71, places=2)

    def test_price_10_to_30(self):
        value_10_to_30 = 15.99
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 5), 10.44, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 10), 9.89, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 15), 9.34, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 10, 5), 5.69, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 10, 10), 5.39, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 10, 15), 5.09, places=2)

    def test_price_30_to_50(self):
        value_30_to_50 = 40.99
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 5, 5), 34.19, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 5, 10), 32.39, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 5, 15), 30.59, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 10, 5), 29.44, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 10, 10), 27.89, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_30_to_50, 10, 15), 26.34, places=2)

    def test_price_50_and_over(self):
        value_50_and_over = 75.99
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 5, 5), 67.44, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 5, 10), 63.89, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 5, 15), 60.34, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 10, 5), 62.69, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 10, 10), 59.39, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_50_and_over, 10, 15), 56.09, places=2)



if __name__ == '__main__':
    unittest.main()
