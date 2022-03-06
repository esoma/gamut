
__all__ = ['generate_math_files']

# gamut
from .vector import generate_vector_files
# python
from pathlib import Path


def generate_math_files(build_dir: Path) -> None:
    generate_vector_files(build_dir)
