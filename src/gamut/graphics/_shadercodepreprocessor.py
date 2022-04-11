
from __future__ import annotations

__all__ = ['ShaderCodePreprocessor']

# python
import re
from typing import Any


class ShaderCodePreprocessor:

    def __call__(
        self,
        code: bytes,
        *,
        defines: dict[str, Any] | None = None
    ) -> bytes:
        code_u = code.decode('utf-8')

        while True:
            include_line = re.search(
                r'^#include\s+((<.+>)|(".+"))$',
                code_u,
                re.MULTILINE
            )
            if include_line is None:
                break
            try:
                include_code = self.include(include_line.group(1)[1:-1])
            except NotImplementedError:
                break
            code_u = (
                code_u[:include_line.span()[0]] +
                include_code.decode('utf-8') +
                code_u[include_line.span()[1]:]
            )

        if defines is None:
            define_code = ''
        else:
            define_code = '\n' + '\n'.join(
                f'#define {key} {value}'
                for key, value in defines.items()
            )

        version_line = re.search(r'^#version.+$', code_u, re.MULTILINE)
        if version_line is None:
            raise RuntimeError('unable to find glsl version')

        code_u = (
            code_u[:version_line.span()[1]] +
            define_code +
            code_u[version_line.span()[1]:]
        )
        return code_u.encode('utf-8')


    def include(self, name: str) -> bytes:
        raise RuntimeError('include not allowed')
