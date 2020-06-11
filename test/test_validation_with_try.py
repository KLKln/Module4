import unittest

from input_validation.input_validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
