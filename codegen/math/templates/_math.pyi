
# generated {{ when }} from codegen/math/templates/_math.pyi

__all__ = [
    {% for type in vector_types %}
    '{{ type }}',
    {% endfor %}
]

# python
from typing import Any, final, overload, SupportsFloat, SupportsInt

Number = SupportsFloat | SupportsInt

{% for type in vector_types %}
{% with component_count=int(type[-1]) %}
{% with component_type='float' if type.startswith('F') else ('bool' if type.startswith('B') else 'int') %}
{% with is_unsigned=type.startswith('U') %}

@final
class {{ type }}:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number): ...

{% if component_count == 2 %}
    @overload
    def __init__(self, x: Number, y: Number): ...
{% endif %}
{% if component_count == 3 %}
    @overload
    def __init__(self, x: Number, y: Number, z: Number): ...
{% endif %}
{% if component_count == 4 %}
    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number): ...
{% endif %}

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> {{ component_type }}: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __add__(self, other: Number) -> {{ type }}: ...
    @overload
    def __radd__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __radd__(self, other: Number) -> {{ type }}: ...

    @overload
    def __sub__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __sub__(self, other: Number) -> {{ type }}: ...
    @overload
    def __rsub__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __rsub__(self, other: Number) -> {{ type }}: ...

    @overload
    def __mul__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __mul__(self, other: Number) -> {{ type }}: ...
    @overload
    def __rmul__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __rmul__(self, other: Number) -> {{ type }}: ...

{% if component_type == 'float' %}
    def __matmul__(self, other: {{ type }}) -> {{ type }}: ...
    def __rmatmul__(self, other: {{ type }}) -> {{ type }}: ...

    @overload
    def __mod__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __mod__(self, other: Number) -> {{ type }}: ...
    @overload
    def __rmod__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __rmod__(self, other: Number) -> {{ type }}: ...

    @overload
    def __pow__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __pow__(self, other: Number) -> {{ type }}: ...
    @overload
    def __rpow__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __rpow__(self, other: Number) -> {{ type }}: ...
{% endif %}

{% if component_type != 'bool' %}
    @overload
    def __truediv__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __truediv__(self, other: Number) -> {{ type }}: ...
    @overload
    def __rtruediv__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __rtruediv__(self, other: Number) -> {{ type }}: ...
{% endif %}

{% if is_unsigned %}
    def __neg__(self) -> {{ type }}: ...
{% endif %}

    def __abs__(self) -> {{ type }}: ...
    def __bool__(self) -> bool: ...

{% for attributes in ['xyzw', 'rgba', 'stqp', 'uv'] %}
{% for count in range(1, component_count + 1) %}
{% for prop in itertools.combinations_with_replacement(attributes, count) %}
    @property
    def {{ ''.join(prop) }}(self) -> {% if count > 1 %}tuple[{% for _ in range(count) %}{{ component_type }}, {% endfor %}]{% else %}{{ component_type }}{% endif %}: ...
{% endfor %}
{% endfor %}
{% endfor %}

{% if component_type == 'float' %}
    @property
    def magnitude(self) -> {{ component_type }}: ...

    def cross(self, other: {{ type }}) -> {{ type }}: ...
    def normalize(self) -> {{ component_type }}: ...
    def distance(self, other: {{ type }}) -> {{ component_type }}: ...
{% endif %}

    @staticmethod
    def get_limits(cls) -> tuple[{{ component_type }}, {{ component_type }}]: ...

{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}