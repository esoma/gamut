
# gamut
from gamut import TransformNode
from gamut.math import FMatrix4, FVector3
# python
from typing import Any, Optional
# pytest
import pytest


def test_defaults() -> None:
    node: TransformNode[Any] = TransformNode()
    assert node.local_transform == FMatrix4(1)
    assert node.transform == FMatrix4(1)
    assert node.parent is None
    assert node.children == set()


@pytest.mark.parametrize("translation_x", [-8, 0, 7])
@pytest.mark.parametrize("translation_y", [-8, 0, 7])
@pytest.mark.parametrize("translation_z", [-8, 0, 7])
def test_transform_no_parent(
    translation_x: int,
    translation_y: int,
    translation_z: int,
) -> None:
    local_transform = FMatrix4(1).translate(
        FVector3(translation_x, translation_y, translation_z)
    )
    node: TransformNode[Any] = TransformNode(local_transform=local_transform)
    assert node.local_transform == local_transform
    assert node.transform == local_transform


@pytest.mark.parametrize("translation_x", [-8, 0, 7])
@pytest.mark.parametrize("translation_y", [-8, 0, 7])
@pytest.mark.parametrize("translation_z", [-8, 0, 7])
def test_transform_parent(
    translation_x: int,
    translation_y: int,
    translation_z: int,
) -> None:
    local_transform = FMatrix4(1).translate(
        FVector3(translation_x, translation_y, translation_z)
    )

    parent: TransformNode[Any] = TransformNode(local_transform=local_transform)
    node = TransformNode(local_transform=local_transform, parent=parent)
    assert node.local_transform == local_transform
    assert node.transform == local_transform @ local_transform


def test_add_parent() -> None:
    node_local_transform = FMatrix4(1).translate(FVector3(1))
    node: TransformNode[Any] = TransformNode(
        local_transform=node_local_transform
    )
    assert node.local_transform == node_local_transform
    assert node.transform == node_local_transform

    parent_local_transform = FMatrix4(1).translate(FVector3(-2))
    parent: TransformNode[Any] = TransformNode(
        local_transform=parent_local_transform
    )
    node.parent = parent
    assert node.local_transform == node_local_transform
    assert node.transform == parent_local_transform @ node_local_transform
    assert parent.children == {node}


def test_remove_parent() -> None:
    parent_local_transform = FMatrix4(1).translate(FVector3(-2))
    parent: TransformNode[Any] = TransformNode(
        local_transform=parent_local_transform
    )

    node_local_transform = FMatrix4(1).translate(FVector3(1, 1, 1))
    node = TransformNode(local_transform=node_local_transform, parent=parent)
    assert node.local_transform == node_local_transform
    assert node.transform == parent_local_transform @ node_local_transform

    node.parent = None
    assert node.local_transform == node_local_transform
    assert node.transform == node_local_transform
    assert parent.children == set()


def test_change_parent_local_transform() -> None:
    parent: TransformNode[Any] = TransformNode()
    node = TransformNode(parent=parent)

    assert parent.transform == FMatrix4(1)
    assert node.transform == FMatrix4(1)

    parent.local_transform = FMatrix4(1).translate(FVector3(-2, 1, 99))
    assert parent.transform == parent.local_transform
    assert node.transform == parent.local_transform


@pytest.mark.parametrize("depth", [1, 2, 4, 10])
def test_cycle(depth: int) -> None:
    nodes: list[TransformNode] = []
    for _ in range(depth):
        parent_node: Optional[TransformNode] = None
        try:
            parent_node = nodes[-1]
        except IndexError:
            pass
        node = TransformNode(parent=parent_node)
        nodes.append(node)

    with pytest.raises(ValueError) as excinfo:
        nodes[0].parent = nodes[-1]
    assert str(excinfo.value) == 'transform parent/child relationship cycle'


def test_descend() -> None:
    root: TransformNode[Any] = TransformNode()
    depth_1_a = TransformNode(parent=root)
    depth_1_b = TransformNode(parent=root)
    depth_2_a_a = TransformNode(parent=depth_1_a)
    depth_2_a_b = TransformNode(parent=depth_1_a)
    depth_2_b_a = TransformNode(parent=depth_1_b)
    depth_2_b_b = TransformNode(parent=depth_1_b)

    order: list[TransformNode[Any]] = []
    root.descend(lambda n: order.append(n))

    assert order[0] is root
    assert (
        (order[1] is depth_1_a and order[2] is depth_1_b) or
        (order[1] is depth_1_b and order[2] is depth_1_a)
    )
    if order[1] is depth_1_a:
        assert (
            (order[3] is depth_2_a_a and order[4] is depth_2_a_b) or
            (order[3] is depth_2_a_b and order[4] is depth_2_a_a)
        )
        assert (
            (order[5] is depth_2_b_a and order[6] is depth_2_b_b) or
            (order[5] is depth_2_b_b and order[6] is depth_2_b_a)
        )
    else:
        assert (
            (order[3] is depth_2_b_a and order[4] is depth_2_b_b) or
            (order[3] is depth_2_b_b and order[4] is depth_2_b_a)
        )
        assert (
            (order[5] is depth_2_a_a and order[6] is depth_2_a_b) or
            (order[5] is depth_2_a_b and order[6] is depth_2_a_a)
        )
