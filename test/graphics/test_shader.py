
# gamut
from gamut import Application, Window
from gamut._glcontext import get_gl_context
from gamut.graphics import (Buffer, Shader, ShaderAttribute, ShaderUniform,
                            Texture, Texture2d, TextureComponents)
from gamut.graphics._shader import use_shader
# python
import sys
import threading
from typing import Any, Optional
# pyglm
import glm
# pytest
import pytest


def test_empty_shader() -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader()
    assert str(excinfo.value) == (
        'vertex, geometry and fragment must be provided'
    )


@pytest.mark.parametrize("vertex", [1, 'string', object(), bytearray()])
def test_invalid_vertex_type(vertex: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader(vertex=vertex)
    assert str(excinfo.value) == 'vertex must be bytes'


@pytest.mark.parametrize("geometry", [1, 'string', object(), bytearray()])
def test_invalid_geometry_type(geometry: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader(geometry=geometry)
    assert str(excinfo.value) == 'geometry must be bytes'


@pytest.mark.parametrize("fragment", [1, 'string', object(), bytearray()])
def test_invalid_fragment_type(fragment: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader(fragment=fragment)
    assert str(excinfo.value) == 'fragment must be bytes'


@pytest.mark.parametrize("stage", ['vertex', 'fragment'])
def test_compile_error(stage: str) -> None:
    with pytest.raises(RuntimeError) as excinfo:
        Shader(**{ # type: ignore
            stage: b'''#version 140
            void main()
            {
                what--what
            }
            '''}
        )
    assert str(excinfo.value).startswith(f'{stage} stage failed to compile:\n')


def test_link_error() -> None:
    with pytest.raises(RuntimeError) as excinfo:
        Shader(
            vertex=f'''
            #version 140
            vec4 some_function_that_doesnt_exist();
            void main()
            {{
                gl_Position = some_function_that_doesnt_exist();
            }}
            '''.encode('utf-8'),
        )
    assert str(excinfo.value).startswith(f'Failed to link:\n')


def test_vertex_only() -> None:
    shader = Shader(vertex=b'''#version 140
    void main()
    {
        gl_Position = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open


def test_geometry_only() -> None:
    with pytest.raises(TypeError) as excinfo:
        shader = Shader(geometry=b'''#version 150
        layout(triangles) in;
        layout(triangle_strip) out;

        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        ''')
    assert str(excinfo.value) == 'geometry shader requires vertex shader'


def test_fragment_only() -> None:
    shader = Shader(fragment=b'''#version 140
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open


def test_vertex_and_fragment() -> None:
    shader = Shader(vertex=b'''#version 140
    void main()
    {
        gl_Position = vec4(0, 0, 0, 1);
    }
    ''', fragment=b'''#version 330
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open


def test_close() -> None:
    shader = Shader(vertex=b'''#version 140
    void main()
    {
        gl_Position = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open
    shader.close()
    assert not shader.is_open
    shader.close()
    assert not shader.is_open

    with pytest.raises(RuntimeError) as excinfo:
        shader.attributes
    assert str(excinfo.value) == 'shader is closed'

    with pytest.raises(RuntimeError) as excinfo:
        shader.uniforms
    assert str(excinfo.value) == 'shader is closed'


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("glsl_type, python_type", [
    ('float', glm.float32),
    ('double', glm.double),
    ('int', glm.int32),
    ('uint', glm.uint32),
])
@pytest.mark.parametrize("array", [False, True])
def test_pod_attributes(
    location: Optional[int],
    glsl_type: str,
    python_type: Any,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'
    if location is not None or array:
        glsl_version = '330 core'
        if get_gl_context().version < (3, 3):
            pytest.xfail()

    if glsl_type == 'double':
        glsl_version = '410 core'
        if get_gl_context().version < (4, 1):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'attr_name[0]'
        y_value = 'attr_name[1]'
    else:
        array_def = ''
        x_value = 'attr_name'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} in {glsl_type} attr_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    attr = shader["attr_name"]
    assert len(shader.attributes) == 1
    assert shader.attributes[0] is attr
    assert isinstance(attr, ShaderAttribute)
    assert attr.name == "attr_name"
    assert attr.type is python_type
    assert attr.size == (2 if array else 1)
    assert attr.location == (0 if location is None else location)


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("glsl_type, python_type", [
    ('float', glm.float32),
    ('double', glm.double),
    ('int', glm.int32),
    ('uint', glm.uint32),
    ('bool', glm.bool_),
])
@pytest.mark.parametrize("array", [False, True])
def test_pod_uniforms(
    location: Optional[int],
    glsl_type: str,
    python_type: Any,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if glsl_type == 'double':
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if location is not None:
        glsl_version = '430 core'
        if get_gl_context().version < (4, 3):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'uni_name[0]'
        y_value = 'uni_name[1]'
    else:
        array_def = ''
        x_value = 'uni_name'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} uniform {glsl_type} uni_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    uni = shader["uni_name"]
    assert len(shader.uniforms) == 1
    assert shader.uniforms[0] is uni
    assert isinstance(uni, ShaderUniform)
    assert uni.name == "uni_name"
    assert uni.type is python_type
    assert uni.size == (2 if array else 1)
    assert uni.location == (0 if location is None else location)

    use_shader(shader)
    if array:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {glm.array} for uni_name (got {type(None)})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(
                uni,
                glm.array.from_numbers(glm.uint8, 0, 100) # type: ignore
            )
        assert str(excinfo.value) == (
            f'expected array of {python_type} for uni_name '
            f'(got array of {glm.uint8})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, glm.array.from_numbers(python_type, 0))
        assert str(excinfo.value) == (
            f'expected array of length 2 for uni_name '
            f'(got array of length 1)'
        )
        shader._set_uniform(uni, glm.array.from_numbers(python_type, 0, 100))
    else:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {python_type} for uni_name (got {type(None)})'
        )
        shader._set_uniform(uni, python_type(100))


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("prefix", ['', 'i', 'u'])
@pytest.mark.parametrize("postfix, components", [
    ('1D', 1),
    ('2D', 2),
    ('3D', 3),
    ('Cube', 3),
    ('2DRect', 2),
    ('1DArray', 2),
    ('2DArray', 3),
    ('CubeArray', 4),
    ('Buffer', 1),
    ('2DMS', 2),
    ('2DMSArray', 3),
])
@pytest.mark.parametrize("array", [False, True])
def test_sampler_uniforms(
    location: Optional[int],
    prefix: str,
    postfix: str,
    components: int,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if postfix in ['2DMS', '2DMSArray']:
        glsl_version = '150'
        if get_gl_context().version < (3, 2):
            pytest.xfail()

    if postfix == 'CubeArray':
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if location is not None:
        glsl_version = '430 core'
        if get_gl_context().version < (4, 3):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    texture_function = 'texture'
    if postfix in ['Buffer', '2DMS', '2DMSArray']:
        texture_function = 'texelFetch'
    texture_lookup = ', '.join('0' * components)
    if components > 1:
        texture_lookup = f'vec{components}({texture_lookup})'
    if postfix in ['2DMS', '2DMSArray']:
        texture_lookup = f'i{texture_lookup}, 0'
    if array:
        array_def = '[2]'
        x_value = f'{texture_function}(uni_name[0], {texture_lookup}).r'
        y_value = f'{texture_function}(uni_name[1], {texture_lookup}).r'
    else:
        array_def = ''
        x_value = f'{texture_function}(uni_name, {texture_lookup}).r'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} uniform {prefix}sampler{postfix} uni_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    uni = shader["uni_name"]
    assert len(shader.uniforms) == 1
    assert shader.uniforms[0] is uni
    assert isinstance(uni, ShaderUniform)
    assert uni.name == "uni_name"
    assert uni.type is Texture
    assert uni.size == (2 if array else 1)
    assert uni.location == (0 if location is None else location)

    use_shader(shader)
    if array:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected sequence of {Texture} for uni_name (got {type(None)})'
        )
        bad_value = glm.array.from_numbers(glm.uint8, 0, 100)
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(
                uni,
                bad_value, # type: ignore
            )
        assert str(excinfo.value) == (
            f'expected sequence of {Texture} for uni_name '
            f'(found {bad_value[0]} in sequence)'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, glm.array.from_numbers(glm.int32, 0))
        assert str(excinfo.value) == (
            f'expected sequence of length 2 for uni_name '
            f'(got sequence of length 1)'
        )
        shader._set_uniform(uni, [
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00'),
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00')
        ])
    else:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {Texture} for uni_name (got {type(None)})'
        )
        shader._set_uniform(
            uni,
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00')
        )


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("postfix, components", [
    ('1DShadow', 3),
    ('2DShadow', 3),
    ('CubeShadow', 4),
    ('2DRectShadow', 3),
    ('1DArrayShadow', 3),
    ('2DArrayShadow', 4),
])
@pytest.mark.parametrize("array", [False, True])
def test_shadow_sampler_uniforms(
    location: Optional[int],
    postfix: str,
    components: int,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if location is not None:
        glsl_version = '430 core'
        if get_gl_context().version < (4, 3):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    texture_lookup = ', '.join('0' * components)
    if components > 1:
        texture_lookup = f'vec{components}({texture_lookup})'
    if array:
        array_def = '[2]'
        x_value = f'texture(uni_name[0], {texture_lookup})'
        y_value = f'texture(uni_name[1], {texture_lookup})'
    else:
        array_def = ''
        x_value = f'texture(uni_name, {texture_lookup})'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} uniform sampler{postfix} uni_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    uni = shader["uni_name"]
    assert len(shader.uniforms) == 1
    assert shader.uniforms[0] is uni
    assert isinstance(uni, ShaderUniform)
    assert uni.name == "uni_name"
    assert uni.type is Texture
    assert uni.size == (2 if array else 1)
    assert uni.location == (0 if location is None else location)

    use_shader(shader)
    if array:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected sequence of {Texture} for uni_name (got {type(None)})'
        )
        bad_value = glm.array.from_numbers(glm.uint8, 0, 100)
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(
                uni,
                bad_value, # type: ignore
            )
        assert str(excinfo.value) == (
            f'expected sequence of {Texture} for uni_name '
            f'(found {bad_value[0]} in sequence)'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, glm.array.from_numbers(glm.int32, 0))
        assert str(excinfo.value) == (
            f'expected sequence of length 2 for uni_name '
            f'(got sequence of length 1)'
        )
        shader._set_uniform(uni, [
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00'),
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00')
        ])
    else:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {Texture} for uni_name (got {type(None)})'
        )
        shader._set_uniform(
            uni,
            Texture2d((1, 1), TextureComponents.R, glm.uint8, b'\x00')
        )


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("components", [2, 3, 4])
@pytest.mark.parametrize("prefix", ['', 'd', 'i', 'u'])
@pytest.mark.parametrize("array", [False, True])
def test_vector_attributes(
    location: Optional[int],
    components: int,
    prefix: str,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if location is not None:
        glsl_version = '330 core'
        if get_gl_context().version < (3, 3):
            pytest.xfail()

    if array:
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if prefix == 'd':
        glsl_version = '410 core'
        if get_gl_context().version < (4, 1):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'attr_name[0].x'
        y_value = 'attr_name[1].x'
    else:
        array_def = ''
        x_value = 'attr_name.x'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} in {prefix}vec{components} attr_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    attr = shader["attr_name"]
    assert len(shader.attributes) == 1
    assert shader.attributes[0] is attr
    assert isinstance(attr, ShaderAttribute)
    assert attr.name == "attr_name"
    assert attr.type is getattr(glm, f'{prefix}vec{components}')
    assert attr.size == (2 if array else 1)
    assert attr.location == (0 if location is None else location)


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("components", [2, 3, 4])
@pytest.mark.parametrize("prefix", ['', 'd', 'i', 'u'])
@pytest.mark.parametrize("array", [False, True])
def test_vector_uniforms(
    location: Optional[int],
    components: int,
    prefix: str,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if prefix == 'd':
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if location is not None:
        glsl_version = '430 core'
        if get_gl_context().version < (4, 3):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'uni_name[0].x'
        y_value = 'uni_name[1].x'
    else:
        array_def = ''
        x_value = 'uni_name.x'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} uniform {prefix}vec{components} uni_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    uni = shader["uni_name"]
    assert len(shader.uniforms) == 1
    assert shader.uniforms[0] is uni
    assert isinstance(uni, ShaderUniform)
    assert uni.name == "uni_name"
    assert uni.type is getattr(glm, f'{prefix}vec{components}')
    assert uni.size == (2 if array else 1)
    assert uni.location == (0 if location is None else location)

    python_type = getattr(glm, f'{prefix}vec{components}')
    use_shader(shader)
    if array:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {glm.array} for uni_name (got {type(None)})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(
                uni,
                glm.array.from_numbers(glm.uint8, 0, 100) # type: ignore
            )
        assert str(excinfo.value) == (
            f'expected array of {python_type} for uni_name '
            f'(got array of {glm.uint8})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, glm.array(python_type(25)))
        assert str(excinfo.value) == (
            f'expected array of length 2 for uni_name '
            f'(got array of length 1)'
        )
        shader._set_uniform(uni, glm.array(python_type(25)).repeat(2))
    else:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {python_type} for uni_name (got {type(None)})'
        )
        shader._set_uniform(uni, python_type(100))


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("rows", [2, 3, 4])
@pytest.mark.parametrize("columns", [2, 3, 4])
@pytest.mark.parametrize("prefix", ['', 'd'])
@pytest.mark.parametrize("array", [False, True])
def test_matrix_attributes(
    location: Optional[int],
    rows: int, columns: int,
    prefix: str,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if location is not None:
        glsl_version = '330 core'
        if get_gl_context().version < (3, 3):
            pytest.xfail()

    if array:
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if prefix == 'd':
        glsl_version = '410 core'
        if get_gl_context().version < (4, 1):
            pytest.xfail()

    # macos has problems with dmat3x3+ in arrays?
    if (sys.platform == 'darwin' and prefix == 'd' and
        columns >= 3 and rows >= 3 and array):
        pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'attr_name[0][0][0]'
        y_value = 'attr_name[1][0][0]'
    else:
        array_def = ''
        x_value = 'attr_name[0][0]'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} in {prefix}mat{rows}x{columns} attr_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    attr = shader["attr_name"]
    assert len(shader.attributes) == 1
    assert shader.attributes[0] is attr
    assert isinstance(attr, ShaderAttribute)
    assert attr.name == "attr_name"
    assert attr.type is getattr(glm, f'{prefix}mat{rows}x{columns}')
    assert attr.size == (2 if array else 1)
    assert attr.location == (0 if location is None else location)


@pytest.mark.parametrize("location", [None, 1])
@pytest.mark.parametrize("rows", [2, 3, 4])
@pytest.mark.parametrize("columns", [2, 3, 4])
@pytest.mark.parametrize("prefix", ['', 'd'])
@pytest.mark.parametrize("array", [False, True])
def test_matrix_uniforms(
    location: Optional[int],
    rows: int, columns: int,
    prefix: str,
    array: bool,
) -> None:
    _ = Window()
    glsl_version = '140'

    if prefix == 'd':
        glsl_version = '400 core'
        if get_gl_context().version < (4, 0):
            pytest.xfail()

    if location is not None:
        glsl_version = '430 core'
        if get_gl_context().version < (4, 3):
            pytest.xfail()

    if location is None:
        layout = ''
    else:
        layout = f'layout(location={location})'
    if array:
        array_def = '[2]'
        x_value = 'uni_name[0][0][0]'
        y_value = 'uni_name[1][0][0]'
    else:
        array_def = ''
        x_value = 'uni_name[0][0]'
        y_value = '0'
    shader = Shader(vertex=f'''#version {glsl_version}
    {layout} uniform {prefix}mat{rows}x{columns} uni_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    uni = shader["uni_name"]
    assert len(shader.uniforms) == 1
    assert shader.uniforms[0] is uni
    assert isinstance(uni, ShaderUniform)
    assert uni.name == "uni_name"
    assert uni.type is getattr(glm, f'{prefix}mat{rows}x{columns}')
    assert uni.size == (2 if array else 1)
    assert uni.location == (0 if location is None else location)

    python_type = getattr(glm, f'{prefix}mat{rows}x{columns}')
    use_shader(shader)
    if array:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {glm.array} for uni_name (got {type(None)})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(
                uni,
                glm.array.from_numbers(glm.uint8, 0, 100) # type: ignore
            )
        assert str(excinfo.value) == (
            f'expected array of {python_type} for uni_name '
            f'(got array of {glm.uint8})'
        )
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, glm.array(python_type(25)))
        assert str(excinfo.value) == (
            f'expected array of length 2 for uni_name '
            f'(got array of length 1)'
        )
        shader._set_uniform(uni, glm.array(python_type(25)).repeat(2))
    else:
        with pytest.raises(ValueError) as excinfo:
            shader._set_uniform(uni, None) # type: ignore
        assert str(excinfo.value) == (
            f'expected {python_type} for uni_name (got {type(None)})'
        )
        shader._set_uniform(uni, python_type(100))


def test_shader_thread_transfer_to_app() -> None:
    shader = Shader(vertex=f'''
    #version 140
    void main()
    {{
        gl_Position = vec4(0, 0, 0, 1);
    }}
    '''.encode('utf-8'))

    class App(Application):
        async def main(self) -> None:
            shader.close()

    app = App()
    app.run()
    assert not shader.is_open


def test_shader_thread_transfer_to_main() -> None:
    shader: Optional[Shader] = None

    class App(Application):
        async def main(self) -> None:
            nonlocal shader
            shader = Shader(vertex=f'''
            #version 140
            void main()
            {{
                gl_Position = vec4(0, 0, 0, 1);
            }}
            '''.encode('utf-8'))

    app = App()
    app.run()
    assert shader is not None
    assert shader.is_open
    shader.close()
    assert not shader.is_open


def test_shader_thread_closed_outside_render_thread() -> None:
    keep_alive_buffer = Buffer()
    shader = Shader(vertex=f'''
    #version 140
    void main()
    {{
        gl_Position = vec4(0, 0, 0, 1);
    }}
    '''.encode('utf-8'))

    def thread_main() -> None:
        shader.close()

    thread = threading.Thread(target=thread_main)
    thread.start()
    thread.join()

    assert not shader.is_open


@pytest.mark.parametrize("ignored_attributes", [
    None,
    [],
    ['hello', 'world'],
])
@pytest.mark.parametrize("ignored_uniforms", [
    None,
    [],
    ['hello', 'world'],
])
def test_shader_ignore(ignored_attributes: Any, ignored_uniforms: Any) -> None:
    shader = Shader(vertex=f'''
        #version 140
        void main()
        {{
            gl_Position = vec4(0, 0, 0, 1);
        }}
        '''.encode('utf-8'),
        ignored_attributes=ignored_attributes,
        ignored_uniforms=ignored_uniforms,
    )
    assert isinstance(shader.ignored_attributes, set)
    assert isinstance(shader.ignored_uniforms, set)
    assert shader.ignored_attributes == set(
        ignored_attributes if ignored_attributes else []
    )
    assert shader.ignored_uniforms == set(
        ignored_uniforms if ignored_uniforms else []
    )
    assert shader.ignored_attributes is not ignored_attributes
    assert shader.ignored_uniforms is not ignored_uniforms


@pytest.mark.parametrize("name", ['abc', '_123'])
def test_shader_attribute_repr(name: str) -> None:
    shader = Shader(vertex=f'''
        #version 140
        in vec4 {name};
        void main()
        {{
            gl_Position = {name};
        }}
        '''.encode('utf-8'),
    )
    assert repr(shader.attributes[0]) == (
        f'<gamut.graphics.ShaderAttribute {name!r}>'
    )


@pytest.mark.parametrize("name", ['abc', '_123'])
def test_shader_uniform_repr(name: str) -> None:
    shader = Shader(vertex=f'''
        #version 140
        uniform vec4 {name};
        void main()
        {{
            gl_Position = {name};
        }}
        '''.encode('utf-8'),
    )
    assert repr(shader.uniforms[0]) == (
        f'<gamut.graphics.ShaderUniform {name!r}>'
    )
