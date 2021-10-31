
# gamut
from gamut.graphics import Shader, ShaderAttribute
# python
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
            stage: b'''#version 330
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
            vertex=b'''
            #version 330
            in vec4 pos[99];
            void main()
            {
                gl_Position = pos[0];
            }
            '''
        )
    assert str(excinfo.value).startswith(f'Failed to link:\n')


def test_vertex_only() -> None:
    shader = Shader(vertex=b'''#version 330
    void main()
    {
        gl_Position = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open


def test_fragment_only() -> None:
    shader = Shader(fragment=b'''#version 330
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(0, 0, 0, 1);
    }
    ''')
    assert shader.is_open


def test_vertex_and_fragment() -> None:
    shader = Shader(vertex=b'''#version 330
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
    shader = Shader(vertex=b'''#version 330
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
    print(f'''#version 410
    {layout} in {prefix}vec{components} attr_name{array_def};
    void main()
    {{
        gl_Position = vec4({x_value}, {y_value}, 0, 1);
    }}
    ''')
    shader = Shader(vertex=f'''#version 410
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
    shader = Shader(vertex=f'''#version 410
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
