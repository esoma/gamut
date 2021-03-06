
from __future__ import annotations
# gamut
from gamut.gltf import Gltf
from gamut.graphics import PrimitiveMode
from gamut.math import FMatrix4, FVector3, FVector3Array, FVector4, U16Array
# python
from pathlib import Path
# pytest
import pytest


@pytest.mark.parametrize("glb", [True, False])
def test_box(glb: bool, resources: Path) -> None:
    if glb:
        with open(resources / 'Box.glb', 'rb') as f:
            gltf = Gltf(f)
    else:
        def file_path_callback(path: Path, length: int | None) -> memoryview:
            if length is None:
                length = 0
            with open(resources / path, 'rb') as f:
                return memoryview(f.read(length))
        with open(resources / 'Box.gltf', 'rb') as f:
            gltf = Gltf(f, file_path_callback=file_path_callback)

    assert len(gltf.buffers) == 1
    buffer = gltf.buffers[0]
    assert isinstance(buffer.data, memoryview)
    assert bytes(buffer.data) == (
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x80?\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?'
        b'\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?'
        b'\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00'
        b'\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?'
        b'\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00'
        b'\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf'
        b'\x00\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00'
        b'\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00'
        b'\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00'
        b'\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00'
        b'\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00'
        b'\xbf\x00\x00\x01\x00\x02\x00\x03\x00\x02\x00\x01\x00\x04\x00\x05\x00'
        b'\x06\x00\x07\x00\x06\x00\x05\x00\x08\x00\t\x00\n\x00\x0b\x00\n\x00'
        b'\t\x00\x0c\x00\r\x00\x0e\x00\x0f\x00\x0e\x00\r\x00\x10\x00\x11\x00'
        b'\x12\x00\x13\x00\x12\x00\x11\x00\x14\x00\x15\x00\x16\x00\x17\x00'
        b'\x16\x00\x15\x00'
    )

    assert len(gltf.buffer_views) == 2
    buffer_view_0 = gltf.buffer_views[0]
    assert isinstance(buffer_view_0.get_data(1), memoryview)
    assert bytes(buffer_view_0.get_data(1)) == (
        b'\x00\x00\x01\x00\x02\x00\x03\x00\x02\x00\x01\x00\x04\x00\x05\x00'
        b'\x06\x00\x07\x00\x06\x00\x05\x00\x08\x00\t\x00\n\x00\x0b\x00\n\x00'
        b'\t\x00\x0c\x00\r\x00\x0e\x00\x0f\x00\x0e\x00\r\x00\x10\x00\x11\x00'
        b'\x12\x00\x13\x00\x12\x00\x11\x00\x14\x00\x15\x00\x16\x00\x17\x00'
        b'\x16\x00\x15\x00'
    )

    buffer_view_1 = gltf.buffer_views[1]
    assert isinstance(buffer_view_1.get_data(1), memoryview)
    assert bytes(buffer_view_1.get_data(1)) == (
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x80?\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x80\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?'
        b'\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?'
        b'\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00'
        b'\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?'
        b'\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00'
        b'\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf'
        b'\x00\x00\x00?\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00'
        b'\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00'
        b'\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00'
        b'\x00?\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00'
        b'\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00\xbf\x00\x00\x00?\x00'
        b'\x00\x00\xbf\x00\x00\x00\xbf\x00\x00\x00?\x00\x00\x00?\x00\x00\x00'
        b'\xbf'
    )

    assert len(gltf.accessors) == 3
    accessor_0 = gltf.accessors[0]
    assert isinstance(accessor_0.data, U16Array)
    assert accessor_0.data == U16Array(
        0, 1, 2, 3, 2, 1, 4, 5, 6, 7, 6, 5, 8, 9, 10, 11, 10, 9, 12, 13, 14,
        15, 14, 13, 16, 17, 18, 19, 18, 17, 20, 21, 22, 23, 22, 21,
    )

    accessor_1 = gltf.accessors[1]
    assert isinstance(accessor_1.data, FVector3Array)
    assert accessor_1.data == FVector3Array(
        FVector3(0.0, 0.0, 1.0), FVector3(0.0, 0.0, 1.0),
        FVector3(0.0, 0.0, 1.0), FVector3(0.0, 0.0, 1.0),
        FVector3(0.0, -1.0, 0.0), FVector3(0.0, -1.0, 0.0),
        FVector3(0.0, -1.0, 0.0), FVector3(0.0, -1.0, 0.0),
        FVector3(1.0, 0.0, 0.0), FVector3(1.0, 0.0, 0.0),
        FVector3(1.0, 0.0, 0.0), FVector3(1.0, 0.0, 0.0),
        FVector3(0.0, 1.0, 0.0), FVector3(0.0, 1.0, 0.0),
        FVector3(0.0, 1.0, 0.0), FVector3(0.0, 1.0, 0.0),
        FVector3(-1.0, 0.0, 0.0), FVector3(-1.0, 0.0, 0.0),
        FVector3(-1.0, 0.0, 0.0), FVector3(-1.0, 0.0, 0.0),
        FVector3(0.0, 0.0, -1.0), FVector3(0.0, 0.0, -1.0),
        FVector3(0.0, 0.0, -1.0), FVector3(0.0, 0.0, -1.0),
    )

    accessor_2 = gltf.accessors[2]
    assert isinstance(accessor_2.data, FVector3Array)
    assert accessor_2.data == FVector3Array(
        FVector3(-0.5, -0.5, 0.5), FVector3(0.5, -0.5, 0.5),
        FVector3(-0.5, 0.5, 0.5), FVector3(0.5, 0.5, 0.5),
        FVector3(0.5, -0.5, 0.5), FVector3(-0.5, -0.5, 0.5),
        FVector3(0.5, -0.5, -0.5), FVector3(-0.5, -0.5, -0.5),
        FVector3(0.5, 0.5, 0.5), FVector3(0.5, -0.5, 0.5),
        FVector3(0.5, 0.5, -0.5), FVector3(0.5, -0.5, -0.5),
        FVector3(-0.5, 0.5, 0.5), FVector3(0.5, 0.5, 0.5),
        FVector3(-0.5, 0.5, -0.5), FVector3(0.5, 0.5, -0.5),
        FVector3(-0.5, -0.5, 0.5), FVector3(-0.5, 0.5, 0.5),
        FVector3(-0.5, -0.5, -0.5), FVector3(-0.5, 0.5, -0.5),
        FVector3(-0.5, -0.5, -0.5), FVector3(-0.5, 0.5, -0.5),
        FVector3(0.5, -0.5, -0.5), FVector3(0.5, 0.5, -0.5)
    )

    assert gltf.animations == []
    assert gltf.cameras == []
    assert gltf.images == []
    assert gltf.samplers == []
    assert gltf.textures == []

    assert len(gltf.materials) == 1
    material_0 = gltf.materials[0]
    assert material_0.name == 'Red'
    assert material_0.pbr_metallic_roughness.base_color_factor == FVector4(
        0.800000011920929, 0.0, 0.0, 1.0
    )
    assert material_0.pbr_metallic_roughness.base_color_texture is None
    assert material_0.pbr_metallic_roughness.base_color_texcoord is None
    assert material_0.pbr_metallic_roughness.metallic_factor == 0
    assert material_0.pbr_metallic_roughness.roughness_factor == 1.0
    assert material_0.pbr_metallic_roughness.metallic_roughness_texture is None
    assert (
        material_0.pbr_metallic_roughness.metallic_roughness_texcoord is None
    )
    assert material_0.normal_texture is None
    assert material_0.normal_texcoord is None
    assert material_0.occlusion_texture is None
    assert material_0.occlusion_texcoord is None
    assert material_0.emissive_texture is None
    assert material_0.emissive_texcoord is None
    assert material_0.emissive_factor == FVector3(0)
    assert material_0.alpha_mode == Gltf.Material.AlphaMode.OPAQUE
    assert material_0.alpha_cutoff == .5
    assert not material_0.is_double_sided

    assert len(gltf.meshes) == 1
    mesh_0 = gltf.meshes[0]
    assert mesh_0.name == 'Mesh'
    assert mesh_0.weights is None
    assert len(mesh_0.primitives) == 1
    mesh_0_primitive = mesh_0.primitives[0]
    mesh_0_primitive.attributes == {
        "NORMAL": accessor_1,
        "POSITION": accessor_2,
    }
    mesh_0_primitive.indices == accessor_0
    mesh_0_primitive.material == material_0
    mesh_0_primitive.mode == PrimitiveMode.TRIANGLE
    mesh_0_primitive.targets is None

    assert gltf.skins == []

    assert len(gltf.nodes) == 2
    node_0 = gltf.nodes[0]
    node_1 = gltf.nodes[1]
    assert node_0.camera is None
    assert node_0.children == [node_1]
    assert node_0.skin is None
    assert node_0.mesh is None
    assert node_0.weights is None
    assert node_0.transform == FMatrix4(
        1, 0, 0, 0,
        0, 0, -1, 0,
        0, 1, 0, 0,
        0, 0, 0, 1
    )

    assert node_1.camera is None
    assert node_1.children == []
    assert node_1.skin is None
    assert node_1.mesh == mesh_0
    assert node_1.weights is None
    assert node_1.transform == FMatrix4(1)

    assert len(gltf.scenes) == 1
    scene_0 = gltf.scenes[0]
    assert scene_0.nodes == [node_0]

    assert gltf.scene == scene_0
