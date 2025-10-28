import unittest
from edgegraph import GraphEL, VertexEL
from solution import bfs


class Test_bfs(unittest.TestCase):
    def test_None_params(self):
        ve = VertexEL("test")
        ge = GraphEL()
        with self.assertRaises(ValueError) as context:
            bfs(None, ve)
        self.assertEqual(str(context.exception), "Invalid graph or vertex")
        with self.assertRaises(ValueError) as context:
            d = bfs(ge, None)
        self.assertEqual(str(context.exception), "Invalid graph or vertex")

    def test_Start_Not_in_Graph(self):
        ve = VertexEL("test")
        ge = GraphEL()
        d = bfs(ge, ve)
        self.assertEqual(d, [])

    def test_Single_Vertex_graph(self):
        ve = VertexEL("test")
        ge = GraphEL()
        ge.add_vertex(ve)
        d = bfs(ge, ve)
        self.assertTrue(len(d) == 1)
        self.assertEqual(d, [ve])


if __name__ == "__main__":
    unittest.main()
