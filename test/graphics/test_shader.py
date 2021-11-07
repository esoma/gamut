
# gamut
from gamut._glcontext import get_gl_context
from gamut.graphics import Shader, ShaderAttribute, ShaderUniform
# python
import sys
from typing import Any, Optional
# pyglm
import glm
# pytest
import pytest


def test_empty_shader() -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader()
    assert str(excinfo.value) == 'vertex or fragment must be provided'


@pytest.mark.parametrize("vertex", [1, 'string', object(), bytearray()])
def test_invalid_vertex_type(vertex: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader(vertex=vertex)
    assert str(excinfo.value) == 'vertex must be bytes'


@pytest.mark.parametrize("fragment", [1, 'string', object(), bytearray()])
def test_invalid_fragment_type(fragment: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Shader(fragment=fragment)
    assert str(excinfo.value) == 'fragment must be bytes'


@pytest.mark.parametrize("stage", ['vertex', 'fragment'])
def test_compile_error(stage: str) -> None:
    with pytest.raises(RuntimeError) as excinfo:
        Shader(**{
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
    if location is not None and get_gl_context().version < (4, 3):
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
    shader = Shader(vertex=f'''#version 410 core
    #extension GL_ARB_explicit_uniform_location : enable
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
    shader = Shader(vertex=f'''#version 410 core
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
    # macos has problems with dmat3+x3+ in arrays?
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
    shader = Shader(vertex=f'''#version 410 core
    {layout} in {prefix}mat{rows}x{columns} attr_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    '''.encode('utf-8'))
    print(shader.attributes)
    attr = shader["attr_name"]
    assert len(shader.attributes) == 1
    assert shader.attributes[0] is attr
    assert isinstance(attr, ShaderAttribute)
    assert attr.name == "attr_name"
    assert attr.type is getattr(glm, f'{prefix}mat{rows}x{columns}')
    assert attr.size == (2 if array else 1)
    assert attr.location == (0 if location is None else location)
