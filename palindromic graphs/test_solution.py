from collections import Counter
import unittest
from solution import pld_graph
from edgegraph import EdgeEL, GraphEL, VertexEL


class TestNQueensFunction(unittest.TestCase):

    def test_null_graph(self):
        with self.assertRaises(ValueError) as context:
            pld_graph(None)
        self.assertEqual(str(context.exception), "Bad Graph")

    def test_empty_graph(self):
        ge = GraphEL()
        self.assertEqual(pld_graph(ge), [])

    def test_no_repeat_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge1.set_value(1)
        edge2 = EdgeEL(2, ve2, ve3)
        edge2.set_value(2)
        edge3 = EdgeEL(3, ve3, ve4)
        edge3.set_value(3)
        edge4 = EdgeEL(4, ve4, ve5)
        edge4.set_value(4)
        edge5 = EdgeEL(5, ve5, ve6)
        edge5.set_value(5)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        d = pld_graph(ge)
        self.assertEquals(d, [])

    def test_sample_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge1.set_value(1)
        edge2 = EdgeEL(2, ve2, ve3)
        edge2.set_value(0)
        edge3 = EdgeEL(3, ve3, ve4)
        edge3.set_value(1)
        edge4 = EdgeEL(4, ve4, ve5)
        edge4.set_value(0)
        edge5 = EdgeEL(5, ve5, ve6)
        edge5.set_value(1)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        d = pld_graph(ge)
        self.assertEquals(d, [1, 0] or [0, 1])


if __name__ == "__main__":
    unittest.main()
