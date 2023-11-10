import unittest

from even_odd import even_odd_number


class TestEvenOdd(unittest.TestCase):

    def test_even_odd(self):
        self.assertTrue(even_odd_number(2))
        self.assertFalse(even_odd_number(-7))
        self.assertTrue(even_odd_number(-8))
        self.assertTrue(even_odd_number(8.0))

        with self.assertRaises(ValueError):
            even_odd_number('6')


if __name__ == '__main__':
    unittest.main()
