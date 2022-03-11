
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self, all: Number, /): ...

{% if component_count == 2 %}
    @overload
    def __init__(self, x: Number, y: Number, /): ...
{% endif %}
{% if component_count == 3 %}
    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...
{% endif %}
{% if component_count == 4 %}
    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...
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
{% for count in range(1, 5) %}
{% for prop in itertools.combinations_with_replacement(attributes[:component_count], count) %}
    @property
    def {{ ''.join(prop) }}(self) -> {% if count > 1 %}{{ type[:-1] }}{{ count }}{% else %}{{ component_type }}{% endif %}: ...
{% endfor %}
{% endfor %}
{% endfor %}

{% if component_type == 'float' %}
    @property
    def magnitude(self) -> {{ component_type }}: ...

    def cross(self, other: {{ type }}, /) -> {{ type }}: ...
    def normalize(self) -> {{ component_type }}: ...
    def distance(self, other: {{ type }}, /) -> {{ component_type }}: ...
{% endif %}

    @classmethod
    def get_limits(cls) -> tuple[{{ component_type }}, {{ component_type }}]: ...


@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *vectors: {{ type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> {{ type }}: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...


{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}


{% for type in matrix_types %}
{% with row_size=int(type[-3]) %}
{% with column_size=int(type[-1]) %}
{% with component_count=row_size * column_size %}
{% with column_type=type[0] + 'Vector' + str(column_size) %}
{% with row_type=type[0] + 'Vector' + str(row_size) %}

@final
class {{ type }}:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,
        {% for i in range(row_size) %}
            _{{ i }}: {{ column_type }},
        {% endfor %}
        /
    ): ...

    @overload
    def __init__(
        self,
        {% for i in range(component_count) %}
            _{{ i }}: Number,
        {% endfor %}
        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> {{ column_type }}: ...
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

    def __mul__(self, other: Number) -> {{ type }}: ...
    def __rmul__(self, other: Number) -> {{ type }}: ...

{% for c in range(2, 5) %}
{% with right_type=type[0] + 'Matrix' + str(c) + 'x' + str(row_size) %}
{% with result_type=type[0] + 'Matrix' + str(c) + 'x' + str(column_size) %}
    @overload
    def __matmul__(self, other: {{ right_type }}) -> {{ result_type }}: ...
{% endwith %}
{% endwith %}
{% endfor %}
    @overload
    def __matmul__(self, other: {{ row_type }}) -> {{ column_type }}: ...

    def __rmatmul__(self, other: {{ column_type }}) -> {{ row_type }}: ...

{% if row_size == column_size %}
    @overload
{% endif %}
    def __truediv__(self, other: Number) -> {{ type }}: ...
{% if row_size == column_size %}
    @overload
    def __truediv__(self, other: {{ type }}) -> {{ type }}: ...
    @overload
    def __truediv__(self, other: {{ row_type }}) -> {{ row_type }}: ...
    @overload
    def __rtruediv__(self, other: {{ row_type }}) -> {{ row_type }}: ...
    @overload
{% endif %}
    def __rtruediv__(self, other: Number) -> {{ type }}: ...

    def __neg__(self) -> {{ type }}: ...
    def __bool__(self) -> bool: ...

{% if row_size == column_size %}
    def inverse(self) -> {{ type }}: ...
{% endif %}

{% with transpose_type=type[0] + 'Matrix' + str(column_size) + 'x' + str(row_size) %}
    def transpose(self) -> {{ transpose_type }}: ...
{% endwith %}

    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...


@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *matrices: {{ type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> {{ type }}: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}
