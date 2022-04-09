
from __future__ import annotations

__all__ = ['Graph', 'WeightProtocol']

# python
# DVector4
from copy import copy
from typing import Generator, Generic, Hashable, Protocol, TypeVar


class WeightProtocol(Protocol):
    def __lt__(self: W, other: W) -> bool:
        ...


M = TypeVar('M')
T = TypeVar('T', bound=Hashable)
W = TypeVar('W', bound=WeightProtocol)


class Graph(Generic[T, W]):

    def __init__(self) -> None:
        self._nodes: dict[T, Node[T, W]] = {}
        self._edges: dict[tuple[T, T], W] = {}

    def __copy__(self) -> Graph:
        g = Graph()
        g._nodes = {v: copy(n) for v, n in self._nodes.items()}
        g._edges = copy(self._edges)
        return g

    def _get_edge_key(self, a: T, b: T) -> tuple(T, T):
        if hash(a) < hash(b):
            return a, b
        else:
            return b, a

    def _add_node(self, value: T) -> Node[T, W]:
        try:
            return self._nodes[value]
        except KeyError:
            pass
        node = self._nodes[value] = Node(value)
        return node

    def _remove_edge(self, a: T, b: T) -> None:
        key = self._get_edge_key(a, b)
        try:
            del self._edges[key]
        except KeyError:
            return
        del self._nodes[a].edges[b]
        del self._nodes[b].edges[a]

    @property
    def nodes(self) -> Generator[T, None, None]:
        yield from self._nodes.keys()

    def add_node(self, value: T) -> None:
        self._add_node(value)

    def contains_node(self, value: T) -> bool:
        return value in self._nodes

    def remove_node(self, value: T) -> None:
        try:
            node = self._nodes[value]
        except KeyError:
            return
        for other_node_value in list(node.edges.keys()):
            self._remove_edge(value, other_node_value)
        del self._nodes[value]

    @property
    def edges(self) -> Generator[tuple[T, T, W], None, None]:
        return ((a, b, w) for (a, b), w in self._edges.items())

    def add_edge(self, a: T, b: T, weight: W) -> None:
        key = self._get_edge_key(a, b)
        self._edges[key] = weight

        node_a = self._add_node(a)
        node_a.edges[b] = weight
        node_b = self._add_node(b)
        node_b.edges[a] = weight

    def contains_edge(self, a: T, b: T) -> None:
        key = self._get_edge_key(a, b)
        return key in self._edges

    def remove_edge(self, a: T, b: T) -> None:
        self._remove_edge(a, b)

    def get_node_edges(
        self,
        value: T
    ) -> Generator[tuple[T, W], None, None]:
        try:
            yield from self._nodes[value].edges.items()
        except KeyError:
            pass

    def get_connected_components(self) -> Generator[tuple[T, ...], None, None]:
        islands: dict[T, IdHashSet[T]] = {
            nv: IdHashSet((nv,))
            for nv in self._nodes
        }
        unique_islands: set[IdHashSet[T]] = set(islands.values())
        for node in self._nodes.values():
            island = islands[node.value]
            for edge_value in node.edges:
                other_island = islands[edge_value]
                if island is not other_island:
                    island |= other_island
                    islands[edge_value] = island
                    try:
                        unique_islands.remove(other_island)
                    except KeyError:
                        pass
        yield from (tuple(island) for island in unique_islands)


class Node(Generic[T, W]):

    __slots__ = ['value', 'edges']

    def __init__(self, value: T):
        self.value = value
        self.edges: dict[T, W] = {}

    def __copy__(self) -> Node:
        n = Node(self.value)
        n.edges = copy(self.edges)
        return n


class IdHashSet(set[T]):

    def __hash__(self) -> int:
        return id(self)
