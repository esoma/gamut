
from __future__ import annotations

import glm
import operator as op
import re
import textwrap
from typing import Mapping, Sequence

VEC_PATTERN = re.compile(r'([bdfiu])?[8|16|32|64]?m?vec(\d)')
MAT_PATTERN = re.compile(r'([dfiu])?mat(\d)x(\d)')

VEC_OPERATORS = [
    op.add, op.iadd,
    op.sub, op.isub,
    op.mul, op.imul,
    op.mod, op.imod,
    op.pow, op.ipow,
    op.floordiv, op.ifloordiv,
    op.truediv, op.itruediv,
    op.matmul, op.imatmul
]

MAT_OPERATORS = [
    op.add, op.iadd,
    op.sub, op.isub,
    op.mul, op.imul,
    op.truediv, op.itruediv,
    op.matmul, op.imatmul
]

TYPE_PREFIX_TO_PYTHON_TYPE = {
    'b': bool,
    'd': float,
    'f': float,
    'i': int,
    'u': int,
    None: float,
}

GLM_TYPES = sorted({
    getattr(glm, name)
    for name in dir(glm)
    if (
        VEC_PATTERN.match(name) or
        MAT_PATTERN.match(name)
    )
}, key=lambda t: t.__name__)


def stub_vec_template(
    name: str,
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
        def __init__(self, x: SupportsFloat) -> None: ...''' if component_count != 1 else ''}
        @overload
        def __init__(self, {', '.join(f'{c}: SupportsFloat' for c in component_names[:component_count])}) -> None: ...{''.join(f'''
        @overload
        def __init__(self, x: {t}) -> None: ...''' for t in initializer_types)}
        
        def __len__(self) -> Literal[{component_count}]: ...
        def __getitem__(self, index: int) -> {python_type}: ...
        def __setitem__(self, index: int, value: SupportsFloat) -> None: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{python_type}, None, None]: ...
        
        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...
        def __abs__(self) -> {name}: ...
        
        def to_list(self) -> List[{python_type}]: ...
        def to_tuple(self) -> Tuple[{', '.join(python_type for i in range(component_count))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...
    """)
    
    for operator, types in operator_map.items():
        if len(types) == 1:
            other_type, result_type = types[0]
            s += textwrap.indent(textwrap.dedent(f"""
                def {operator}(self, other: {other_type}) -> {result_type}: ...
            """), '    ')
        elif types:
            for other_type, result_type in types:
                s += textwrap.indent(textwrap.dedent(f"""
                    @overload
                    def {operator}(self, other: {other_type}) -> {result_type}: ...
                """), '    ').rstrip()
            s += '\n'
    
    return s
    

def stub_vec(vec):
    re_match = VEC_PATTERN.match(vec.__name__)
    python_type = TYPE_PREFIX_TO_PYTHON_TYPE[re_match[1]]
    component_count = int(re_match[2])
    # all vectors support being created from a tuple of SupportsFloat as long
    # as the vector has the minimum number of required components
    initializer_types = {
        'Tuple[SupportsFloat, SupportsFloat, SupportsFloat, SupportsFloat]',
    }
    if component_count == 1:
        initializer_types.add('Tuple[SupportsFloat]')
    if component_count <= 2:
        initializer_types.add('Tuple[SupportsFloat, SupportsFloat]')
    if component_count <= 3:
        initializer_types.add('Tuple[SupportsFloat, SupportsFloat, SupportsFloat]')
    # check which types can be used to initialize this vector
    for other_type in GLM_TYPES:
        try:
            vec(other_type())
        except TypeError:
            continue
        initializer_types.add(other_type.__name__)
    initializer_types = sorted(initializer_types)
    # get all the types that can be used standard operators and what the result
    # will be
    operator_map = {}
    for operator in VEC_OPERATORS:
        operator_types = set()
        for other_type in GLM_TYPES:
            try:
                result_type = type(operator(vec(), other_type(1)))
            except TypeError:
                continue
            operator_types.add(
                (other_type.__name__, result_type.__name__)
            )
            # if it supports a vector then it also supports a tuple of the same
            # size made of 'SupportsFloat'
            other_re_match = VEC_PATTERN.match(other_type.__name__)
            if other_re_match:
                other_component_count = int(other_re_match[2])
                operator_types.add(
                    (f'Tuple[{", ".join("SupportsFloat" for i in range(other_component_count))}]', result_type.__name__)
                )
        # if any other types are supported for the operation, then it should
        # also support 'SupportsFloat'
        if operator_types:
            operator_types.add(('SupportsFloat', vec.__name__))
        operator_map[f'__{operator.__name__}__'] = sorted(operator_types)
    # divmod is sort of a special operator
    operator_types = set()
    for other_type in GLM_TYPES:
        try:
            result = divmod(vec(), other_type(1))
        except TypeError:
            continue
        if result[0] is NotImplemented:
            continue
        result_type = f'Tuple[{type(result[0]).__name__}, {type(result[1]).__name__}]'
        operator_types.add(
            (other_type.__name__, result_type)
        )
    operator_map[f'__divmod__'] = sorted(operator_types)
            
    return stub_vec_template(
        vec.__name__,
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
        def __init__(self, _: SupportsFloat, /) -> None: ...
        @overload
        def __init__(self, {', '.join(f'_{c}: SupportsFloat' for c in range(row_count * column_count))}, /) -> None: ...{''.join(f'''
        @overload
        def __init__(self, _: {t}, /) -> None: ...''' for t in initializer_types)}
    
        def length(self) -> Literal[{row_count}]: ...
        def __len__(self) -> Literal[{row_count}]: ...
        def __getitem__(self, index: int) -> {mvec}: ...
        
        @overload
        def __setitem__(self, index: Tuple[int, int], value: SupportsFloat) -> None: ...
        @overload
        def __setitem__(self, index: int, value: Union[{vec}, {mvec}]) -> None: ...
        
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{mvec}, None, None]: ...
        
        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...
        
        def to_list(self) -> List[List[{python_type}]]: ...
        def to_tuple(self) -> Tuple[{', '.join(f'Tuple[{", ".join(python_type for i in range(column_count))}]' for i in range(row_count))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...
    """)
    return s
    
    
def stub_mat(mat):
    re_match = MAT_PATTERN.match(mat.__name__)
    data_type_prefix = re_match[1]
    python_type = TYPE_PREFIX_TO_PYTHON_TYPE[data_type_prefix]
    row_count = int(re_match[2])
    column_count = int(re_match[3])
    # all matrices support being created from a tuple of tuple SupportsFloat as
    # long as the matrix has the minimum number of required rows and columns
    def mat_tuple_str(rows, columns):
        row = f'Tuple[{", ".join("SupportsFloat" for i in range(columns))}]'
        return f'Tuple[{", ".join(row for i in range(rows))}]'
    initializer_types = {
        mat_tuple_str(4, 4),
    }
    if row_count <= 3:
        initializer_types.add(mat_tuple_str(3, 4))
        if column_count <= 3:
            initializer_types.add(mat_tuple_str(3, 3))
        if column_count <= 2:
            initializer_types.add(mat_tuple_str(3, 2))
    if row_count <= 2:
        initializer_types.add(mat_tuple_str(2, 4))
        if column_count <= 3:
            initializer_types.add(mat_tuple_str(2, 3))
        if column_count <= 2:
            initializer_types.add(mat_tuple_str(2, 2))
    # check which types can be used to initialize this vector
    for other_type in GLM_TYPES:
        try:
            mat(other_type())
        except TypeError:
            continue
        initializer_types.add(other_type.__name__)
    initializer_types = sorted(initializer_types)
    
    operator_map = {}
    return stub_mat_template(
        mat.__name__,
        data_type_prefix,
        row_count,
        column_count,
        python_type.__name__,
        initializer_types,
        operator_map
    )
    
print('from numbers import Number')
print('from typing import Any, overload, List, Literal, Generator, SupportsFloat, Tuple')
for glm_type in GLM_TYPES:
    if 'vec' in glm_type.__name__:
        print(stub_vec(glm_type))
    elif 'mat' in glm_type.__name__:
        print(stub_mat(glm_type))

    
#print(create_vec1('vec1', 'float', ['vec1', 'vec2']))