
from __future__ import annotations
# gamut
from gamut.graph import Graph
# pytest
import pytest


def test_defaults() -> None:
    g = Graph()
    assert list(g.nodes) == []
    assert list(g.edges) == []


def test_add_unhashable_node() -> None:
    g = Graph()
    with pytest.raises(TypeError):
        g.add_node([1])


def test_node() -> None:
    g = Graph()

    g.add_node(None)
    assert list(g.nodes) == [None]
    assert list(g.edges) == []
    assert list(g.get_node_edges(None)) == []

    g.add_node(None)
    assert list(g.nodes) == [None]
    assert list(g.edges) == []
    assert list(g.get_node_edges(None)) == []

    g.add_node(1)
    assert set(g.nodes) == {None, 1}
    assert list(g.edges) == []
    assert list(g.get_node_edges(None)) == []
    assert list(g.get_node_edges(1)) == []

    g.remove_node(None)
    assert set(g.nodes) == {1}
    assert list(g.edges) == []
    assert list(g.get_node_edges(None)) == []
    assert list(g.get_node_edges(1)) == []


def test_edge() -> None:
    g = Graph()

    g.add_edge(1, 2, .5)
    assert set(g.nodes) == {1, 2}
    assert set(g.edges) == {(1, 2, .5)}
    assert list(g.get_node_edges(1)) == [(2, .5)]
    assert list(g.get_node_edges(2)) == [(1, .5)]

    g.add_edge(1, 2, .8)
    assert set(g.nodes) == {1, 2}
    assert set(g.edges) == {(1, 2, .8)}
    assert list(g.get_node_edges(1)) == [(2, .8)]
    assert list(g.get_node_edges(2)) == [(1, .8)]

    g.add_edge(1, 3, .2)
    assert set(g.nodes) == {1, 2, 3}
    assert set(g.edges) == {(1, 2, .8), (1, 3, .2)}
    assert list(g.get_node_edges(1)) == [(2, .8), (3, .2)]
    assert list(g.get_node_edges(2)) == [(1, .8)]
    assert list(g.get_node_edges(3)) == [(1, .2)]

    g.remove_node(2)
    assert set(g.nodes) == {1, 3}
    assert set(g.edges) == {(1, 3, .2)}
    assert list(g.get_node_edges(1)) == [(3, .2)]
    assert list(g.get_node_edges(2)) == []
    assert list(g.get_node_edges(3)) == [(1, .2)]

    g.remove_edge(3, 1)
    assert set(g.nodes) == {1, 3}
    assert list(g.edges) == []
    assert list(g.get_node_edges(1)) == []
    assert list(g.get_node_edges(2)) == []
    assert list(g.get_node_edges(3)) == []


def test_get_node_edges_does_not_exist() -> None:
    g = Graph()
    assert list(g.get_node_edges(0)) == []
