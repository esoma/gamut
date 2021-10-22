
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
GLM_VECTOR_1_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[4] == '1'
]
GLM_VECTOR_2_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[4] == '2'
]
GLM_VECTOR_3_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[4] == '3'
]
GLM_VECTOR_4_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[4] == '4'
]
GLM_BOOL_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] == 'b'
]
GLM_FLOAT_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
]
GLM_F_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in (None, 'f')
]
GLM_D_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] == 'd'
]
GLM_FLOAT3_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
    if VEC_PATTERN.match(t.__name__)[4] == '3'
]
GLM_INT_VECTOR_TYPES = [
    t for t in GLM_TYPES
    if VEC_PATTERN.match(t.__name__)
    if VEC_PATTERN.match(t.__name__)[1] in ('i', 'u')
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
GLM_MAT_2_N_TYPES = [
    t for t in GLM_TYPES
    if MAT_PATTERN.match(t.__name__)
    if MAT_PATTERN.match(t.__name__)[2] == '2'
]
GLM_MAT_3_N_TYPES = [
    t for t in GLM_TYPES
    if MAT_PATTERN.match(t.__name__)
    if MAT_PATTERN.match(t.__name__)[2] == '3'
]
GLM_MAT_4_N_TYPES = [
    t for t in GLM_TYPES
    if MAT_PATTERN.match(t.__name__)
    if MAT_PATTERN.match(t.__name__)[2] == '4'
]
GLM_FLOAT_MATRIX_TYPES = [
    t for t in GLM_TYPES
    if MAT_PATTERN.match(t.__name__)
    if MAT_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
]
GLM_SQUARE_FLOAT_MATRIX_TYPES = [
    t for t in GLM_TYPES
    if MAT_PATTERN.match(t.__name__)
    if MAT_PATTERN.match(t.__name__)[1] in (None, 'f', 'd')
    if MAT_PATTERN.match(t.__name__)[2] == MAT_PATTERN.match(t.__name__)[3]
]

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
GLM_CTYPES_TYPES_UNION = f'Union[{", ".join(t for t in ARRAY_CTYPE_TO_PYTHON)}]'
GLM_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_TYPES)}]'
VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_TYPES)}]'
VECTOR_1_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_1_TYPES)}]'
VECTOR_2_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_2_TYPES)}]'
VECTOR_3_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_3_TYPES)}]'
VECTOR_4_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_VECTOR_4_TYPES)}]'
FLOAT_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_FLOAT_VECTOR_TYPES)}]'
FLOAT_VECTOR_3_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_FLOAT3_VECTOR_TYPES)}]'
INT_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_INT_VECTOR_TYPES)}]'
BOOL_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_BOOL_VECTOR_TYPES)}]'
I_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_I_VECTOR_TYPES)}]'
U_VECTOR_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_U_VECTOR_TYPES)}]'
MATRIX_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_MATRIX_TYPES)}]'
FLOAT_MATRIX_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_FLOAT_MATRIX_TYPES)}]'
SQUARE_FLOAT_MATRIX_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_SQUARE_FLOAT_MATRIX_TYPES)}]'
MAT_2_N_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_MAT_2_N_TYPES)}]'
MAT_3_N_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_MAT_3_N_TYPES)}]'
MAT_4_N_TYPES_UNION = f'Union[{", ".join(t.__name__ for t in GLM_MAT_4_N_TYPES)}]'

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


def transpose_mat_type(mat):
    match = MAT_PATTERN.match(mat.__name__)
    data_type = match[1] if match[1] else ''
    row_count = match[2]
    column_count = match[3]
    return f'{data_type}mat{column_count}x{row_count}'


def mat_column_type(mat):
    match = MAT_PATTERN.match(mat.__name__)
    data_type = match[1] if match[1] else ''
    column_count = match[3]
    return f'{data_type}vec{column_count}'


def mat_row_type(mat):
    match = MAT_PATTERN.match(mat.__name__)
    data_type = match[1] if match[1] else ''
    row_count = match[2]
    return f'{data_type}vec{row_count}'


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
_CTYPES = {GLM_CTYPES_TYPES_UNION}
_GLM_TYPES = {GLM_TYPES_UNION}
_VECTOR = {VECTOR_TYPES_UNION}
_VECTOR_1 = {VECTOR_1_TYPES_UNION}
_VECTOR_2 = {VECTOR_2_TYPES_UNION}
_VECTOR_3 = {VECTOR_3_TYPES_UNION}
_VECTOR_4 = {VECTOR_4_TYPES_UNION}
_FLOAT_VECTOR = {FLOAT_VECTOR_TYPES_UNION}
_FLOAT_VECTOR_3 = {FLOAT_VECTOR_3_TYPES_UNION}
_BOOL_VECTOR = {BOOL_VECTOR_TYPES_UNION}
_INT_VECTOR = {INT_VECTOR_TYPES_UNION}
_I_VECTOR = {I_VECTOR_TYPES_UNION}
_U_VECTOR = {U_VECTOR_TYPES_UNION}
_QUAT = Union[quat, dquat]
_MATRIX = {MATRIX_TYPES_UNION}
_FLOAT_MATRIX = {FLOAT_MATRIX_TYPES_UNION}
_SQUARE_FLOAT_MATRIX = {SQUARE_FLOAT_MATRIX_TYPES_UNION}
_MAT_2_N = {MAT_2_N_TYPES_UNION}
_MAT_3_N = {MAT_3_N_TYPES_UNION}
_MAT_4_N = {MAT_4_N_TYPES_UNION}


T = TypeVar('T')
_VT = TypeVar('_VT', bound=_VECTOR)
_V1T = TypeVar('_V1T', bound=_VECTOR_1)
_V2T = TypeVar('_V2T', bound=_VECTOR_2)
_V3T = TypeVar('_V3T', bound=_VECTOR_3)
_V4T = TypeVar('_V4T', bound=_VECTOR_4)
_FVT = TypeVar('_FVT', bound=_FLOAT_VECTOR)
_FV3T = TypeVar('_FV3T', bound=_FLOAT_VECTOR_3)
_IVT = TypeVar('_IVT', bound=_INT_VECTOR)
_iVT = TypeVar('_iVT', bound=_I_VECTOR)
_uVT = TypeVar('_uVT', bound=_U_VECTOR)
_QT = TypeVar('_QT', bound=_QUAT)
_MT = TypeVar('_MT', bound=_MATRIX)
_FMT = TypeVar('_FMT', bound=_FLOAT_MATRIX)
_SFMT = TypeVar('_SFMT', bound=_SQUARE_FLOAT_MATRIX)
_M2NT = TypeVar('_M2NT', bound=_MAT_2_N)
_M3NT = TypeVar('_M3NT', bound=_MAT_3_N)
_M4NT = TypeVar('_M4NT', bound=_MAT_4_N)


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
def exp(x: _QT, /) -> _QT: ...

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

@overload
def distance(p0: _Number, p1: _Number, /) -> float: ...
@overload
def distance(p0: _FVT, p1: _FVT, /) -> _FVT: ...

@overload
def dot(x: _Number, y: _Number, /) -> float: ...
@overload
def dot(x: _FVT, y: _FVT, /) -> float: ...
@overload
def dot(x: _QT, y: _QT, /) -> float: ...

@overload
def faceforward(N: _Number, I: _Number, Nref: float, /) -> float: ...
@overload
def faceforward(N: _FVT, I: _FVT, Nref: _FVT, /) -> _FVT: ...

@overload
def length(x: _Number, /) -> float: ...
@overload
def length(x: _FVT, /) -> float: ...
@overload
def length(x: _QT, /) -> float: ...

@overload
def normalize(x: _FVT, /) -> _FVT: ...
@overload
def normalize(x: _QT, /) -> _QT: ...

@overload
def reflect(I: _Number, N: _Number, /) -> float: ...
@overload
def reflect(I: _FVT, N: _FVT, /) -> _FVT: ...

@overload
def refract(I: _Number, N: _Number, eta: float, /) -> float: ...
@overload
def refract(I: _FVT, N: _FVT, eta: float, /) -> _FVT: ...


# func_integer

@overload
def bitCount(v: int, /) -> int: ...{"".join(f'''
@overload
def bitCount(v: {ivec.__name__}, /) -> {change_vec_data_type(ivec, 'i')}: ...''' for ivec in GLM_INT_VECTOR_TYPES)}

@overload
def bitfieldExtract(value: int, offset: int, bits: int, /) -> int: ...
@overload
def bitfieldExtract(value: _IVT, offset: int, bits: int, /) -> _IVT: ...

@overload
def bitfieldInsert(base: int, insert: int, offset: int, bits: int, /) -> int: ...
@overload
def bitfieldInsert(base: _IVT, insert: _IVT, offset: int, bits: int, /) -> _IVT: ...

@overload
def bitfieldReverse(value: int, /) -> int: ...
@overload
def bitfieldReverse(value: _IVT, /) -> _IVT: ...

@overload
def findLSB(value: int, /) -> int: ...
@overload
def findLSB(value: _IVT, /) -> _IVT: ...

@overload
def findMSB(value: int, /) -> int: ...
@overload
def findMSB(value: _IVT, /) -> _IVT: ...

def imulExtended(x: _iVT, y: _iVT, msb: _iVT, lsb: _iVT, /) -> None: ...

def uaddCarry(x: _uVT, y: _uVT, carry: _uVT, /) -> _uVT: ...

def umulExtended(x: _uVT, y: _uVT, msb: _uVT, lsb: _uVT, /) -> None: ...

def usubBorrow(x: _uVT, y: _uVT, borrow: _uVT, /) -> _uVT: ...


# func_matrix

def determinant(m: _SQUARE_FLOAT_MATRIX, /) -> float: ...

@overload
def inverse(m: _SFMT, /) -> _SFMT: ...
@overload
def inverse(q: _QT, /) -> _QT: ...

def matrixCompMult(x: _FMT, y: _FMT) -> _FMT: ...
{"".join(f'''
@overload
def outerProduct(c: {data_type}vec{c}, r: {data_type}vec{r}, /) -> {data_type}mat{r}x{c}: ...''' for data_type in ['', 'd'] for c in range(2, 5) for r in range(2, 5))}
{"".join(f'''
@overload
def transpose(x: {mat.__name__}, /) -> {transpose_mat_type(mat)}: ...''' for mat in GLM_MATRIX_TYPES)}


# func_packing

def packDouble2x32(v: uvec2, /) -> float: ...

def packHalf2x16(v: vec2, /) -> int: ...

def packSnorm2x16(v: vec2, /) -> int: ...

def packSnorm4x8(v: vec4, /) -> int: ...

def packUnorm2x16(v: vec2, /) -> int: ...

def packUnorm4x8(v: vec4, /) -> int: ...

def unpackDouble2x32(v: float, /) -> uvec2: ...

def unpackHalf2x16(v: int, /) -> vec2: ...

def unpackSnorm2x16(p: int, /) -> vec2: ...

def unpackSnorm4x8(p: int, /) -> vec4: ...

def unpackUnorm2x16(p: int, /) -> vec2: ...

def unpackUnorm4x8(p: int, /) -> vec4: ...


# func_trigonometric

@overload
def acos(x: _Number, /) -> float: ...
@overload
def acos(x: _FVT, /) -> _FVT: ...

@overload
def acosh(x: _Number, /) -> float: ...
@overload
def acosh(x: _FVT, /) -> _FVT: ...

@overload
def asin(x: _Number, /) -> float: ...
@overload
def asin(x: _FVT, /) -> _FVT: ...

@overload
def asinh(x: _Number, /) -> float: ...
@overload
def asinh(x: _FVT, /) -> _FVT: ...

@overload
def atan(y_over_x: _Number, /) -> float: ...
@overload
def atan(y_over_x: _FVT, /) -> _FVT: ...
@overload
def atan(y: _Number, x: _Number, /) -> float: ...
@overload
def atan(y: _FVT, x: _FVT, /) -> _FVT: ...

@overload
def atanh(x: _Number, /) -> float: ...
@overload
def atanh(x: _FVT, /) -> _FVT: ...

@overload
def cos(angle: _Number, /) -> float: ...
@overload
def cos(angle: _FVT, /) -> _FVT: ...

@overload
def cosh(angle: _Number, /) -> float: ...
@overload
def cosh(angle: _FVT, /) -> _FVT: ...

@overload
def degrees(angle: _Number, /) -> float: ...
@overload
def degrees(angle: _FVT, /) -> _FVT: ...

@overload
def radians(angle: _Number, /) -> float: ...
@overload
def radians(angle: _FVT, /) -> _FVT: ...

@overload
def sin(x: _Number, /) -> float: ...
@overload
def sin(x: _FVT, /) -> _FVT: ...

@overload
def sinh(x: _Number, /) -> float: ...
@overload
def sinh(x: _FVT, /) -> _FVT: ...

@overload
def tan(x: _Number, /) -> float: ...
@overload
def tan(x: _FVT, /) -> _FVT: ...

@overload
def tanh(x: _Number, /) -> float: ...
@overload
def tanh(x: _FVT, /) -> _FVT: ...


# func_vector_relational

def all(v: _BOOL_VECTOR, /) -> bool: ...

def any(v: _BOOL_VECTOR, /) -> bool: ...

@overload
def equal(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def equal(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def equal(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def equal(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def equal(x: _QT, y: _QT, /) -> bvec4: ...
@overload
def equal(x: _M2NT, y: _M2NT, /) -> bvec2: ...
@overload
def equal(x: _M3NT, y: _M3NT, /) -> bvec3: ...
@overload
def equal(x: _M4NT, y: _M4NT, /) -> bvec4: ...
@overload
def equal(x: _Number, y: _Number, ULPs: int, /) -> int: ...
@overload
def equal(x: _V1T, y: _V1T, ULPs: _Number, /) -> bvec1: ...
@overload
def equal(x: _V2T, y: _V2T, ULPs: _Number, /) -> bvec2: ...
@overload
def equal(x: _V3T, y: _V3T, ULPs: _Number, /) -> bvec3: ...
@overload
def equal(x: _V4T, y: _V4T, ULPs: _Number, /) -> bvec4: ...
@overload
def equal(x: _M2NT, y: _M2NT, ULPs: _Number, /) -> bvec2: ...
@overload
def equal(x: _M3NT, y: _M3NT, ULPs: _Number, /) -> bvec3: ...
@overload
def equal(x: _M4NT, y: _M4NT, ULPs: _Number, /) -> bvec4: ...
@overload
def equal(x: _V1T, y: _V1T, ULPs: ivec1, /) -> bvec1: ...
@overload
def equal(x: _V2T, y: _V2T, ULPs: ivec2, /) -> bvec2: ...
@overload
def equal(x: _V3T, y: _V3T, ULPs: ivec3, /) -> bvec3: ...
@overload
def equal(x: _V4T, y: _V4T, ULPs: ivec4, /) -> bvec4: ...
@overload
def equal(x: _M2NT, y: _M2NT, ULPs: ivec2, /) -> bvec2: ...
@overload
def equal(x: _M3NT, y: _M3NT, ULPs: ivec3, /) -> bvec3: ...
@overload
def equal(x: _M4NT, y: _M4NT, ULPs: ivec4, /) -> bvec4: ...
@overload
def equal(x: _V1T, y: _V1T, epsilon: vec1, /) -> bvec1: ...
@overload
def equal(x: _V2T, y: _V2T, epsilon: vec2, /) -> bvec2: ...
@overload
def equal(x: _V3T, y: _V3T, epsilon: vec3, /) -> bvec3: ...
@overload
def equal(x: _V4T, y: _V4T, epsilon: vec4, /) -> bvec4: ...
@overload
def equal(x: _M2NT, y: _M2NT, epsilon: vec2, /) -> bvec2: ...
@overload
def equal(x: _M3NT, y: _M3NT, epsilon: vec3, /) -> bvec3: ...
@overload
def equal(x: _M4NT, y: _M4NT, epsilon: vec4, /) -> bvec4: ...

@overload
def greaterThan(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def greaterThan(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def greaterThan(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def greaterThan(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def greaterThan(x: _QT, y: _QT, /) -> bvec4: ...

@overload
def greaterThanEqual(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def greaterThanEqual(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def greaterThanEqual(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def greaterThanEqual(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def greaterThanEqual(x: _QT, y: _QT, /) -> bvec4: ...

@overload
def lessThan(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def lessThan(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def lessThan(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def lessThan(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def lessThan(x: _QT, y: _QT, /) -> bvec4: ...

@overload
def lessThanEqual(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def lessThanEqual(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def lessThanEqual(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def lessThanEqual(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def lessThanEqual(x: _QT, y: _QT, /) -> bvec4: ...

@overload
def notEqual(x: _V1T, y: _V1T, /) -> bvec1: ...
@overload
def notEqual(x: _V2T, y: _V2T, /) -> bvec2: ...
@overload
def notEqual(x: _V3T, y: _V3T, /) -> bvec3: ...
@overload
def notEqual(x: _V4T, y: _V4T, /) -> bvec4: ...
@overload
def notEqual(x: _QT, y: _QT, /) -> bvec4: ...

def not_(v: _BOOL_VECTOR, /) -> bool: ...


# other

def add(a: Any, b: Any, /) -> Any: ...
def and_(a: Any, b: Any, /) -> Any: ...
def cmp(a: Any, b: Any, /) -> Any: ...
def div(a: Any, b: Any, /) -> Any: ...
def floordiv(a: Any, b: Any, /) -> Any: ...
def if_else(b: Any, x: Any, y: Any, /) -> Any: ...
def inv(a: Any, /) -> Any: ...
def lshift(a: Any, b: Any, /) -> Any: ...
def mul(a: Any, b: Any, /) -> Any: ...
def neg(a: Any, /) -> Any: ...
def or_(a: Any, b: Any, /) -> Any: ...
def pos(a: Any, /) -> Any: ...
def rshift(a: Any, b: Any, /) -> Any: ...
def sub(a: Any, b: Any, /) -> Any: ...
def xor(a: Any, b: Any, /) -> Any: ...


# color_space

@overload
def convertLinearToSRGB(ColorLinear: _FVT) -> _FVT: ...
@overload
def convertLinearToSRGB(ColorLinear: _FVT, Gamma: _Number) -> _FVT: ...

@overload
def convertSRGBToLinear(ColorLinear: _FVT) -> _FVT: ...
@overload
def convertSRGBToLinear(ColorLinear: _FVT, Gamma: _Number) -> _FVT: ...


# constants

def e() -> float: ...
def epsilon() -> float: ...
def euler() -> float: ...
def four_over_pi() -> float: ...
def golden_ratio() -> float: ...
def half_pi() -> float: ...
def ln_ln_two() -> float: ...
def ln_ten() -> float: ...
def ln_two() -> float: ...
def one() -> float: ...
def one_over_pi() -> float: ...
def one_over_root_two() -> float: ...
def one_over_two_pi() -> float: ...
def pi() -> float: ...
def quarter_pi() -> float: ...
def root_five() -> float: ...
def root_half_pi() -> float: ...
def root_ln_four() -> float: ...
def root_pi() -> float: ...
def root_three() -> float: ...
def root_two() -> float: ...
def root_two_pi() -> float: ...
def third() -> float: ...
def three_over_two_pi() -> float: ...
def two_over_pi() -> float: ...
def two_over_root_pi() -> float: ...
def two_pi() -> float: ...
def two_thirds() -> float: ...
def zero() -> float: ...


# epsilon

@overload
def epsilonEqual(x: _Number, y: _Number, epsilon: _Number, /) -> bool: ...{"".join(f'''
@overload
def epsilonEqual(x: {fvec.__name__}, y: {fvec.__name__}, epsilon: _Number, /) -> {change_vec_data_type(fvec, 'b')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def epsilonNotEqual(x: _Number, y: _Number, epsilon: _Number) -> bool: ...{"".join(f'''
@overload
def epsilonNotEqual(x: {fvec.__name__}, y: {fvec.__name__}, epsilon: _Number, /) -> {change_vec_data_type(fvec, 'b')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}


# integer

@overload
def iround(x: _Number, /) -> int: ...{"".join(f'''
@overload
def iround(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'i')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def uround(x: _Number, /) -> int: ...{"".join(f'''
@overload
def uround(x: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'u')}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}


# matrix_access
{"".join(f'''
@overload
def column(m: {mat.__name__}, index: int, /) -> {mat_column_type(mat)}: ...''' for mat in GLM_MATRIX_TYPES)}{"".join(f'''
@overload
def column(m: {mat.__name__}, index: int, x: {mat_column_type(mat)}, /) -> {mat.__name__}: ...''' for mat in GLM_MATRIX_TYPES)}

{"".join(f'''
@overload
def row(m: {mat.__name__}, index: int, /) -> {mat_row_type(mat)}: ...''' for mat in GLM_MATRIX_TYPES)}{"".join(f'''
@overload
def row(m: {mat.__name__}, index: int, x: {mat_row_type(mat)}, /) -> {mat.__name__}: ...''' for mat in GLM_MATRIX_TYPES)}


# matrix_inverse

@overload
def affineInverse(m: mat3x3, /) -> mat3x3: ...
@overload
def affineInverse(m: dmat3x3, /) -> dmat3x3: ...
@overload
def affineInverse(m: mat4x4, /) -> mat4x4: ...
@overload
def affineInverse(m: dmat4x4, /) -> dmat4x4: ...

@overload
def inverseTranspose(m: mat2x2, /) -> mat2x2: ...
@overload
def inverseTranspose(m: dmat2x2, /) -> dmat2x2: ...
@overload
def inverseTranspose(m: mat3x3, /) -> mat3x3: ...
@overload
def inverseTranspose(m: dmat3x3, /) -> dmat3x3: ...
@overload
def inverseTranspose(m: mat4x4, /) -> mat4x4: ...
@overload
def inverseTranspose(m: dmat4x4, /) -> dmat4x4: ...


# noise

@overload
def perlin(p: _FLOAT_VECTOR, /) -> float: ...
@overload
def perlin(p: _FLOAT_VECTOR, rep: _FLOAT_VECTOR, /) -> float: ...

def simplex(p: _FLOAT_VECTOR, /) -> float: ...


# packing

def packF2x11_1x10(v: vec3, /) -> int: ...

def packF3x9_E1x5(v: vec3, /) -> int: ...

@overload
def packHalf(v: vec1, /) -> u16vec1: ...
@overload
def packHalf(v: vec2, /) -> u16vec2: ...
@overload
def packHalf(v: vec3, /) -> u16vec3: ...
@overload
def packHalf(v: vec4, /) -> u16vec4: ...

def packHalf1x16(v: float, /) -> int: ...

def packHalf4x16(v: vec4, /) -> int: ...

def packI3x10_1x2(v: ivec4, /) -> int: ...

def packInt2x16(v: i16vec2, /) -> int: ...

def packInt2x32(v: i32vec2, /) -> int: ...

def packInt2x8(v: i8vec2, /) -> int: ...

def packInt4x16(v: i16vec4, /) -> int: ...

def packInt4x8(v: i8vec4, /) -> int: ...

def packRGBM(v: vec3, /) -> vec4: ...

{"".join(f'''
@overload
def packSnorm(t: ctypes.{ctype.__name__}, v: {fvec.__name__}, /) -> {change_vec_data_type(fvec, dtype)}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES for ctype, dtype in [(ctypes.c_int8, 'i8'), (ctypes.c_uint8, 'u8'), (ctypes.c_int16, 'i16'), (ctypes.c_uint16, 'u16'), (ctypes.c_int32, 'i32'), (ctypes.c_uint32, 'u32'), (ctypes.c_int64, 'i64'), (ctypes.c_uint64, 'u64')])}

def packSnorm1x16(v: float, /) -> int: ...

def packSnorm1x8(v: float, /) -> int: ...

def packSnorm2x8(v: vec2, /) -> int: ...

def packSnorm3x10_1x2(v: vec4, /) -> int: ...

def packSnorm4x16(v: vec4, /) -> int: ...

def packU3x10_1x2(v: uvec4, /) -> int: ...

def packUint2x16(v: u16vec2, /) -> int: ...

def packUint2x32(v: u32vec2, /) -> int: ...

def packUint2x8(v: u8vec2, /) -> int: ...

def packUint4x16(v: u16vec4, /) -> int: ...

def packUint4x8(v: u16vec4, /) -> int: ...
{"".join(f'''
@overload
def packUnorm(t: ctypes.{ctype.__name__}, v: {fvec.__name__}, /) -> {change_vec_data_type(fvec, dtype)}: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES for ctype, dtype in [(ctypes.c_uint8, 'u8'), (ctypes.c_uint16, 'u16'), (ctypes.c_uint32, 'u32'), (ctypes.c_uint64, 'u64')])}

def packUnorm1x16(v: float, /) -> int: ...

def packUnorm1x5_1x6_1x5(v: vec3, /) -> int: ...

def packUnorm2x4(v: vec2, /) -> int: ...

def packUnorm2x8(v: vec2, /) -> int: ...

def packUnorm3x10_1x2(v: vec4, /) -> int: ...

def packUnorm4x16(v: vec4, /) -> int: ...

def packUnorm4x4(v: vec4, /) -> int: ...

def unpackF2x11_1x10(p: int, /) -> vec3: ...

def unpackF3x9_E1x5(p: int, /) -> vec3: ...

@overload
def unpackHalf(p: u16vec1, /) -> vec1: ...
@overload
def unpackHalf(p: u16vec2, /) -> vec2: ...
@overload
def unpackHalf(p: u16vec3, /) -> vec3: ...
@overload
def unpackHalf(p: u16vec4, /) -> vec4: ...

def unpackHalf1x16(p: int, /) -> float: ...

def unpackI3x10_1x2(p: int, /) -> ivec4: ...

def unpackInt2x16(p: int, /) -> i16vec2: ...

def unpackInt2x32(p: int, /) -> i32vec2: ...

def unpackInt2x8(p: int, /) -> i8vec2: ...

def unpackInt4x16(p: int, /) -> i16vec4: ...

def unpackInt4x8(p: int, /) -> i8vec4: ...

def unpackRGBM(p: vec4, /) -> vec3: ...
{"".join(f'''
@overload
def unpackSnorm(t: ctypes.{ctype.__name__}, v: {ivec.__name__}, /) -> {change_vec_data_type(ivec, dtype)}: ...''' for ivec in GLM_INT_VECTOR_TYPES for ctype, dtype in [(ctypes.c_float, ''), (ctypes.c_double, 'd')])}

def unpackSnorm1x16(p: int, /) -> float: ...

def unpackSnorm1x8(p: int, /) -> float: ...

def unpackSnorm2x8(p: int, /) -> vec2: ...

def unpackSnorm3x10_1x2(p: int, /) -> vec4: ...

def unpackSnorm4x16(p: int, /) -> vec4: ...

def unpackU3x10_1x2(p: int, /) -> uvec4: ...

def unpackUint2x16(p: int, /) -> u16vec2: ...

def unpackUint2x32(p: int, /) -> u32vec2: ...

def unpackUint2x8(p: int, /) -> u8vec2: ...

def unpackUint4x16(p: int, /) -> u16vec4: ...

def unpackUint4x8(p: int, /) -> u8vec4: ...
{"".join(f'''
@overload
def unpackUnorm(t: ctypes.{ctype.__name__}, v: {uvec.__name__}, /) -> {change_vec_data_type(uvec, dtype)}: ...''' for uvec in GLM_U_VECTOR_TYPES for ctype, dtype in [(ctypes.c_float, ''), (ctypes.c_double, 'd')])}

def unpackUnorm1x16(p: int, /) -> float: ...

def unpackUnorm1x5_1x6_1x5(p: int, /) -> vec3: ...

def unpackUnorm1x8(p: int, /) -> float: ...

def unpackUnorm2x3_1x2(p: int, /) -> vec3: ...

def unpackUnorm2x4(p: int, /) -> vec2: ...

def unpackUnorm2x8(p: int, /) -> vec2: ...

def unpackUnorm3x10_1x2(p: int, /) -> vec4: ...

def unpackUnorm3x5_1x1(p: int, /) -> vec4: ...

def unpackUnorm4x16(p: int, /) -> vec4: ...

def unpackUnorm4x4(p: int, /) -> vec4: ...


# quaternion

def eulerAngles(x: _QUAT, /) -> vec3: ...

def mat3_cast(x: _QUAT, /) -> mat3: ...

def mat4_cast(x: _QUAT, /) -> mat4: ...

def pitch(x: _QUAT, /) -> float: ...

def quatLookAtLH(direction: vec3, up: vec3, /) -> quat: ...

def quatLookAtRH(direction: vec3, up: vec3, /) -> quat: ...

quatLookAt = quatLookAtRH

def quat_cast(x: Union[mat3, mat4], /) -> quat: ...

def roll(x: _QUAT, /) -> float: ...

def yaw(x: _QUAT, /) -> float: ...


# random

def ballRand(Radius: _Number, /) -> vec3: ...

def circularRand(Radius: _Number, /) -> vec2: ...

def diskRand(Radius: _Number, /) -> vec2: ...

@overload
def gaussRand(Mean: _Number, Deviation: _Number, /) -> float: ...
@overload
def gaussRand(Mean: _VT, Deviation: _VT, /) -> _VT: ...

@overload
def linearRand(Min: _Number, Max: _Number, /) -> float: ...
@overload
def linearRand(Min: _VT, Max: _VT, /) -> _VT: ...

def setSeed(seed: SupportsInt, /) -> None: ...

def sphericalRand(Radius: _Number, /) -> vec3: ...


# reciprocal

def acot(x: _Number, /) -> float: ...

def acoth(x: _Number, /) -> float: ...

def acsc(x: _Number, /) -> float: ...

def acsch(x: _Number, /) -> float: ...

def asec(x: _Number, /) -> float: ...

def asech(x: _Number, /) -> float: ...

def cot(x: _Number, /) -> float: ...

def coth(x: _Number, /) -> float: ...

def csc(x: _Number, /) -> float: ...

def csch(x: _Number, /) -> float: ...

def sec(x: _Number, /) -> float: ...

def sech(x: _Number, /) -> float: ...


# round

@overload
def ceilMultiple(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def ceilMultiple(v: _iVT, Multiple: _iVT, /) -> _iVT: ...

@overload
def ceilPowerOfTwo(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def ceilPowerOfTwo(v: _iVT, Multiple: _iVT, /) -> _iVT: ...

@overload
def floorMultiple(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def floorMultiple(v: _iVT, Multiple: _iVT, /) -> _iVT: ...

@overload
def floorPowerOfTwo(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def floorPowerOfTwo(v: _iVT, Multiple: _iVT, /) -> _iVT: ...

@overload
def roundMultiple(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def roundMultiple(v: _iVT, Multiple: _iVT, /) -> _iVT: ...

@overload
def roundPowerOfTwo(v: _Number, Multiple: _Number, /) -> int: ...
@overload
def roundPowerOfTwo(v: _iVT, Multiple: _iVT, /) -> _iVT: ...


# type_ptr

def make_mat2x2(x: ctypes.c_void_p) -> mat2x2: ...

def make_mat2x3(x: ctypes.c_void_p) -> mat2x3: ...

def make_mat2x4(x: ctypes.c_void_p) -> mat2x4: ...

def make_mat3x2(x: ctypes.c_void_p) -> mat3x2: ...

def make_mat3x3(x: ctypes.c_void_p) -> mat3x3: ...

def make_mat3x4(x: ctypes.c_void_p) -> mat3x4: ...

def make_mat4x2(x: ctypes.c_void_p) -> mat4x2: ...

def make_mat4x3(x: ctypes.c_void_p) -> mat4x3: ...

def make_mat4x4(x: ctypes.c_void_p) -> mat4x4: ...

make_mat2 = make_mat2x2
make_mat3 = make_mat3x3
make_mat4 = make_mat4x4

def make_quat(x: ctypes.c_void_p) -> quat: ...

def make_vec2(x: ctypes.c_void_p) -> vec2: ...

def make_vec3(x: ctypes.c_void_p) -> vec3: ...

def make_vec4(x: ctypes.c_void_p) -> vec4: ...

def sizeof(x: Type[Union[_GLM_TYPES, _CTYPES]]) -> int: ...

def value_ptr(x: Union[_GLM_TYPES, _CTYPES]) -> ctypes.c_void_p: ...


# ulp

@overload
def float_distance(x: _Number, y: _Number) -> float: ...{"".join(f'''
@overload
def float_distance(x: {fvec.__name__}, y: {fvec.__name__}, /) -> {change_vec_data_type(fvec, 'i')}: ...''' for fvec in GLM_F_VECTOR_TYPES)}{"".join(f'''
@overload
def float_distance(x: {dvec.__name__}, y: {dvec.__name__}, /) -> {change_vec_data_type(dvec, 'i64')}: ...''' for dvec in GLM_D_VECTOR_TYPES)}

@overload
def next_float(x: _Number) -> float: ...
@overload
def next_float(x: _FVT) -> _FVT: ...
@overload
def next_float(x: _Number, ULPs: _Number) -> float: ...
@overload
def next_float(x: _FVT, ULPs: _Number) -> _FVT: ...{"".join(f'''
@overload
def next_float(x: {fvec.__name__}, ULPs: {change_vec_data_type(fvec, 'i')}, /) -> float: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}

@overload
def prev_float(x: _Number) -> float: ...
@overload
def prev_float(x: _FVT) -> _FVT: ...
@overload
def prev_float(x: _Number, ULPs: _Number) -> float: ...
@overload
def prev_float(x: _FVT, ULPs: _Number) -> _FVT: ...{"".join(f'''
@overload
def prev_float(x: {fvec.__name__}, ULPs: {change_vec_data_type(fvec, 'i')}, /) -> float: ...''' for fvec in GLM_FLOAT_VECTOR_TYPES)}


# matrix_clip_space

def frustumLH_NO(left: _Number, right: _Number, bottom: _Number, top: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def frustumLH_ZO(left: _Number, right: _Number, bottom: _Number, top: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def frustumRH_NO(left: _Number, right: _Number, bottom: _Number, top: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def frustumRH_ZO(left: _Number, right: _Number, bottom: _Number, top: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

frustum = frustumRH_NO
frustumNO = frustumRH_NO
frustumRH = frustumRH_NO
frustumLH = frustumLH_NO
frustumZO = frustumRH_ZO

def infinitePerspectiveLH(fovy: _Number, aspect: _Number, near: _Number, /) -> mat4x4: ...

def infinitePerspectiveRH(fovy: _Number, aspect: _Number, near: _Number, /) -> mat4x4: ...

infinitePerspective = infinitePerspectiveRH

def orthoLH_NO(left: _Number, right: _Number, bottom: _Number, top: _Number, zNear: _Number, zFar: _Number, /) -> mat4x4: ...

def orthoLH_ZO(left: _Number, right: _Number, bottom: _Number, top: _Number, zNear: _Number, zFar: _Number, /) -> mat4x4: ...

def orthoRH_NO(left: _Number, right: _Number, bottom: _Number, top: _Number, zNear: _Number, zFar: _Number, /) -> mat4x4: ...

def orthoRH_ZO(left: _Number, right: _Number, bottom: _Number, top: _Number, zNear: _Number, zFar: _Number, /) -> mat4x4: ...

ortho = orthoRH_NO
orthoLH = orthoLH_NO
orthoNO = orthoRH_NO
orthoRH = orthoRH_NO
orthoZO = orthoRH_ZO

def perspectiveLH_NO(fovy: _Number, aspect: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveLH_ZO(fovy: _Number, aspect: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveRH_NO(fovy: _Number, aspect: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveRH_ZO(fovy: _Number, aspect: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

perspective = perspectiveRH_NO
perspectiveLH = perspectiveLH_NO
perspectiveNO = perspectiveRH_NO
perspectiveRH = perspectiveRH_NO
perspectiveZO = perspectiveRH_ZO

def perspectiveFovLH_NO(fov: _Number, width: _Number, height: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveFovLH_ZO(fov: _Number, width: _Number, height: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveFovRH_NO(fov: _Number, width: _Number, height: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

def perspectiveFovRH_ZO(fov: _Number, width: _Number, height: _Number, near: _Number, far: _Number, /) -> mat4x4: ...

perspectiveFov = perspectiveFovRH_NO
perspectiveFovLH = perspectiveFovLH_NO
perspectiveFovNO = perspectiveFovRH_NO
perspectiveFovRH = perspectiveFovRH_NO
perspectiveFovZO = perspectiveFovRH_ZO

@overload
def tweakedInfinitePerspective(fovy: _Number, aspect: _Number, near: _Number, /) -> mat4x4: ...
@overload
def tweakedInfinitePerspective(fovy: _Number, aspect: _Number, near: _Number, epsilon: float, /) -> mat4x4: ...


# matrix_projection

@overload
def pickMatrix(center: vec2, delta: vec2, viewport: vec4, /) -> mat4x4: ...
@overload
def pickMatrix(center: dvec2, delta: dvec2, viewport: dvec4, /) -> dmat4x4: ...

@overload
def projectNO(obj: vec3, model: mat4x4, proj: mat4x4, viewport: vec4, /) -> vec3: ...
@overload
def projectNO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

project = projectNO

@overload
def projectZO(obj: vec3, model: mat4x4, proj: mat4x4, viewport: vec4, /) -> vec3: ...
@overload
def projectZO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

@overload
def unProjectNO(win: vec3, model: mat4x4, proj: mat4x4, viewport: vec4, /) -> vec3: ...
@overload
def unProjectNO(win: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

unProject = unProjectNO

@overload
def unProjectZO(win: vec3, model: mat4x4, proj: mat4x4, viewport: vec4, /) -> vec3: ...
@overload
def unProjectZO(win: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...


# matrix_transform

def identity(matrix_type: Type[_MT], /) -> _MT: ...

@overload
def lookAtLH(eye: vec3, center: vec3, up: vec3, /) -> mat4x4: ...
@overload
def lookAtLH(eye: dvec3, center: dvec3, up: dvec3, /) -> dmat4x4: ...

@overload
def lookAtRH(eye: vec3, center: vec3, up: vec3, /) -> mat4x4: ...
@overload
def lookAtRH(eye: dvec3, center: dvec3, up: dvec3, /) -> dmat4x4: ...

lookAt = lookAtRH

@overload
def rotate(angle: _Number, axis: vec3, /) -> mat4x4: ...
@overload
def rotate(angle: _Number, axis: dvec3, /) -> dmat4x4: ...
@overload
def rotate(angle: _Number, /) -> mat3x3: ...
@overload
def rotate(m: mat4x4, angle: _Number, axis: vec3, /) -> mat4x4: ...
@overload
def rotate(m: dmat4x4, angle: _Number, axis: dvec3, /) -> mat4x4: ...
@overload
def rotate(m: mat3x3, angle: _Number, /) -> mat3x3: ...
@overload
def rotate(m: dmat3x3, angle: _Number, /) -> dmat3x3: ...
@overload
def rotate(v: vec2, angle: _Number, /) -> vec2: ...
@overload
def rotate(v: dvec2, angle: _Number, /) -> dvec2: ...
@overload
def rotate(v: vec3, angle: _Number, normal: vec3, /) -> vec3: ...
@overload
def rotate(v: dvec3, angle: _Number, normal: dvec3, /) -> dvec3: ...
@overload
def rotate(v: dvec4, angle: _Number, normal: dvec3, /) -> dvec4: ...
@overload
def rotate(v: quat, angle: _Number, normal: vec3, /) -> quat: ...
@overload
def rotate(v: dquat, angle: _Number, normal: dvec3, /) -> dquat: ...

@overload
def rotate_slow(m: mat4x4, angle: _Number, axis: vec3, /) -> mat4x4: ...
@overload
def rotate_slow(m: dmat4x4, angle: _Number, axis: dvec3, /) -> dmat4x4: ...

@overload
def scale(v: vec3, /) -> mat4x4: ...
@overload
def scale(v: dvec3, /) -> dmat4x4: ...
@overload
def scale(v: vec2, /) -> mat3x3: ...
@overload
def scale(v: dvec2, /) -> mat3x3: ...
@overload
def scale(m: mat4x4, v: vec3, /) -> mat4x4: ...
@overload
def scale(m: dmat4x4, v: dvec3, /) -> dmat4x4: ...
@overload
def scale(m: mat3x3, v: vec2, /) -> mat3x3: ...
@overload
def scale(m: dmat3x3, v: dvec2, /) -> dmat3x3: ...

@overload
def scale_slow(m: mat4x4, v: vec3, /) -> mat4x4: ...
@overload
def scale_slow(m: dmat4x4, v: dvec3, /) -> dmat4x4: ...

@overload
def translate(v: vec3, /) -> mat4x4: ...
@overload
def translate(v: dvec3, /) -> dmat4x4: ...
@overload
def translate(v: vec2, /) -> mat3x3: ...
@overload
def translate(v: dvec2, /) -> dmat3x3: ...
@overload
def translate(m: mat4x4, v: vec3, /) -> mat4x4: ...
@overload
def translate(m: dmat4x4, v: dvec3, /) -> dmat4x4: ...
@overload
def translate(m: mat3x3, v: vec2, /) -> mat3x3: ...
@overload
def translate(m: dmat3x3, v: dvec2, /) -> dmat3x3: ...


# quaternion_common

def conjugate(q: _QT, /) -> _QT: ...

def lerp(x: _QT, y: _QT, a: _Number, /) -> _QT: ...

@overload
def slerp(x: _QT, y: _QT, a: _Number, /) -> _QT: ...
@overload
def slerp(x: vec3, y: vec3, a: _Number, /) -> vec3: ...
@overload
def slerp(x: dvec3, y: dvec3, a: _Number, /) -> dvec3: ...


# quaternion_trigonometric

def angle(x: _QT, /) -> float: ...

@overload
def angleAxis(angle: _Number, axis: vec3, /) -> quat: ...
@overload
def angleAxis(angle: _Number, axis: dvec3, /) -> dquat: ...

@overload
def axis(x: quat, /) -> vec3: ...
@overload
def axis(x: dquat, /) -> dvec3: ...


# decompose

@overload
def decompose(modelMatrix: mat4x4, scale: vec3, orientation: quat, translation: vec3, skew: vec3, perspective: vec4, /) -> bool: ...
@overload
def decompose(modelMatrix: dmat4x4, scale: dvec3, orientation: dquat, translation: dvec3, skew: dvec3, perspective: dvec4, /) -> bool: ...


# matrix_transform_2d

@overload
def shearX(m: mat3x3, y: _Number, /) -> mat3x3: ...
@overload
def shearX(m: dmat3x3, y: _Number, /) -> dmat3x3: ...

@overload
def shearY(m: mat3x3, y: _Number, /) -> mat3x3: ...
@overload
def shearY(m: dmat3x3, y: _Number, /) -> dmat3x3: ...


# norm

def distance2(p0: _FVT, p1: _FVT, /) -> float: ...

@overload
def l1Norm(v: Union[vec3, dvec3], /) -> float: ...
@overload
def l1Norm(x: vec3, y: vec3, /) -> float: ...
@overload
def l1Norm(x: dvec3, y: dvec3, /) -> float: ...

@overload
def l2Norm(v: Union[vec3, dvec3], /) -> float: ...
@overload
def l2Norm(x: vec3, y: vec3, /) -> float: ...
@overload
def l2Norm(x: dvec3, y: dvec3, /) -> float: ...

@overload
def lMaxNorm(v: Union[vec3, dvec3], /) -> float: ...
@overload
def lMaxNorm(x: vec3, y: vec3, /) -> float: ...
@overload
def lMaxNorm(x: dvec3, y: dvec3, /) -> float: ...

def length2(p0: _FVT, p1: _FVT, /) -> float: ...

@overload
def lxNorm(v: Union[vec3, dvec3], Depth: int, /) -> float: ...
@overload
def lxNorm(x: vec3, y: vec3, Depth: int, /) -> float: ...
@overload
def lxNorm(x: dvec3, y: dvec3, Depth: int, /) -> float: ...


# polar_coordinates

@overload
def euclidean(polar: vec2, /) -> vec3: ...
@overload
def euclidean(polar: dvec2, /) -> dvec3: ...

@overload
def poldar(euclidean: vec3, /) -> vec3: ...
@overload
def poldar(euclidean: dvec3, /) -> dvec3: ...


# rotate_vector

@overload
def orientation(Normal: vec3, Up: vec3, /) -> mat4x4: ...
@overload
def orientation(Normal: dvec3, Up: dvec3, /) -> dmat4x4: ...

@overload
def rotateX(v: vec3, angle: _Number) -> vec3: ...
@overload
def rotateX(v: dvec3, angle: _Number) -> dvec3: ...
@overload
def rotateX(v: vec4, angle: _Number) -> vec4: ...
@overload
def rotateX(v: dvec4, angle: _Number) -> dvec4: ...

@overload
def rotateY(v: vec3, angle: _Number) -> vec3: ...
@overload
def rotateY(v: dvec3, angle: _Number) -> dvec3: ...
@overload
def rotateY(v: vec4, angle: _Number) -> vec4: ...
@overload
def rotateY(v: dvec4, angle: _Number) -> dvec4: ...

@overload
def rotateZ(v: vec3, angle: _Number) -> vec3: ...
@overload
def rotateZ(v: dvec3, angle: _Number) -> dvec3: ...
@overload
def rotateZ(v: vec4, angle: _Number) -> vec4: ...
@overload
def rotateZ(v: dvec4, angle: _Number) -> dvec4: ...


""")
print(f"""
_ARRAY_TYPES = Union[_CTYPES, _GLM_TYPES]

_AT = TypeVar('_AT', bound=_ARRAY_TYPES)
_AT2 = TypeVar('_AT2', bound=_ARRAY_TYPES)
_GT = TypeVar('_GT', bound=_GLM_TYPES)
_ACT = TypeVar('_ACT', bound=_CTYPES)
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
    def ctype(self) -> _CTYPES: ...

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
    for alias in aliases:
        print(alias, '=', type_name)
