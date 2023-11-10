import unittest
from number_in_interval import number_in_interval


class TestEvenOdd(unittest.TestCase):

    def test_number_in_interval(self):
        self.assertFalse(number_in_interval(0))
        self.assertIsNotNone(number_in_interval(-90))
        self.assertEqual(number_in_interval(10), False)

        with self.assertRaises(ValueError):
            number_in_interval('is not number')


if __name__ == '__main__':
    unittest.main()
