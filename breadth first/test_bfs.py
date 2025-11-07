import unittest
from edgegraph import EdgeEL, GraphEL, VertexEL
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
        self.assertEqual(d, [(ve,)])

    def test_Two_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ge = GraphEL()
        ge.add_vertex(ve1)
        ge.add_vertex(ve2)
        edge1 = EdgeEL(1, ve1, ve2)
        ge.add_edge(edge1)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 2)
        self.assertEqual(d, [(ve1,), (ve2,)])

    def test_3x2_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve1, ve3)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 2)
        self.assertEqual(d, [(ve1,), (ve2, ve3)])

    def test_3x3_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve2, ve3)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 3)
        self.assertEqual(d, [(ve1,), (ve2,), (ve3,)])

    def test_9x3_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")
        ve7 = VertexEL("test7")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve2, ve3)
        edge3 = EdgeEL(3, ve1, ve4)
        edge4 = EdgeEL(4, ve4, ve5)
        edge5 = EdgeEL(5, ve1, ve6)
        edge6 = EdgeEL(6, ve6, ve7)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        ge.add_edge(edge6)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 3)
        self.assertEqual(d, [(ve1,), (ve2, ve4, ve6), (ve3, ve5, ve7)])

    def test_complex_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")
        ve7 = VertexEL("test7")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve2, ve3)
        edge3 = EdgeEL(3, ve1, ve4)
        edge4 = EdgeEL(4, ve4, ve5)
        edge5 = EdgeEL(5, ve1, ve6)
        edge6 = EdgeEL(6, ve6, ve7)
        edge7 = EdgeEL(7, ve1, ve3)
        edge8 = EdgeEL(8, ve1, ve5)
        edge9 = EdgeEL(9, ve1, ve7)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        ge.add_edge(edge6)
        ge.add_edge(edge7)
        ge.add_edge(edge8)
        ge.add_edge(edge9)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 2)
        self.assertEqual(d, [(ve1,), (ve2, ve4, ve6, ve3, ve5, ve7)])

    def test_big_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")
        ve7 = VertexEL("test7")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve2, ve3)
        edge3 = EdgeEL(3, ve1, ve4)
        edge4 = EdgeEL(4, ve4, ve5)
        edge5 = EdgeEL(5, ve1, ve6)
        edge6 = EdgeEL(6, ve6, ve7)
        edge7 = EdgeEL(7, ve1, ve3)
        edge8 = EdgeEL(8, ve1, ve5)
        edge9 = EdgeEL(9, ve1, ve7)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        ge.add_edge(edge6)
        ge.add_edge(edge7)
        ge.add_edge(edge8)
        ge.add_edge(edge9)
        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 2)
        self.assertEqual(d, [(ve1,), (ve2, ve4, ve6, ve3, ve5, ve7)])

    def test_simple_chain(self):
        ve1 = VertexEL("v1")
        ve2 = VertexEL("v2")
        ve3 = VertexEL("v3")

        ge = GraphEL()
        edge1 = EdgeEL("e1", ve1, ve2)
        edge2 = EdgeEL("e2", ve2, ve3)

        ge.add_edge(edge1)
        ge.add_edge(edge2)

        d = bfs(ge, ve1)
        self.assertEqual(d, [(ve1,), (ve2,), (ve3,)])

    def test_branching_graph(self):
        ve1 = VertexEL("v1")
        ve2 = VertexEL("v2")
        ve3 = VertexEL("v3")
        ve4 = VertexEL("v4")
        ve5 = VertexEL("v5")

        ge = GraphEL()
        e1 = EdgeEL("e1", ve1, ve2)
        e2 = EdgeEL("e2", ve1, ve3)
        e3 = EdgeEL("e3", ve2, ve4)
        e4 = EdgeEL("e4", ve3, ve5)

        ge.add_edge(e1)
        ge.add_edge(e2)
        ge.add_edge(e3)
        ge.add_edge(e4)

        d = bfs(ge, ve1)
        self.assertEqual(d, [(ve1,), (ve2, ve3), (ve4, ve5)])

    def test_big_Vertex_graph(self):
        ve1 = VertexEL("test1")
        ve2 = VertexEL("test2")
        ve3 = VertexEL("test3")
        ve4 = VertexEL("test4")
        ve5 = VertexEL("test5")
        ve6 = VertexEL("test6")
        ve7 = VertexEL("test7")

        ge = GraphEL()
        edge1 = EdgeEL(1, ve1, ve2)
        edge2 = EdgeEL(2, ve2, ve3)
        edge3 = EdgeEL(3, ve1, ve4)
        edge4 = EdgeEL(4, ve4, ve5)
        edge5 = EdgeEL(5, ve1, ve6)
        edge6 = EdgeEL(6, ve6, ve7)
        edge7 = EdgeEL(7, ve1, ve3)
        edge8 = EdgeEL(8, ve1, ve5)
        edge9 = EdgeEL(9, ve1, ve7)

        ge.add_edge(edge1)
        ge.add_edge(edge2)
        ge.add_edge(edge3)
        ge.add_edge(edge4)
        ge.add_edge(edge5)
        ge.add_edge(edge6)
        ge.add_edge(edge7)
        ge.add_edge(edge8)
        ge.add_edge(edge9)

        d = bfs(ge, ve1)
        self.assertTrue(len(d) == 2)
        self.assertEqual(d, [(ve1,), (ve2, ve4, ve6, ve3, ve5, ve7)])

    def test_disconnected_graph(self):
        ve1 = VertexEL("v1")
        ve2 = VertexEL("v2")
        ve3 = VertexEL("v3")

        ge = GraphEL()
        edge1 = EdgeEL("e1", ve1, ve2)
        ge.add_edge(edge1)
        ge.add_vertex(ve3)  # disconnected vertex

        d = bfs(ge, ve1)
        self.assertEqual(d, [(ve1,), (ve2,)])

    def test_single_vertex(self):
        ve1 = VertexEL("only")
        ge = GraphEL()
        ge.add_vertex(ve1)

        d = bfs(ge, ve1)
        self.assertEqual(d, [(ve1,)])

    def test_cyclic_graph(self):
        ve1 = VertexEL("A")
        ve2 = VertexEL("B")
        ve3 = VertexEL("C")

        ge = GraphEL()
        e1 = EdgeEL("e1", ve1, ve2)
        e2 = EdgeEL("e2", ve2, ve3)
        e3 = EdgeEL("e3", ve3, ve1)

        ge.add_edge(e1)
        ge.add_edge(e2)
        ge.add_edge(e3)

        d = bfs(ge, ve1)
        # Should not loop infinitely
        self.assertEqual(d, [(ve1,), (ve2, ve3)])


if __name__ == "__main__":
    unittest.main()
