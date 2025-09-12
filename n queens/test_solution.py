import unittest
from solution import nQueens, nQueensAll


class TestNQueensFunction(unittest.TestCase):
    def test_4_nqueens(self):
        self.assertEqual(nQueens(4), [(0, 1), (1, 3), (2, 0), (3, 2)])

    def test_less_than_4_nqueens(self):
        print("Running less than 4 queens test...")
        with self.assertRaises(ValueError) as err:
            nQueens(3)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueens(0)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueens(-4)
        self.assertIn("Input must be 4 or greater.", str(err.exception))

    def test_less_than_4_nQueensAll(self):
        print("Running less than 4 queens test...")
        with self.assertRaises(ValueError) as err:
            nQueensAll(3)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueensAll(0)
        self.assertIn("Input must be 4 or greater.", str(err.exception))
        with self.assertRaises(ValueError) as err:
            nQueensAll(-4)
        self.assertIn("Input must be 4 or greater.", str(err.exception))

    def test_4_nQueensAll(self):
        self.assertEqual(
            nQueensAll(4),
            [[(0, 1), (1, 3), (2, 0), (3, 2)], [(0, 2), (1, 0), (2, 3), (3, 1)]],
        )

    def test_8_nQueensAll(self):
        self.assertEqual(len(nQueensAll(8)), 92)

    def test_10_nQueensAll(self):
        self.assertEqual(len(nQueensAll(10)), 724)

    # def test_8_queens(self):
    #     self.assertEqual(add(0, 7), 7)


if __name__ == "__main__":
    unittest.main()
