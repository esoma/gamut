
# gamut
from gamut.math import _test_api


def _make_test(attr):
    def _():
        getattr(_test_api, attr)()
    return _

for attr in dir(_test_api):
    if attr.startswith("test_"):
        globals()[attr] = _make_test(attr)
