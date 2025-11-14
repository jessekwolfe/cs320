from edgegraph import EdgeEL, GraphEL, VertexEL
from collections import Counter


def pld_graph(g: GraphEL) -> list:
    # If param is null error
    if g is None:
        raise ValueError("Bad Graph")

    palindromic = []

    if g.num_edges() < 3:
        return palindromic

    edge_count, multiValues = count_and_unique_multiples(g)

    # If there are no duplicates there are no palendromes.
    if len(multiValues) == 0:
        return palindromic

    return multiValues

    # We can also only start from a duplicate

    # Start with on edge go until you are no longer hitting a duplicate then try to continue following the path in reverse.

    # if palendrom created and it's not added to the list then add to list
    pass


def count_and_unique_multiples(g):
    # Count occurances of each edge name.
    edge_counter = Counter(e.get_value() for e in g.edges())
    # create a list of duplicates for tracking
    unique_multiples = [weight for weight, count in edge_counter.items() if count > 1]

    return edge_counter, unique_multiples
