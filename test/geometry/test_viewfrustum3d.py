
# gamut
from gamut.geometry import Plane, ViewFrustum3d
# python
from typing import Any
# pyglm
from glm import (mat4, perspective, radians, rotate, row, scale, translate,
                 vec2, vec3, vec4)
# pytest
import pytest


def test_repr() -> None:
    planes = [Plane(i, vec3(1, 2, 3)) for i in range(6)]
    frustum = ViewFrustum3d(*planes)
    assert (
        repr(frustum) ==
        f'<gamut.geometry.ViewFrustum3d '
        f'near_plane={planes[0]} '
        f'far_plane={planes[1]} '
        f'left_plane={planes[2]} '
        f'right_plane={planes[3]} '
        f'bottom_plane={planes[4]} '
        f'top_plane={planes[5]}>'
    )


@pytest.mark.parametrize("plane", [None, 'x', object()])
@pytest.mark.parametrize("name", [
    'near_plane', 'far_plane',
    'left_plane', 'right_plane',
    'bottom_plane', 'top_plane',
])
def test_invalid_plane(plane: Any, name: str) -> None:
    kwargs = {
        "near_plane": Plane(0, vec3(0, 1, 0)),
        "far_plane": Plane(0, vec3(0, 1, 0)),
        "left_plane": Plane(0, vec3(0, 1, 0)),
        "right_plane": Plane(0, vec3(0, 1, 0)),
        "bottom_plane": Plane(0, vec3(0, 1, 0)),
        "top_plane": Plane(0, vec3(0, 1, 0)),
    }
    kwargs[name] = plane
    with pytest.raises(TypeError) as excinfo:
        ViewFrustum3d(**kwargs)
    assert str(excinfo.value) == f'{name.replace("_", " ")} must be Plane'


def test_planes() -> None:
    planes = [Plane(i, vec3(1, 2, 3)) for i in range(6)]
    frustum = ViewFrustum3d(*planes)
    assert frustum.near_plane is planes[0]
    assert frustum.planes[0] is planes[0]
    assert frustum.far_plane is planes[1]
    assert frustum.planes[1] is planes[1]
    assert frustum.left_plane is planes[2]
    assert frustum.planes[2] is planes[2]
    assert frustum.right_plane is planes[3]
    assert frustum.planes[3] is planes[3]
    assert frustum.bottom_plane is planes[4]
    assert frustum.planes[4] is planes[4]
    assert frustum.top_plane is planes[5]
    assert frustum.planes[5] is planes[5]
    assert len(frustum.planes) == 6


@pytest.mark.parametrize("transform", [
    translate(mat4(1), vec3(1, 0, 0)),
    translate(mat4(1), vec3(0, 1, 0)),
    translate(mat4(1), vec3(0, 0, 1)),
    rotate(mat4(1), radians(90), vec3(1, 0, 0)),
    rotate(mat4(1), radians(90), vec3(0, 1, 0)),
    rotate(mat4(1), radians(90), vec3(0, 0, 1)),
    scale(mat4(1), vec3(2, 3, 4)),
])
def test_transform(transform: mat4) -> None:
    planes = [Plane(i, vec3(1, 2, 3)) for i in range(6)]
    frustum = ViewFrustum3d(*planes)
    new_frustum = transform * frustum
    assert new_frustum is not frustum

    for original_plane, new_plane in zip(frustum.planes, new_frustum.planes):
        assert original_plane is not new_plane
        assert new_plane == (transform * original_plane)


@pytest.mark.parametrize("transform", [None, 123, vec4(1), vec2(1)])
def test_transform_invalid(transform: Any) -> None:
    planes = [Plane(i, vec3(1, 2, 3)) for i in range(6)]
    frustum = ViewFrustum3d(*planes)
    with pytest.raises(TypeError) as excinfo:
        transform * frustum
    assert str(excinfo.value).startswith('unsupported operand type(s) for *:')


def test_equal() -> None:
    planes = [Plane(i, vec3(1, 2, 3)) for i in range(6)]
    assert ViewFrustum3d(*planes) == ViewFrustum3d(*planes)
    assert ViewFrustum3d(*planes) != ViewFrustum3d(*reversed(planes))
    assert ViewFrustum3d(*planes) != object()


@pytest.mark.parametrize("transform", [
    mat4(1),
    tuple((tuple(c) for c in mat4(1))),
    list((list(c) for c in mat4(1))),
    perspective(radians(45), 1, .1, 10),
])
def test_from_view_projection_transform(transform: mat4) -> None:
    frustum = ViewFrustum3d.from_view_projection_transform(transform)
    rows = [row(mat4(transform), i) for i in range(4)]
    assert frustum.near_plane == Plane(
        rows[3].w + rows[2].w,
        rows[3].xyz + rows[2].xyz
    )
    assert frustum.far_plane == Plane(
        rows[3].w - rows[2].w,
        rows[3].xyz - rows[2].xyz
    )
    assert frustum.left_plane == Plane(
        rows[3].w + rows[0].w,
        rows[3].xyz + rows[0].xyz
    )
    assert frustum.right_plane == Plane(
        rows[3].w - rows[0].w,
        rows[3].xyz - rows[0].xyz
    )
    assert frustum.bottom_plane == Plane(
        rows[3].w + rows[1].w,
        rows[3].xyz + rows[1].xyz
    )
    assert frustum.top_plane == Plane(
        rows[3].w - rows[1].w,
        rows[3].xyz - rows[1].xyz
    )