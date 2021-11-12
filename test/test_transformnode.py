
# gamut
from gamut import TransformNode
# pyglm
from glm import mat4


def test_defaults() -> None:
    node = TransformNode()
    assert node.local_transform == mat4(1)
    assert node.transform == mat4(1)
    assert node.parent is None
