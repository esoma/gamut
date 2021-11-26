
# gamut
from gamut.text import character_normally_rendered
# pytest
import pytest


@pytest.mark.parametrize("character, result", [
    ('\n', False), ('\t', False), ('\r', False),
    ('\u2028', False), ('\u2029', False),
    ('a', True), ('A', True), ('食', True),
])
def test_character_normally_rendered(
    character: str,
    result: bool
) -> None:
    assert character_normally_rendered(character) == result


def test_character_normally_rendered_too_many() -> None:
    with pytest.raises(TypeError) as excinfo:
        character_normally_rendered('ab')
