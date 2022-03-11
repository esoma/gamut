
__all__ = ['generate_math_files']

# gamut
from .matrix import generate_matrix_files
from .template import get_template
from .vector import generate_vector_files
# python
from datetime import datetime
from pathlib import Path
from typing import Sequence


def generate_math_files(build_dir: Path) -> None:
    vector_types = list(generate_vector_files(build_dir))
    matrix_types = list(generate_matrix_files(build_dir))
    generate_modulestate_file(build_dir, vector_types + matrix_types)
    generate_math_file(build_dir, vector_types + matrix_types)
    generate_typestubs(build_dir, vector_types, matrix_types)


def generate_modulestate_file(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template('_modulestate.hpp')
    with open(build_dir / f'_modulestate.hpp', 'w') as f:
        f.write(template.render(
            types=types,
            when=datetime.utcnow()
        ))


def generate_math_file(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template('_math.cpp')
    with open(build_dir / f'_math.cpp', 'w') as f:
        f.write(template.render(
            types=types,
            when=datetime.utcnow()
        ))

def generate_typestubs(
    build_dir: Path,
    vector_types: Sequence[str],
    matrix_types: Sequence[str],
) -> None:
    template = get_template('_math.pyi')
    with open(build_dir / f'_math.pyi', 'w') as f:
        f.write(template.render(
            vector_types=vector_types,
            matrix_types=matrix_types,
            when=datetime.utcnow()
        ))