"""
Program: test.py
Author: Kelly Klein
Last date modified: 6/9/2020
This program will test  the program if_elif_statements
"""
import unittest
import unittest.mock as mock
from main import if_elif_statements as t1


class MyTestCase(unittest.TestCase):

#asks user to sgn up for a tier of programmers monthly sub box.
#user mus select level of membership

#Platinum $60
#Gold $50
#Silver $40
#Bronze $30
#free trial $0

#Write an if statment that prints cost for each level

    def test_sign_up_for_platinum(self):
        self.assertEqual(60, t1.return_string_cost_of_box("Platinum"))

    def test_sign_up_for_gold(self):
        self.assertEqual(50, t1.return_string_cost_of_box("Gold"))

    def test_sign_up_for_silver(self):
        self.assertEqual(40, t1.return_string_cost_of_box("Silver"))

    def test_sign_up_for_Bronze(self):
        self.assertEqual(30, t1.return_string_cost_of_box("Bronze"))

    def test_sign_up_for_trial(self):
        self.assertEqual(0, t1.return_string_cost_of_box("Free Trial"))


if __name__ == '__main__':
    unittest.main()
