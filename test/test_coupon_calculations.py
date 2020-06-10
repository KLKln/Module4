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
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 5, 15), 9.16, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 15, 25), 9.16, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 20, 20), 9.16, places=4)
        self.assertAlmostEqual(cc.calculate_price(value_10_to_30, 25, 10), 9.16, places=4)


if __name__ == '__main__':
    unittest.main()
