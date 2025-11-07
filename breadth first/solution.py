from edgegraph import GraphEL, VertexEL


def bfs(graph, start) -> list:
    try:
        validParams(graph, start)
    except ValueError:
        raise

    vertexCount = graph.num_vertices()

    try:
        lot, explored = set_up_start(graph, start)
    except KeyError:
        return []

    lot_index = 0
    while len(explored) != vertexCount:
        tempLot = []
        for last_lot in lot[lot_index]:
            for edge in graph.incident(graph.find_vertex(last_lot)):
                get_unexplored_vertex(edge, explored, tempLot)

        if len(tempLot) == 0:
            break
        lot.append(tuple(tempLot))
        lot_index += 1

    return lot


def get_unexplored_vertex(edge, explored, tempLot):
    for v in edge.ends():
        if v not in explored:
            explored.append(v)
            tempLot.append(v)


def set_up_start(graph, start):
    start_vertex = graph.find_vertex(start)
    return [(start_vertex,)], [start_vertex]


def validParams(graph, start):
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")
