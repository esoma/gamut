
__all__ = ['generate_vector_files']

# gamut
from .template import get_template
# python
from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_vector_files(build_dir: Path) -> Generator[str, None, None]:
    yield generate_vector_file(build_dir, 'float', 2, 'FVector2', 'f')
    yield generate_vector_file(build_dir, 'double', 2, 'DVector2', 'd')
    yield generate_vector_file(build_dir, 'float', 3, 'FVector3', 'f')
    yield generate_vector_file(build_dir, 'double', 3, 'DVector3', 'd')
    yield generate_vector_file(build_dir, 'float', 4, 'FVector4', 'f')
    yield generate_vector_file(build_dir, 'double', 4, 'DVector4', 'd')


def generate_vector_file(
    build_dir: Path,
    c_type: str,
    component_count: int,
    name: str,
    struct_format: str,
) -> str:
    template = get_template('vector.hpp')
    with open(build_dir / f'_{name.lower()}.hpp', 'w') as f:
        f.write(template.render(
            name=name,
            component_count=component_count,
            c_type=c_type,
            struct_format=struct_format,
            when=datetime.utcnow()
        ))
    return name
