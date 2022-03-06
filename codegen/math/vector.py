
__all__ = ['generate_vector_files']

# gamut
from .template import get_template
# python
from pathlib import Path


def generate_vector_files(build_dir: Path) -> None:
    generate_vector_file(build_dir, 'double', 3, 'DVector3')


def generate_vector_file(
    build_dir: Path,
    c_type: str,
    component_count: int,
    name: str
) -> None:
    template = get_template('vector.hpp')
    with open(build_dir / f'_{name.lower()}.hpp', 'w') as f:
        f.write(template.render(
            name=name,
            component_count=component_count,
            c_type=c_type,
        ))
