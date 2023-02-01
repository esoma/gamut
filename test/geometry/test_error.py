
# gamut
from gamut.geometry import DegenerateGeometryError
# pytest
import pytest


def test_degenerate_error_is_value_error():
    assert issubclass(DegenerateGeometryError, ValueError)

@pytest.mark.parametrize("degenerate_form", [None, 1, object()])
@pytest.mark.parametrize("message", ['hello world', 'none'])
def test_degenerate_geometry_error(degenerate_form, message):
    ex = DegenerateGeometryError(degenerate_form, message)
    assert ex.degenerate_form is degenerate_form
    assert str(ex) == message
