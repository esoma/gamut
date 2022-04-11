
from __future__ import annotations

__all__ = ['JsonShaderLoader', 'JsonFileShaderLoader']

# gamut
from ._shader import Shader
from ._shadercodepreprocessor import ShaderCodePreprocessor
# python
import json
from pathlib import Path
from typing import Callable


class JsonShaderLoader:

    def __init__(self) -> None:
        self._preprocessor = JsonShaderCodePreprocessor(self._include_callback)

    def __call__(self, raw_data: bytes) -> Shader:
        data = json.loads(raw_data.decode('utf-8'))
        defines = data.get("defines")
        ignored_attributes = set(data.get("ignored_attributes", []))
        ignored_uniforms = set(data.get("ignored_uniforms", []))

        stages: dict[str, bytes] = {}
        for stage_name in ['vertex', 'geometry', 'fragment']:
            try:
                stage_data = data[stage_name]
            except KeyError:
                continue
            stages[stage_name] = self._parse_stage(stage_data, defines)
        if not stages:
            raise RuntimeError('no stages defined')

        return Shader(
            ignored_attributes=ignored_attributes,
            ignored_uniforms=ignored_uniforms,
            **stages
        )

    def _include_callback(self, name: str) -> bytes:
        return self.load(name)

    def _parse_stage(
        self,
        stage_data: dict[str, Any],
        defines: dict[str, Any] | None
    ) -> bytes:
        code_type = stage_data.get("code_type", 'inline')
        if code_type not in {'inline', 'external'}:
            raise RuntimeError(f'unexpected shader code type: {code_type!r}')

        try:
            code = stage_data["code"]
        except KeyError:
            raise RuntimeError('stage missing code')
        if not isinstance(code, str):
            raise RuntimeError(
                f'shader stage code expected to be string, got {code!r}'
            )

        if code_type == 'external':
            code = self.load(code)
        else:
            code = code.encode('utf-8')

        code = self._preprocessor(code, defines=defines)
        return code

    def load(self, name: str) -> bytes:
        raise RuntimeError('loading external files not allowed')


class JsonShaderCodePreprocessor(ShaderCodePreprocessor):

    def __init__(self, include_callback: Callable[[str], bytes]):
        self._include_callback = include_callback

    def include(self, name: str) -> bytes:
        return self._include_callback(name)


class JsonFileShaderLoader(JsonShaderLoader):

    def __init__(self, base_directory: Path):
        super().__init__()
        self.base_directory = Path(base_directory)

    def from_file(self, path: Path) -> Shader:
        with open(self.base_directory / path, 'rb') as f:
            raw_data = f.read()
        return self(raw_data)

    def load(self, name: str) -> bytes:
        with open(self.base_directory / name, 'rb') as f:
            return f.read()
