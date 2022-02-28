

class Graph:

    def __init__(self) -> None:
        self._nodes = set()
        self._edges = set()

    def add_edge(self, node_a, node_b) -> None:
        nodes = tuple(sorted((node_a, node_b), key=lambda n: id(n)))
        self._edges.add(nodes)