
__all__ = ['generate_math_files']

# gamut
from .template import get_template
from .vector import generate_vector_files
# python
from datetime import datetime
from pathlib import Path
from typing import Sequence


def generate_math_files(build_dir: Path) -> None:
    vector_types = list(generate_vector_files(build_dir))
    generate_math_file(build_dir, vector_types)


def generate_math_file(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template('math.cpp')
    with open(build_dir / f'_math.cpp', 'w') as f:
        f.write(template.render(
            types=types,
            when=datetime.utcnow()
        ))
