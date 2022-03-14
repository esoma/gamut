
__all__ = ['generate_vector_files']

# gamut
from .template import get_template
# python
from datetime import datetime
from pathlib import Path
from typing import Generator, Sequence


def generate_vector_files(build_dir: Path) -> Generator[str, None, None]:
    types: list[tuple[str, int, str]] = []
    b = build_dir
    for i in range(1, 5):
        types.append(generate_vector_file(b,
            'bool', i, f'BVector{i}', '?'))
        types.append(generate_vector_file(b,
            'double', i, f'DVector{i}', 'd'))
        types.append(generate_vector_file(b,
            'float', i, f'FVector{i}', 'f'))
        types.append(generate_vector_file(b,
            'int8_t', i, f'I8Vector{i}', '=b'))
        types.append(generate_vector_file(b,
            'uint8_t', i, f'U8Vector{i}', '=B'))
        types.append(generate_vector_file(b,
            'int16_t', i, f'I16Vector{i}', '=h'))
        types.append(generate_vector_file(b,
            'uint16_t', i, f'U16Vector{i}', '=H'))
        types.append(generate_vector_file(b,
            'int32_t', i, f'I32Vector{i}', '=i'))
        types.append(generate_vector_file(b,
            'uint32_t', i, f'U32Vector{i}', '=I'))
        types.append(generate_vector_file(b,
            'int', i, f'IVector{i}', 'i'))
        types.append(generate_vector_file(b,
            'unsigned int', i, f'UVector{i}', 'I'))
        types.append(generate_vector_file(b,
            'int64_t', i, f'I64Vector{i}', '=q'))
        types.append(generate_vector_file(b,
            'uint64_t', i, f'U64Vector{i}', '=Q'))
    yield from (t[0] for t in types)
    generate_vector_type_file(build_dir, types)


def generate_vector_type_file(
    build_dir: Path,
    types: Sequence[tuple[str, int, str]]
) -> None:
    template = get_template('_vectortype.hpp')
    with open(build_dir / f'_vectortype.hpp', 'w') as f:
        f.write(template.render(
            types=types,
            when=datetime.utcnow()
        ))


def generate_vector_file(
    build_dir: Path,
    c_type: str,
    component_count: int,
    name: str,
    struct_format: str,
) -> str:
    template = get_template('_vector.hpp')
    with open(build_dir / f'_{name.lower()}.hpp', 'w') as f:
        f.write(template.render(
            name=name,
            component_count=component_count,
            c_type=c_type,
            struct_format=struct_format,
            when=datetime.utcnow()
        ))
    return name, component_count, c_type
