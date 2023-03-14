
# gamut
from gamut.ai import NavigationMesh3d
from gamut.geometry import Triangle3d
from gamut.gltf import Gltf
from gamut.math import DVector3, FVector3
# python
from math import isclose
from pathlib import Path
# pytest
import pytest


def vector_is_close(a: DVector3, b: DVector3) -> bool:
    return (
        isclose(a.x, b.x),
        isclose(a.y, b.y),
        isclose(a.z, b.z),
    )


def test_find_basic_path() -> None:
    nm = NavigationMesh3d()

    nm.remove_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.remove_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 1),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    assert nm.contains_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    assert nm.contains_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-1, 0, 0)
    ))
    assert nm.contains_triangle(Triangle3d(
        DVector3(1, 0, 1),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    triangles = list(set(t.positions) for t in nm.triangles)
    assert {
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    } in triangles
    assert {
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-1, 0, 0)
    } in triangles
    assert {
        DVector3(1, 0, 1),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    } in triangles

    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 1),
        Triangle3d(DVector3(1, 0, 1), DVector3(0, 0, 1), DVector3(1, 0, 0))
    )
    assert path == (DVector3(0, 0, 0), DVector3(1, 0, 1))

    nm.remove_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 1),
        Triangle3d(DVector3(1, 0, 1), DVector3(0, 0, 1), DVector3(1, 0, 0))
    )
    assert path is None


def test_custom_weight() -> None:
    triangle_1 = Triangle3d(
        DVector3(-.5, 0, 0),
        DVector3(.5, 0, 0),
        DVector3(0, 0, 1)
    )
    triangle_2 = Triangle3d(
        DVector3(.5, 0, 0),
        DVector3(0, 0, 1),
        DVector3(.5, 0, 2),
    )

    def custom_calculate_weight(
        a: Triangle3d[DVector3], b: Triangle3d[DVector3]
    ) -> float:
        if {a, b} == {triangle_1, triangle_2}:
            return 1
        return .1

    nm = NavigationMesh3d(custom_calculate_weight)
    nm.add_triangle(triangle_1)
    nm.add_triangle(Triangle3d(
        DVector3(-.5, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-.5, 0, 2),
    ))
    nm.add_triangle(triangle_2)
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 1),
        DVector3(.5, 0, 2),
        DVector3(-.5, 0, 2)
    ))
    path = nm.find_path(
        DVector3(-.5, 0, 0),
        triangle_1,
        DVector3(.25, 0, -1),
        triangle_2
    )
    assert path == (
        DVector3(-0.5, 0.0, 0.0),
        DVector3(0.0, 0.0, 1.0),
        DVector3(0.25, 0.0, -1.0)
    )


def test_find_single_triangle() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
    )
    assert path == (DVector3(0, 0, 0), DVector3(1, 0, 0))


@pytest.mark.parametrize("c", [
    DVector3(1),
    DVector3(-1, 1, 1),
    DVector3(1, 1, -1),
    DVector3(-1, 1, -1),
]
)
def test_find_path_string_pull(c: DVector3) -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(1, 0, 0) * c,
        DVector3(0, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, 1) * c,
        DVector3(-1, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 1) * c,
        DVector3(0, 0, 1) * c,
        DVector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 1) * c,
        DVector3(-2, 0, 1) * c,
        DVector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, 1) * c,
        DVector3(-2, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-2, 0, 1) * c,
        DVector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, -1) * c,
        DVector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, -1) * c,
        DVector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, -1) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(0, 0, -1) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(-1, 0, -2) * c,
        DVector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(0, 0, -3) * c,
        DVector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(1, 0, -2) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(1, 0, -2) * c,
        DVector3(0, 0, -3) * c
    ))

    path = nm.find_path(
        DVector3(1, 0, 0) * c,
        Triangle3d(
            DVector3(1, 0, 0) * c,
            DVector3(0, 0, 1) * c,
            DVector3(0, 0, 0) * c,
        ),
        DVector3(-1, 0, -2) * c,
        Triangle3d(
            DVector3(-1, 0, -2) * c,
            DVector3(-1, 0, -3) * c,
            DVector3(0, 0, -2) * c,
        )
    )
    assert path == (
        DVector3(1, 0, 0) * c,
        DVector3(-1, 0, 1) * c,
        DVector3(-1, 0, 0) * c,
        DVector3(0, 0, -1) * c,
        DVector3(0, 0, -2) * c,
        DVector3(-1, 0, -2) * c,
    )


def test_find_path_string_pull_y() -> None:
    nm = NavigationMesh3d()
    # _
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(1, 0, 0),
        DVector3(1, 0, 1),
    ))
    # __
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 0),
        DVector3(1, 0, 1),
        DVector3(2, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 0),
        DVector3(2, 0, 0),
        DVector3(2, 0, 1),
    ))
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(2, 0, 0),
        DVector3(2, 0, 1),
        DVector3(3, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(2, 0, 0),
        DVector3(3, 1, 0),
        DVector3(3, 1, 1),
    ))
    #    _
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(3, 1, 0),
        DVector3(3, 1, 1),
        DVector3(4, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(3, 1, 0),
        DVector3(4, 1, 0),
        DVector3(4, 1, 1),
    ))
    #    __
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(4, 1, 0),
        DVector3(4, 1, 1),
        DVector3(5, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(4, 1, 0),
        DVector3(5, 1, 0),
        DVector3(5, 1, 1),
    ))
    #    __
    # __/  \
    nm.add_triangle(Triangle3d(
        DVector3(5, 1, 0),
        DVector3(5, 1, 1),
        DVector3(6, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(5, 1, 0),
        DVector3(6, 0, 0),
        DVector3(6, 0, 1),
    ))
    #    __
    # __/  \_
    nm.add_triangle(Triangle3d(
        DVector3(6, 0, 0),
        DVector3(6, 0, 1),
        DVector3(7, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(6, 0, 0),
        DVector3(7, 0, 0),
        DVector3(7, 0, 1),
    ))
    #    __
    # __/  \__
    nm.add_triangle(Triangle3d(
        DVector3(7, 0, 0),
        DVector3(7, 0, 1),
        DVector3(8, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(7, 0, 0),
        DVector3(8, 0, 0),
        DVector3(8, 0, 1),
    ))
    #    __
    # s_/  \_e
    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(
            DVector3(1, 0, 1),
            DVector3(0, 0, 0),
            DVector3(0, 0, 1),
        ),
        DVector3(8, 0, 1),
        Triangle3d(
            DVector3(8, 0, 1),
            DVector3(7, 0, 0),
            DVector3(8, 0, 0),
        )
    )
    print(path)
    assert vector_is_close(path[0], DVector3(0.0, 0.0, 0.0))
    assert vector_is_close(path[1], DVector3(2.0, 0.0, 0.25))
    assert vector_is_close(
        path[2],
        DVector3(2.2857142857142856, 0.2857142857142857, 0.2857142857142857)
    )
    assert vector_is_close(path[3], DVector3(3.0, 1.0, 0.3750000000000001))
    assert vector_is_close(path[4], DVector3(5.0, 1.0, 0.625))
    assert vector_is_close(
        path[5],
        DVector3(5.714285714285714, 0.2857142857142857, 0.7142857142857143)
    )
    assert vector_is_close(path[6], DVector3(6.0, 0.0, 0.75))
    assert vector_is_close(path[7], DVector3(8.0, 0.0, 1.0))


def test_find_path_string_pull_bug(resources: Path) -> None:
    with open(resources / 'navmesh.glb', 'rb') as f:
        navmesh_gltf = Gltf(f)
    navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
    navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
    navmesh_positions = navmesh_attrs["POSITION"].data

    nm = NavigationMesh3d()
    for i in range(len(navmesh_indices) // 3):
        nm.add_triangle(Triangle3d(
            navmesh_positions[navmesh_indices[(i * 3)]],
            navmesh_positions[navmesh_indices[(i * 3) + 1]],
            navmesh_positions[navmesh_indices[(i * 3) + 2]],
        ))

    path = nm.find_path(
        FVector3(-5.265909194946289, 2.0, 3.866203784942627),
        Triangle3d(
            FVector3(-6.0, 2.0, 4.0),
            FVector3(-4.0, 2.0, 4.0),
            FVector3(-4.0, 2.0, 1.0)
        ),
        FVector3(4.608282566070557, 2.0, -2.154895782470703),
        Triangle3d(
            FVector3(4.0, 2.0, -4.0),
            FVector3(4.0, 2.0, -1.0),
            FVector3(6.0, 2.0, -4.0)
        )
    )
    assert vector_is_close(
        path[0],
        FVector3(-5.265909194946289, 2.0, 3.866203784942627)
    )
    assert vector_is_close(path[1], FVector3(-4.0, 2.0, 1.0))
    assert vector_is_close(path[2], FVector3(4.0, 2.0, -1.0))
    assert vector_is_close(
        path[3],
        FVector3(4.608282566070557, 2.0, -2.154895782470703)
    )
