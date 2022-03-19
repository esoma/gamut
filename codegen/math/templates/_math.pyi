
# generated {{ when }} from codegen/math/templates/_math.pyi

__all__ = [
    {% for type in vector_types %}
    '{{ type }}',
    {% endfor %}
]

# python
import ctypes
from typing import Any, final, overload, SupportsFloat, SupportsInt

Number = SupportsFloat | SupportsInt

{% for type in vector_types %}
{% with component_count=int(type[-1]) %}
{% with component_type='float' if type.startswith('F') else ('bool' if type.startswith('B') else 'int') %}
{% with is_unsigned=type.startswith('U') %}
{% with ctypes_type={
    "B": 'ctypes.c_bool',
    "D": 'ctypes.c_double',
    "F": 'ctypes.c_float',
    "I8": 'ctypes.c_int8',
    "U8": 'ctypes.c_uint8',
    "I16": 'ctypes.c_int16',
    "U16": 'ctypes.c_uint16',
    "I32": 'ctypes.c_int32',
    "U32": 'ctypes.c_uint32',
    "I64": 'ctypes.c_int64',
    "U64": 'ctypes.c_uint64',
    "I": 'ctypes.c_int',
    "U": 'ctypes.c_uint',
}[type[:type.find('V')]] %}

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
    def __matmul__(self, other: {{ type }}) -> {{ component_type }}: ...
    def __rmatmul__(self, other: {{ type }}) -> {{ component_type }}: ...

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

{% if component_count == 3 %}
    def cross(self, other: {{ type }}, /) -> {{ type }}: ...
    def to_quaternion(self) -> {{ type[0] + 'Quaternion' }}: ...
{% endif %}
    def normalize(self) -> {{ type }}: ...
    def distance(self, other: {{ type }}, /) -> {{ component_type }}: ...
    def lerp(self, other: {{ type }}, x: {{ component_type }}, /) -> {{ type }}: ...
{% endif %}

    def min(self, min: {{ component_type }}) -> {{ type }}: ...
    def max(self, max: {{ component_type }}) -> {{ type }}: ...
    def clamp(self, min: {{ component_type }}, max: {{ component_type }}) -> {{ type }}: ...

    @classmethod
    def get_limits(cls) -> tuple[{{ component_type }}, {{ component_type }}]: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...

    @classmethod
    def get_size(self) -> int: ...

    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...


@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *vectors: {{ type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> {{ type }}: ...
    @overload
    def __getitem__(self, index: slice) -> {{ type }}Array: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...
    @property
    def size(self) -> int: ...
    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

{% endwith %}
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
{% with ctypes_type={
    "D": 'ctypes.c_double',
    "F": 'ctypes.c_float',
}[type[:type.find('M')]] %}

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
{% if row_size == 4 and column_size == 4 %}
    @overload
    def __matmul__(self, other: {{ type[0] }}Vector3) -> {{ type[0] }}Vector3: ...
{% endif %}
    @overload
    def __matmul__(self, other: {{ row_type }}) -> {{ column_type }}: ...

{% if row_size == 4 and column_size == 4 %}
    @overload
    def __rmatmul__(self, other: {{ type[0] }}Vector3) -> {{ type[0] }}Vector3: ...
    @overload
{% endif %}
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

{% if row_size == 4 and column_size == 4 %}
    def rotate(self, angle: float, axis: {{ type[0] }}Vector3, /) -> {{ type }}: ...
    def scale(self, scaling: {{ type[0] }}Vector3, /) -> {{ type }}: ...
    def translate(self, translation: {{ type[0] }}Vector3, /) -> {{ type }}: ...
    @classmethod
    def perspective(cls, fov: float, aspect_ratio: float, near: float, far: float, /) -> {{ type }}: ...
    @classmethod
    def orthographic(cls, left: float, right: float, top: float, bottom: float, near: float, far: float, /) -> {{ type }}: ...
    @classmethod
    def look_at(cls, eye: {{ type[0] }}Vector3, center: {{ type[0] }}Vector3, up: {{ type[0] }}Vector3, /) -> {{ type }}: ...
    def to_matrix3(self) -> {{ type[0] }}Matrix3x3: ...
{% endif %}

    def get_row(self, index: int, /) -> {{ row_type }}: ...

    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...
    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...
    @classmethod
    def get_size(self) -> int: ...
    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *matrices: {{ type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> {{ type }}: ...
    @overload
    def __getitem__(self, index: slice) -> {{ type }}Array: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...
    @property
    def size(self) -> int: ...
    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}


{% for type in quaternion_types %}
{% with vector3_type=type[0] + 'Vector3' %}
{% with vector4_type=type[0] + 'Vector4' %}
{% with ctypes_type={
    "D": 'ctypes.c_double',
    "F": 'ctypes.c_float',
}[type[:type.find('Q')]] %}

@final
class {{ type }}:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, w: Number, /): ...
    @overload
    def __init__(self, w: Number, x: Number, y: Number, z: Number, /): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> float: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    def __add__(self, other: {{ type }}) -> {{ type }}: ...
    def __radd__(self, other: {{ type }}) -> {{ type }}: ...

    def __sub__(self, other: {{ type }}) -> {{ type }}: ...
    def __rsub__(self, other: {{ type }}) -> {{ type }}: ...

    def __mul__(self, other: Number) -> {{ type }}: ...
    def __rmul__(self, other: Number) -> {{ type }}: ...

    @overload
    def __matmul__(self, other: {{ type }}) -> float: ...
    @overload
    def __matmul__(self, other: {{ vector3_type }}) -> {{ vector3_type }}: ...
    @overload
    def __matmul__(self, other: {{ vector4_type }}) -> {{ vector4_type }}: ...

    @overload
    def __rmatmul__(self, other: {{ type }}) -> float: ...
    @overload
    def __rmatmul__(self, other: {{ vector3_type }}) -> {{ vector3_type }}: ...
    @overload
    def __rmatmul__(self, other: {{ vector4_type }}) -> {{ vector4_type }}: ...

    def __truediv__(self, other: Number) -> {{ type }}: ...

    def __neg__(self) -> {{ type }}: ...

    def __bool__(self) -> bool: ...

    @property
    def w(self) -> float: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...

    @property
    def magnitude(self) -> float: ...

    def cross(self, other: {{ type }}, /) -> {{ type }}: ...

    def to_matrix3(self) -> {{ type[0] }}Matrix3x3: ...
    def to_matrix4(self) -> {{ type[0] }}Matrix4x4: ...

    def normalize(self) -> {{ type }}: ...
    def lerp(self, other: {{ type }}, x: float, /) -> {{ type }}: ...

    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...

    @classmethod
    def get_size(self) -> int: ...

    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *vectors: {{ type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> {{ type }}: ...
    @overload
    def __getitem__(self, index: slice) -> {{ type }}Array: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...
    @property
    def size(self) -> int: ...
    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}


{% for type in pod_types %}
{% with pod_type='float' if type.startswith('F') else ('bool' if type.startswith('B') else 'int') %}
{% with ctypes_type={
    "B": 'ctypes.c_bool',
    "D": 'ctypes.c_double',
    "F": 'ctypes.c_float',
    "I8": 'ctypes.c_int8',
    "U8": 'ctypes.c_uint8',
    "I16": 'ctypes.c_int16',
    "U16": 'ctypes.c_uint16',
    "I32": 'ctypes.c_int32',
    "U32": 'ctypes.c_uint32',
    "I64": 'ctypes.c_int64',
    "U64": 'ctypes.c_uint64',
    "I": 'ctypes.c_int',
    "U": 'ctypes.c_uint',
}[type] %}

@final
class {{ type }}Array:

    __slots__ = ['__weakref__']

    def __init__(self, *pods: {{ pod_type }}): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> {{ pod_type }}: ...
    @overload
    def __getitem__(self, index: slice) -> {{ type }}Array: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

    @property
    def pointer(self) -> ctypes.pointer[{{ ctypes_type }}]: ...
    @property
    def size(self) -> int: ...
    @classmethod
    def from_buffer(cls, buffer: Any) -> {{ type }}: ...

{% endwith %}
{% endwith %}
{% endfor %}