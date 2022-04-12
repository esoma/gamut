
# gamut
from gamut.graphics import ShaderCodePreprocessor
# python
from textwrap import dedent
# pytest
import pytest


def test_noop() -> None:
    scp = ShaderCodePreprocessor()
    input_code = dedent('''
    #version 140
    in vec3 pos;
    in vec2 uv;
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')
    output_code = scp(input_code)
    assert output_code == input_code


def test_defines() -> None:
    scp = ShaderCodePreprocessor()
    input_code = dedent('''
    #version 140
    in vec3 pos;
    in vec2 uv;
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')
    output_code = scp(input_code, defines={
        "def1": 1,
        "def2": 'abc',
    })
    assert output_code == dedent('''
    #version 140
    #define def1 1
    #define def2 abc
    in vec3 pos;
    in vec2 uv;
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')


def test_include() -> None:
    class ShaderCodePreprocessorInclude(ShaderCodePreprocessor):
        def include(self, name: str) -> bytes:
            if name == "first.glsl":
                return b'// first glsl'
            elif name == "second.glsl":
                return b'// second glsl'
            assert False

    scp = ShaderCodePreprocessorInclude()
    input_code = dedent('''
    #version 140
    in vec3 pos;
    #include <first.glsl>
    in vec2 uv;
    #include "second.glsl"
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')
    output_code = scp(input_code)
    assert output_code == dedent('''
    #version 140
    in vec3 pos;
    // first glsl
    in vec2 uv;
    // second glsl
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')


def test_default_include() -> None:
    scp = ShaderCodePreprocessor()
    input_code = dedent('''
    #version 140
    in vec3 pos;
    #include <first.glsl>
    in vec2 uv;
    #include "second.glsl"
    out vec2 vertex_uv;
    uniform mat4 camera_transform;
    uniform mat4 model_transform;
    void main()
    {
        vertex_uv = uv;
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
    }
    ''').encode('utf-8')
    with pytest.raises(RuntimeError) as ex:
        output_code = scp(input_code)
    assert str(ex.value) == 'include not allowed'


def test_default_include_windows_line_ending() -> None:
    scp = ShaderCodePreprocessor()
    input_code = dedent('''
    #version 140\r
    in vec3 pos;\r
    #include <first.glsl>\r
    in vec2 uv;\r
    #include "second.glsl"\r
    out vec2 vertex_uv;\r
    uniform mat4 camera_transform;\r
    uniform mat4 model_transform;\r
    void main()\r
    {\r
        vertex_uv = uv;\r
        gl_Position = camera_transform * model_transform * vec4(pos, 1.0);\r
    }\r
    ''').encode('utf-8')
    with pytest.raises(RuntimeError) as ex:
        output_code = scp(input_code)
    assert str(ex.value) == 'include not allowed'
