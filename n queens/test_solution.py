import unittest
from solution import nQueensAll

class TestNQueensFunction(unittest.TestCase):

    def test_n_queens_all(self):
        print("Running nQueensAll test: ", end="")
        self.assertTrue(nQueensAll())
        if(self.assertTrue(nQueensAll()) == None):
            print("Passed")
            
    # def test_4_queens(self):
    #     self.assertEqual(solution.nQueensAll())
    #     self.assertEqual(add(2, 3), 5)

    # def test_less_than_4_queens(self):
    #     self.assertEqual(add(-1, -5), -6)

    # def test_8_queens(self):
    #     self.assertEqual(add(0, 7), 7)

if __name__ == '__main__':
    unittest.main()