from typing import Set, Tuple


def find_smallest_set_of_vertices(n: int, edges: Set[Tuple[int, int]]) -> Set[int]:
    """Find smallest set of vertices to reach all vertices given a directed acyclic graph.

    Args:
        n (int): The number of vertices in the graph.
        edges (Set[Tuple[int, int]]): The set of edges contained in the graph.

    Returns:
        Set[int]: The set of vertices that have paths to all vertices in the directed acyclic graph.
    """
    # find all vertices without an incoming edge as they HAVE to be part of the solution
    vertices = set()
    for _, dest in edges:
        if dest not in vertices:
            vertices.add(dest)

    unvisited_vertices = set(i for i in range(0, n)) - vertices
    return unvisited_vertices
