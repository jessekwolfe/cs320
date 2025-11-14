import unittest
from solution import nQueens, nQueensAll


class TestPLDGraph(unittest.TestCase):
    def test_pld(self):
        GraphEL test = new GraphEL();
        self.assertPass(pld_graph(), [(0, 1), (1, 3), (2, 0), (3, 2)])


if __name__ == "__main__":
    unittest.main()
