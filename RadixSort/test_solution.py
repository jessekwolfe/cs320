import unittest
from solution import radix_base


class TestNQueensFunction(unittest.TestCase):
    def test_temp_bases(self):
        self.assertEqual(radix_base([1, 2], 2), 1)

    def test_empty_array_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([], 2)

    def test_none_array_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base(None, 2)

    def test_base_too_low_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2], 1)

    def test_base_none_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2], None)

    def test_nonManthmatical_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, "hello", 3], 2)


if __name__ == "__main__":
    unittest.main()
