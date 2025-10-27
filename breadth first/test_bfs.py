import unittest
from edgegraph import GraphEL, VertexEL
from solution import bfs


class Test_bfs(unittest.TestCase):
    def test_bfs(self):
        ve = VertexEL("test")
        ge = GraphEL()
        d = bfs(ge, ve)
        self.assertIsNone(d)


if __name__ == "__main__":
    unittest.main()
