
# gamut
from gamut.graphics import JsonFileShaderLoader, JsonShaderLoader
# python
from pathlib import Path
# pytest
import pytest


def test_empty():
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        loader(b'{}')
    assert str(ex.value) == 'no stages defined'


@pytest.mark.parametrize("stage", ['vertex', 'geometry', 'fragment'])
def test_stage_no_code(stage: str) -> None:
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        shader = loader(f'''
        {{
            "{stage}": {{ }}
        }}
        '''.encode('utf-8'))
    assert str(ex.value) == 'stage missing code'


@pytest.mark.parametrize("stage", ['vertex', 'geometry', 'fragment'])
def test_stage_invalid_code_type(stage: str) -> None:
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        shader = loader(f'''
        {{
            "{stage}": {{ "code_type": "not-a-type", "code": "" }}
        }}
        '''.encode('utf-8'))
    assert str(ex.value) == f'unexpected shader code type: {"not-a-type"!r}'


@pytest.mark.parametrize("stage", ['vertex', 'geometry', 'fragment'])
def test_stage_code_not_string(stage: str) -> None:
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        shader = loader(f'''
        {{
            "{stage}": {{ "code": 1 }}
        }}
        '''.encode('utf-8'))
    assert str(ex.value) == f'shader stage code expected to be string, got 1'


def test_inline_shaders() -> None:
    loader = JsonShaderLoader()
    shader = loader(r'''
    {
        "vertex": {
            "code": "#version 140\nin vec4 pos;void main(){ gl_Position = pos; }"
        },
        "geometry": {
            "code_type": "inline",
            "code": "#version 330 core\nlayout(triangles) in;layout(line_strip, max_vertices = 12) out; uniform vec4 g_pos;void main(){ gl_Position = gl_in[0].gl_Position + g_pos; EmitVertex(); EndPrimitive(); }"
        },
        "fragment": {
            "code_type": "inline",
            "code": "#version 140\nuniform vec4 color; out vec4 o_color; void main(){ o_color = color; }"
        }
    }
    '''.encode('utf-8')) # noqa
    assert shader.ignored_attributes == set()
    assert shader.ignored_uniforms == set()
    assert {u.name for u in shader.uniforms} == {"color", "g_pos"}
    assert {a.name for a in shader.attributes} == {"pos"}


@pytest.mark.parametrize("stage", ['vertex', 'geometry', 'fragment'])
def test_external_shader(stage: str) -> None:
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        shader = loader(f'''
        {{
            "{stage}": {{ "code_type": "external", "code": "" }}
        }}
        '''.encode('utf-8'))
    assert str(ex.value) == f'loading external files not allowed'



def test_ignored() -> None:
    loader = JsonShaderLoader()
    shader = loader(r'''
    {
        "ignored_attributes": ["abc"],
        "ignored_uniforms": ["hello", "world"],
        "vertex": {
            "code_type": "inline",
            "code": "#version 140\nin vec4 pos;void main(){ gl_Position = pos; }"
        }
    }
    '''.encode('utf-8')) # noqa
    assert shader.ignored_attributes == {'abc'}
    assert shader.ignored_uniforms == {'hello', 'world'}


def test_defines() -> None:
    loader = JsonShaderLoader()
    shader = loader(r'''
    {
        "defines": {"MACRO": "xxx"},
        "vertex": {
            "code_type": "inline",
            "code": "#version 140\nin vec4 MACRO;void main(){ gl_Position = MACRO; }"
        }
    }
    '''.encode('utf-8')) # noqa
    assert shader.ignored_attributes == set()
    assert shader.ignored_uniforms == set()
    assert {u.name for u in shader.uniforms} == set()
    assert {a.name for a in shader.attributes} == {"xxx"}


def test_include() -> None:
    loader = JsonShaderLoader()
    with pytest.raises(RuntimeError) as ex:
        shader = loader(r'''
        {
            "vertex": {
                "code_type": "inline",
                "code": "#version 140\n#include <something>\nin vec4 pos;void main(){ gl_Position = pos; }"
            }
        }
        '''.encode('utf-8')) # noqa
    assert str(ex.value) == 'loading external files not allowed'


def test_from_file(resources: Path) -> None:
    loader = JsonFileShaderLoader(resources)
    shader = loader.from_file('shader.json')
    assert shader.ignored_attributes == set()
    assert shader.ignored_uniforms == set()
    assert {u.name for u in shader.uniforms} == {"color", "g_pos"}
    assert {a.name for a in shader.attributes} == {"pos"}
