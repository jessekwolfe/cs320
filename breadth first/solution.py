from edgegraph import GraphEL, VertexEL


def bfs(graph, start) -> list:
    try:
        validParams(graph, start)
    except ValueError:
        raise

    lot = []
    try:
        lot.append(graph.find_vertex(start))
    except KeyError:
        return lot

    return lot


def validParams(graph, start):
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")


# Algorithm BFS(G,s)
#     Input:    An undirected graph and a vertex of Output: A labeling of edges in the connected compontent of as tree edges and cross edges

#     Create an empty list, L0
#     Mark as explored and insert s into L0
#     while Li is not empty do
#         Create an empty list, Li+1
#         for each vertex, u, in Li do
#             for each edge, e=(u,v), incident to v in G do
#                 if vertex v is unexplored then
#                     Label {e} as a tree edge for discovering vertex v
#                     Mark as explored and insert {v} into {L(i+1)}
#                 else
#                     Label {e} as a cross or back edge
