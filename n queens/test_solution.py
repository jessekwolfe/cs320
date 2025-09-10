import unittest
from solution import nQueensAll

class TestNQueensFunction(unittest.TestCase):
    # def test_4_queens(self):
    #     self.assertEqual(solution.nQueensAll())
    #     self.assertEqual(add(2, 3), 5)

    def test_less_than_4_queens(self):
        print("Running less than 4 queens test: ")
        with self.assertRaises(ValueError) as err:
            nQueensAll(3)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueensAll(0)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueensAll(-4)
        self.assertIn("Input must be 4 or greater.", str(err.exception))

    # def test_8_queens(self):
    #     self.assertEqual(add(0, 7), 7)

if __name__ == '__main__':
    unittest.main()