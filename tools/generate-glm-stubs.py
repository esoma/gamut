
from __future__ import annotations

import ctypes
import glm
import operator as op
import re
import textwrap
from typing import Mapping, Sequence

TYPE_PREFIX_TO_PYTHON_TYPE = {
    'b': bool,
    'd': float,
    'f': float,
    'i': int,
    'u': int,
    '': float,
}

TYPE_PREFIX_PATTERN = '[' + ''.join(TYPE_PREFIX_TO_PYTHON_TYPE) + ']'

VEC_PATTERN = re.compile(f'^({TYPE_PREFIX_PATTERN})?(\d*)(m)?vec(\d)$')
MAT_PATTERN = re.compile(f'^({TYPE_PREFIX_PATTERN})?mat(\d)x(\d)$')
QUAT_PATTERN = re.compile(f'^({TYPE_PREFIX_PATTERN})?\d*quat$')

GLM_TYPES = sorted({
    getattr(glm, name)
    for name in dir(glm)
    if (
        VEC_PATTERN.match(name) or
        MAT_PATTERN.match(name) or
        QUAT_PATTERN.match(name)
    )
}, key=lambda t: t.__name__)

GLM_VECTOR_TYPES = [t for t in GLM_TYPES if 'vec' in t.__name__]
GLM_FLOAT_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
]
GLM_FLOAT3_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
    if VEC_PATTERN.match(t.__name__)[4] == '3'
]
GLM_I_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] == 'i'
    if not VEC_PATTERN.match(t.__name__)[2]
]
GLM_U_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] == 'u'
    if not VEC_PATTERN.match(t.__name__)[2]
]

GLM_MATRIX_TYPES = [t for t in GLM_TYPES if 'mat' in t.__name__]

TYPE_ALIASES = {}
for name in dir(glm):
    alias_obj = getattr(glm, name)
    if not hasattr(alias_obj, "__name__"):
        continue
    if alias_obj.__name__ in dir(ctypes):
        actual_obj = alias_obj
    else:
        try:
            actual_obj = [t for t in GLM_TYPES if t is alias_obj][0]
        except IndexError:
            continue
    if actual_obj.__name__ == name:
        continue
    if actual_obj.__module__ != 'glm':
        actual_name = f'{actual_obj.__module__}.{actual_obj.__name__}'
    else:
        actual_name = actual_obj.__name__
    try:
        aliases = TYPE_ALIASES[actual_name]
    except KeyError:
        aliases = TYPE_ALIASES[actual_name] = []
    aliases.append(name)


ARRAY_CTYPE_TO_PYTHON = {
    'ctypes.c_bool': int,
    'ctypes.c_byte': int,
    'ctypes.c_int8': int,
    'ctypes.c_ubyte': int,
    'ctypes.c_uint8': int,
    'ctypes.c_short': int,
    'ctypes.c_int16': int,
    'ctypes.c_ushort': int,
    'ctypes.c_uint16': int,
    'ctypes.c_int': int,
    'ctypes.c_int32': int,
    'ctypes.c_uint': int,
    'ctypes.c_uint32': int,
    'ctypes.c_long': int,
    'ctypes.c_int64': int,
    'ctypes.c_ulong': int,
    'ctypes.c_uint64': int,
    'ctypes.c_longlong': int,
    'ctypes.c_ulonglong': int,
    'ctypes.c_size_t': int,
    'ctypes.c_ssize_t': int,
    'ctypes.c_float': float,
    'ctypes.c_double': float,
    'ctypes.c_longdouble': float,
}
ARRAY_CTYPES_TYPES_UNION = f'Union[{", ".join(t for t in ARRAY_CTYPE_TO_PYTHON)}]'
GLM_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_TYPES)}]'
VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_TYPES)}]'
FLOAT_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_FLOAT_VECTOR_TYPES)}]'
FLOAT_VECTOR_3_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_FLOAT3_VECTOR_TYPES)}]'
ARRAY_TYPE_TO_PYTHON = {
    **ARRAY_CTYPE_TO_PYTHON,
    **{t.__name__: t.__name__ for t in GLM_TYPES},
}
ARRAY_CTYPE_UNIONS_TO_PYTHON = [
    (
        [c for c, p in ARRAY_CTYPE_TO_PYTHON.items() if p == python_type],
        python_type.__name__
    )
    for python_type in set(ARRAY_CTYPE_TO_PYTHON.values())
]

def get_array_reference_type(glm_type):
    for pattern in [VEC_PATTERN, QUAT_PATTERN]:
        match = pattern.match(glm_type.__name__)
        if match:
            return TYPE_PREFIX_TO_PYTHON_TYPE[match[1] if match[1] else ''].__name__
            break
    else:
        match = MAT_PATTERN.match(glm_type.__name__)
        if not match:
            raise ValueError(glm_type)
        return f'{match[1] if match[1] else ""}vec{match[2]}'


def change_vec_data_type(vec, data_type, remove_m=True):
    if data_type == 'f':
        data_type = ''
    match = VEC_PATTERN.match(vec.__name__)
    if remove_m:
        is_m = ''
    else:
        is_m = match[3] if match[3] else ''
    component_count = match[4]
    return f'{data_type}{is_m}vec{component_count}'


def change_mat_data_type(mat, data_type):
    if data_type == 'f':
        data_type = ''
    match = MAT_PATTERN.match(mat.__name__)
    row_count = match[2]
    column_count = match[3]
    return f'{data_type}mat{row_count}x{column_count}'


def vec_tuple_annotation(components):
    """Generate a Tuple annotation for a vector with the specified number of
    components.
    """
    return f'Tuple[{", ".join("_Number" for i in range(components))}]'


def mat_tuple_annotation(rows, columns):
    """Generate a Tuple annotation for a matrix with the specified rows and
    columns.
    """
    row = f'Tuple[{", ".join("_Number" for i in range(columns))}]'
    return f'Tuple[{", ".join(row for i in range(rows))}]'


def generate_initializer_types(glm_type):
    initializer_types = set()
    for other_type in GLM_TYPES:
        try:
            glm_type(other_type())
        except TypeError:
            continue
        initializer_types.add(other_type.__name__)
    return initializer_types


def stub_operator_map(operator_map, simplify = True):
    s = ''
    for operator, types in operator_map.items():
        union_types = sorted([
            (
                f'Union[{", ".join(ot for ot, rt in types if rt == result_type)}]',
                result_type
            )
            for result_type in set(rt for _, rt in types)
        ]) if simplify else types
        if len(union_types) == 1:
            other_type, result_type = union_types[0]
            s += textwrap.indent(textwrap.dedent(f"""
                def {operator}(self, other: {other_type}) -> {result_type}: ...
            """), '    ')
        elif union_types:
            for other_type, result_type in union_types:
                s += textwrap.indent(textwrap.dedent(f"""
                    @overload
                    def {operator}(self, other: {other_type}) -> {result_type}: ...
                """), '    ').rstrip()
            s += '\n'
    return s


def generate_operator_map(glm_type):
    OPERATORS = [
        op.add, op.iadd,
        op.sub, op.isub,
        op.mul, op.imul,
        op.mod, op.imod,
        op.pow, op.ipow,
        op.floordiv, op.ifloordiv,
        op.truediv, op.itruediv,
        op.matmul, op.imatmul,
    ]

    operator_map = {}
    for operator in OPERATORS:
        operator_types = set()
        for other_type in GLM_TYPES:
            try:
                result_type = type(operator(glm_type(), other_type(1)))
            except TypeError:
                continue
            operator_types.add(
                (other_type.__name__, result_type.__name__)
            )
            # if it supports a vector then it also supports a tuple of the same
            # size made of '_Number'
            other_re_match = VEC_PATTERN.match(other_type.__name__)
            if other_re_match:
                other_components = int(other_re_match[4])
                operator_types.add(
                    (vec_tuple_annotation(other_components), result_type.__name__)
                )
            # if it supports a matrix then it also supports a tuple of the same
            # dimensions made of '_Number'
            other_re_match = MAT_PATTERN.match(other_type.__name__)
            if other_re_match:
                other_row_count = int(other_re_match[2])
                other_column_count = int(other_re_match[3])
                operator_types.add(
                    (mat_tuple_annotation(other_row_count, other_column_count), result_type.__name__)
                )
        # if any other types are supported for the operation, then it should
        # also support '_Number'
        if operator_types:
            operator_types.add(('_Number', glm_type.__name__))
        operator_map[f'__{operator.__name__}__'] = sorted(operator_types)
    # divmod is sort of a special operator
    operator_types = set()
    for other_type in GLM_TYPES:
        try:
            result = divmod(glm_type(), other_type(1))
        except TypeError:
            continue
        if result[0] is NotImplemented:
            continue
        result_type = f'Tuple[{type(result[0]).__name__}, {type(result[1]).__name__}]'
        operator_types.add(
            (other_type.__name__, result_type)
        )
    operator_map[f'__divmod__'] = sorted(operator_types)
    return operator_map


def stub_vec_template(
    name: str,
    is_m: bool,
    component_count: int,
    python_type: str,
    initializer_types: Sequence[str],
    operator_map: Mapping[str, tuple[str, str]],
) -> str:
    component_names = ['x', 'y', 'z', 'w']
    s = textwrap.dedent(f"""
    class {name}:
        {''.join(f'''
        {c}: {python_type}''' for c in component_names[:component_count])}

        @overload
        def __init__(self) -> None: ...{f'''
        @overload
        def __init__(self, x: _Number) -> None: ...''' if component_count != 1 else ''}
        @overload
        def __init__(self, {', '.join(f'{c}: _Number' for c in component_names[:component_count])}) -> None: ...
        @overload
        def __init__(self, x: Union[{', '.join(initializer_types)}]) -> None: ...

        def __len__(self) -> Literal[{component_count}]: ...
        def __getitem__(self, index: int) -> {python_type}: ...
        def __setitem__(self, index: int, value: _Number) -> None: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{python_type}, None, None]: ...

        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...
        def __abs__(self) -> {name}: ...

        def __lt__(self, other: Any) -> bool: ...
        def __le__(self, other: Any) -> bool: ...
        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...
        def __ge__(self, other: Any) -> bool: ...
        def __gt__(self, other: Any) -> bool: ...

        def to_list(self) -> List[{python_type}]: ...
        def to_tuple(self) -> Tuple[{', '.join(python_type for i in range(component_count))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...
    """)
    s += stub_operator_map(operator_map, simplify=not is_m)
    return s


def stub_vec(vec):
    re_match = VEC_PATTERN.match(vec.__name__)
    python_type = TYPE_PREFIX_TO_PYTHON_TYPE[re_match[1] if re_match[1] else '']
    is_m = bool(re_match[3])
    component_count = int(re_match[4])

    initializer_types = generate_initializer_types(vec)
    initializer_types.add(vec_tuple_annotation(4))
    if component_count == 1:
        initializer_types.add(vec_tuple_annotation(1))
    if component_count <= 2:
        initializer_types.add(vec_tuple_annotation(2))
    if component_count <= 3:
        initializer_types.add(vec_tuple_annotation(3))
    initializer_types = sorted(initializer_types)

    operator_map = generate_operator_map(vec)

    return stub_vec_template(
        vec.__name__,
        is_m,
        component_count,
        python_type.__name__,
        initializer_types,
        operator_map
    )


def stub_mat_template(
    name: str,
    data_type_prefix: str,
    row_count: int,
    column_count: int,
    python_type: str,
    initializer_types: Sequence[str],
    operator_map: Mapping[str, tuple[str, str]],
) -> str:
    mvec = f'{data_type_prefix}mvec{column_count}'
    vec = f'{data_type_prefix}vec{column_count}'
    s = textwrap.dedent(f"""
    class {name}:

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, _: _Number, /) -> None: ...
        @overload
        def __init__(self, {', '.join(f'_{c}: _Number' for c in range(row_count * column_count))}, /) -> None: ...
        @overload
        def __init__(self, x: Union[{', '.join(initializer_types)}]) -> None: ...

        def length(self) -> Literal[{row_count}]: ...
        def __len__(self) -> Literal[{row_count}]: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{mvec}, None, None]: ...

        @overload
        def __getitem__(self, index: Tuple[int, int]) -> {python_type}: ...
        @overload
        def __getitem__(self, index: int) -> {mvec}: ...

        @overload
        def __setitem__(self, index: Tuple[int, int], value: _Number) -> None: ...
        @overload
        def __setitem__(self, index: int, value: Union[{vec}, {mvec}]) -> None: ...

        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...

        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...

        def to_list(self) -> List[List[{python_type}]]: ...
        def to_tuple(self) -> Tuple[{', '.join(f'Tuple[{", ".join(python_type for i in range(column_count))}]' for i in range(row_count))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...
    """)
    s += stub_operator_map(operator_map)
    return s


def stub_mat(mat):
    re_match = MAT_PATTERN.match(mat.__name__)
    data_type_prefix = re_match[1] if re_match[1] else ''
    python_type = TYPE_PREFIX_TO_PYTHON_TYPE[data_type_prefix]
    row_count = int(re_match[2])
    column_count = int(re_match[3])

    initializer_types = generate_initializer_types(mat)
    initializer_types |= {
        mat_tuple_annotation(2, 2),
        mat_tuple_annotation(2, 3),
        mat_tuple_annotation(2, 4),
        mat_tuple_annotation(3, 2),
        mat_tuple_annotation(3, 3),
        mat_tuple_annotation(3, 4),
        mat_tuple_annotation(4, 2),
        mat_tuple_annotation(4, 3),
        mat_tuple_annotation(4, 4),
    }
    initializer_types = sorted(initializer_types)

    operator_map = generate_operator_map(mat)

    return stub_mat_template(
        mat.__name__,
        data_type_prefix,
        row_count,
        column_count,
        python_type.__name__,
        initializer_types,
        operator_map
    )


def stub_quat_template(
    name: str,
    python_type: str,
    initializer_types: Sequence[str],
    operator_map: Mapping[str, tuple[str, str]],
) -> str:
    s = textwrap.dedent(f"""
    class {name}:

        x: {python_type}
        y: {python_type}
        w: {python_type}
        z: {python_type}

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, w: _Number, x: _Number, y: _Number, z: _Number) -> None: ...
        @overload
        def __init__(self, x: Union[{', '.join(initializer_types)}]) -> None: ...

        def length(self) -> Literal[4]: ...
        def __len__(self) -> Literal[4]: ...
        def __getitem__(self, index: int) -> {python_type}: ...
        def __setitem__(self, index: int, value: _Number) -> None: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{python_type}, None, None]: ...

        def to_list(self) -> List[{python_type}]: ...
        def to_tuple(self) -> Tuple[{', '.join(python_type for i in range(4))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...

        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...

   """)
    s += stub_operator_map(operator_map)
    return s


def stub_quat(quat):
    re_match = QUAT_PATTERN.match(quat.__name__)
    python_type = TYPE_PREFIX_TO_PYTHON_TYPE[re_match[1] if re_match[1] else '']

    initializer_types = generate_initializer_types(quat)
    initializer_types.add(vec_tuple_annotation(4))
    initializer_types.add(vec_tuple_annotation(3))
    initializer_types = sorted(initializer_types)

    operator_map = generate_operator_map(quat)

    return stub_quat_template(
        quat.__name__,
        python_type.__name__,
        initializer_types,
        operator_map
    )


print(f"""
from typing import Any, Callable, Generator, Generic, List, Literal, NewType, Optional, overload, Iterable, SupportsFloat, SupportsInt, Tuple, Type, TypeVar, Union
import ctypes

_Number = Union[SupportsFloat, SupportsInt]
_GLM_TYPES = {GLM_TYPES_UNION}
_VECTOR = {VECTOR_TYPES_UNION}
_FLOAT_VECTOR = {FLOAT_VECTOR_TYPES_UNION}
_FLOAT_VECTOR_3 = {FLOAT_VECTOR_3_TYPES_UNION}
_QUAT = Union[quat, dquat]

T = TypeVar('T')
_VT = TypeVar('_VT', bound=_VECTOR)
_FVT = TypeVar('_FVT', bound=_FLOAT_VECTOR)
_FV3T = TypeVar('_FV3T', bound=_FLOAT_VECTOR_3)
_QT = TypeVar('_QT', bound=_QUAT)


# func_common

@overload
def abs(x: _Number, /) -> float: ...
@overload
def abs(x: _VT, /) -> _VT: ...

@overload
def ceil(x: _Number, /) -> float: ...
@overload
def ceil(x: _VT, /) -> _VT: ...

@overload
def clamp(x: _Number, min: _Number, max: _Number, /) -> _Number: ...
@overload
def clamp(x: _VT, min: _Number, max: _Number, /) -> _VT: ...
@overload
def clamp(x: _VT, min: _VT, max: _VT, /) -> _VT: ...

@overload
def floatBitsToInt(x: float, /) -> int: ...{"".join(f'''
@overload
def floatBitsToInt(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'i')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def floatBitsToUint(x: float, /) -> int: ...{"".join(f'''
@overload
def floatBitsToUint(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'u')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def floor(x: _Number, /) -> float: ...
@overload
def floor(x: _VT, /) -> _VT: ...

def fma(a: _Number, b: _Number, c: _Number, /) -> float: ...

@overload
def fmax(x: _Number, y: _Number, /) -> float: ...
@overload
def fmax(a: _Number, b: _Number, c: _Number, /) -> float: ...
@overload
def fmax(a: _Number, b: _Number, c: _Number, d: _Number, /) -> float: ...
@overload
def fmax(x: _VT, y: _Number, /) -> _VT: ...
@overload
def fmax(x: _VT, y: _VT, /) -> _VT: ...
@overload
def fmax(a: _VT, b: _VT, c: _VT, /) -> _VT: ...
@overload
def fmax(a: _VT, b: _VT, c: _VT, d: _VT, /) -> _VT: ...

@overload
def fmin(x: _Number, y: _Number, /) -> float: ...
@overload
def fmin(a: _Number, b: _Number, c: _Number, /) -> float: ...
@overload
def fmin(a: _Number, b: _Number, c: _Number, d: _Number, /) -> float: ...
@overload
def fmin(x: _VT, y: _Number, /) -> _VT: ...
@overload
def fmin(x: _VT, y: _VT, /) -> _VT: ...
@overload
def fmin(a: _VT, b: _VT, c: _VT, /) -> _VT: ...
@overload
def fmin(a: _VT, b: _VT, c: _VT, d: _VT, /) -> _VT: ...

@overload
def fract(x: _Number, /) -> float: ...
@overload
def fract(x: _VT, /) -> _VT: ...

@overload
def frexp(x: _Number, /) -> Tuple[float, int]: ...{"".join(f'''
@overload
def frexp(x: {fvec.__name__}, exp: {change_vec_data_type(fvec, 'i')}, /) -> {fvec.__name__}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def intBitsToFloat(x: int, /) -> float: ...{"".join(f'''
@overload
def intBitsToFloat(x: {ivec.__name__}, /) -> {change_vec_data_type(ivec, 'f')}: ...''' for ivec in GLM_I_VECTOR_TYPES)}

@overload
def isinf(x: _Number, /) -> bool: ...{"".join(f'''
@overload
def isinf(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'b')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}
@overload
def isinf(x: _QUAT, /) -> bvec4: ...

@overload
def isnan(x: _Number, /) -> bool: ...{"".join(f'''
@overload
def isnan(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'b')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}
@overload
def isnan(x: _QUAT, /) -> bvec4: ...

@overload
def ldexp(x: _Number, exp: _Number, /) -> float: ...{"".join(f'''
@overload
def ldexp(x: {fvec.__name__}, exp: {change_vec_data_type(fvec, 'i')}, /) -> {fvec.__name__}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def max(x: _Number, y: _Number, /) -> float: ...
@overload
def max(a: _Number, b: _Number, c: _Number, /) -> float: ...
@overload
def max(a: _Number, b: _Number, c: _Number, d: _Number, /) -> float: ...
@overload
def max(x: _VT, y: _Number, /) -> _VT: ...
@overload
def max(x: _VT, y: _VT, /) -> _VT: ...
@overload
def max(a: _VT, b: _VT, c: _VT, /) -> _VT: ...
@overload
def max(a: _VT, b: _VT, c: _VT, d: _VT, /) -> _VT: ...
@overload
def max(_: Iterable[T], /) -> T: ...

@overload
def min(x: _Number, y: _Number, /) -> float: ...
@overload
def min(a: _Number, b: _Number, c: _Number, /) -> float: ...
@overload
def min(a: _Number, b: _Number, c: _Number, d: _Number, /) -> float: ...
@overload
def min(x: _VT, y: _Number, /) -> _VT: ...
@overload
def min(x: _VT, y: _VT, /) -> _VT: ...
@overload
def min(a: _VT, b: _VT, c: _VT, /) -> _VT: ...
@overload
def min(a: _VT, b: _VT, c: _VT, d: _VT, /) -> _VT: ...
@overload
def min(_: Iterable[T], /) -> T: ...

@overload
def mix(x: _Number, y: _Number, a: _Number, /) -> float: ...{"".join(f'''
@overload
def mix(x: {vec.__name__}, y: {vec.__name__}, a: Union[{change_vec_data_type(vec, 'f')}, {change_vec_data_type(vec, 'b')}], /) -> {vec.__name__}: ...''' for vec in GLM_VECTOR_TYPES)}{"".join(f'''
@overload
def mix(x: {mat.__name__}, y: {mat.__name__}, a: Union[{change_mat_data_type(mat, 'f')}, _Number], /) -> {mat.__name__}: ...''' for mat in GLM_MATRIX_TYPES)}
@overload
def mix(x: _QT, y: _QT, a: _Number, /) -> _QT: ...

@overload
def modf(x: _Number, /) -> Tuple[float, float]: ...
@overload
def modf(x: _FVT, i: _FVT, /) -> _FVT: ...

@overload
def round(x: _Number, /) -> float: ...
@overload
def round(x: _FVT, i: _FVT, /) -> _FVT: ...

@overload
def roundEven(x: _Number, /) -> float: ...
@overload
def roundEven(x: _FVT, i: _FVT, /) -> _FVT: ...

@overload
def sign(x: _Number, /) -> float: ...
@overload
def sign(x: _FVT, i: _FVT, /) -> _FVT: ...

@overload
def smoothstep(edge0: _Number, edge1: _Number, x: _Number, /) -> float: ...
@overload
def smoothstep(edge0: _Number, edge1: _Number, x: _FVT, /) -> _FVT: ...
@overload
def smoothstep(edge0: _FVT, edge1: _FVT, x: _FVT, /) -> _FVT: ...

@overload
def step(edge: _Number, x: _Number, /) -> float: ...
@overload
def step(edge: _Number, x: _VT, /) -> _VT: ...
@overload
def step(edge: _VT, x: _VT, /) -> _VT: ...

@overload
def trunc(x: _Number, /) -> float: ...
@overload
def trunc(x: _FVT, /) -> _FVT: ...

@overload
def uintBitsToFloat(x: int, /) -> float: ...{"".join(f'''
@overload
def uintBitsToFloat(x: {uvec.__name__}, /) -> {change_vec_data_type(uvec, 'f')}: ...''' for uvec in GLM_U_VECTOR_TYPES)}


# func_exponential

@overload
def exp(x: _Number, /) -> float: ...
@overload
def exp(x: _FVT, /) -> _FVT: ...
@overload
def exp(x: _QT, /) -> QT: ...

@overload
def exp2(x: _Number, /) -> float: ...
@overload
def exp2(x: _FVT, /) -> _FVT: ...

@overload
def inversesqrt(x: _Number, /) -> float: ...
@overload
def inversesqrt(x: _FVT, /) -> _FVT: ...

@overload
def log(x: _Number, /) -> float: ...
@overload
def log(x: _FVT, /) -> _FVT: ...
@overload
def log(x: _QT, /) -> _QT: ...

@overload
def log2(x: _Number, /) -> float: ...
@overload
def log2(x: _FVT, /) -> _FVT: ...

@overload
def pow(base: _Number, exponent: _Number, /) -> float: ...
@overload
def pow(base: _FVT, exponent: _FVT, /) -> _FVT: ...
@overload
def pow(base: _QT, exponent: _QT, /) -> _QT: ...

@overload
def sqrt(x: _Number, /) -> float: ...
@overload
def sqrt(x: _FVT, /) -> _FVT: ...
@overload
def sqrt(x: _QT, /) -> _QT: ...


# func_geometric

@overload
def cross(x: _FV3T, y: _FV3T, /) -> _FV3T: ...
@overload
def cross(x: _QT, y: _QT, /) -> _QT: ...

""")
print(f"""
_ARRAY_CTYPES = {ARRAY_CTYPES_TYPES_UNION}
_ARRAY_TYPES = Union[_ARRAY_CTYPES, _GLM_TYPES]

_AT = TypeVar('_AT', bound=_ARRAY_TYPES)
_AT2 = TypeVar('_AT2', bound=_ARRAY_TYPES)
_GT = TypeVar('_GT', bound=_GLM_TYPES)
_ACT = TypeVar('_ACT', bound=_ARRAY_CTYPES)
class array(Generic[_AT]):

    nbytes: int
    typecode: str
    element_type: Type[_AT]
    itemsize: int
    dt_size: int
    address: int
    length: int
    readonly: bool
    reference: Union[_ARRAY_TYPES, array]

    @property
    def ptr(self) -> ctypes.c_void_p: ...

    # todo: can make this more precise by overloading on `self: array[...]`
    @property
    def dtype(self) -> str: ...

    # todo: can make this more precise by overloading on `self: array[...]`
    @property
    def ctype(self) -> _ARRAY_CTYPES: ...

    @overload
    def __init__(self, _1: _AT, /, *_: _AT) -> None: ...
    @overload
    def __init__(self, _: array[_AT], /) -> None: ...
    @overload
    def __init__(self, _: Iterable[_AT], /) -> None: ...

    def __len__(self) -> int: ...
    def __contains__(self, value: Any) -> bool: ...
    {"".join(f'''
    @overload
    def __iter__(self: Union[{", ".join(f'array[{at}]' for at in array_types)}]) -> Generator[{output_type}, None, None]: ...''' for array_types, output_type in ARRAY_CTYPE_UNIONS_TO_PYTHON)}
    @overload
    def __iter__(self: array[_GT]) -> Generator[_GT, None, None]: ...
    {"".join(f'''
    @overload
    def __getitem__(self: Union[{", ".join(f'array[{at}]' for at in array_types)}], index: int) -> {output_type}: ...''' for array_types, output_type in ARRAY_CTYPE_UNIONS_TO_PYTHON)}
    @overload
    def __getitem__(self: array[_GT], index: int) -> _GT: ...
    @overload
    def __getitem__(self, index: slice) -> array[_AT]: ...
    {"".join(f'''
    @overload
    def __setitem__(self: Union[{", ".join(f'array[{at}]' for at in array_types)}], index: int, value: {input_type}) -> None: ...''' for array_types, input_type in ARRAY_CTYPE_UNIONS_TO_PYTHON)}
    @overload
    def __setitem__(self: array[_GT], index: int, value: _AT) -> None: ...
    @overload
    def __setitem__(self, index: slice, value: array[_AT]) -> None: ...

    @staticmethod
    def from_bytes(bytes: bytes, type: Type[_AT], /) -> array[_AT]: ...
    @staticmethod
    def from_numbers(type: Type[_ACT], /, *numbers: _Number) -> array[_ACT]: ...
    @staticmethod
    def zeros(type: Type[_AT], length: int, /) -> array[_AT]: ...

    def to_bytes(self) -> bytes: ...
    {"".join(f'''
    @overload
    def to_list(self: Union[{", ".join(f'array[{at}]' for at in array_types)}]) -> List[{output_type}]: ...''' for array_types, output_type in ARRAY_CTYPE_UNIONS_TO_PYTHON)}
    @overload
    def to_list(self: array[_GT]) -> List[_GT]: ...
    {"".join(f'''
    @overload
    def to_tuple(self: Union[{", ".join(f'array[{at}]' for at in array_types)}]) -> Tuple[{output_type}]: ...''' for array_types, output_type in ARRAY_CTYPE_UNIONS_TO_PYTHON)}
    @overload
    def to_tuple(self: array[_GT]) -> Tuple[_GT]: ...

    # todo: can make this more precise by overloading on `self: array[...]`
    def split_components(self) -> Tuple[array[Any]]: ...

    def reduce(self, func: Callable[[_AT, _AT], _AT], init: Optional[_AT] = None, /) -> _AT: ...
    def filter(self, _: Callable[[_AT], Any], /) -> array[_AT]: ...
    def map(self, _: Callable[[_AT], _AT2], /) -> array[_AT2]: ...
    def sort(self, _: Callable[[_AT], SupportsInt], /) -> array[_AT]: ...
    def concat(self, other: array[_AT], /) -> array[_AT]: ...
    def iconcat(self, other: array[_AT], /) -> None: ...
    def repeat(self, count: int, /) -> array[_AT]: ...
    def irepeat(self, count: int, /) -> None: ...

    @overload
    @staticmethod
    def as_reference(array: array[_AT2], /) -> array[_AT2]: ...
    @overload
    @staticmethod
    def as_reference(obj: _GT, /) -> array[_GT]: ...

    def reinterpret_cast(self, type: Type[_AT2], /) -> array[_AT2]: ...

    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    {"".join(f'''
    def __{op}__(self, other: Union[_Number, _AT, array[_AT]]) -> array[_AT]: ...
    def __i{op}__(self, other: Union[_Number, _AT, array[_AT]]) -> array[_AT]: ...''' for op in ('add', 'sub', 'mul', 'mod', 'pow', 'lshift', 'rshift', 'and', 'xor', 'or', 'truediv'))}

    def __neg__(self) -> array[_AT]: ...
    def __pos__(self) -> array[_AT]: ...
    def __abs__(self) -> array[_AT]: ...
    def __inv__(self) -> array[_AT]: ...
""")
for glm_type in GLM_TYPES:
    if 'vec' in glm_type.__name__:
        print(stub_vec(glm_type))
    elif 'mat' in glm_type.__name__:
        print(stub_mat(glm_type))
    elif 'quat' in glm_type.__name__:
        print(stub_quat(glm_type))
for type_name, aliases in TYPE_ALIASES.items():
    print(' = '.join((*aliases, type_name)))