
__all__ = ['generate_matrix_files']

# gamut
from .template import get_template
# python
from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_matrix_files(build_dir: Path) -> Generator[str, None, None]:
    b = build_dir
    for r in range(2, 5):
        for c in range(2, 5):
            yield generate_matrix_file(b,
                'double', r, c, f'DMatrix{c}x{r}', 'd', f'DVector{r}'
            )
            yield generate_matrix_file(b,
                'float', r, c, f'FVector{c}x{r}', 'f', f'FVector{r}'
            )

def generate_matrix_file(
    build_dir: Path,
    c_type: str,
    row_count: int,
    column_count: int,
    name: str,
    struct_format: str,
    column_type: str
) -> str:
    template = get_template('_matrix.hpp')
    with open(build_dir / f'_{name.lower()}.hpp', 'w') as f:
        f.write(template.render(
            name=name,
            row_count=row_count,
            column_count=column_count,
            component_count=row_count * column_count,
            c_type=c_type,
            struct_format=struct_format,
            column_type=column_type,
            when=datetime.utcnow()
        ))
    return name
