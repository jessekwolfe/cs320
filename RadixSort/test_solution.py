import unittest
from solution import radix_base


class TestNQueensFunction(unittest.TestCase):
    def test_bases(self):
        self.assertEqual(radix_base([], 2), 1)


if __name__ == "__main__":
    unittest.main()
