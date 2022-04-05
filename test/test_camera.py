
# gamut
from gamut import Camera, TransformNode
from gamut.geometry import ViewFrustum3d
from gamut.math import FMatrix4, FVector2, FVector3
# python
from math import isclose as _isclose
from math import radians
from typing import Any
# pytest
import pytest


def isclose(a, b):
    return _isclose(a, b, rel_tol=1e-06)


@pytest.mark.parametrize("projection_transform", [None, 'str', 1])
def test_invalid_projection_transform(projection_transform: Any) -> None:
    with pytest.raises(TypeError) as ex:
        Camera(projection_transform)
    assert str(ex.value) == 'projection transform must be FMatrix4x4'


@pytest.mark.parametrize("local_transform", ['str', 1])
def test_invalid_local_transform(local_transform: Any) -> None:
    with pytest.raises(TypeError) as ex:
        Camera(FMatrix4(1), local_transform=local_transform)
    assert str(ex.value) == 'local transform must be FMatrix4x4'


def test_transforms() -> None:
    perspective = FMatrix4.perspective(0.78, .5, .1, 100)
    parent = TransformNode()
    camera = Camera(perspective, parent=parent)

    assert camera.view_transform == FMatrix4(1)
    assert camera.projection_transform == perspective
    assert camera.view_projection_transform == perspective
    assert camera.view_frustum == ViewFrustum3d.from_view_projection_transform(
        camera.view_projection_transform.to_dmatrix()
    )

    camera.local_transform = FMatrix4(1).translate(FVector3(1))
    assert camera.projection_transform == perspective
    assert camera.view_projection_transform == perspective @ camera.transform
    assert camera.view_frustum == ViewFrustum3d.from_view_projection_transform(
        camera.view_projection_transform.to_dmatrix()
    )

    parent.local_transform = FMatrix4(1).translate(FVector3(1))
    assert camera.projection_transform == perspective
    assert camera.view_projection_transform == perspective @ camera.transform
    assert camera.view_frustum == ViewFrustum3d.from_view_projection_transform(
        camera.view_projection_transform.to_dmatrix()
    )


def test_generate_ray() -> None:
    perspective = FMatrix4.perspective(0.78, .5, .1, 100)
    camera = Camera(perspective)

    ray = camera.generate_ray(FVector2(0, 0))
    assert ray.a.x == 0
    assert ray.a.y == 0
    assert isclose(ray.a.z, -0.10000000894069672)
    assert ray.b.x == 0
    assert ray.b.y == 0
    assert isclose(ray.b.z, -99.99771118164062)

    ray = camera.generate_ray(FVector2(-1, -1))
    assert isclose(ray.a.x, -0.0205527450889349)
    assert isclose(ray.a.y, -0.0411054901778698)
    assert isclose(ray.a.z, -0.10000000894069672)
    assert isclose(ray.b.x, -20.55227279663086)
    assert isclose(ray.b.y, -41.10454559326172)
    assert isclose(ray.b.z, -99.99771118164062)

    camera.local_transform = FMatrix4(1).rotate(
        radians(180),
        FVector3(0, 1, 0)
    )
    ray = camera.generate_ray(FVector2(0, 0))
    assert isclose(ray.a.x, -8.742278900797373e-09)
    assert isclose(ray.a.y, 0)
    assert isclose(ray.a.z, 0.10000000894069672)
    assert isclose(ray.b.x, -8.742077625356615e-06)
    assert isclose(ray.b.y, 0)
    assert isclose(ray.b.z, 99.99771118164062)

    ray = camera.generate_ray(FVector2(1, 1))
    assert isclose(ray.a.x, -0.020552754402160645)
    assert isclose(ray.a.y, 0.0411054901778698)
    assert isclose(ray.a.z, 0.10000000894069672)
    assert isclose(ray.b.x, -20.552282333374023)
    assert isclose(ray.b.y, 41.10454559326172)
    assert isclose(ray.b.z, 99.99771118164062)
