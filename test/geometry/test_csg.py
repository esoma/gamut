
# gamut
from gamut.geometry import RectangularCuboid, Triangle3d
from gamut.geometry._csg import CsgBrush, CsgOperation
from gamut.math import FVector3


def test_get_intersections():
    cube_a = RectangularCuboid(FVector3(.5), FVector3(1))
    cube_b = RectangularCuboid(FVector3(1.25), FVector3(1))

    csg_a = CsgBrush()
    positions, _, _, indices = cube_a.render()
    for i in range(0, len(indices), 3):
        tri = Triangle3d(
            positions[indices[i]],
            positions[indices[i + 1]],
            positions[indices[i + 2]]
        )
        csg_a.add_triangle(tri)

    csg_b = CsgBrush()
    positions, _, _, indices = cube_b.render()
    for i in range(0, len(indices), 3):
        tri = Triangle3d(
            positions[indices[i]],
            positions[indices[i + 1]],
            positions[indices[i + 2]]
        )
        csg_b.add_triangle(tri)

    op = CsgOperation(csg_a, csg_b, 0)
    a_intersections, b_intersections = op._get_intersections()

    a_ltb_rtf_rtb = Triangle3d(
        # ltb
        FVector3(0, 1, 0),
        # rtf
        FVector3(1, 1, 1),
        # rtb
        FVector3(1, 1, 0)
    )
    a_ltb_ltf_rtf = Triangle3d(
        # ltb
        FVector3(0, 1, 0),
        # ltf
        FVector3(0, 1, 1),
        # rtf
        FVector3(1, 1, 1)
    )
    a_rbf_rtb_rtf = Triangle3d(
        # rbf
        FVector3(1, 0, 1),
        # rtb
        FVector3(1, 1, 0),
        # rtf
        FVector3(1, 1, 1)
    )
    a_ltf_rbf_rtf = Triangle3d(
        # ltf
        FVector3(0, 1, 1),
        # rbf
        FVector3(1, 0, 1),
        # rtf
        FVector3(1, 1, 1)
    )

    b_lbb_rtb_rbb = Triangle3d(
        # lbb
        FVector3(.75, .75, .75),
        # rtb
        FVector3(1.75, 1.75, .75),
        # rbb
        FVector3(1.75, .75, .75)
    )
    b_lbb_ltb_rtb = Triangle3d(
        # lbb
        FVector3(.75, .75, .75),
        # ltb
        FVector3(.75, 1.75, .75),
        # rtb
        FVector3(1.75, 1.75, .75)
    )
    b_lbb_lbf_ltb = Triangle3d(
        # lbb
        FVector3(.75, .75, .75),
        # lbf
        FVector3(.75, .75, 1.75),
        # ltb
        FVector3(.75, 1.75, .75)
    )
    b_lbb_rbb_rbf = Triangle3d(
        # lbb
        FVector3(.75, .75, .75),
        # rbb
        FVector3(1.75, .75, .75),
        # rbf
        FVector3(1.75, .75, 1.75)
    )
    b_lbb_rbf_lbf = Triangle3d(
        # lbb
        FVector3(.75, .75, .75),
        # rbf
        FVector3(1.75, .75, 1.75),
        # lbf
        FVector3(.75, .75, 1.75)
    )

    assert a_intersections == {
        a_ltb_rtf_rtb: {
            b_lbb_rtb_rbb,
            b_lbb_ltb_rtb,
            b_lbb_lbf_ltb,
        },
        a_ltb_ltf_rtf: {
            b_lbb_lbf_ltb,
            b_lbb_ltb_rtb,
        },
        a_rbf_rtb_rtf: {
            b_lbb_rbb_rbf,
            b_lbb_rbf_lbf,
            b_lbb_rtb_rbb,
            b_lbb_ltb_rtb,
        },
        a_ltf_rbf_rtf: {
            b_lbb_rbb_rbf,
            b_lbb_rbf_lbf,
            b_lbb_lbf_ltb,
        },
    }

    assert b_intersections == {
        b_lbb_rtb_rbb: {
            a_ltb_rtf_rtb,
            a_rbf_rtb_rtf
        },
        b_lbb_ltb_rtb: {
            a_ltb_rtf_rtb,
            a_ltb_ltf_rtf,
            a_rbf_rtb_rtf,
        },
        b_lbb_lbf_ltb: {
            a_ltb_rtf_rtb,
            a_ltb_ltf_rtf,
            a_ltf_rbf_rtf,
        },
        b_lbb_rbb_rbf: {
            a_rbf_rtb_rtf,
            a_ltf_rbf_rtf,
        },
        b_lbb_rbf_lbf: {
            a_rbf_rtb_rtf,
            a_ltf_rbf_rtf,
        },
    }

def test_get_tri_2d_intersections():
    cube_a = RectangularCuboid(FVector3(.5), FVector3(1))
    cube_b = RectangularCuboid(FVector3(1.25), FVector3(1))

    csg_a = CsgBrush()
    positions, _, _, indices = cube_a.render()
    for i in range(0, len(indices), 3):
        tri = Triangle3d(
            positions[indices[i]],
            positions[indices[i + 1]],
            positions[indices[i + 2]]
        )
        csg_a.add_triangle(tri)

    csg_b = CsgBrush()
    positions, _, _, indices = cube_b.render()
    for i in range(0, len(indices), 3):
        tri = Triangle3d(
            positions[indices[i]],
            positions[indices[i + 1]],
            positions[indices[i + 2]]
        )
        csg_b.add_triangle(tri)

    op = CsgOperation(csg_a, csg_b, 0)
    a_intersections, b_intersections = op._get_tri_2d_intersections()

    a_ltb_rtf_rtb = Triangle3d(
        # ltb
        FVector3(0, 1, 0),
        # rtf
        FVector3(1, 1, 1),
        # rtb
        FVector3(1, 1, 0)
    )
    a_ltb_ltf_rtf = Triangle3d(
        # ltb
        FVector3(0, 1, 0),
        # ltf
        FVector3(0, 1, 1),
        # rtf
        FVector3(1, 1, 1)
    )
    a_rbf_rtb_rtf = Triangle3d(
        # rbf
        FVector3(1, 0, 1),
        # rtb
        FVector3(1, 1, 0),
        # rtf
        FVector3(1, 1, 1)
    )
    a_ltf_rbf_rtf = Triangle3d(
        # ltf
        FVector3(0, 1, 1),
        # rbf
        FVector3(1, 0, 1),
        # rtf
        FVector3(1, 1, 1)
    )

    assert len(a_intersections) == 4
    a_ltb_rtf_rtb_intersections = a_intersections[a_ltb_rtf_rtb]
    assert set(a_ltb_rtf_rtb_intersections.get_tris()) == {
        Triangle3d(
            FVector3(0, 1, 0),
            FVector3(1, 1, 0),
            FVector3(1, 1, .75),
        ),
        Triangle3d(
            FVector3(.75, 1, .75),
            FVector3(1, 1, .75),
            FVector3(1, 1, 1),
        ),
        Triangle3d(
            FVector3(0, 1, 0),
            FVector3(.75, 1, .75),
            FVector3(1, 1, .75),
        ),
    }
    a_ltb_ltf_rtf_intersections = a_intersections[a_ltb_ltf_rtf]
    print(a_ltb_ltf_rtf)
    print('----')
    for tri in a_ltb_ltf_rtf_intersections._2d_tris:
        print(tri)


    assert False

