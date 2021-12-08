
# python
from dataclasses import dataclass
from os import path
import re
import textwrap
# mypy
import mypy
import mypy.api
# pytest
import pytest

if mypy.__file__.endswith('.py'):
    pytestmark = pytest.mark.skip('mypy is pure python')

mypy_error_pattern = re.compile(r'<string>:(\d+): (.+)')

directory = path.dirname(path.realpath(__file__))

@dataclass
class MypyResult:
    line: int
    text: str


def test_transform_node_children_any() -> None:
    assert run_mypy("""
        from gamut import TransformNode
        from typing import Any
        node: TransformNode[Any] = TransformNode()
        reveal_type(node.children)
    """) == [
        MypyResult(5, 'note: Revealed type is '
                      '"builtins.set['
                            'gamut._transformnode.TransformNode[Any]'
                      ']"'),
    ]


def test_transform_node_children_node() -> None:
    assert run_mypy("""
        from gamut import TransformNode
        class A(TransformNode['A']): ...
        node = A()
        reveal_type(node.children)
    """) == [
        MypyResult(5, 'note: Revealed type is '
                      '"builtins.set[__main__.A*]"'),
    ]


def run_mypy(src: str) -> list[MypyResult]:
    return run_mypy_with_config(
        src,
        path.join(directory, 'mypy-main-plugin.ini')
    )


def run_mypy_with_config(src: str, config_file: str) -> list[MypyResult]:
    report, _, _ = mypy.api.run([
        '--config-file', config_file,
        '-c', textwrap.dedent(src),
        '--show-traceback',
    ])
    errors: list[MypyResult] = []
    for line in report.split('\n'):
        print(line)
        match = mypy_error_pattern.match(line)
        if match:
            errors.append(MypyResult(int(match.group(1)), match.group(2)))
    return errors
