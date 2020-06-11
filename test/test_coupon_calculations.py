import unittest
from store import coupon_calculations as cc


class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon):
    def test_price_under_10(self):
        value_under_10 = 7.99
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 15), 2.54, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 15), 2.54, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 15), 2.54, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_under_10, 5, 15), 2.54, places=6)

    def test_price_10_to_30(self):
        value_10_to_30 = 15.99
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 15), 9.3415, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 15, 25), .7425, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 10, 20), 4.792, places=6)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 10), 9.891, places=6)


if __name__ == '__main__':
    unittest.main()
