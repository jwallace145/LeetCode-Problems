from dataclasses import dataclass, field
from typing import List, Dict, Set
from collections import deque


@dataclass
class Graph:

    file: str
    _adjacency_list: Dict[int, List[int]] = field(default_factory=lambda: {})
    _visited_nodes: Set[int] = field(default_factory=lambda: set())

    def __post_init__(self) -> None:
        self._init_adjacency_list()

    def _init_adjacency_list(self) -> None:
        for line in open(self.file, "r").readlines():
            src_vertex, dest_vertices = line.strip().split(":")
            src_vertex = int(src_vertex)
            dest_vertices = dest_vertices.split(",")
            dest_vertices = [int(vertex) for vertex in dest_vertices if vertex != ""]
            self._adjacency_list[src_vertex] = dest_vertices

    def depth_first_search(self, root: int) -> None:
        self._visited_nodes.clear()
        self._dfs(root)

    def _dfs(self, root: int) -> None:
        print(f"vertex: {root}")
        self._visited_nodes.add(root)
        for adjacent_vertex in self._adjacency_list[root]:
            if adjacent_vertex not in self._visited_nodes:
                self.depth_first_search(adjacent_vertex)

    def breadth_first_search(self, root: int):
        self._visited_nodes.clear()
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            vertex = queue.popleft()
            for adjacent_vertex in self._adjacency_list[vertex]:
                if adjacent_vertex not in self._visited_nodes:
                    print(f"vertex: {adjacent_vertex}")
                    self._visited_nodes.add(adjacent_vertex)
                    queue.append(adjacent_vertex)


graph = Graph(file="graph.txt")
graph.depth_first_search(root=0)
graph.breadth_first_search(root=0)
