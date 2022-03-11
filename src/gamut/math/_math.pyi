
# generated 2022-03-10 23:24:28.498431 from codegen/math/templates/_math.pyi

__all__ = [

    'BVector2',

    'DVector2',

    'FVector2',

    'I8Vector2',

    'U8Vector2',

    'I16Vector2',

    'U16Vector2',

    'I32Vector2',

    'U32Vector2',

    'IVector2',

    'UVector2',

    'I64Vector2',

    'U64Vector2',

    'BVector3',

    'DVector3',

    'FVector3',

    'I8Vector3',

    'U8Vector3',

    'I16Vector3',

    'U16Vector3',

    'I32Vector3',

    'U32Vector3',

    'IVector3',

    'UVector3',

    'I64Vector3',

    'U64Vector3',

    'BVector4',

    'DVector4',

    'FVector4',

    'I8Vector4',

    'U8Vector4',

    'I16Vector4',

    'U16Vector4',

    'I32Vector4',

    'U32Vector4',

    'IVector4',

    'UVector4',

    'I64Vector4',

    'U64Vector4',

]

# python
from typing import Any, final, overload, SupportsFloat, SupportsInt

Number = SupportsFloat | SupportsInt






@final
class BVector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: BVector2) -> BVector2: ...
    @overload
    def __add__(self, other: Number) -> BVector2: ...
    @overload
    def __radd__(self, other: BVector2) -> BVector2: ...
    @overload
    def __radd__(self, other: Number) -> BVector2: ...

    @overload
    def __sub__(self, other: BVector2) -> BVector2: ...
    @overload
    def __sub__(self, other: Number) -> BVector2: ...
    @overload
    def __rsub__(self, other: BVector2) -> BVector2: ...
    @overload
    def __rsub__(self, other: Number) -> BVector2: ...

    @overload
    def __mul__(self, other: BVector2) -> BVector2: ...
    @overload
    def __mul__(self, other: Number) -> BVector2: ...
    @overload
    def __rmul__(self, other: BVector2) -> BVector2: ...
    @overload
    def __rmul__(self, other: Number) -> BVector2: ...







    def __abs__(self) -> BVector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> bool: ...

    @property
    def y(self) -> bool: ...



    @property
    def xx(self) -> BVector2: ...

    @property
    def xy(self) -> BVector2: ...

    @property
    def yy(self) -> BVector2: ...



    @property
    def xxx(self) -> BVector3: ...

    @property
    def xxy(self) -> BVector3: ...

    @property
    def xyy(self) -> BVector3: ...

    @property
    def yyy(self) -> BVector3: ...



    @property
    def xxxx(self) -> BVector4: ...

    @property
    def xxxy(self) -> BVector4: ...

    @property
    def xxyy(self) -> BVector4: ...

    @property
    def xyyy(self) -> BVector4: ...

    @property
    def yyyy(self) -> BVector4: ...





    @property
    def r(self) -> bool: ...

    @property
    def g(self) -> bool: ...



    @property
    def rr(self) -> BVector2: ...

    @property
    def rg(self) -> BVector2: ...

    @property
    def gg(self) -> BVector2: ...



    @property
    def rrr(self) -> BVector3: ...

    @property
    def rrg(self) -> BVector3: ...

    @property
    def rgg(self) -> BVector3: ...

    @property
    def ggg(self) -> BVector3: ...



    @property
    def rrrr(self) -> BVector4: ...

    @property
    def rrrg(self) -> BVector4: ...

    @property
    def rrgg(self) -> BVector4: ...

    @property
    def rggg(self) -> BVector4: ...

    @property
    def gggg(self) -> BVector4: ...





    @property
    def s(self) -> bool: ...

    @property
    def t(self) -> bool: ...



    @property
    def ss(self) -> BVector2: ...

    @property
    def st(self) -> BVector2: ...

    @property
    def tt(self) -> BVector2: ...



    @property
    def sss(self) -> BVector3: ...

    @property
    def sst(self) -> BVector3: ...

    @property
    def stt(self) -> BVector3: ...

    @property
    def ttt(self) -> BVector3: ...



    @property
    def ssss(self) -> BVector4: ...

    @property
    def ssst(self) -> BVector4: ...

    @property
    def sstt(self) -> BVector4: ...

    @property
    def sttt(self) -> BVector4: ...

    @property
    def tttt(self) -> BVector4: ...





    @property
    def u(self) -> bool: ...

    @property
    def v(self) -> bool: ...



    @property
    def uu(self) -> BVector2: ...

    @property
    def uv(self) -> BVector2: ...

    @property
    def vv(self) -> BVector2: ...



    @property
    def uuu(self) -> BVector3: ...

    @property
    def uuv(self) -> BVector3: ...

    @property
    def uvv(self) -> BVector3: ...

    @property
    def vvv(self) -> BVector3: ...



    @property
    def uuuu(self) -> BVector4: ...

    @property
    def uuuv(self) -> BVector4: ...

    @property
    def uuvv(self) -> BVector4: ...

    @property
    def uvvv(self) -> BVector4: ...

    @property
    def vvvv(self) -> BVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[bool, bool]: ...









@final
class DVector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DVector2) -> DVector2: ...
    @overload
    def __add__(self, other: Number) -> DVector2: ...
    @overload
    def __radd__(self, other: DVector2) -> DVector2: ...
    @overload
    def __radd__(self, other: Number) -> DVector2: ...

    @overload
    def __sub__(self, other: DVector2) -> DVector2: ...
    @overload
    def __sub__(self, other: Number) -> DVector2: ...
    @overload
    def __rsub__(self, other: DVector2) -> DVector2: ...
    @overload
    def __rsub__(self, other: Number) -> DVector2: ...

    @overload
    def __mul__(self, other: DVector2) -> DVector2: ...
    @overload
    def __mul__(self, other: Number) -> DVector2: ...
    @overload
    def __rmul__(self, other: DVector2) -> DVector2: ...
    @overload
    def __rmul__(self, other: Number) -> DVector2: ...




    @overload
    def __truediv__(self, other: DVector2) -> DVector2: ...
    @overload
    def __truediv__(self, other: Number) -> DVector2: ...
    @overload
    def __rtruediv__(self, other: DVector2) -> DVector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> DVector2: ...




    def __abs__(self) -> DVector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> DVector2: ...

    @property
    def xy(self) -> DVector2: ...

    @property
    def yy(self) -> DVector2: ...



    @property
    def xxx(self) -> DVector3: ...

    @property
    def xxy(self) -> DVector3: ...

    @property
    def xyy(self) -> DVector3: ...

    @property
    def yyy(self) -> DVector3: ...



    @property
    def xxxx(self) -> DVector4: ...

    @property
    def xxxy(self) -> DVector4: ...

    @property
    def xxyy(self) -> DVector4: ...

    @property
    def xyyy(self) -> DVector4: ...

    @property
    def yyyy(self) -> DVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> DVector2: ...

    @property
    def rg(self) -> DVector2: ...

    @property
    def gg(self) -> DVector2: ...



    @property
    def rrr(self) -> DVector3: ...

    @property
    def rrg(self) -> DVector3: ...

    @property
    def rgg(self) -> DVector3: ...

    @property
    def ggg(self) -> DVector3: ...



    @property
    def rrrr(self) -> DVector4: ...

    @property
    def rrrg(self) -> DVector4: ...

    @property
    def rrgg(self) -> DVector4: ...

    @property
    def rggg(self) -> DVector4: ...

    @property
    def gggg(self) -> DVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> DVector2: ...

    @property
    def st(self) -> DVector2: ...

    @property
    def tt(self) -> DVector2: ...



    @property
    def sss(self) -> DVector3: ...

    @property
    def sst(self) -> DVector3: ...

    @property
    def stt(self) -> DVector3: ...

    @property
    def ttt(self) -> DVector3: ...



    @property
    def ssss(self) -> DVector4: ...

    @property
    def ssst(self) -> DVector4: ...

    @property
    def sstt(self) -> DVector4: ...

    @property
    def sttt(self) -> DVector4: ...

    @property
    def tttt(self) -> DVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> DVector2: ...

    @property
    def uv(self) -> DVector2: ...

    @property
    def vv(self) -> DVector2: ...



    @property
    def uuu(self) -> DVector3: ...

    @property
    def uuv(self) -> DVector3: ...

    @property
    def uvv(self) -> DVector3: ...

    @property
    def vvv(self) -> DVector3: ...



    @property
    def uuuu(self) -> DVector4: ...

    @property
    def uuuv(self) -> DVector4: ...

    @property
    def uuvv(self) -> DVector4: ...

    @property
    def uvvv(self) -> DVector4: ...

    @property
    def vvvv(self) -> DVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class FVector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> float: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FVector2) -> FVector2: ...
    @overload
    def __add__(self, other: Number) -> FVector2: ...
    @overload
    def __radd__(self, other: FVector2) -> FVector2: ...
    @overload
    def __radd__(self, other: Number) -> FVector2: ...

    @overload
    def __sub__(self, other: FVector2) -> FVector2: ...
    @overload
    def __sub__(self, other: Number) -> FVector2: ...
    @overload
    def __rsub__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rsub__(self, other: Number) -> FVector2: ...

    @overload
    def __mul__(self, other: FVector2) -> FVector2: ...
    @overload
    def __mul__(self, other: Number) -> FVector2: ...
    @overload
    def __rmul__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rmul__(self, other: Number) -> FVector2: ...


    def __matmul__(self, other: FVector2) -> FVector2: ...
    def __rmatmul__(self, other: FVector2) -> FVector2: ...

    @overload
    def __mod__(self, other: FVector2) -> FVector2: ...
    @overload
    def __mod__(self, other: Number) -> FVector2: ...
    @overload
    def __rmod__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rmod__(self, other: Number) -> FVector2: ...

    @overload
    def __pow__(self, other: FVector2) -> FVector2: ...
    @overload
    def __pow__(self, other: Number) -> FVector2: ...
    @overload
    def __rpow__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rpow__(self, other: Number) -> FVector2: ...



    @overload
    def __truediv__(self, other: FVector2) -> FVector2: ...
    @overload
    def __truediv__(self, other: Number) -> FVector2: ...
    @overload
    def __rtruediv__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> FVector2: ...




    def __abs__(self) -> FVector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...



    @property
    def xx(self) -> FVector2: ...

    @property
    def xy(self) -> FVector2: ...

    @property
    def yy(self) -> FVector2: ...



    @property
    def xxx(self) -> FVector3: ...

    @property
    def xxy(self) -> FVector3: ...

    @property
    def xyy(self) -> FVector3: ...

    @property
    def yyy(self) -> FVector3: ...



    @property
    def xxxx(self) -> FVector4: ...

    @property
    def xxxy(self) -> FVector4: ...

    @property
    def xxyy(self) -> FVector4: ...

    @property
    def xyyy(self) -> FVector4: ...

    @property
    def yyyy(self) -> FVector4: ...





    @property
    def r(self) -> float: ...

    @property
    def g(self) -> float: ...



    @property
    def rr(self) -> FVector2: ...

    @property
    def rg(self) -> FVector2: ...

    @property
    def gg(self) -> FVector2: ...



    @property
    def rrr(self) -> FVector3: ...

    @property
    def rrg(self) -> FVector3: ...

    @property
    def rgg(self) -> FVector3: ...

    @property
    def ggg(self) -> FVector3: ...



    @property
    def rrrr(self) -> FVector4: ...

    @property
    def rrrg(self) -> FVector4: ...

    @property
    def rrgg(self) -> FVector4: ...

    @property
    def rggg(self) -> FVector4: ...

    @property
    def gggg(self) -> FVector4: ...





    @property
    def s(self) -> float: ...

    @property
    def t(self) -> float: ...



    @property
    def ss(self) -> FVector2: ...

    @property
    def st(self) -> FVector2: ...

    @property
    def tt(self) -> FVector2: ...



    @property
    def sss(self) -> FVector3: ...

    @property
    def sst(self) -> FVector3: ...

    @property
    def stt(self) -> FVector3: ...

    @property
    def ttt(self) -> FVector3: ...



    @property
    def ssss(self) -> FVector4: ...

    @property
    def ssst(self) -> FVector4: ...

    @property
    def sstt(self) -> FVector4: ...

    @property
    def sttt(self) -> FVector4: ...

    @property
    def tttt(self) -> FVector4: ...





    @property
    def u(self) -> float: ...

    @property
    def v(self) -> float: ...



    @property
    def uu(self) -> FVector2: ...

    @property
    def uv(self) -> FVector2: ...

    @property
    def vv(self) -> FVector2: ...



    @property
    def uuu(self) -> FVector3: ...

    @property
    def uuv(self) -> FVector3: ...

    @property
    def uvv(self) -> FVector3: ...

    @property
    def vvv(self) -> FVector3: ...



    @property
    def uuuu(self) -> FVector4: ...

    @property
    def uuuv(self) -> FVector4: ...

    @property
    def uuvv(self) -> FVector4: ...

    @property
    def uvvv(self) -> FVector4: ...

    @property
    def vvvv(self) -> FVector4: ...





    @property
    def magnitude(self) -> float: ...

    def cross(self, other: FVector2, /) -> FVector2: ...
    def normalize(self) -> float: ...
    def distance(self, other: FVector2, /) -> float: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...









@final
class I8Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __add__(self, other: Number) -> I8Vector2: ...
    @overload
    def __radd__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __radd__(self, other: Number) -> I8Vector2: ...

    @overload
    def __sub__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __sub__(self, other: Number) -> I8Vector2: ...
    @overload
    def __rsub__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> I8Vector2: ...

    @overload
    def __mul__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __mul__(self, other: Number) -> I8Vector2: ...
    @overload
    def __rmul__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> I8Vector2: ...




    @overload
    def __truediv__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> I8Vector2: ...
    @overload
    def __rtruediv__(self, other: I8Vector2) -> I8Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> I8Vector2: ...




    def __abs__(self) -> I8Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> I8Vector2: ...

    @property
    def xy(self) -> I8Vector2: ...

    @property
    def yy(self) -> I8Vector2: ...



    @property
    def xxx(self) -> I8Vector3: ...

    @property
    def xxy(self) -> I8Vector3: ...

    @property
    def xyy(self) -> I8Vector3: ...

    @property
    def yyy(self) -> I8Vector3: ...



    @property
    def xxxx(self) -> I8Vector4: ...

    @property
    def xxxy(self) -> I8Vector4: ...

    @property
    def xxyy(self) -> I8Vector4: ...

    @property
    def xyyy(self) -> I8Vector4: ...

    @property
    def yyyy(self) -> I8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> I8Vector2: ...

    @property
    def rg(self) -> I8Vector2: ...

    @property
    def gg(self) -> I8Vector2: ...



    @property
    def rrr(self) -> I8Vector3: ...

    @property
    def rrg(self) -> I8Vector3: ...

    @property
    def rgg(self) -> I8Vector3: ...

    @property
    def ggg(self) -> I8Vector3: ...



    @property
    def rrrr(self) -> I8Vector4: ...

    @property
    def rrrg(self) -> I8Vector4: ...

    @property
    def rrgg(self) -> I8Vector4: ...

    @property
    def rggg(self) -> I8Vector4: ...

    @property
    def gggg(self) -> I8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> I8Vector2: ...

    @property
    def st(self) -> I8Vector2: ...

    @property
    def tt(self) -> I8Vector2: ...



    @property
    def sss(self) -> I8Vector3: ...

    @property
    def sst(self) -> I8Vector3: ...

    @property
    def stt(self) -> I8Vector3: ...

    @property
    def ttt(self) -> I8Vector3: ...



    @property
    def ssss(self) -> I8Vector4: ...

    @property
    def ssst(self) -> I8Vector4: ...

    @property
    def sstt(self) -> I8Vector4: ...

    @property
    def sttt(self) -> I8Vector4: ...

    @property
    def tttt(self) -> I8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I8Vector2: ...

    @property
    def uv(self) -> I8Vector2: ...

    @property
    def vv(self) -> I8Vector2: ...



    @property
    def uuu(self) -> I8Vector3: ...

    @property
    def uuv(self) -> I8Vector3: ...

    @property
    def uvv(self) -> I8Vector3: ...

    @property
    def vvv(self) -> I8Vector3: ...



    @property
    def uuuu(self) -> I8Vector4: ...

    @property
    def uuuv(self) -> I8Vector4: ...

    @property
    def uuvv(self) -> I8Vector4: ...

    @property
    def uvvv(self) -> I8Vector4: ...

    @property
    def vvvv(self) -> I8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U8Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __add__(self, other: Number) -> U8Vector2: ...
    @overload
    def __radd__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __radd__(self, other: Number) -> U8Vector2: ...

    @overload
    def __sub__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __sub__(self, other: Number) -> U8Vector2: ...
    @overload
    def __rsub__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> U8Vector2: ...

    @overload
    def __mul__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __mul__(self, other: Number) -> U8Vector2: ...
    @overload
    def __rmul__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> U8Vector2: ...




    @overload
    def __truediv__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> U8Vector2: ...
    @overload
    def __rtruediv__(self, other: U8Vector2) -> U8Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> U8Vector2: ...



    def __neg__(self) -> U8Vector2: ...


    def __abs__(self) -> U8Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> U8Vector2: ...

    @property
    def xy(self) -> U8Vector2: ...

    @property
    def yy(self) -> U8Vector2: ...



    @property
    def xxx(self) -> U8Vector3: ...

    @property
    def xxy(self) -> U8Vector3: ...

    @property
    def xyy(self) -> U8Vector3: ...

    @property
    def yyy(self) -> U8Vector3: ...



    @property
    def xxxx(self) -> U8Vector4: ...

    @property
    def xxxy(self) -> U8Vector4: ...

    @property
    def xxyy(self) -> U8Vector4: ...

    @property
    def xyyy(self) -> U8Vector4: ...

    @property
    def yyyy(self) -> U8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> U8Vector2: ...

    @property
    def rg(self) -> U8Vector2: ...

    @property
    def gg(self) -> U8Vector2: ...



    @property
    def rrr(self) -> U8Vector3: ...

    @property
    def rrg(self) -> U8Vector3: ...

    @property
    def rgg(self) -> U8Vector3: ...

    @property
    def ggg(self) -> U8Vector3: ...



    @property
    def rrrr(self) -> U8Vector4: ...

    @property
    def rrrg(self) -> U8Vector4: ...

    @property
    def rrgg(self) -> U8Vector4: ...

    @property
    def rggg(self) -> U8Vector4: ...

    @property
    def gggg(self) -> U8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> U8Vector2: ...

    @property
    def st(self) -> U8Vector2: ...

    @property
    def tt(self) -> U8Vector2: ...



    @property
    def sss(self) -> U8Vector3: ...

    @property
    def sst(self) -> U8Vector3: ...

    @property
    def stt(self) -> U8Vector3: ...

    @property
    def ttt(self) -> U8Vector3: ...



    @property
    def ssss(self) -> U8Vector4: ...

    @property
    def ssst(self) -> U8Vector4: ...

    @property
    def sstt(self) -> U8Vector4: ...

    @property
    def sttt(self) -> U8Vector4: ...

    @property
    def tttt(self) -> U8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U8Vector2: ...

    @property
    def uv(self) -> U8Vector2: ...

    @property
    def vv(self) -> U8Vector2: ...



    @property
    def uuu(self) -> U8Vector3: ...

    @property
    def uuv(self) -> U8Vector3: ...

    @property
    def uvv(self) -> U8Vector3: ...

    @property
    def vvv(self) -> U8Vector3: ...



    @property
    def uuuu(self) -> U8Vector4: ...

    @property
    def uuuv(self) -> U8Vector4: ...

    @property
    def uuvv(self) -> U8Vector4: ...

    @property
    def uvvv(self) -> U8Vector4: ...

    @property
    def vvvv(self) -> U8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I16Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __add__(self, other: Number) -> I16Vector2: ...
    @overload
    def __radd__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __radd__(self, other: Number) -> I16Vector2: ...

    @overload
    def __sub__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __sub__(self, other: Number) -> I16Vector2: ...
    @overload
    def __rsub__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> I16Vector2: ...

    @overload
    def __mul__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __mul__(self, other: Number) -> I16Vector2: ...
    @overload
    def __rmul__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> I16Vector2: ...




    @overload
    def __truediv__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> I16Vector2: ...
    @overload
    def __rtruediv__(self, other: I16Vector2) -> I16Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> I16Vector2: ...




    def __abs__(self) -> I16Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> I16Vector2: ...

    @property
    def xy(self) -> I16Vector2: ...

    @property
    def yy(self) -> I16Vector2: ...



    @property
    def xxx(self) -> I16Vector3: ...

    @property
    def xxy(self) -> I16Vector3: ...

    @property
    def xyy(self) -> I16Vector3: ...

    @property
    def yyy(self) -> I16Vector3: ...



    @property
    def xxxx(self) -> I16Vector4: ...

    @property
    def xxxy(self) -> I16Vector4: ...

    @property
    def xxyy(self) -> I16Vector4: ...

    @property
    def xyyy(self) -> I16Vector4: ...

    @property
    def yyyy(self) -> I16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> I16Vector2: ...

    @property
    def rg(self) -> I16Vector2: ...

    @property
    def gg(self) -> I16Vector2: ...



    @property
    def rrr(self) -> I16Vector3: ...

    @property
    def rrg(self) -> I16Vector3: ...

    @property
    def rgg(self) -> I16Vector3: ...

    @property
    def ggg(self) -> I16Vector3: ...



    @property
    def rrrr(self) -> I16Vector4: ...

    @property
    def rrrg(self) -> I16Vector4: ...

    @property
    def rrgg(self) -> I16Vector4: ...

    @property
    def rggg(self) -> I16Vector4: ...

    @property
    def gggg(self) -> I16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> I16Vector2: ...

    @property
    def st(self) -> I16Vector2: ...

    @property
    def tt(self) -> I16Vector2: ...



    @property
    def sss(self) -> I16Vector3: ...

    @property
    def sst(self) -> I16Vector3: ...

    @property
    def stt(self) -> I16Vector3: ...

    @property
    def ttt(self) -> I16Vector3: ...



    @property
    def ssss(self) -> I16Vector4: ...

    @property
    def ssst(self) -> I16Vector4: ...

    @property
    def sstt(self) -> I16Vector4: ...

    @property
    def sttt(self) -> I16Vector4: ...

    @property
    def tttt(self) -> I16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I16Vector2: ...

    @property
    def uv(self) -> I16Vector2: ...

    @property
    def vv(self) -> I16Vector2: ...



    @property
    def uuu(self) -> I16Vector3: ...

    @property
    def uuv(self) -> I16Vector3: ...

    @property
    def uvv(self) -> I16Vector3: ...

    @property
    def vvv(self) -> I16Vector3: ...



    @property
    def uuuu(self) -> I16Vector4: ...

    @property
    def uuuv(self) -> I16Vector4: ...

    @property
    def uuvv(self) -> I16Vector4: ...

    @property
    def uvvv(self) -> I16Vector4: ...

    @property
    def vvvv(self) -> I16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U16Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __add__(self, other: Number) -> U16Vector2: ...
    @overload
    def __radd__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __radd__(self, other: Number) -> U16Vector2: ...

    @overload
    def __sub__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __sub__(self, other: Number) -> U16Vector2: ...
    @overload
    def __rsub__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> U16Vector2: ...

    @overload
    def __mul__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __mul__(self, other: Number) -> U16Vector2: ...
    @overload
    def __rmul__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> U16Vector2: ...




    @overload
    def __truediv__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> U16Vector2: ...
    @overload
    def __rtruediv__(self, other: U16Vector2) -> U16Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> U16Vector2: ...



    def __neg__(self) -> U16Vector2: ...


    def __abs__(self) -> U16Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> U16Vector2: ...

    @property
    def xy(self) -> U16Vector2: ...

    @property
    def yy(self) -> U16Vector2: ...



    @property
    def xxx(self) -> U16Vector3: ...

    @property
    def xxy(self) -> U16Vector3: ...

    @property
    def xyy(self) -> U16Vector3: ...

    @property
    def yyy(self) -> U16Vector3: ...



    @property
    def xxxx(self) -> U16Vector4: ...

    @property
    def xxxy(self) -> U16Vector4: ...

    @property
    def xxyy(self) -> U16Vector4: ...

    @property
    def xyyy(self) -> U16Vector4: ...

    @property
    def yyyy(self) -> U16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> U16Vector2: ...

    @property
    def rg(self) -> U16Vector2: ...

    @property
    def gg(self) -> U16Vector2: ...



    @property
    def rrr(self) -> U16Vector3: ...

    @property
    def rrg(self) -> U16Vector3: ...

    @property
    def rgg(self) -> U16Vector3: ...

    @property
    def ggg(self) -> U16Vector3: ...



    @property
    def rrrr(self) -> U16Vector4: ...

    @property
    def rrrg(self) -> U16Vector4: ...

    @property
    def rrgg(self) -> U16Vector4: ...

    @property
    def rggg(self) -> U16Vector4: ...

    @property
    def gggg(self) -> U16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> U16Vector2: ...

    @property
    def st(self) -> U16Vector2: ...

    @property
    def tt(self) -> U16Vector2: ...



    @property
    def sss(self) -> U16Vector3: ...

    @property
    def sst(self) -> U16Vector3: ...

    @property
    def stt(self) -> U16Vector3: ...

    @property
    def ttt(self) -> U16Vector3: ...



    @property
    def ssss(self) -> U16Vector4: ...

    @property
    def ssst(self) -> U16Vector4: ...

    @property
    def sstt(self) -> U16Vector4: ...

    @property
    def sttt(self) -> U16Vector4: ...

    @property
    def tttt(self) -> U16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U16Vector2: ...

    @property
    def uv(self) -> U16Vector2: ...

    @property
    def vv(self) -> U16Vector2: ...



    @property
    def uuu(self) -> U16Vector3: ...

    @property
    def uuv(self) -> U16Vector3: ...

    @property
    def uvv(self) -> U16Vector3: ...

    @property
    def vvv(self) -> U16Vector3: ...



    @property
    def uuuu(self) -> U16Vector4: ...

    @property
    def uuuv(self) -> U16Vector4: ...

    @property
    def uuvv(self) -> U16Vector4: ...

    @property
    def uvvv(self) -> U16Vector4: ...

    @property
    def vvvv(self) -> U16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I32Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __add__(self, other: Number) -> I32Vector2: ...
    @overload
    def __radd__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __radd__(self, other: Number) -> I32Vector2: ...

    @overload
    def __sub__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __sub__(self, other: Number) -> I32Vector2: ...
    @overload
    def __rsub__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> I32Vector2: ...

    @overload
    def __mul__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __mul__(self, other: Number) -> I32Vector2: ...
    @overload
    def __rmul__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> I32Vector2: ...




    @overload
    def __truediv__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> I32Vector2: ...
    @overload
    def __rtruediv__(self, other: I32Vector2) -> I32Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> I32Vector2: ...




    def __abs__(self) -> I32Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> I32Vector2: ...

    @property
    def xy(self) -> I32Vector2: ...

    @property
    def yy(self) -> I32Vector2: ...



    @property
    def xxx(self) -> I32Vector3: ...

    @property
    def xxy(self) -> I32Vector3: ...

    @property
    def xyy(self) -> I32Vector3: ...

    @property
    def yyy(self) -> I32Vector3: ...



    @property
    def xxxx(self) -> I32Vector4: ...

    @property
    def xxxy(self) -> I32Vector4: ...

    @property
    def xxyy(self) -> I32Vector4: ...

    @property
    def xyyy(self) -> I32Vector4: ...

    @property
    def yyyy(self) -> I32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> I32Vector2: ...

    @property
    def rg(self) -> I32Vector2: ...

    @property
    def gg(self) -> I32Vector2: ...



    @property
    def rrr(self) -> I32Vector3: ...

    @property
    def rrg(self) -> I32Vector3: ...

    @property
    def rgg(self) -> I32Vector3: ...

    @property
    def ggg(self) -> I32Vector3: ...



    @property
    def rrrr(self) -> I32Vector4: ...

    @property
    def rrrg(self) -> I32Vector4: ...

    @property
    def rrgg(self) -> I32Vector4: ...

    @property
    def rggg(self) -> I32Vector4: ...

    @property
    def gggg(self) -> I32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> I32Vector2: ...

    @property
    def st(self) -> I32Vector2: ...

    @property
    def tt(self) -> I32Vector2: ...



    @property
    def sss(self) -> I32Vector3: ...

    @property
    def sst(self) -> I32Vector3: ...

    @property
    def stt(self) -> I32Vector3: ...

    @property
    def ttt(self) -> I32Vector3: ...



    @property
    def ssss(self) -> I32Vector4: ...

    @property
    def ssst(self) -> I32Vector4: ...

    @property
    def sstt(self) -> I32Vector4: ...

    @property
    def sttt(self) -> I32Vector4: ...

    @property
    def tttt(self) -> I32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I32Vector2: ...

    @property
    def uv(self) -> I32Vector2: ...

    @property
    def vv(self) -> I32Vector2: ...



    @property
    def uuu(self) -> I32Vector3: ...

    @property
    def uuv(self) -> I32Vector3: ...

    @property
    def uvv(self) -> I32Vector3: ...

    @property
    def vvv(self) -> I32Vector3: ...



    @property
    def uuuu(self) -> I32Vector4: ...

    @property
    def uuuv(self) -> I32Vector4: ...

    @property
    def uuvv(self) -> I32Vector4: ...

    @property
    def uvvv(self) -> I32Vector4: ...

    @property
    def vvvv(self) -> I32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U32Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __add__(self, other: Number) -> U32Vector2: ...
    @overload
    def __radd__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __radd__(self, other: Number) -> U32Vector2: ...

    @overload
    def __sub__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __sub__(self, other: Number) -> U32Vector2: ...
    @overload
    def __rsub__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> U32Vector2: ...

    @overload
    def __mul__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __mul__(self, other: Number) -> U32Vector2: ...
    @overload
    def __rmul__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> U32Vector2: ...




    @overload
    def __truediv__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> U32Vector2: ...
    @overload
    def __rtruediv__(self, other: U32Vector2) -> U32Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> U32Vector2: ...



    def __neg__(self) -> U32Vector2: ...


    def __abs__(self) -> U32Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> U32Vector2: ...

    @property
    def xy(self) -> U32Vector2: ...

    @property
    def yy(self) -> U32Vector2: ...



    @property
    def xxx(self) -> U32Vector3: ...

    @property
    def xxy(self) -> U32Vector3: ...

    @property
    def xyy(self) -> U32Vector3: ...

    @property
    def yyy(self) -> U32Vector3: ...



    @property
    def xxxx(self) -> U32Vector4: ...

    @property
    def xxxy(self) -> U32Vector4: ...

    @property
    def xxyy(self) -> U32Vector4: ...

    @property
    def xyyy(self) -> U32Vector4: ...

    @property
    def yyyy(self) -> U32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> U32Vector2: ...

    @property
    def rg(self) -> U32Vector2: ...

    @property
    def gg(self) -> U32Vector2: ...



    @property
    def rrr(self) -> U32Vector3: ...

    @property
    def rrg(self) -> U32Vector3: ...

    @property
    def rgg(self) -> U32Vector3: ...

    @property
    def ggg(self) -> U32Vector3: ...



    @property
    def rrrr(self) -> U32Vector4: ...

    @property
    def rrrg(self) -> U32Vector4: ...

    @property
    def rrgg(self) -> U32Vector4: ...

    @property
    def rggg(self) -> U32Vector4: ...

    @property
    def gggg(self) -> U32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> U32Vector2: ...

    @property
    def st(self) -> U32Vector2: ...

    @property
    def tt(self) -> U32Vector2: ...



    @property
    def sss(self) -> U32Vector3: ...

    @property
    def sst(self) -> U32Vector3: ...

    @property
    def stt(self) -> U32Vector3: ...

    @property
    def ttt(self) -> U32Vector3: ...



    @property
    def ssss(self) -> U32Vector4: ...

    @property
    def ssst(self) -> U32Vector4: ...

    @property
    def sstt(self) -> U32Vector4: ...

    @property
    def sttt(self) -> U32Vector4: ...

    @property
    def tttt(self) -> U32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U32Vector2: ...

    @property
    def uv(self) -> U32Vector2: ...

    @property
    def vv(self) -> U32Vector2: ...



    @property
    def uuu(self) -> U32Vector3: ...

    @property
    def uuv(self) -> U32Vector3: ...

    @property
    def uvv(self) -> U32Vector3: ...

    @property
    def vvv(self) -> U32Vector3: ...



    @property
    def uuuu(self) -> U32Vector4: ...

    @property
    def uuuv(self) -> U32Vector4: ...

    @property
    def uuvv(self) -> U32Vector4: ...

    @property
    def uvvv(self) -> U32Vector4: ...

    @property
    def vvvv(self) -> U32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class IVector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: IVector2) -> IVector2: ...
    @overload
    def __add__(self, other: Number) -> IVector2: ...
    @overload
    def __radd__(self, other: IVector2) -> IVector2: ...
    @overload
    def __radd__(self, other: Number) -> IVector2: ...

    @overload
    def __sub__(self, other: IVector2) -> IVector2: ...
    @overload
    def __sub__(self, other: Number) -> IVector2: ...
    @overload
    def __rsub__(self, other: IVector2) -> IVector2: ...
    @overload
    def __rsub__(self, other: Number) -> IVector2: ...

    @overload
    def __mul__(self, other: IVector2) -> IVector2: ...
    @overload
    def __mul__(self, other: Number) -> IVector2: ...
    @overload
    def __rmul__(self, other: IVector2) -> IVector2: ...
    @overload
    def __rmul__(self, other: Number) -> IVector2: ...




    @overload
    def __truediv__(self, other: IVector2) -> IVector2: ...
    @overload
    def __truediv__(self, other: Number) -> IVector2: ...
    @overload
    def __rtruediv__(self, other: IVector2) -> IVector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> IVector2: ...




    def __abs__(self) -> IVector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> IVector2: ...

    @property
    def xy(self) -> IVector2: ...

    @property
    def yy(self) -> IVector2: ...



    @property
    def xxx(self) -> IVector3: ...

    @property
    def xxy(self) -> IVector3: ...

    @property
    def xyy(self) -> IVector3: ...

    @property
    def yyy(self) -> IVector3: ...



    @property
    def xxxx(self) -> IVector4: ...

    @property
    def xxxy(self) -> IVector4: ...

    @property
    def xxyy(self) -> IVector4: ...

    @property
    def xyyy(self) -> IVector4: ...

    @property
    def yyyy(self) -> IVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> IVector2: ...

    @property
    def rg(self) -> IVector2: ...

    @property
    def gg(self) -> IVector2: ...



    @property
    def rrr(self) -> IVector3: ...

    @property
    def rrg(self) -> IVector3: ...

    @property
    def rgg(self) -> IVector3: ...

    @property
    def ggg(self) -> IVector3: ...



    @property
    def rrrr(self) -> IVector4: ...

    @property
    def rrrg(self) -> IVector4: ...

    @property
    def rrgg(self) -> IVector4: ...

    @property
    def rggg(self) -> IVector4: ...

    @property
    def gggg(self) -> IVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> IVector2: ...

    @property
    def st(self) -> IVector2: ...

    @property
    def tt(self) -> IVector2: ...



    @property
    def sss(self) -> IVector3: ...

    @property
    def sst(self) -> IVector3: ...

    @property
    def stt(self) -> IVector3: ...

    @property
    def ttt(self) -> IVector3: ...



    @property
    def ssss(self) -> IVector4: ...

    @property
    def ssst(self) -> IVector4: ...

    @property
    def sstt(self) -> IVector4: ...

    @property
    def sttt(self) -> IVector4: ...

    @property
    def tttt(self) -> IVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> IVector2: ...

    @property
    def uv(self) -> IVector2: ...

    @property
    def vv(self) -> IVector2: ...



    @property
    def uuu(self) -> IVector3: ...

    @property
    def uuv(self) -> IVector3: ...

    @property
    def uvv(self) -> IVector3: ...

    @property
    def vvv(self) -> IVector3: ...



    @property
    def uuuu(self) -> IVector4: ...

    @property
    def uuuv(self) -> IVector4: ...

    @property
    def uuvv(self) -> IVector4: ...

    @property
    def uvvv(self) -> IVector4: ...

    @property
    def vvvv(self) -> IVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class UVector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: UVector2) -> UVector2: ...
    @overload
    def __add__(self, other: Number) -> UVector2: ...
    @overload
    def __radd__(self, other: UVector2) -> UVector2: ...
    @overload
    def __radd__(self, other: Number) -> UVector2: ...

    @overload
    def __sub__(self, other: UVector2) -> UVector2: ...
    @overload
    def __sub__(self, other: Number) -> UVector2: ...
    @overload
    def __rsub__(self, other: UVector2) -> UVector2: ...
    @overload
    def __rsub__(self, other: Number) -> UVector2: ...

    @overload
    def __mul__(self, other: UVector2) -> UVector2: ...
    @overload
    def __mul__(self, other: Number) -> UVector2: ...
    @overload
    def __rmul__(self, other: UVector2) -> UVector2: ...
    @overload
    def __rmul__(self, other: Number) -> UVector2: ...




    @overload
    def __truediv__(self, other: UVector2) -> UVector2: ...
    @overload
    def __truediv__(self, other: Number) -> UVector2: ...
    @overload
    def __rtruediv__(self, other: UVector2) -> UVector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> UVector2: ...



    def __neg__(self) -> UVector2: ...


    def __abs__(self) -> UVector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> UVector2: ...

    @property
    def xy(self) -> UVector2: ...

    @property
    def yy(self) -> UVector2: ...



    @property
    def xxx(self) -> UVector3: ...

    @property
    def xxy(self) -> UVector3: ...

    @property
    def xyy(self) -> UVector3: ...

    @property
    def yyy(self) -> UVector3: ...



    @property
    def xxxx(self) -> UVector4: ...

    @property
    def xxxy(self) -> UVector4: ...

    @property
    def xxyy(self) -> UVector4: ...

    @property
    def xyyy(self) -> UVector4: ...

    @property
    def yyyy(self) -> UVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> UVector2: ...

    @property
    def rg(self) -> UVector2: ...

    @property
    def gg(self) -> UVector2: ...



    @property
    def rrr(self) -> UVector3: ...

    @property
    def rrg(self) -> UVector3: ...

    @property
    def rgg(self) -> UVector3: ...

    @property
    def ggg(self) -> UVector3: ...



    @property
    def rrrr(self) -> UVector4: ...

    @property
    def rrrg(self) -> UVector4: ...

    @property
    def rrgg(self) -> UVector4: ...

    @property
    def rggg(self) -> UVector4: ...

    @property
    def gggg(self) -> UVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> UVector2: ...

    @property
    def st(self) -> UVector2: ...

    @property
    def tt(self) -> UVector2: ...



    @property
    def sss(self) -> UVector3: ...

    @property
    def sst(self) -> UVector3: ...

    @property
    def stt(self) -> UVector3: ...

    @property
    def ttt(self) -> UVector3: ...



    @property
    def ssss(self) -> UVector4: ...

    @property
    def ssst(self) -> UVector4: ...

    @property
    def sstt(self) -> UVector4: ...

    @property
    def sttt(self) -> UVector4: ...

    @property
    def tttt(self) -> UVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> UVector2: ...

    @property
    def uv(self) -> UVector2: ...

    @property
    def vv(self) -> UVector2: ...



    @property
    def uuu(self) -> UVector3: ...

    @property
    def uuv(self) -> UVector3: ...

    @property
    def uvv(self) -> UVector3: ...

    @property
    def vvv(self) -> UVector3: ...



    @property
    def uuuu(self) -> UVector4: ...

    @property
    def uuuv(self) -> UVector4: ...

    @property
    def uuvv(self) -> UVector4: ...

    @property
    def uvvv(self) -> UVector4: ...

    @property
    def vvvv(self) -> UVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I64Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __add__(self, other: Number) -> I64Vector2: ...
    @overload
    def __radd__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __radd__(self, other: Number) -> I64Vector2: ...

    @overload
    def __sub__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __sub__(self, other: Number) -> I64Vector2: ...
    @overload
    def __rsub__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> I64Vector2: ...

    @overload
    def __mul__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __mul__(self, other: Number) -> I64Vector2: ...
    @overload
    def __rmul__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> I64Vector2: ...




    @overload
    def __truediv__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> I64Vector2: ...
    @overload
    def __rtruediv__(self, other: I64Vector2) -> I64Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> I64Vector2: ...




    def __abs__(self) -> I64Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> I64Vector2: ...

    @property
    def xy(self) -> I64Vector2: ...

    @property
    def yy(self) -> I64Vector2: ...



    @property
    def xxx(self) -> I64Vector3: ...

    @property
    def xxy(self) -> I64Vector3: ...

    @property
    def xyy(self) -> I64Vector3: ...

    @property
    def yyy(self) -> I64Vector3: ...



    @property
    def xxxx(self) -> I64Vector4: ...

    @property
    def xxxy(self) -> I64Vector4: ...

    @property
    def xxyy(self) -> I64Vector4: ...

    @property
    def xyyy(self) -> I64Vector4: ...

    @property
    def yyyy(self) -> I64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> I64Vector2: ...

    @property
    def rg(self) -> I64Vector2: ...

    @property
    def gg(self) -> I64Vector2: ...



    @property
    def rrr(self) -> I64Vector3: ...

    @property
    def rrg(self) -> I64Vector3: ...

    @property
    def rgg(self) -> I64Vector3: ...

    @property
    def ggg(self) -> I64Vector3: ...



    @property
    def rrrr(self) -> I64Vector4: ...

    @property
    def rrrg(self) -> I64Vector4: ...

    @property
    def rrgg(self) -> I64Vector4: ...

    @property
    def rggg(self) -> I64Vector4: ...

    @property
    def gggg(self) -> I64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> I64Vector2: ...

    @property
    def st(self) -> I64Vector2: ...

    @property
    def tt(self) -> I64Vector2: ...



    @property
    def sss(self) -> I64Vector3: ...

    @property
    def sst(self) -> I64Vector3: ...

    @property
    def stt(self) -> I64Vector3: ...

    @property
    def ttt(self) -> I64Vector3: ...



    @property
    def ssss(self) -> I64Vector4: ...

    @property
    def ssst(self) -> I64Vector4: ...

    @property
    def sstt(self) -> I64Vector4: ...

    @property
    def sttt(self) -> I64Vector4: ...

    @property
    def tttt(self) -> I64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I64Vector2: ...

    @property
    def uv(self) -> I64Vector2: ...

    @property
    def vv(self) -> I64Vector2: ...



    @property
    def uuu(self) -> I64Vector3: ...

    @property
    def uuv(self) -> I64Vector3: ...

    @property
    def uvv(self) -> I64Vector3: ...

    @property
    def vvv(self) -> I64Vector3: ...



    @property
    def uuuu(self) -> I64Vector4: ...

    @property
    def uuuv(self) -> I64Vector4: ...

    @property
    def uuvv(self) -> I64Vector4: ...

    @property
    def uvvv(self) -> I64Vector4: ...

    @property
    def vvvv(self) -> I64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U64Vector2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...


    @overload
    def __init__(self, x: Number, y: Number, /): ...




    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __add__(self, other: Number) -> U64Vector2: ...
    @overload
    def __radd__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __radd__(self, other: Number) -> U64Vector2: ...

    @overload
    def __sub__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __sub__(self, other: Number) -> U64Vector2: ...
    @overload
    def __rsub__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __rsub__(self, other: Number) -> U64Vector2: ...

    @overload
    def __mul__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __mul__(self, other: Number) -> U64Vector2: ...
    @overload
    def __rmul__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __rmul__(self, other: Number) -> U64Vector2: ...




    @overload
    def __truediv__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __truediv__(self, other: Number) -> U64Vector2: ...
    @overload
    def __rtruediv__(self, other: U64Vector2) -> U64Vector2: ...
    @overload
    def __rtruediv__(self, other: Number) -> U64Vector2: ...



    def __neg__(self) -> U64Vector2: ...


    def __abs__(self) -> U64Vector2: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...



    @property
    def xx(self) -> U64Vector2: ...

    @property
    def xy(self) -> U64Vector2: ...

    @property
    def yy(self) -> U64Vector2: ...



    @property
    def xxx(self) -> U64Vector3: ...

    @property
    def xxy(self) -> U64Vector3: ...

    @property
    def xyy(self) -> U64Vector3: ...

    @property
    def yyy(self) -> U64Vector3: ...



    @property
    def xxxx(self) -> U64Vector4: ...

    @property
    def xxxy(self) -> U64Vector4: ...

    @property
    def xxyy(self) -> U64Vector4: ...

    @property
    def xyyy(self) -> U64Vector4: ...

    @property
    def yyyy(self) -> U64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...



    @property
    def rr(self) -> U64Vector2: ...

    @property
    def rg(self) -> U64Vector2: ...

    @property
    def gg(self) -> U64Vector2: ...



    @property
    def rrr(self) -> U64Vector3: ...

    @property
    def rrg(self) -> U64Vector3: ...

    @property
    def rgg(self) -> U64Vector3: ...

    @property
    def ggg(self) -> U64Vector3: ...



    @property
    def rrrr(self) -> U64Vector4: ...

    @property
    def rrrg(self) -> U64Vector4: ...

    @property
    def rrgg(self) -> U64Vector4: ...

    @property
    def rggg(self) -> U64Vector4: ...

    @property
    def gggg(self) -> U64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...



    @property
    def ss(self) -> U64Vector2: ...

    @property
    def st(self) -> U64Vector2: ...

    @property
    def tt(self) -> U64Vector2: ...



    @property
    def sss(self) -> U64Vector3: ...

    @property
    def sst(self) -> U64Vector3: ...

    @property
    def stt(self) -> U64Vector3: ...

    @property
    def ttt(self) -> U64Vector3: ...



    @property
    def ssss(self) -> U64Vector4: ...

    @property
    def ssst(self) -> U64Vector4: ...

    @property
    def sstt(self) -> U64Vector4: ...

    @property
    def sttt(self) -> U64Vector4: ...

    @property
    def tttt(self) -> U64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U64Vector2: ...

    @property
    def uv(self) -> U64Vector2: ...

    @property
    def vv(self) -> U64Vector2: ...



    @property
    def uuu(self) -> U64Vector3: ...

    @property
    def uuv(self) -> U64Vector3: ...

    @property
    def uvv(self) -> U64Vector3: ...

    @property
    def vvv(self) -> U64Vector3: ...



    @property
    def uuuu(self) -> U64Vector4: ...

    @property
    def uuuv(self) -> U64Vector4: ...

    @property
    def uuvv(self) -> U64Vector4: ...

    @property
    def uvvv(self) -> U64Vector4: ...

    @property
    def vvvv(self) -> U64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class BVector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: BVector3) -> BVector3: ...
    @overload
    def __add__(self, other: Number) -> BVector3: ...
    @overload
    def __radd__(self, other: BVector3) -> BVector3: ...
    @overload
    def __radd__(self, other: Number) -> BVector3: ...

    @overload
    def __sub__(self, other: BVector3) -> BVector3: ...
    @overload
    def __sub__(self, other: Number) -> BVector3: ...
    @overload
    def __rsub__(self, other: BVector3) -> BVector3: ...
    @overload
    def __rsub__(self, other: Number) -> BVector3: ...

    @overload
    def __mul__(self, other: BVector3) -> BVector3: ...
    @overload
    def __mul__(self, other: Number) -> BVector3: ...
    @overload
    def __rmul__(self, other: BVector3) -> BVector3: ...
    @overload
    def __rmul__(self, other: Number) -> BVector3: ...







    def __abs__(self) -> BVector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> bool: ...

    @property
    def y(self) -> bool: ...

    @property
    def z(self) -> bool: ...



    @property
    def xx(self) -> BVector2: ...

    @property
    def xy(self) -> BVector2: ...

    @property
    def xz(self) -> BVector2: ...

    @property
    def yy(self) -> BVector2: ...

    @property
    def yz(self) -> BVector2: ...

    @property
    def zz(self) -> BVector2: ...



    @property
    def xxx(self) -> BVector3: ...

    @property
    def xxy(self) -> BVector3: ...

    @property
    def xxz(self) -> BVector3: ...

    @property
    def xyy(self) -> BVector3: ...

    @property
    def xyz(self) -> BVector3: ...

    @property
    def xzz(self) -> BVector3: ...

    @property
    def yyy(self) -> BVector3: ...

    @property
    def yyz(self) -> BVector3: ...

    @property
    def yzz(self) -> BVector3: ...

    @property
    def zzz(self) -> BVector3: ...



    @property
    def xxxx(self) -> BVector4: ...

    @property
    def xxxy(self) -> BVector4: ...

    @property
    def xxxz(self) -> BVector4: ...

    @property
    def xxyy(self) -> BVector4: ...

    @property
    def xxyz(self) -> BVector4: ...

    @property
    def xxzz(self) -> BVector4: ...

    @property
    def xyyy(self) -> BVector4: ...

    @property
    def xyyz(self) -> BVector4: ...

    @property
    def xyzz(self) -> BVector4: ...

    @property
    def xzzz(self) -> BVector4: ...

    @property
    def yyyy(self) -> BVector4: ...

    @property
    def yyyz(self) -> BVector4: ...

    @property
    def yyzz(self) -> BVector4: ...

    @property
    def yzzz(self) -> BVector4: ...

    @property
    def zzzz(self) -> BVector4: ...





    @property
    def r(self) -> bool: ...

    @property
    def g(self) -> bool: ...

    @property
    def b(self) -> bool: ...



    @property
    def rr(self) -> BVector2: ...

    @property
    def rg(self) -> BVector2: ...

    @property
    def rb(self) -> BVector2: ...

    @property
    def gg(self) -> BVector2: ...

    @property
    def gb(self) -> BVector2: ...

    @property
    def bb(self) -> BVector2: ...



    @property
    def rrr(self) -> BVector3: ...

    @property
    def rrg(self) -> BVector3: ...

    @property
    def rrb(self) -> BVector3: ...

    @property
    def rgg(self) -> BVector3: ...

    @property
    def rgb(self) -> BVector3: ...

    @property
    def rbb(self) -> BVector3: ...

    @property
    def ggg(self) -> BVector3: ...

    @property
    def ggb(self) -> BVector3: ...

    @property
    def gbb(self) -> BVector3: ...

    @property
    def bbb(self) -> BVector3: ...



    @property
    def rrrr(self) -> BVector4: ...

    @property
    def rrrg(self) -> BVector4: ...

    @property
    def rrrb(self) -> BVector4: ...

    @property
    def rrgg(self) -> BVector4: ...

    @property
    def rrgb(self) -> BVector4: ...

    @property
    def rrbb(self) -> BVector4: ...

    @property
    def rggg(self) -> BVector4: ...

    @property
    def rggb(self) -> BVector4: ...

    @property
    def rgbb(self) -> BVector4: ...

    @property
    def rbbb(self) -> BVector4: ...

    @property
    def gggg(self) -> BVector4: ...

    @property
    def gggb(self) -> BVector4: ...

    @property
    def ggbb(self) -> BVector4: ...

    @property
    def gbbb(self) -> BVector4: ...

    @property
    def bbbb(self) -> BVector4: ...





    @property
    def s(self) -> bool: ...

    @property
    def t(self) -> bool: ...

    @property
    def q(self) -> bool: ...



    @property
    def ss(self) -> BVector2: ...

    @property
    def st(self) -> BVector2: ...

    @property
    def sq(self) -> BVector2: ...

    @property
    def tt(self) -> BVector2: ...

    @property
    def tq(self) -> BVector2: ...

    @property
    def qq(self) -> BVector2: ...



    @property
    def sss(self) -> BVector3: ...

    @property
    def sst(self) -> BVector3: ...

    @property
    def ssq(self) -> BVector3: ...

    @property
    def stt(self) -> BVector3: ...

    @property
    def stq(self) -> BVector3: ...

    @property
    def sqq(self) -> BVector3: ...

    @property
    def ttt(self) -> BVector3: ...

    @property
    def ttq(self) -> BVector3: ...

    @property
    def tqq(self) -> BVector3: ...

    @property
    def qqq(self) -> BVector3: ...



    @property
    def ssss(self) -> BVector4: ...

    @property
    def ssst(self) -> BVector4: ...

    @property
    def sssq(self) -> BVector4: ...

    @property
    def sstt(self) -> BVector4: ...

    @property
    def sstq(self) -> BVector4: ...

    @property
    def ssqq(self) -> BVector4: ...

    @property
    def sttt(self) -> BVector4: ...

    @property
    def sttq(self) -> BVector4: ...

    @property
    def stqq(self) -> BVector4: ...

    @property
    def sqqq(self) -> BVector4: ...

    @property
    def tttt(self) -> BVector4: ...

    @property
    def tttq(self) -> BVector4: ...

    @property
    def ttqq(self) -> BVector4: ...

    @property
    def tqqq(self) -> BVector4: ...

    @property
    def qqqq(self) -> BVector4: ...





    @property
    def u(self) -> bool: ...

    @property
    def v(self) -> bool: ...



    @property
    def uu(self) -> BVector2: ...

    @property
    def uv(self) -> BVector2: ...

    @property
    def vv(self) -> BVector2: ...



    @property
    def uuu(self) -> BVector3: ...

    @property
    def uuv(self) -> BVector3: ...

    @property
    def uvv(self) -> BVector3: ...

    @property
    def vvv(self) -> BVector3: ...



    @property
    def uuuu(self) -> BVector4: ...

    @property
    def uuuv(self) -> BVector4: ...

    @property
    def uuvv(self) -> BVector4: ...

    @property
    def uvvv(self) -> BVector4: ...

    @property
    def vvvv(self) -> BVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[bool, bool]: ...









@final
class DVector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DVector3) -> DVector3: ...
    @overload
    def __add__(self, other: Number) -> DVector3: ...
    @overload
    def __radd__(self, other: DVector3) -> DVector3: ...
    @overload
    def __radd__(self, other: Number) -> DVector3: ...

    @overload
    def __sub__(self, other: DVector3) -> DVector3: ...
    @overload
    def __sub__(self, other: Number) -> DVector3: ...
    @overload
    def __rsub__(self, other: DVector3) -> DVector3: ...
    @overload
    def __rsub__(self, other: Number) -> DVector3: ...

    @overload
    def __mul__(self, other: DVector3) -> DVector3: ...
    @overload
    def __mul__(self, other: Number) -> DVector3: ...
    @overload
    def __rmul__(self, other: DVector3) -> DVector3: ...
    @overload
    def __rmul__(self, other: Number) -> DVector3: ...




    @overload
    def __truediv__(self, other: DVector3) -> DVector3: ...
    @overload
    def __truediv__(self, other: Number) -> DVector3: ...
    @overload
    def __rtruediv__(self, other: DVector3) -> DVector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> DVector3: ...




    def __abs__(self) -> DVector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> DVector2: ...

    @property
    def xy(self) -> DVector2: ...

    @property
    def xz(self) -> DVector2: ...

    @property
    def yy(self) -> DVector2: ...

    @property
    def yz(self) -> DVector2: ...

    @property
    def zz(self) -> DVector2: ...



    @property
    def xxx(self) -> DVector3: ...

    @property
    def xxy(self) -> DVector3: ...

    @property
    def xxz(self) -> DVector3: ...

    @property
    def xyy(self) -> DVector3: ...

    @property
    def xyz(self) -> DVector3: ...

    @property
    def xzz(self) -> DVector3: ...

    @property
    def yyy(self) -> DVector3: ...

    @property
    def yyz(self) -> DVector3: ...

    @property
    def yzz(self) -> DVector3: ...

    @property
    def zzz(self) -> DVector3: ...



    @property
    def xxxx(self) -> DVector4: ...

    @property
    def xxxy(self) -> DVector4: ...

    @property
    def xxxz(self) -> DVector4: ...

    @property
    def xxyy(self) -> DVector4: ...

    @property
    def xxyz(self) -> DVector4: ...

    @property
    def xxzz(self) -> DVector4: ...

    @property
    def xyyy(self) -> DVector4: ...

    @property
    def xyyz(self) -> DVector4: ...

    @property
    def xyzz(self) -> DVector4: ...

    @property
    def xzzz(self) -> DVector4: ...

    @property
    def yyyy(self) -> DVector4: ...

    @property
    def yyyz(self) -> DVector4: ...

    @property
    def yyzz(self) -> DVector4: ...

    @property
    def yzzz(self) -> DVector4: ...

    @property
    def zzzz(self) -> DVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> DVector2: ...

    @property
    def rg(self) -> DVector2: ...

    @property
    def rb(self) -> DVector2: ...

    @property
    def gg(self) -> DVector2: ...

    @property
    def gb(self) -> DVector2: ...

    @property
    def bb(self) -> DVector2: ...



    @property
    def rrr(self) -> DVector3: ...

    @property
    def rrg(self) -> DVector3: ...

    @property
    def rrb(self) -> DVector3: ...

    @property
    def rgg(self) -> DVector3: ...

    @property
    def rgb(self) -> DVector3: ...

    @property
    def rbb(self) -> DVector3: ...

    @property
    def ggg(self) -> DVector3: ...

    @property
    def ggb(self) -> DVector3: ...

    @property
    def gbb(self) -> DVector3: ...

    @property
    def bbb(self) -> DVector3: ...



    @property
    def rrrr(self) -> DVector4: ...

    @property
    def rrrg(self) -> DVector4: ...

    @property
    def rrrb(self) -> DVector4: ...

    @property
    def rrgg(self) -> DVector4: ...

    @property
    def rrgb(self) -> DVector4: ...

    @property
    def rrbb(self) -> DVector4: ...

    @property
    def rggg(self) -> DVector4: ...

    @property
    def rggb(self) -> DVector4: ...

    @property
    def rgbb(self) -> DVector4: ...

    @property
    def rbbb(self) -> DVector4: ...

    @property
    def gggg(self) -> DVector4: ...

    @property
    def gggb(self) -> DVector4: ...

    @property
    def ggbb(self) -> DVector4: ...

    @property
    def gbbb(self) -> DVector4: ...

    @property
    def bbbb(self) -> DVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> DVector2: ...

    @property
    def st(self) -> DVector2: ...

    @property
    def sq(self) -> DVector2: ...

    @property
    def tt(self) -> DVector2: ...

    @property
    def tq(self) -> DVector2: ...

    @property
    def qq(self) -> DVector2: ...



    @property
    def sss(self) -> DVector3: ...

    @property
    def sst(self) -> DVector3: ...

    @property
    def ssq(self) -> DVector3: ...

    @property
    def stt(self) -> DVector3: ...

    @property
    def stq(self) -> DVector3: ...

    @property
    def sqq(self) -> DVector3: ...

    @property
    def ttt(self) -> DVector3: ...

    @property
    def ttq(self) -> DVector3: ...

    @property
    def tqq(self) -> DVector3: ...

    @property
    def qqq(self) -> DVector3: ...



    @property
    def ssss(self) -> DVector4: ...

    @property
    def ssst(self) -> DVector4: ...

    @property
    def sssq(self) -> DVector4: ...

    @property
    def sstt(self) -> DVector4: ...

    @property
    def sstq(self) -> DVector4: ...

    @property
    def ssqq(self) -> DVector4: ...

    @property
    def sttt(self) -> DVector4: ...

    @property
    def sttq(self) -> DVector4: ...

    @property
    def stqq(self) -> DVector4: ...

    @property
    def sqqq(self) -> DVector4: ...

    @property
    def tttt(self) -> DVector4: ...

    @property
    def tttq(self) -> DVector4: ...

    @property
    def ttqq(self) -> DVector4: ...

    @property
    def tqqq(self) -> DVector4: ...

    @property
    def qqqq(self) -> DVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> DVector2: ...

    @property
    def uv(self) -> DVector2: ...

    @property
    def vv(self) -> DVector2: ...



    @property
    def uuu(self) -> DVector3: ...

    @property
    def uuv(self) -> DVector3: ...

    @property
    def uvv(self) -> DVector3: ...

    @property
    def vvv(self) -> DVector3: ...



    @property
    def uuuu(self) -> DVector4: ...

    @property
    def uuuv(self) -> DVector4: ...

    @property
    def uuvv(self) -> DVector4: ...

    @property
    def uvvv(self) -> DVector4: ...

    @property
    def vvvv(self) -> DVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class FVector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> float: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FVector3) -> FVector3: ...
    @overload
    def __add__(self, other: Number) -> FVector3: ...
    @overload
    def __radd__(self, other: FVector3) -> FVector3: ...
    @overload
    def __radd__(self, other: Number) -> FVector3: ...

    @overload
    def __sub__(self, other: FVector3) -> FVector3: ...
    @overload
    def __sub__(self, other: Number) -> FVector3: ...
    @overload
    def __rsub__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rsub__(self, other: Number) -> FVector3: ...

    @overload
    def __mul__(self, other: FVector3) -> FVector3: ...
    @overload
    def __mul__(self, other: Number) -> FVector3: ...
    @overload
    def __rmul__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rmul__(self, other: Number) -> FVector3: ...


    def __matmul__(self, other: FVector3) -> FVector3: ...
    def __rmatmul__(self, other: FVector3) -> FVector3: ...

    @overload
    def __mod__(self, other: FVector3) -> FVector3: ...
    @overload
    def __mod__(self, other: Number) -> FVector3: ...
    @overload
    def __rmod__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rmod__(self, other: Number) -> FVector3: ...

    @overload
    def __pow__(self, other: FVector3) -> FVector3: ...
    @overload
    def __pow__(self, other: Number) -> FVector3: ...
    @overload
    def __rpow__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rpow__(self, other: Number) -> FVector3: ...



    @overload
    def __truediv__(self, other: FVector3) -> FVector3: ...
    @overload
    def __truediv__(self, other: Number) -> FVector3: ...
    @overload
    def __rtruediv__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> FVector3: ...




    def __abs__(self) -> FVector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...

    @property
    def z(self) -> float: ...



    @property
    def xx(self) -> FVector2: ...

    @property
    def xy(self) -> FVector2: ...

    @property
    def xz(self) -> FVector2: ...

    @property
    def yy(self) -> FVector2: ...

    @property
    def yz(self) -> FVector2: ...

    @property
    def zz(self) -> FVector2: ...



    @property
    def xxx(self) -> FVector3: ...

    @property
    def xxy(self) -> FVector3: ...

    @property
    def xxz(self) -> FVector3: ...

    @property
    def xyy(self) -> FVector3: ...

    @property
    def xyz(self) -> FVector3: ...

    @property
    def xzz(self) -> FVector3: ...

    @property
    def yyy(self) -> FVector3: ...

    @property
    def yyz(self) -> FVector3: ...

    @property
    def yzz(self) -> FVector3: ...

    @property
    def zzz(self) -> FVector3: ...



    @property
    def xxxx(self) -> FVector4: ...

    @property
    def xxxy(self) -> FVector4: ...

    @property
    def xxxz(self) -> FVector4: ...

    @property
    def xxyy(self) -> FVector4: ...

    @property
    def xxyz(self) -> FVector4: ...

    @property
    def xxzz(self) -> FVector4: ...

    @property
    def xyyy(self) -> FVector4: ...

    @property
    def xyyz(self) -> FVector4: ...

    @property
    def xyzz(self) -> FVector4: ...

    @property
    def xzzz(self) -> FVector4: ...

    @property
    def yyyy(self) -> FVector4: ...

    @property
    def yyyz(self) -> FVector4: ...

    @property
    def yyzz(self) -> FVector4: ...

    @property
    def yzzz(self) -> FVector4: ...

    @property
    def zzzz(self) -> FVector4: ...





    @property
    def r(self) -> float: ...

    @property
    def g(self) -> float: ...

    @property
    def b(self) -> float: ...



    @property
    def rr(self) -> FVector2: ...

    @property
    def rg(self) -> FVector2: ...

    @property
    def rb(self) -> FVector2: ...

    @property
    def gg(self) -> FVector2: ...

    @property
    def gb(self) -> FVector2: ...

    @property
    def bb(self) -> FVector2: ...



    @property
    def rrr(self) -> FVector3: ...

    @property
    def rrg(self) -> FVector3: ...

    @property
    def rrb(self) -> FVector3: ...

    @property
    def rgg(self) -> FVector3: ...

    @property
    def rgb(self) -> FVector3: ...

    @property
    def rbb(self) -> FVector3: ...

    @property
    def ggg(self) -> FVector3: ...

    @property
    def ggb(self) -> FVector3: ...

    @property
    def gbb(self) -> FVector3: ...

    @property
    def bbb(self) -> FVector3: ...



    @property
    def rrrr(self) -> FVector4: ...

    @property
    def rrrg(self) -> FVector4: ...

    @property
    def rrrb(self) -> FVector4: ...

    @property
    def rrgg(self) -> FVector4: ...

    @property
    def rrgb(self) -> FVector4: ...

    @property
    def rrbb(self) -> FVector4: ...

    @property
    def rggg(self) -> FVector4: ...

    @property
    def rggb(self) -> FVector4: ...

    @property
    def rgbb(self) -> FVector4: ...

    @property
    def rbbb(self) -> FVector4: ...

    @property
    def gggg(self) -> FVector4: ...

    @property
    def gggb(self) -> FVector4: ...

    @property
    def ggbb(self) -> FVector4: ...

    @property
    def gbbb(self) -> FVector4: ...

    @property
    def bbbb(self) -> FVector4: ...





    @property
    def s(self) -> float: ...

    @property
    def t(self) -> float: ...

    @property
    def q(self) -> float: ...



    @property
    def ss(self) -> FVector2: ...

    @property
    def st(self) -> FVector2: ...

    @property
    def sq(self) -> FVector2: ...

    @property
    def tt(self) -> FVector2: ...

    @property
    def tq(self) -> FVector2: ...

    @property
    def qq(self) -> FVector2: ...



    @property
    def sss(self) -> FVector3: ...

    @property
    def sst(self) -> FVector3: ...

    @property
    def ssq(self) -> FVector3: ...

    @property
    def stt(self) -> FVector3: ...

    @property
    def stq(self) -> FVector3: ...

    @property
    def sqq(self) -> FVector3: ...

    @property
    def ttt(self) -> FVector3: ...

    @property
    def ttq(self) -> FVector3: ...

    @property
    def tqq(self) -> FVector3: ...

    @property
    def qqq(self) -> FVector3: ...



    @property
    def ssss(self) -> FVector4: ...

    @property
    def ssst(self) -> FVector4: ...

    @property
    def sssq(self) -> FVector4: ...

    @property
    def sstt(self) -> FVector4: ...

    @property
    def sstq(self) -> FVector4: ...

    @property
    def ssqq(self) -> FVector4: ...

    @property
    def sttt(self) -> FVector4: ...

    @property
    def sttq(self) -> FVector4: ...

    @property
    def stqq(self) -> FVector4: ...

    @property
    def sqqq(self) -> FVector4: ...

    @property
    def tttt(self) -> FVector4: ...

    @property
    def tttq(self) -> FVector4: ...

    @property
    def ttqq(self) -> FVector4: ...

    @property
    def tqqq(self) -> FVector4: ...

    @property
    def qqqq(self) -> FVector4: ...





    @property
    def u(self) -> float: ...

    @property
    def v(self) -> float: ...



    @property
    def uu(self) -> FVector2: ...

    @property
    def uv(self) -> FVector2: ...

    @property
    def vv(self) -> FVector2: ...



    @property
    def uuu(self) -> FVector3: ...

    @property
    def uuv(self) -> FVector3: ...

    @property
    def uvv(self) -> FVector3: ...

    @property
    def vvv(self) -> FVector3: ...



    @property
    def uuuu(self) -> FVector4: ...

    @property
    def uuuv(self) -> FVector4: ...

    @property
    def uuvv(self) -> FVector4: ...

    @property
    def uvvv(self) -> FVector4: ...

    @property
    def vvvv(self) -> FVector4: ...





    @property
    def magnitude(self) -> float: ...

    def cross(self, other: FVector3, /) -> FVector3: ...
    def normalize(self) -> float: ...
    def distance(self, other: FVector3, /) -> float: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...









@final
class I8Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __add__(self, other: Number) -> I8Vector3: ...
    @overload
    def __radd__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __radd__(self, other: Number) -> I8Vector3: ...

    @overload
    def __sub__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __sub__(self, other: Number) -> I8Vector3: ...
    @overload
    def __rsub__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> I8Vector3: ...

    @overload
    def __mul__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __mul__(self, other: Number) -> I8Vector3: ...
    @overload
    def __rmul__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> I8Vector3: ...




    @overload
    def __truediv__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> I8Vector3: ...
    @overload
    def __rtruediv__(self, other: I8Vector3) -> I8Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> I8Vector3: ...




    def __abs__(self) -> I8Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> I8Vector2: ...

    @property
    def xy(self) -> I8Vector2: ...

    @property
    def xz(self) -> I8Vector2: ...

    @property
    def yy(self) -> I8Vector2: ...

    @property
    def yz(self) -> I8Vector2: ...

    @property
    def zz(self) -> I8Vector2: ...



    @property
    def xxx(self) -> I8Vector3: ...

    @property
    def xxy(self) -> I8Vector3: ...

    @property
    def xxz(self) -> I8Vector3: ...

    @property
    def xyy(self) -> I8Vector3: ...

    @property
    def xyz(self) -> I8Vector3: ...

    @property
    def xzz(self) -> I8Vector3: ...

    @property
    def yyy(self) -> I8Vector3: ...

    @property
    def yyz(self) -> I8Vector3: ...

    @property
    def yzz(self) -> I8Vector3: ...

    @property
    def zzz(self) -> I8Vector3: ...



    @property
    def xxxx(self) -> I8Vector4: ...

    @property
    def xxxy(self) -> I8Vector4: ...

    @property
    def xxxz(self) -> I8Vector4: ...

    @property
    def xxyy(self) -> I8Vector4: ...

    @property
    def xxyz(self) -> I8Vector4: ...

    @property
    def xxzz(self) -> I8Vector4: ...

    @property
    def xyyy(self) -> I8Vector4: ...

    @property
    def xyyz(self) -> I8Vector4: ...

    @property
    def xyzz(self) -> I8Vector4: ...

    @property
    def xzzz(self) -> I8Vector4: ...

    @property
    def yyyy(self) -> I8Vector4: ...

    @property
    def yyyz(self) -> I8Vector4: ...

    @property
    def yyzz(self) -> I8Vector4: ...

    @property
    def yzzz(self) -> I8Vector4: ...

    @property
    def zzzz(self) -> I8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> I8Vector2: ...

    @property
    def rg(self) -> I8Vector2: ...

    @property
    def rb(self) -> I8Vector2: ...

    @property
    def gg(self) -> I8Vector2: ...

    @property
    def gb(self) -> I8Vector2: ...

    @property
    def bb(self) -> I8Vector2: ...



    @property
    def rrr(self) -> I8Vector3: ...

    @property
    def rrg(self) -> I8Vector3: ...

    @property
    def rrb(self) -> I8Vector3: ...

    @property
    def rgg(self) -> I8Vector3: ...

    @property
    def rgb(self) -> I8Vector3: ...

    @property
    def rbb(self) -> I8Vector3: ...

    @property
    def ggg(self) -> I8Vector3: ...

    @property
    def ggb(self) -> I8Vector3: ...

    @property
    def gbb(self) -> I8Vector3: ...

    @property
    def bbb(self) -> I8Vector3: ...



    @property
    def rrrr(self) -> I8Vector4: ...

    @property
    def rrrg(self) -> I8Vector4: ...

    @property
    def rrrb(self) -> I8Vector4: ...

    @property
    def rrgg(self) -> I8Vector4: ...

    @property
    def rrgb(self) -> I8Vector4: ...

    @property
    def rrbb(self) -> I8Vector4: ...

    @property
    def rggg(self) -> I8Vector4: ...

    @property
    def rggb(self) -> I8Vector4: ...

    @property
    def rgbb(self) -> I8Vector4: ...

    @property
    def rbbb(self) -> I8Vector4: ...

    @property
    def gggg(self) -> I8Vector4: ...

    @property
    def gggb(self) -> I8Vector4: ...

    @property
    def ggbb(self) -> I8Vector4: ...

    @property
    def gbbb(self) -> I8Vector4: ...

    @property
    def bbbb(self) -> I8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> I8Vector2: ...

    @property
    def st(self) -> I8Vector2: ...

    @property
    def sq(self) -> I8Vector2: ...

    @property
    def tt(self) -> I8Vector2: ...

    @property
    def tq(self) -> I8Vector2: ...

    @property
    def qq(self) -> I8Vector2: ...



    @property
    def sss(self) -> I8Vector3: ...

    @property
    def sst(self) -> I8Vector3: ...

    @property
    def ssq(self) -> I8Vector3: ...

    @property
    def stt(self) -> I8Vector3: ...

    @property
    def stq(self) -> I8Vector3: ...

    @property
    def sqq(self) -> I8Vector3: ...

    @property
    def ttt(self) -> I8Vector3: ...

    @property
    def ttq(self) -> I8Vector3: ...

    @property
    def tqq(self) -> I8Vector3: ...

    @property
    def qqq(self) -> I8Vector3: ...



    @property
    def ssss(self) -> I8Vector4: ...

    @property
    def ssst(self) -> I8Vector4: ...

    @property
    def sssq(self) -> I8Vector4: ...

    @property
    def sstt(self) -> I8Vector4: ...

    @property
    def sstq(self) -> I8Vector4: ...

    @property
    def ssqq(self) -> I8Vector4: ...

    @property
    def sttt(self) -> I8Vector4: ...

    @property
    def sttq(self) -> I8Vector4: ...

    @property
    def stqq(self) -> I8Vector4: ...

    @property
    def sqqq(self) -> I8Vector4: ...

    @property
    def tttt(self) -> I8Vector4: ...

    @property
    def tttq(self) -> I8Vector4: ...

    @property
    def ttqq(self) -> I8Vector4: ...

    @property
    def tqqq(self) -> I8Vector4: ...

    @property
    def qqqq(self) -> I8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I8Vector2: ...

    @property
    def uv(self) -> I8Vector2: ...

    @property
    def vv(self) -> I8Vector2: ...



    @property
    def uuu(self) -> I8Vector3: ...

    @property
    def uuv(self) -> I8Vector3: ...

    @property
    def uvv(self) -> I8Vector3: ...

    @property
    def vvv(self) -> I8Vector3: ...



    @property
    def uuuu(self) -> I8Vector4: ...

    @property
    def uuuv(self) -> I8Vector4: ...

    @property
    def uuvv(self) -> I8Vector4: ...

    @property
    def uvvv(self) -> I8Vector4: ...

    @property
    def vvvv(self) -> I8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U8Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __add__(self, other: Number) -> U8Vector3: ...
    @overload
    def __radd__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __radd__(self, other: Number) -> U8Vector3: ...

    @overload
    def __sub__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __sub__(self, other: Number) -> U8Vector3: ...
    @overload
    def __rsub__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> U8Vector3: ...

    @overload
    def __mul__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __mul__(self, other: Number) -> U8Vector3: ...
    @overload
    def __rmul__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> U8Vector3: ...




    @overload
    def __truediv__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> U8Vector3: ...
    @overload
    def __rtruediv__(self, other: U8Vector3) -> U8Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> U8Vector3: ...



    def __neg__(self) -> U8Vector3: ...


    def __abs__(self) -> U8Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> U8Vector2: ...

    @property
    def xy(self) -> U8Vector2: ...

    @property
    def xz(self) -> U8Vector2: ...

    @property
    def yy(self) -> U8Vector2: ...

    @property
    def yz(self) -> U8Vector2: ...

    @property
    def zz(self) -> U8Vector2: ...



    @property
    def xxx(self) -> U8Vector3: ...

    @property
    def xxy(self) -> U8Vector3: ...

    @property
    def xxz(self) -> U8Vector3: ...

    @property
    def xyy(self) -> U8Vector3: ...

    @property
    def xyz(self) -> U8Vector3: ...

    @property
    def xzz(self) -> U8Vector3: ...

    @property
    def yyy(self) -> U8Vector3: ...

    @property
    def yyz(self) -> U8Vector3: ...

    @property
    def yzz(self) -> U8Vector3: ...

    @property
    def zzz(self) -> U8Vector3: ...



    @property
    def xxxx(self) -> U8Vector4: ...

    @property
    def xxxy(self) -> U8Vector4: ...

    @property
    def xxxz(self) -> U8Vector4: ...

    @property
    def xxyy(self) -> U8Vector4: ...

    @property
    def xxyz(self) -> U8Vector4: ...

    @property
    def xxzz(self) -> U8Vector4: ...

    @property
    def xyyy(self) -> U8Vector4: ...

    @property
    def xyyz(self) -> U8Vector4: ...

    @property
    def xyzz(self) -> U8Vector4: ...

    @property
    def xzzz(self) -> U8Vector4: ...

    @property
    def yyyy(self) -> U8Vector4: ...

    @property
    def yyyz(self) -> U8Vector4: ...

    @property
    def yyzz(self) -> U8Vector4: ...

    @property
    def yzzz(self) -> U8Vector4: ...

    @property
    def zzzz(self) -> U8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> U8Vector2: ...

    @property
    def rg(self) -> U8Vector2: ...

    @property
    def rb(self) -> U8Vector2: ...

    @property
    def gg(self) -> U8Vector2: ...

    @property
    def gb(self) -> U8Vector2: ...

    @property
    def bb(self) -> U8Vector2: ...



    @property
    def rrr(self) -> U8Vector3: ...

    @property
    def rrg(self) -> U8Vector3: ...

    @property
    def rrb(self) -> U8Vector3: ...

    @property
    def rgg(self) -> U8Vector3: ...

    @property
    def rgb(self) -> U8Vector3: ...

    @property
    def rbb(self) -> U8Vector3: ...

    @property
    def ggg(self) -> U8Vector3: ...

    @property
    def ggb(self) -> U8Vector3: ...

    @property
    def gbb(self) -> U8Vector3: ...

    @property
    def bbb(self) -> U8Vector3: ...



    @property
    def rrrr(self) -> U8Vector4: ...

    @property
    def rrrg(self) -> U8Vector4: ...

    @property
    def rrrb(self) -> U8Vector4: ...

    @property
    def rrgg(self) -> U8Vector4: ...

    @property
    def rrgb(self) -> U8Vector4: ...

    @property
    def rrbb(self) -> U8Vector4: ...

    @property
    def rggg(self) -> U8Vector4: ...

    @property
    def rggb(self) -> U8Vector4: ...

    @property
    def rgbb(self) -> U8Vector4: ...

    @property
    def rbbb(self) -> U8Vector4: ...

    @property
    def gggg(self) -> U8Vector4: ...

    @property
    def gggb(self) -> U8Vector4: ...

    @property
    def ggbb(self) -> U8Vector4: ...

    @property
    def gbbb(self) -> U8Vector4: ...

    @property
    def bbbb(self) -> U8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> U8Vector2: ...

    @property
    def st(self) -> U8Vector2: ...

    @property
    def sq(self) -> U8Vector2: ...

    @property
    def tt(self) -> U8Vector2: ...

    @property
    def tq(self) -> U8Vector2: ...

    @property
    def qq(self) -> U8Vector2: ...



    @property
    def sss(self) -> U8Vector3: ...

    @property
    def sst(self) -> U8Vector3: ...

    @property
    def ssq(self) -> U8Vector3: ...

    @property
    def stt(self) -> U8Vector3: ...

    @property
    def stq(self) -> U8Vector3: ...

    @property
    def sqq(self) -> U8Vector3: ...

    @property
    def ttt(self) -> U8Vector3: ...

    @property
    def ttq(self) -> U8Vector3: ...

    @property
    def tqq(self) -> U8Vector3: ...

    @property
    def qqq(self) -> U8Vector3: ...



    @property
    def ssss(self) -> U8Vector4: ...

    @property
    def ssst(self) -> U8Vector4: ...

    @property
    def sssq(self) -> U8Vector4: ...

    @property
    def sstt(self) -> U8Vector4: ...

    @property
    def sstq(self) -> U8Vector4: ...

    @property
    def ssqq(self) -> U8Vector4: ...

    @property
    def sttt(self) -> U8Vector4: ...

    @property
    def sttq(self) -> U8Vector4: ...

    @property
    def stqq(self) -> U8Vector4: ...

    @property
    def sqqq(self) -> U8Vector4: ...

    @property
    def tttt(self) -> U8Vector4: ...

    @property
    def tttq(self) -> U8Vector4: ...

    @property
    def ttqq(self) -> U8Vector4: ...

    @property
    def tqqq(self) -> U8Vector4: ...

    @property
    def qqqq(self) -> U8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U8Vector2: ...

    @property
    def uv(self) -> U8Vector2: ...

    @property
    def vv(self) -> U8Vector2: ...



    @property
    def uuu(self) -> U8Vector3: ...

    @property
    def uuv(self) -> U8Vector3: ...

    @property
    def uvv(self) -> U8Vector3: ...

    @property
    def vvv(self) -> U8Vector3: ...



    @property
    def uuuu(self) -> U8Vector4: ...

    @property
    def uuuv(self) -> U8Vector4: ...

    @property
    def uuvv(self) -> U8Vector4: ...

    @property
    def uvvv(self) -> U8Vector4: ...

    @property
    def vvvv(self) -> U8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I16Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __add__(self, other: Number) -> I16Vector3: ...
    @overload
    def __radd__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __radd__(self, other: Number) -> I16Vector3: ...

    @overload
    def __sub__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __sub__(self, other: Number) -> I16Vector3: ...
    @overload
    def __rsub__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> I16Vector3: ...

    @overload
    def __mul__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __mul__(self, other: Number) -> I16Vector3: ...
    @overload
    def __rmul__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> I16Vector3: ...




    @overload
    def __truediv__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> I16Vector3: ...
    @overload
    def __rtruediv__(self, other: I16Vector3) -> I16Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> I16Vector3: ...




    def __abs__(self) -> I16Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> I16Vector2: ...

    @property
    def xy(self) -> I16Vector2: ...

    @property
    def xz(self) -> I16Vector2: ...

    @property
    def yy(self) -> I16Vector2: ...

    @property
    def yz(self) -> I16Vector2: ...

    @property
    def zz(self) -> I16Vector2: ...



    @property
    def xxx(self) -> I16Vector3: ...

    @property
    def xxy(self) -> I16Vector3: ...

    @property
    def xxz(self) -> I16Vector3: ...

    @property
    def xyy(self) -> I16Vector3: ...

    @property
    def xyz(self) -> I16Vector3: ...

    @property
    def xzz(self) -> I16Vector3: ...

    @property
    def yyy(self) -> I16Vector3: ...

    @property
    def yyz(self) -> I16Vector3: ...

    @property
    def yzz(self) -> I16Vector3: ...

    @property
    def zzz(self) -> I16Vector3: ...



    @property
    def xxxx(self) -> I16Vector4: ...

    @property
    def xxxy(self) -> I16Vector4: ...

    @property
    def xxxz(self) -> I16Vector4: ...

    @property
    def xxyy(self) -> I16Vector4: ...

    @property
    def xxyz(self) -> I16Vector4: ...

    @property
    def xxzz(self) -> I16Vector4: ...

    @property
    def xyyy(self) -> I16Vector4: ...

    @property
    def xyyz(self) -> I16Vector4: ...

    @property
    def xyzz(self) -> I16Vector4: ...

    @property
    def xzzz(self) -> I16Vector4: ...

    @property
    def yyyy(self) -> I16Vector4: ...

    @property
    def yyyz(self) -> I16Vector4: ...

    @property
    def yyzz(self) -> I16Vector4: ...

    @property
    def yzzz(self) -> I16Vector4: ...

    @property
    def zzzz(self) -> I16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> I16Vector2: ...

    @property
    def rg(self) -> I16Vector2: ...

    @property
    def rb(self) -> I16Vector2: ...

    @property
    def gg(self) -> I16Vector2: ...

    @property
    def gb(self) -> I16Vector2: ...

    @property
    def bb(self) -> I16Vector2: ...



    @property
    def rrr(self) -> I16Vector3: ...

    @property
    def rrg(self) -> I16Vector3: ...

    @property
    def rrb(self) -> I16Vector3: ...

    @property
    def rgg(self) -> I16Vector3: ...

    @property
    def rgb(self) -> I16Vector3: ...

    @property
    def rbb(self) -> I16Vector3: ...

    @property
    def ggg(self) -> I16Vector3: ...

    @property
    def ggb(self) -> I16Vector3: ...

    @property
    def gbb(self) -> I16Vector3: ...

    @property
    def bbb(self) -> I16Vector3: ...



    @property
    def rrrr(self) -> I16Vector4: ...

    @property
    def rrrg(self) -> I16Vector4: ...

    @property
    def rrrb(self) -> I16Vector4: ...

    @property
    def rrgg(self) -> I16Vector4: ...

    @property
    def rrgb(self) -> I16Vector4: ...

    @property
    def rrbb(self) -> I16Vector4: ...

    @property
    def rggg(self) -> I16Vector4: ...

    @property
    def rggb(self) -> I16Vector4: ...

    @property
    def rgbb(self) -> I16Vector4: ...

    @property
    def rbbb(self) -> I16Vector4: ...

    @property
    def gggg(self) -> I16Vector4: ...

    @property
    def gggb(self) -> I16Vector4: ...

    @property
    def ggbb(self) -> I16Vector4: ...

    @property
    def gbbb(self) -> I16Vector4: ...

    @property
    def bbbb(self) -> I16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> I16Vector2: ...

    @property
    def st(self) -> I16Vector2: ...

    @property
    def sq(self) -> I16Vector2: ...

    @property
    def tt(self) -> I16Vector2: ...

    @property
    def tq(self) -> I16Vector2: ...

    @property
    def qq(self) -> I16Vector2: ...



    @property
    def sss(self) -> I16Vector3: ...

    @property
    def sst(self) -> I16Vector3: ...

    @property
    def ssq(self) -> I16Vector3: ...

    @property
    def stt(self) -> I16Vector3: ...

    @property
    def stq(self) -> I16Vector3: ...

    @property
    def sqq(self) -> I16Vector3: ...

    @property
    def ttt(self) -> I16Vector3: ...

    @property
    def ttq(self) -> I16Vector3: ...

    @property
    def tqq(self) -> I16Vector3: ...

    @property
    def qqq(self) -> I16Vector3: ...



    @property
    def ssss(self) -> I16Vector4: ...

    @property
    def ssst(self) -> I16Vector4: ...

    @property
    def sssq(self) -> I16Vector4: ...

    @property
    def sstt(self) -> I16Vector4: ...

    @property
    def sstq(self) -> I16Vector4: ...

    @property
    def ssqq(self) -> I16Vector4: ...

    @property
    def sttt(self) -> I16Vector4: ...

    @property
    def sttq(self) -> I16Vector4: ...

    @property
    def stqq(self) -> I16Vector4: ...

    @property
    def sqqq(self) -> I16Vector4: ...

    @property
    def tttt(self) -> I16Vector4: ...

    @property
    def tttq(self) -> I16Vector4: ...

    @property
    def ttqq(self) -> I16Vector4: ...

    @property
    def tqqq(self) -> I16Vector4: ...

    @property
    def qqqq(self) -> I16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I16Vector2: ...

    @property
    def uv(self) -> I16Vector2: ...

    @property
    def vv(self) -> I16Vector2: ...



    @property
    def uuu(self) -> I16Vector3: ...

    @property
    def uuv(self) -> I16Vector3: ...

    @property
    def uvv(self) -> I16Vector3: ...

    @property
    def vvv(self) -> I16Vector3: ...



    @property
    def uuuu(self) -> I16Vector4: ...

    @property
    def uuuv(self) -> I16Vector4: ...

    @property
    def uuvv(self) -> I16Vector4: ...

    @property
    def uvvv(self) -> I16Vector4: ...

    @property
    def vvvv(self) -> I16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U16Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __add__(self, other: Number) -> U16Vector3: ...
    @overload
    def __radd__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __radd__(self, other: Number) -> U16Vector3: ...

    @overload
    def __sub__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __sub__(self, other: Number) -> U16Vector3: ...
    @overload
    def __rsub__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> U16Vector3: ...

    @overload
    def __mul__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __mul__(self, other: Number) -> U16Vector3: ...
    @overload
    def __rmul__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> U16Vector3: ...




    @overload
    def __truediv__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> U16Vector3: ...
    @overload
    def __rtruediv__(self, other: U16Vector3) -> U16Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> U16Vector3: ...



    def __neg__(self) -> U16Vector3: ...


    def __abs__(self) -> U16Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> U16Vector2: ...

    @property
    def xy(self) -> U16Vector2: ...

    @property
    def xz(self) -> U16Vector2: ...

    @property
    def yy(self) -> U16Vector2: ...

    @property
    def yz(self) -> U16Vector2: ...

    @property
    def zz(self) -> U16Vector2: ...



    @property
    def xxx(self) -> U16Vector3: ...

    @property
    def xxy(self) -> U16Vector3: ...

    @property
    def xxz(self) -> U16Vector3: ...

    @property
    def xyy(self) -> U16Vector3: ...

    @property
    def xyz(self) -> U16Vector3: ...

    @property
    def xzz(self) -> U16Vector3: ...

    @property
    def yyy(self) -> U16Vector3: ...

    @property
    def yyz(self) -> U16Vector3: ...

    @property
    def yzz(self) -> U16Vector3: ...

    @property
    def zzz(self) -> U16Vector3: ...



    @property
    def xxxx(self) -> U16Vector4: ...

    @property
    def xxxy(self) -> U16Vector4: ...

    @property
    def xxxz(self) -> U16Vector4: ...

    @property
    def xxyy(self) -> U16Vector4: ...

    @property
    def xxyz(self) -> U16Vector4: ...

    @property
    def xxzz(self) -> U16Vector4: ...

    @property
    def xyyy(self) -> U16Vector4: ...

    @property
    def xyyz(self) -> U16Vector4: ...

    @property
    def xyzz(self) -> U16Vector4: ...

    @property
    def xzzz(self) -> U16Vector4: ...

    @property
    def yyyy(self) -> U16Vector4: ...

    @property
    def yyyz(self) -> U16Vector4: ...

    @property
    def yyzz(self) -> U16Vector4: ...

    @property
    def yzzz(self) -> U16Vector4: ...

    @property
    def zzzz(self) -> U16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> U16Vector2: ...

    @property
    def rg(self) -> U16Vector2: ...

    @property
    def rb(self) -> U16Vector2: ...

    @property
    def gg(self) -> U16Vector2: ...

    @property
    def gb(self) -> U16Vector2: ...

    @property
    def bb(self) -> U16Vector2: ...



    @property
    def rrr(self) -> U16Vector3: ...

    @property
    def rrg(self) -> U16Vector3: ...

    @property
    def rrb(self) -> U16Vector3: ...

    @property
    def rgg(self) -> U16Vector3: ...

    @property
    def rgb(self) -> U16Vector3: ...

    @property
    def rbb(self) -> U16Vector3: ...

    @property
    def ggg(self) -> U16Vector3: ...

    @property
    def ggb(self) -> U16Vector3: ...

    @property
    def gbb(self) -> U16Vector3: ...

    @property
    def bbb(self) -> U16Vector3: ...



    @property
    def rrrr(self) -> U16Vector4: ...

    @property
    def rrrg(self) -> U16Vector4: ...

    @property
    def rrrb(self) -> U16Vector4: ...

    @property
    def rrgg(self) -> U16Vector4: ...

    @property
    def rrgb(self) -> U16Vector4: ...

    @property
    def rrbb(self) -> U16Vector4: ...

    @property
    def rggg(self) -> U16Vector4: ...

    @property
    def rggb(self) -> U16Vector4: ...

    @property
    def rgbb(self) -> U16Vector4: ...

    @property
    def rbbb(self) -> U16Vector4: ...

    @property
    def gggg(self) -> U16Vector4: ...

    @property
    def gggb(self) -> U16Vector4: ...

    @property
    def ggbb(self) -> U16Vector4: ...

    @property
    def gbbb(self) -> U16Vector4: ...

    @property
    def bbbb(self) -> U16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> U16Vector2: ...

    @property
    def st(self) -> U16Vector2: ...

    @property
    def sq(self) -> U16Vector2: ...

    @property
    def tt(self) -> U16Vector2: ...

    @property
    def tq(self) -> U16Vector2: ...

    @property
    def qq(self) -> U16Vector2: ...



    @property
    def sss(self) -> U16Vector3: ...

    @property
    def sst(self) -> U16Vector3: ...

    @property
    def ssq(self) -> U16Vector3: ...

    @property
    def stt(self) -> U16Vector3: ...

    @property
    def stq(self) -> U16Vector3: ...

    @property
    def sqq(self) -> U16Vector3: ...

    @property
    def ttt(self) -> U16Vector3: ...

    @property
    def ttq(self) -> U16Vector3: ...

    @property
    def tqq(self) -> U16Vector3: ...

    @property
    def qqq(self) -> U16Vector3: ...



    @property
    def ssss(self) -> U16Vector4: ...

    @property
    def ssst(self) -> U16Vector4: ...

    @property
    def sssq(self) -> U16Vector4: ...

    @property
    def sstt(self) -> U16Vector4: ...

    @property
    def sstq(self) -> U16Vector4: ...

    @property
    def ssqq(self) -> U16Vector4: ...

    @property
    def sttt(self) -> U16Vector4: ...

    @property
    def sttq(self) -> U16Vector4: ...

    @property
    def stqq(self) -> U16Vector4: ...

    @property
    def sqqq(self) -> U16Vector4: ...

    @property
    def tttt(self) -> U16Vector4: ...

    @property
    def tttq(self) -> U16Vector4: ...

    @property
    def ttqq(self) -> U16Vector4: ...

    @property
    def tqqq(self) -> U16Vector4: ...

    @property
    def qqqq(self) -> U16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U16Vector2: ...

    @property
    def uv(self) -> U16Vector2: ...

    @property
    def vv(self) -> U16Vector2: ...



    @property
    def uuu(self) -> U16Vector3: ...

    @property
    def uuv(self) -> U16Vector3: ...

    @property
    def uvv(self) -> U16Vector3: ...

    @property
    def vvv(self) -> U16Vector3: ...



    @property
    def uuuu(self) -> U16Vector4: ...

    @property
    def uuuv(self) -> U16Vector4: ...

    @property
    def uuvv(self) -> U16Vector4: ...

    @property
    def uvvv(self) -> U16Vector4: ...

    @property
    def vvvv(self) -> U16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I32Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __add__(self, other: Number) -> I32Vector3: ...
    @overload
    def __radd__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __radd__(self, other: Number) -> I32Vector3: ...

    @overload
    def __sub__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __sub__(self, other: Number) -> I32Vector3: ...
    @overload
    def __rsub__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> I32Vector3: ...

    @overload
    def __mul__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __mul__(self, other: Number) -> I32Vector3: ...
    @overload
    def __rmul__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> I32Vector3: ...




    @overload
    def __truediv__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> I32Vector3: ...
    @overload
    def __rtruediv__(self, other: I32Vector3) -> I32Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> I32Vector3: ...




    def __abs__(self) -> I32Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> I32Vector2: ...

    @property
    def xy(self) -> I32Vector2: ...

    @property
    def xz(self) -> I32Vector2: ...

    @property
    def yy(self) -> I32Vector2: ...

    @property
    def yz(self) -> I32Vector2: ...

    @property
    def zz(self) -> I32Vector2: ...



    @property
    def xxx(self) -> I32Vector3: ...

    @property
    def xxy(self) -> I32Vector3: ...

    @property
    def xxz(self) -> I32Vector3: ...

    @property
    def xyy(self) -> I32Vector3: ...

    @property
    def xyz(self) -> I32Vector3: ...

    @property
    def xzz(self) -> I32Vector3: ...

    @property
    def yyy(self) -> I32Vector3: ...

    @property
    def yyz(self) -> I32Vector3: ...

    @property
    def yzz(self) -> I32Vector3: ...

    @property
    def zzz(self) -> I32Vector3: ...



    @property
    def xxxx(self) -> I32Vector4: ...

    @property
    def xxxy(self) -> I32Vector4: ...

    @property
    def xxxz(self) -> I32Vector4: ...

    @property
    def xxyy(self) -> I32Vector4: ...

    @property
    def xxyz(self) -> I32Vector4: ...

    @property
    def xxzz(self) -> I32Vector4: ...

    @property
    def xyyy(self) -> I32Vector4: ...

    @property
    def xyyz(self) -> I32Vector4: ...

    @property
    def xyzz(self) -> I32Vector4: ...

    @property
    def xzzz(self) -> I32Vector4: ...

    @property
    def yyyy(self) -> I32Vector4: ...

    @property
    def yyyz(self) -> I32Vector4: ...

    @property
    def yyzz(self) -> I32Vector4: ...

    @property
    def yzzz(self) -> I32Vector4: ...

    @property
    def zzzz(self) -> I32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> I32Vector2: ...

    @property
    def rg(self) -> I32Vector2: ...

    @property
    def rb(self) -> I32Vector2: ...

    @property
    def gg(self) -> I32Vector2: ...

    @property
    def gb(self) -> I32Vector2: ...

    @property
    def bb(self) -> I32Vector2: ...



    @property
    def rrr(self) -> I32Vector3: ...

    @property
    def rrg(self) -> I32Vector3: ...

    @property
    def rrb(self) -> I32Vector3: ...

    @property
    def rgg(self) -> I32Vector3: ...

    @property
    def rgb(self) -> I32Vector3: ...

    @property
    def rbb(self) -> I32Vector3: ...

    @property
    def ggg(self) -> I32Vector3: ...

    @property
    def ggb(self) -> I32Vector3: ...

    @property
    def gbb(self) -> I32Vector3: ...

    @property
    def bbb(self) -> I32Vector3: ...



    @property
    def rrrr(self) -> I32Vector4: ...

    @property
    def rrrg(self) -> I32Vector4: ...

    @property
    def rrrb(self) -> I32Vector4: ...

    @property
    def rrgg(self) -> I32Vector4: ...

    @property
    def rrgb(self) -> I32Vector4: ...

    @property
    def rrbb(self) -> I32Vector4: ...

    @property
    def rggg(self) -> I32Vector4: ...

    @property
    def rggb(self) -> I32Vector4: ...

    @property
    def rgbb(self) -> I32Vector4: ...

    @property
    def rbbb(self) -> I32Vector4: ...

    @property
    def gggg(self) -> I32Vector4: ...

    @property
    def gggb(self) -> I32Vector4: ...

    @property
    def ggbb(self) -> I32Vector4: ...

    @property
    def gbbb(self) -> I32Vector4: ...

    @property
    def bbbb(self) -> I32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> I32Vector2: ...

    @property
    def st(self) -> I32Vector2: ...

    @property
    def sq(self) -> I32Vector2: ...

    @property
    def tt(self) -> I32Vector2: ...

    @property
    def tq(self) -> I32Vector2: ...

    @property
    def qq(self) -> I32Vector2: ...



    @property
    def sss(self) -> I32Vector3: ...

    @property
    def sst(self) -> I32Vector3: ...

    @property
    def ssq(self) -> I32Vector3: ...

    @property
    def stt(self) -> I32Vector3: ...

    @property
    def stq(self) -> I32Vector3: ...

    @property
    def sqq(self) -> I32Vector3: ...

    @property
    def ttt(self) -> I32Vector3: ...

    @property
    def ttq(self) -> I32Vector3: ...

    @property
    def tqq(self) -> I32Vector3: ...

    @property
    def qqq(self) -> I32Vector3: ...



    @property
    def ssss(self) -> I32Vector4: ...

    @property
    def ssst(self) -> I32Vector4: ...

    @property
    def sssq(self) -> I32Vector4: ...

    @property
    def sstt(self) -> I32Vector4: ...

    @property
    def sstq(self) -> I32Vector4: ...

    @property
    def ssqq(self) -> I32Vector4: ...

    @property
    def sttt(self) -> I32Vector4: ...

    @property
    def sttq(self) -> I32Vector4: ...

    @property
    def stqq(self) -> I32Vector4: ...

    @property
    def sqqq(self) -> I32Vector4: ...

    @property
    def tttt(self) -> I32Vector4: ...

    @property
    def tttq(self) -> I32Vector4: ...

    @property
    def ttqq(self) -> I32Vector4: ...

    @property
    def tqqq(self) -> I32Vector4: ...

    @property
    def qqqq(self) -> I32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I32Vector2: ...

    @property
    def uv(self) -> I32Vector2: ...

    @property
    def vv(self) -> I32Vector2: ...



    @property
    def uuu(self) -> I32Vector3: ...

    @property
    def uuv(self) -> I32Vector3: ...

    @property
    def uvv(self) -> I32Vector3: ...

    @property
    def vvv(self) -> I32Vector3: ...



    @property
    def uuuu(self) -> I32Vector4: ...

    @property
    def uuuv(self) -> I32Vector4: ...

    @property
    def uuvv(self) -> I32Vector4: ...

    @property
    def uvvv(self) -> I32Vector4: ...

    @property
    def vvvv(self) -> I32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U32Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __add__(self, other: Number) -> U32Vector3: ...
    @overload
    def __radd__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __radd__(self, other: Number) -> U32Vector3: ...

    @overload
    def __sub__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __sub__(self, other: Number) -> U32Vector3: ...
    @overload
    def __rsub__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> U32Vector3: ...

    @overload
    def __mul__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __mul__(self, other: Number) -> U32Vector3: ...
    @overload
    def __rmul__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> U32Vector3: ...




    @overload
    def __truediv__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> U32Vector3: ...
    @overload
    def __rtruediv__(self, other: U32Vector3) -> U32Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> U32Vector3: ...



    def __neg__(self) -> U32Vector3: ...


    def __abs__(self) -> U32Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> U32Vector2: ...

    @property
    def xy(self) -> U32Vector2: ...

    @property
    def xz(self) -> U32Vector2: ...

    @property
    def yy(self) -> U32Vector2: ...

    @property
    def yz(self) -> U32Vector2: ...

    @property
    def zz(self) -> U32Vector2: ...



    @property
    def xxx(self) -> U32Vector3: ...

    @property
    def xxy(self) -> U32Vector3: ...

    @property
    def xxz(self) -> U32Vector3: ...

    @property
    def xyy(self) -> U32Vector3: ...

    @property
    def xyz(self) -> U32Vector3: ...

    @property
    def xzz(self) -> U32Vector3: ...

    @property
    def yyy(self) -> U32Vector3: ...

    @property
    def yyz(self) -> U32Vector3: ...

    @property
    def yzz(self) -> U32Vector3: ...

    @property
    def zzz(self) -> U32Vector3: ...



    @property
    def xxxx(self) -> U32Vector4: ...

    @property
    def xxxy(self) -> U32Vector4: ...

    @property
    def xxxz(self) -> U32Vector4: ...

    @property
    def xxyy(self) -> U32Vector4: ...

    @property
    def xxyz(self) -> U32Vector4: ...

    @property
    def xxzz(self) -> U32Vector4: ...

    @property
    def xyyy(self) -> U32Vector4: ...

    @property
    def xyyz(self) -> U32Vector4: ...

    @property
    def xyzz(self) -> U32Vector4: ...

    @property
    def xzzz(self) -> U32Vector4: ...

    @property
    def yyyy(self) -> U32Vector4: ...

    @property
    def yyyz(self) -> U32Vector4: ...

    @property
    def yyzz(self) -> U32Vector4: ...

    @property
    def yzzz(self) -> U32Vector4: ...

    @property
    def zzzz(self) -> U32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> U32Vector2: ...

    @property
    def rg(self) -> U32Vector2: ...

    @property
    def rb(self) -> U32Vector2: ...

    @property
    def gg(self) -> U32Vector2: ...

    @property
    def gb(self) -> U32Vector2: ...

    @property
    def bb(self) -> U32Vector2: ...



    @property
    def rrr(self) -> U32Vector3: ...

    @property
    def rrg(self) -> U32Vector3: ...

    @property
    def rrb(self) -> U32Vector3: ...

    @property
    def rgg(self) -> U32Vector3: ...

    @property
    def rgb(self) -> U32Vector3: ...

    @property
    def rbb(self) -> U32Vector3: ...

    @property
    def ggg(self) -> U32Vector3: ...

    @property
    def ggb(self) -> U32Vector3: ...

    @property
    def gbb(self) -> U32Vector3: ...

    @property
    def bbb(self) -> U32Vector3: ...



    @property
    def rrrr(self) -> U32Vector4: ...

    @property
    def rrrg(self) -> U32Vector4: ...

    @property
    def rrrb(self) -> U32Vector4: ...

    @property
    def rrgg(self) -> U32Vector4: ...

    @property
    def rrgb(self) -> U32Vector4: ...

    @property
    def rrbb(self) -> U32Vector4: ...

    @property
    def rggg(self) -> U32Vector4: ...

    @property
    def rggb(self) -> U32Vector4: ...

    @property
    def rgbb(self) -> U32Vector4: ...

    @property
    def rbbb(self) -> U32Vector4: ...

    @property
    def gggg(self) -> U32Vector4: ...

    @property
    def gggb(self) -> U32Vector4: ...

    @property
    def ggbb(self) -> U32Vector4: ...

    @property
    def gbbb(self) -> U32Vector4: ...

    @property
    def bbbb(self) -> U32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> U32Vector2: ...

    @property
    def st(self) -> U32Vector2: ...

    @property
    def sq(self) -> U32Vector2: ...

    @property
    def tt(self) -> U32Vector2: ...

    @property
    def tq(self) -> U32Vector2: ...

    @property
    def qq(self) -> U32Vector2: ...



    @property
    def sss(self) -> U32Vector3: ...

    @property
    def sst(self) -> U32Vector3: ...

    @property
    def ssq(self) -> U32Vector3: ...

    @property
    def stt(self) -> U32Vector3: ...

    @property
    def stq(self) -> U32Vector3: ...

    @property
    def sqq(self) -> U32Vector3: ...

    @property
    def ttt(self) -> U32Vector3: ...

    @property
    def ttq(self) -> U32Vector3: ...

    @property
    def tqq(self) -> U32Vector3: ...

    @property
    def qqq(self) -> U32Vector3: ...



    @property
    def ssss(self) -> U32Vector4: ...

    @property
    def ssst(self) -> U32Vector4: ...

    @property
    def sssq(self) -> U32Vector4: ...

    @property
    def sstt(self) -> U32Vector4: ...

    @property
    def sstq(self) -> U32Vector4: ...

    @property
    def ssqq(self) -> U32Vector4: ...

    @property
    def sttt(self) -> U32Vector4: ...

    @property
    def sttq(self) -> U32Vector4: ...

    @property
    def stqq(self) -> U32Vector4: ...

    @property
    def sqqq(self) -> U32Vector4: ...

    @property
    def tttt(self) -> U32Vector4: ...

    @property
    def tttq(self) -> U32Vector4: ...

    @property
    def ttqq(self) -> U32Vector4: ...

    @property
    def tqqq(self) -> U32Vector4: ...

    @property
    def qqqq(self) -> U32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U32Vector2: ...

    @property
    def uv(self) -> U32Vector2: ...

    @property
    def vv(self) -> U32Vector2: ...



    @property
    def uuu(self) -> U32Vector3: ...

    @property
    def uuv(self) -> U32Vector3: ...

    @property
    def uvv(self) -> U32Vector3: ...

    @property
    def vvv(self) -> U32Vector3: ...



    @property
    def uuuu(self) -> U32Vector4: ...

    @property
    def uuuv(self) -> U32Vector4: ...

    @property
    def uuvv(self) -> U32Vector4: ...

    @property
    def uvvv(self) -> U32Vector4: ...

    @property
    def vvvv(self) -> U32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class IVector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: IVector3) -> IVector3: ...
    @overload
    def __add__(self, other: Number) -> IVector3: ...
    @overload
    def __radd__(self, other: IVector3) -> IVector3: ...
    @overload
    def __radd__(self, other: Number) -> IVector3: ...

    @overload
    def __sub__(self, other: IVector3) -> IVector3: ...
    @overload
    def __sub__(self, other: Number) -> IVector3: ...
    @overload
    def __rsub__(self, other: IVector3) -> IVector3: ...
    @overload
    def __rsub__(self, other: Number) -> IVector3: ...

    @overload
    def __mul__(self, other: IVector3) -> IVector3: ...
    @overload
    def __mul__(self, other: Number) -> IVector3: ...
    @overload
    def __rmul__(self, other: IVector3) -> IVector3: ...
    @overload
    def __rmul__(self, other: Number) -> IVector3: ...




    @overload
    def __truediv__(self, other: IVector3) -> IVector3: ...
    @overload
    def __truediv__(self, other: Number) -> IVector3: ...
    @overload
    def __rtruediv__(self, other: IVector3) -> IVector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> IVector3: ...




    def __abs__(self) -> IVector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> IVector2: ...

    @property
    def xy(self) -> IVector2: ...

    @property
    def xz(self) -> IVector2: ...

    @property
    def yy(self) -> IVector2: ...

    @property
    def yz(self) -> IVector2: ...

    @property
    def zz(self) -> IVector2: ...



    @property
    def xxx(self) -> IVector3: ...

    @property
    def xxy(self) -> IVector3: ...

    @property
    def xxz(self) -> IVector3: ...

    @property
    def xyy(self) -> IVector3: ...

    @property
    def xyz(self) -> IVector3: ...

    @property
    def xzz(self) -> IVector3: ...

    @property
    def yyy(self) -> IVector3: ...

    @property
    def yyz(self) -> IVector3: ...

    @property
    def yzz(self) -> IVector3: ...

    @property
    def zzz(self) -> IVector3: ...



    @property
    def xxxx(self) -> IVector4: ...

    @property
    def xxxy(self) -> IVector4: ...

    @property
    def xxxz(self) -> IVector4: ...

    @property
    def xxyy(self) -> IVector4: ...

    @property
    def xxyz(self) -> IVector4: ...

    @property
    def xxzz(self) -> IVector4: ...

    @property
    def xyyy(self) -> IVector4: ...

    @property
    def xyyz(self) -> IVector4: ...

    @property
    def xyzz(self) -> IVector4: ...

    @property
    def xzzz(self) -> IVector4: ...

    @property
    def yyyy(self) -> IVector4: ...

    @property
    def yyyz(self) -> IVector4: ...

    @property
    def yyzz(self) -> IVector4: ...

    @property
    def yzzz(self) -> IVector4: ...

    @property
    def zzzz(self) -> IVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> IVector2: ...

    @property
    def rg(self) -> IVector2: ...

    @property
    def rb(self) -> IVector2: ...

    @property
    def gg(self) -> IVector2: ...

    @property
    def gb(self) -> IVector2: ...

    @property
    def bb(self) -> IVector2: ...



    @property
    def rrr(self) -> IVector3: ...

    @property
    def rrg(self) -> IVector3: ...

    @property
    def rrb(self) -> IVector3: ...

    @property
    def rgg(self) -> IVector3: ...

    @property
    def rgb(self) -> IVector3: ...

    @property
    def rbb(self) -> IVector3: ...

    @property
    def ggg(self) -> IVector3: ...

    @property
    def ggb(self) -> IVector3: ...

    @property
    def gbb(self) -> IVector3: ...

    @property
    def bbb(self) -> IVector3: ...



    @property
    def rrrr(self) -> IVector4: ...

    @property
    def rrrg(self) -> IVector4: ...

    @property
    def rrrb(self) -> IVector4: ...

    @property
    def rrgg(self) -> IVector4: ...

    @property
    def rrgb(self) -> IVector4: ...

    @property
    def rrbb(self) -> IVector4: ...

    @property
    def rggg(self) -> IVector4: ...

    @property
    def rggb(self) -> IVector4: ...

    @property
    def rgbb(self) -> IVector4: ...

    @property
    def rbbb(self) -> IVector4: ...

    @property
    def gggg(self) -> IVector4: ...

    @property
    def gggb(self) -> IVector4: ...

    @property
    def ggbb(self) -> IVector4: ...

    @property
    def gbbb(self) -> IVector4: ...

    @property
    def bbbb(self) -> IVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> IVector2: ...

    @property
    def st(self) -> IVector2: ...

    @property
    def sq(self) -> IVector2: ...

    @property
    def tt(self) -> IVector2: ...

    @property
    def tq(self) -> IVector2: ...

    @property
    def qq(self) -> IVector2: ...



    @property
    def sss(self) -> IVector3: ...

    @property
    def sst(self) -> IVector3: ...

    @property
    def ssq(self) -> IVector3: ...

    @property
    def stt(self) -> IVector3: ...

    @property
    def stq(self) -> IVector3: ...

    @property
    def sqq(self) -> IVector3: ...

    @property
    def ttt(self) -> IVector3: ...

    @property
    def ttq(self) -> IVector3: ...

    @property
    def tqq(self) -> IVector3: ...

    @property
    def qqq(self) -> IVector3: ...



    @property
    def ssss(self) -> IVector4: ...

    @property
    def ssst(self) -> IVector4: ...

    @property
    def sssq(self) -> IVector4: ...

    @property
    def sstt(self) -> IVector4: ...

    @property
    def sstq(self) -> IVector4: ...

    @property
    def ssqq(self) -> IVector4: ...

    @property
    def sttt(self) -> IVector4: ...

    @property
    def sttq(self) -> IVector4: ...

    @property
    def stqq(self) -> IVector4: ...

    @property
    def sqqq(self) -> IVector4: ...

    @property
    def tttt(self) -> IVector4: ...

    @property
    def tttq(self) -> IVector4: ...

    @property
    def ttqq(self) -> IVector4: ...

    @property
    def tqqq(self) -> IVector4: ...

    @property
    def qqqq(self) -> IVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> IVector2: ...

    @property
    def uv(self) -> IVector2: ...

    @property
    def vv(self) -> IVector2: ...



    @property
    def uuu(self) -> IVector3: ...

    @property
    def uuv(self) -> IVector3: ...

    @property
    def uvv(self) -> IVector3: ...

    @property
    def vvv(self) -> IVector3: ...



    @property
    def uuuu(self) -> IVector4: ...

    @property
    def uuuv(self) -> IVector4: ...

    @property
    def uuvv(self) -> IVector4: ...

    @property
    def uvvv(self) -> IVector4: ...

    @property
    def vvvv(self) -> IVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class UVector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: UVector3) -> UVector3: ...
    @overload
    def __add__(self, other: Number) -> UVector3: ...
    @overload
    def __radd__(self, other: UVector3) -> UVector3: ...
    @overload
    def __radd__(self, other: Number) -> UVector3: ...

    @overload
    def __sub__(self, other: UVector3) -> UVector3: ...
    @overload
    def __sub__(self, other: Number) -> UVector3: ...
    @overload
    def __rsub__(self, other: UVector3) -> UVector3: ...
    @overload
    def __rsub__(self, other: Number) -> UVector3: ...

    @overload
    def __mul__(self, other: UVector3) -> UVector3: ...
    @overload
    def __mul__(self, other: Number) -> UVector3: ...
    @overload
    def __rmul__(self, other: UVector3) -> UVector3: ...
    @overload
    def __rmul__(self, other: Number) -> UVector3: ...




    @overload
    def __truediv__(self, other: UVector3) -> UVector3: ...
    @overload
    def __truediv__(self, other: Number) -> UVector3: ...
    @overload
    def __rtruediv__(self, other: UVector3) -> UVector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> UVector3: ...



    def __neg__(self) -> UVector3: ...


    def __abs__(self) -> UVector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> UVector2: ...

    @property
    def xy(self) -> UVector2: ...

    @property
    def xz(self) -> UVector2: ...

    @property
    def yy(self) -> UVector2: ...

    @property
    def yz(self) -> UVector2: ...

    @property
    def zz(self) -> UVector2: ...



    @property
    def xxx(self) -> UVector3: ...

    @property
    def xxy(self) -> UVector3: ...

    @property
    def xxz(self) -> UVector3: ...

    @property
    def xyy(self) -> UVector3: ...

    @property
    def xyz(self) -> UVector3: ...

    @property
    def xzz(self) -> UVector3: ...

    @property
    def yyy(self) -> UVector3: ...

    @property
    def yyz(self) -> UVector3: ...

    @property
    def yzz(self) -> UVector3: ...

    @property
    def zzz(self) -> UVector3: ...



    @property
    def xxxx(self) -> UVector4: ...

    @property
    def xxxy(self) -> UVector4: ...

    @property
    def xxxz(self) -> UVector4: ...

    @property
    def xxyy(self) -> UVector4: ...

    @property
    def xxyz(self) -> UVector4: ...

    @property
    def xxzz(self) -> UVector4: ...

    @property
    def xyyy(self) -> UVector4: ...

    @property
    def xyyz(self) -> UVector4: ...

    @property
    def xyzz(self) -> UVector4: ...

    @property
    def xzzz(self) -> UVector4: ...

    @property
    def yyyy(self) -> UVector4: ...

    @property
    def yyyz(self) -> UVector4: ...

    @property
    def yyzz(self) -> UVector4: ...

    @property
    def yzzz(self) -> UVector4: ...

    @property
    def zzzz(self) -> UVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> UVector2: ...

    @property
    def rg(self) -> UVector2: ...

    @property
    def rb(self) -> UVector2: ...

    @property
    def gg(self) -> UVector2: ...

    @property
    def gb(self) -> UVector2: ...

    @property
    def bb(self) -> UVector2: ...



    @property
    def rrr(self) -> UVector3: ...

    @property
    def rrg(self) -> UVector3: ...

    @property
    def rrb(self) -> UVector3: ...

    @property
    def rgg(self) -> UVector3: ...

    @property
    def rgb(self) -> UVector3: ...

    @property
    def rbb(self) -> UVector3: ...

    @property
    def ggg(self) -> UVector3: ...

    @property
    def ggb(self) -> UVector3: ...

    @property
    def gbb(self) -> UVector3: ...

    @property
    def bbb(self) -> UVector3: ...



    @property
    def rrrr(self) -> UVector4: ...

    @property
    def rrrg(self) -> UVector4: ...

    @property
    def rrrb(self) -> UVector4: ...

    @property
    def rrgg(self) -> UVector4: ...

    @property
    def rrgb(self) -> UVector4: ...

    @property
    def rrbb(self) -> UVector4: ...

    @property
    def rggg(self) -> UVector4: ...

    @property
    def rggb(self) -> UVector4: ...

    @property
    def rgbb(self) -> UVector4: ...

    @property
    def rbbb(self) -> UVector4: ...

    @property
    def gggg(self) -> UVector4: ...

    @property
    def gggb(self) -> UVector4: ...

    @property
    def ggbb(self) -> UVector4: ...

    @property
    def gbbb(self) -> UVector4: ...

    @property
    def bbbb(self) -> UVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> UVector2: ...

    @property
    def st(self) -> UVector2: ...

    @property
    def sq(self) -> UVector2: ...

    @property
    def tt(self) -> UVector2: ...

    @property
    def tq(self) -> UVector2: ...

    @property
    def qq(self) -> UVector2: ...



    @property
    def sss(self) -> UVector3: ...

    @property
    def sst(self) -> UVector3: ...

    @property
    def ssq(self) -> UVector3: ...

    @property
    def stt(self) -> UVector3: ...

    @property
    def stq(self) -> UVector3: ...

    @property
    def sqq(self) -> UVector3: ...

    @property
    def ttt(self) -> UVector3: ...

    @property
    def ttq(self) -> UVector3: ...

    @property
    def tqq(self) -> UVector3: ...

    @property
    def qqq(self) -> UVector3: ...



    @property
    def ssss(self) -> UVector4: ...

    @property
    def ssst(self) -> UVector4: ...

    @property
    def sssq(self) -> UVector4: ...

    @property
    def sstt(self) -> UVector4: ...

    @property
    def sstq(self) -> UVector4: ...

    @property
    def ssqq(self) -> UVector4: ...

    @property
    def sttt(self) -> UVector4: ...

    @property
    def sttq(self) -> UVector4: ...

    @property
    def stqq(self) -> UVector4: ...

    @property
    def sqqq(self) -> UVector4: ...

    @property
    def tttt(self) -> UVector4: ...

    @property
    def tttq(self) -> UVector4: ...

    @property
    def ttqq(self) -> UVector4: ...

    @property
    def tqqq(self) -> UVector4: ...

    @property
    def qqqq(self) -> UVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> UVector2: ...

    @property
    def uv(self) -> UVector2: ...

    @property
    def vv(self) -> UVector2: ...



    @property
    def uuu(self) -> UVector3: ...

    @property
    def uuv(self) -> UVector3: ...

    @property
    def uvv(self) -> UVector3: ...

    @property
    def vvv(self) -> UVector3: ...



    @property
    def uuuu(self) -> UVector4: ...

    @property
    def uuuv(self) -> UVector4: ...

    @property
    def uuvv(self) -> UVector4: ...

    @property
    def uvvv(self) -> UVector4: ...

    @property
    def vvvv(self) -> UVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I64Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __add__(self, other: Number) -> I64Vector3: ...
    @overload
    def __radd__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __radd__(self, other: Number) -> I64Vector3: ...

    @overload
    def __sub__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __sub__(self, other: Number) -> I64Vector3: ...
    @overload
    def __rsub__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> I64Vector3: ...

    @overload
    def __mul__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __mul__(self, other: Number) -> I64Vector3: ...
    @overload
    def __rmul__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> I64Vector3: ...




    @overload
    def __truediv__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> I64Vector3: ...
    @overload
    def __rtruediv__(self, other: I64Vector3) -> I64Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> I64Vector3: ...




    def __abs__(self) -> I64Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> I64Vector2: ...

    @property
    def xy(self) -> I64Vector2: ...

    @property
    def xz(self) -> I64Vector2: ...

    @property
    def yy(self) -> I64Vector2: ...

    @property
    def yz(self) -> I64Vector2: ...

    @property
    def zz(self) -> I64Vector2: ...



    @property
    def xxx(self) -> I64Vector3: ...

    @property
    def xxy(self) -> I64Vector3: ...

    @property
    def xxz(self) -> I64Vector3: ...

    @property
    def xyy(self) -> I64Vector3: ...

    @property
    def xyz(self) -> I64Vector3: ...

    @property
    def xzz(self) -> I64Vector3: ...

    @property
    def yyy(self) -> I64Vector3: ...

    @property
    def yyz(self) -> I64Vector3: ...

    @property
    def yzz(self) -> I64Vector3: ...

    @property
    def zzz(self) -> I64Vector3: ...



    @property
    def xxxx(self) -> I64Vector4: ...

    @property
    def xxxy(self) -> I64Vector4: ...

    @property
    def xxxz(self) -> I64Vector4: ...

    @property
    def xxyy(self) -> I64Vector4: ...

    @property
    def xxyz(self) -> I64Vector4: ...

    @property
    def xxzz(self) -> I64Vector4: ...

    @property
    def xyyy(self) -> I64Vector4: ...

    @property
    def xyyz(self) -> I64Vector4: ...

    @property
    def xyzz(self) -> I64Vector4: ...

    @property
    def xzzz(self) -> I64Vector4: ...

    @property
    def yyyy(self) -> I64Vector4: ...

    @property
    def yyyz(self) -> I64Vector4: ...

    @property
    def yyzz(self) -> I64Vector4: ...

    @property
    def yzzz(self) -> I64Vector4: ...

    @property
    def zzzz(self) -> I64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> I64Vector2: ...

    @property
    def rg(self) -> I64Vector2: ...

    @property
    def rb(self) -> I64Vector2: ...

    @property
    def gg(self) -> I64Vector2: ...

    @property
    def gb(self) -> I64Vector2: ...

    @property
    def bb(self) -> I64Vector2: ...



    @property
    def rrr(self) -> I64Vector3: ...

    @property
    def rrg(self) -> I64Vector3: ...

    @property
    def rrb(self) -> I64Vector3: ...

    @property
    def rgg(self) -> I64Vector3: ...

    @property
    def rgb(self) -> I64Vector3: ...

    @property
    def rbb(self) -> I64Vector3: ...

    @property
    def ggg(self) -> I64Vector3: ...

    @property
    def ggb(self) -> I64Vector3: ...

    @property
    def gbb(self) -> I64Vector3: ...

    @property
    def bbb(self) -> I64Vector3: ...



    @property
    def rrrr(self) -> I64Vector4: ...

    @property
    def rrrg(self) -> I64Vector4: ...

    @property
    def rrrb(self) -> I64Vector4: ...

    @property
    def rrgg(self) -> I64Vector4: ...

    @property
    def rrgb(self) -> I64Vector4: ...

    @property
    def rrbb(self) -> I64Vector4: ...

    @property
    def rggg(self) -> I64Vector4: ...

    @property
    def rggb(self) -> I64Vector4: ...

    @property
    def rgbb(self) -> I64Vector4: ...

    @property
    def rbbb(self) -> I64Vector4: ...

    @property
    def gggg(self) -> I64Vector4: ...

    @property
    def gggb(self) -> I64Vector4: ...

    @property
    def ggbb(self) -> I64Vector4: ...

    @property
    def gbbb(self) -> I64Vector4: ...

    @property
    def bbbb(self) -> I64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> I64Vector2: ...

    @property
    def st(self) -> I64Vector2: ...

    @property
    def sq(self) -> I64Vector2: ...

    @property
    def tt(self) -> I64Vector2: ...

    @property
    def tq(self) -> I64Vector2: ...

    @property
    def qq(self) -> I64Vector2: ...



    @property
    def sss(self) -> I64Vector3: ...

    @property
    def sst(self) -> I64Vector3: ...

    @property
    def ssq(self) -> I64Vector3: ...

    @property
    def stt(self) -> I64Vector3: ...

    @property
    def stq(self) -> I64Vector3: ...

    @property
    def sqq(self) -> I64Vector3: ...

    @property
    def ttt(self) -> I64Vector3: ...

    @property
    def ttq(self) -> I64Vector3: ...

    @property
    def tqq(self) -> I64Vector3: ...

    @property
    def qqq(self) -> I64Vector3: ...



    @property
    def ssss(self) -> I64Vector4: ...

    @property
    def ssst(self) -> I64Vector4: ...

    @property
    def sssq(self) -> I64Vector4: ...

    @property
    def sstt(self) -> I64Vector4: ...

    @property
    def sstq(self) -> I64Vector4: ...

    @property
    def ssqq(self) -> I64Vector4: ...

    @property
    def sttt(self) -> I64Vector4: ...

    @property
    def sttq(self) -> I64Vector4: ...

    @property
    def stqq(self) -> I64Vector4: ...

    @property
    def sqqq(self) -> I64Vector4: ...

    @property
    def tttt(self) -> I64Vector4: ...

    @property
    def tttq(self) -> I64Vector4: ...

    @property
    def ttqq(self) -> I64Vector4: ...

    @property
    def tqqq(self) -> I64Vector4: ...

    @property
    def qqqq(self) -> I64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I64Vector2: ...

    @property
    def uv(self) -> I64Vector2: ...

    @property
    def vv(self) -> I64Vector2: ...



    @property
    def uuu(self) -> I64Vector3: ...

    @property
    def uuv(self) -> I64Vector3: ...

    @property
    def uvv(self) -> I64Vector3: ...

    @property
    def vvv(self) -> I64Vector3: ...



    @property
    def uuuu(self) -> I64Vector4: ...

    @property
    def uuuv(self) -> I64Vector4: ...

    @property
    def uuvv(self) -> I64Vector4: ...

    @property
    def uvvv(self) -> I64Vector4: ...

    @property
    def vvvv(self) -> I64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U64Vector3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...



    @overload
    def __init__(self, x: Number, y: Number, z: Number, /): ...



    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __add__(self, other: Number) -> U64Vector3: ...
    @overload
    def __radd__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __radd__(self, other: Number) -> U64Vector3: ...

    @overload
    def __sub__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __sub__(self, other: Number) -> U64Vector3: ...
    @overload
    def __rsub__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __rsub__(self, other: Number) -> U64Vector3: ...

    @overload
    def __mul__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __mul__(self, other: Number) -> U64Vector3: ...
    @overload
    def __rmul__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __rmul__(self, other: Number) -> U64Vector3: ...




    @overload
    def __truediv__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __truediv__(self, other: Number) -> U64Vector3: ...
    @overload
    def __rtruediv__(self, other: U64Vector3) -> U64Vector3: ...
    @overload
    def __rtruediv__(self, other: Number) -> U64Vector3: ...



    def __neg__(self) -> U64Vector3: ...


    def __abs__(self) -> U64Vector3: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...



    @property
    def xx(self) -> U64Vector2: ...

    @property
    def xy(self) -> U64Vector2: ...

    @property
    def xz(self) -> U64Vector2: ...

    @property
    def yy(self) -> U64Vector2: ...

    @property
    def yz(self) -> U64Vector2: ...

    @property
    def zz(self) -> U64Vector2: ...



    @property
    def xxx(self) -> U64Vector3: ...

    @property
    def xxy(self) -> U64Vector3: ...

    @property
    def xxz(self) -> U64Vector3: ...

    @property
    def xyy(self) -> U64Vector3: ...

    @property
    def xyz(self) -> U64Vector3: ...

    @property
    def xzz(self) -> U64Vector3: ...

    @property
    def yyy(self) -> U64Vector3: ...

    @property
    def yyz(self) -> U64Vector3: ...

    @property
    def yzz(self) -> U64Vector3: ...

    @property
    def zzz(self) -> U64Vector3: ...



    @property
    def xxxx(self) -> U64Vector4: ...

    @property
    def xxxy(self) -> U64Vector4: ...

    @property
    def xxxz(self) -> U64Vector4: ...

    @property
    def xxyy(self) -> U64Vector4: ...

    @property
    def xxyz(self) -> U64Vector4: ...

    @property
    def xxzz(self) -> U64Vector4: ...

    @property
    def xyyy(self) -> U64Vector4: ...

    @property
    def xyyz(self) -> U64Vector4: ...

    @property
    def xyzz(self) -> U64Vector4: ...

    @property
    def xzzz(self) -> U64Vector4: ...

    @property
    def yyyy(self) -> U64Vector4: ...

    @property
    def yyyz(self) -> U64Vector4: ...

    @property
    def yyzz(self) -> U64Vector4: ...

    @property
    def yzzz(self) -> U64Vector4: ...

    @property
    def zzzz(self) -> U64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...



    @property
    def rr(self) -> U64Vector2: ...

    @property
    def rg(self) -> U64Vector2: ...

    @property
    def rb(self) -> U64Vector2: ...

    @property
    def gg(self) -> U64Vector2: ...

    @property
    def gb(self) -> U64Vector2: ...

    @property
    def bb(self) -> U64Vector2: ...



    @property
    def rrr(self) -> U64Vector3: ...

    @property
    def rrg(self) -> U64Vector3: ...

    @property
    def rrb(self) -> U64Vector3: ...

    @property
    def rgg(self) -> U64Vector3: ...

    @property
    def rgb(self) -> U64Vector3: ...

    @property
    def rbb(self) -> U64Vector3: ...

    @property
    def ggg(self) -> U64Vector3: ...

    @property
    def ggb(self) -> U64Vector3: ...

    @property
    def gbb(self) -> U64Vector3: ...

    @property
    def bbb(self) -> U64Vector3: ...



    @property
    def rrrr(self) -> U64Vector4: ...

    @property
    def rrrg(self) -> U64Vector4: ...

    @property
    def rrrb(self) -> U64Vector4: ...

    @property
    def rrgg(self) -> U64Vector4: ...

    @property
    def rrgb(self) -> U64Vector4: ...

    @property
    def rrbb(self) -> U64Vector4: ...

    @property
    def rggg(self) -> U64Vector4: ...

    @property
    def rggb(self) -> U64Vector4: ...

    @property
    def rgbb(self) -> U64Vector4: ...

    @property
    def rbbb(self) -> U64Vector4: ...

    @property
    def gggg(self) -> U64Vector4: ...

    @property
    def gggb(self) -> U64Vector4: ...

    @property
    def ggbb(self) -> U64Vector4: ...

    @property
    def gbbb(self) -> U64Vector4: ...

    @property
    def bbbb(self) -> U64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...



    @property
    def ss(self) -> U64Vector2: ...

    @property
    def st(self) -> U64Vector2: ...

    @property
    def sq(self) -> U64Vector2: ...

    @property
    def tt(self) -> U64Vector2: ...

    @property
    def tq(self) -> U64Vector2: ...

    @property
    def qq(self) -> U64Vector2: ...



    @property
    def sss(self) -> U64Vector3: ...

    @property
    def sst(self) -> U64Vector3: ...

    @property
    def ssq(self) -> U64Vector3: ...

    @property
    def stt(self) -> U64Vector3: ...

    @property
    def stq(self) -> U64Vector3: ...

    @property
    def sqq(self) -> U64Vector3: ...

    @property
    def ttt(self) -> U64Vector3: ...

    @property
    def ttq(self) -> U64Vector3: ...

    @property
    def tqq(self) -> U64Vector3: ...

    @property
    def qqq(self) -> U64Vector3: ...



    @property
    def ssss(self) -> U64Vector4: ...

    @property
    def ssst(self) -> U64Vector4: ...

    @property
    def sssq(self) -> U64Vector4: ...

    @property
    def sstt(self) -> U64Vector4: ...

    @property
    def sstq(self) -> U64Vector4: ...

    @property
    def ssqq(self) -> U64Vector4: ...

    @property
    def sttt(self) -> U64Vector4: ...

    @property
    def sttq(self) -> U64Vector4: ...

    @property
    def stqq(self) -> U64Vector4: ...

    @property
    def sqqq(self) -> U64Vector4: ...

    @property
    def tttt(self) -> U64Vector4: ...

    @property
    def tttq(self) -> U64Vector4: ...

    @property
    def ttqq(self) -> U64Vector4: ...

    @property
    def tqqq(self) -> U64Vector4: ...

    @property
    def qqqq(self) -> U64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U64Vector2: ...

    @property
    def uv(self) -> U64Vector2: ...

    @property
    def vv(self) -> U64Vector2: ...



    @property
    def uuu(self) -> U64Vector3: ...

    @property
    def uuv(self) -> U64Vector3: ...

    @property
    def uvv(self) -> U64Vector3: ...

    @property
    def vvv(self) -> U64Vector3: ...



    @property
    def uuuu(self) -> U64Vector4: ...

    @property
    def uuuv(self) -> U64Vector4: ...

    @property
    def uuvv(self) -> U64Vector4: ...

    @property
    def uvvv(self) -> U64Vector4: ...

    @property
    def vvvv(self) -> U64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class BVector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: BVector4) -> BVector4: ...
    @overload
    def __add__(self, other: Number) -> BVector4: ...
    @overload
    def __radd__(self, other: BVector4) -> BVector4: ...
    @overload
    def __radd__(self, other: Number) -> BVector4: ...

    @overload
    def __sub__(self, other: BVector4) -> BVector4: ...
    @overload
    def __sub__(self, other: Number) -> BVector4: ...
    @overload
    def __rsub__(self, other: BVector4) -> BVector4: ...
    @overload
    def __rsub__(self, other: Number) -> BVector4: ...

    @overload
    def __mul__(self, other: BVector4) -> BVector4: ...
    @overload
    def __mul__(self, other: Number) -> BVector4: ...
    @overload
    def __rmul__(self, other: BVector4) -> BVector4: ...
    @overload
    def __rmul__(self, other: Number) -> BVector4: ...







    def __abs__(self) -> BVector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> bool: ...

    @property
    def y(self) -> bool: ...

    @property
    def z(self) -> bool: ...

    @property
    def w(self) -> bool: ...



    @property
    def xx(self) -> BVector2: ...

    @property
    def xy(self) -> BVector2: ...

    @property
    def xz(self) -> BVector2: ...

    @property
    def xw(self) -> BVector2: ...

    @property
    def yy(self) -> BVector2: ...

    @property
    def yz(self) -> BVector2: ...

    @property
    def yw(self) -> BVector2: ...

    @property
    def zz(self) -> BVector2: ...

    @property
    def zw(self) -> BVector2: ...

    @property
    def ww(self) -> BVector2: ...



    @property
    def xxx(self) -> BVector3: ...

    @property
    def xxy(self) -> BVector3: ...

    @property
    def xxz(self) -> BVector3: ...

    @property
    def xxw(self) -> BVector3: ...

    @property
    def xyy(self) -> BVector3: ...

    @property
    def xyz(self) -> BVector3: ...

    @property
    def xyw(self) -> BVector3: ...

    @property
    def xzz(self) -> BVector3: ...

    @property
    def xzw(self) -> BVector3: ...

    @property
    def xww(self) -> BVector3: ...

    @property
    def yyy(self) -> BVector3: ...

    @property
    def yyz(self) -> BVector3: ...

    @property
    def yyw(self) -> BVector3: ...

    @property
    def yzz(self) -> BVector3: ...

    @property
    def yzw(self) -> BVector3: ...

    @property
    def yww(self) -> BVector3: ...

    @property
    def zzz(self) -> BVector3: ...

    @property
    def zzw(self) -> BVector3: ...

    @property
    def zww(self) -> BVector3: ...

    @property
    def www(self) -> BVector3: ...



    @property
    def xxxx(self) -> BVector4: ...

    @property
    def xxxy(self) -> BVector4: ...

    @property
    def xxxz(self) -> BVector4: ...

    @property
    def xxxw(self) -> BVector4: ...

    @property
    def xxyy(self) -> BVector4: ...

    @property
    def xxyz(self) -> BVector4: ...

    @property
    def xxyw(self) -> BVector4: ...

    @property
    def xxzz(self) -> BVector4: ...

    @property
    def xxzw(self) -> BVector4: ...

    @property
    def xxww(self) -> BVector4: ...

    @property
    def xyyy(self) -> BVector4: ...

    @property
    def xyyz(self) -> BVector4: ...

    @property
    def xyyw(self) -> BVector4: ...

    @property
    def xyzz(self) -> BVector4: ...

    @property
    def xyzw(self) -> BVector4: ...

    @property
    def xyww(self) -> BVector4: ...

    @property
    def xzzz(self) -> BVector4: ...

    @property
    def xzzw(self) -> BVector4: ...

    @property
    def xzww(self) -> BVector4: ...

    @property
    def xwww(self) -> BVector4: ...

    @property
    def yyyy(self) -> BVector4: ...

    @property
    def yyyz(self) -> BVector4: ...

    @property
    def yyyw(self) -> BVector4: ...

    @property
    def yyzz(self) -> BVector4: ...

    @property
    def yyzw(self) -> BVector4: ...

    @property
    def yyww(self) -> BVector4: ...

    @property
    def yzzz(self) -> BVector4: ...

    @property
    def yzzw(self) -> BVector4: ...

    @property
    def yzww(self) -> BVector4: ...

    @property
    def ywww(self) -> BVector4: ...

    @property
    def zzzz(self) -> BVector4: ...

    @property
    def zzzw(self) -> BVector4: ...

    @property
    def zzww(self) -> BVector4: ...

    @property
    def zwww(self) -> BVector4: ...

    @property
    def wwww(self) -> BVector4: ...





    @property
    def r(self) -> bool: ...

    @property
    def g(self) -> bool: ...

    @property
    def b(self) -> bool: ...

    @property
    def a(self) -> bool: ...



    @property
    def rr(self) -> BVector2: ...

    @property
    def rg(self) -> BVector2: ...

    @property
    def rb(self) -> BVector2: ...

    @property
    def ra(self) -> BVector2: ...

    @property
    def gg(self) -> BVector2: ...

    @property
    def gb(self) -> BVector2: ...

    @property
    def ga(self) -> BVector2: ...

    @property
    def bb(self) -> BVector2: ...

    @property
    def ba(self) -> BVector2: ...

    @property
    def aa(self) -> BVector2: ...



    @property
    def rrr(self) -> BVector3: ...

    @property
    def rrg(self) -> BVector3: ...

    @property
    def rrb(self) -> BVector3: ...

    @property
    def rra(self) -> BVector3: ...

    @property
    def rgg(self) -> BVector3: ...

    @property
    def rgb(self) -> BVector3: ...

    @property
    def rga(self) -> BVector3: ...

    @property
    def rbb(self) -> BVector3: ...

    @property
    def rba(self) -> BVector3: ...

    @property
    def raa(self) -> BVector3: ...

    @property
    def ggg(self) -> BVector3: ...

    @property
    def ggb(self) -> BVector3: ...

    @property
    def gga(self) -> BVector3: ...

    @property
    def gbb(self) -> BVector3: ...

    @property
    def gba(self) -> BVector3: ...

    @property
    def gaa(self) -> BVector3: ...

    @property
    def bbb(self) -> BVector3: ...

    @property
    def bba(self) -> BVector3: ...

    @property
    def baa(self) -> BVector3: ...

    @property
    def aaa(self) -> BVector3: ...



    @property
    def rrrr(self) -> BVector4: ...

    @property
    def rrrg(self) -> BVector4: ...

    @property
    def rrrb(self) -> BVector4: ...

    @property
    def rrra(self) -> BVector4: ...

    @property
    def rrgg(self) -> BVector4: ...

    @property
    def rrgb(self) -> BVector4: ...

    @property
    def rrga(self) -> BVector4: ...

    @property
    def rrbb(self) -> BVector4: ...

    @property
    def rrba(self) -> BVector4: ...

    @property
    def rraa(self) -> BVector4: ...

    @property
    def rggg(self) -> BVector4: ...

    @property
    def rggb(self) -> BVector4: ...

    @property
    def rgga(self) -> BVector4: ...

    @property
    def rgbb(self) -> BVector4: ...

    @property
    def rgba(self) -> BVector4: ...

    @property
    def rgaa(self) -> BVector4: ...

    @property
    def rbbb(self) -> BVector4: ...

    @property
    def rbba(self) -> BVector4: ...

    @property
    def rbaa(self) -> BVector4: ...

    @property
    def raaa(self) -> BVector4: ...

    @property
    def gggg(self) -> BVector4: ...

    @property
    def gggb(self) -> BVector4: ...

    @property
    def ggga(self) -> BVector4: ...

    @property
    def ggbb(self) -> BVector4: ...

    @property
    def ggba(self) -> BVector4: ...

    @property
    def ggaa(self) -> BVector4: ...

    @property
    def gbbb(self) -> BVector4: ...

    @property
    def gbba(self) -> BVector4: ...

    @property
    def gbaa(self) -> BVector4: ...

    @property
    def gaaa(self) -> BVector4: ...

    @property
    def bbbb(self) -> BVector4: ...

    @property
    def bbba(self) -> BVector4: ...

    @property
    def bbaa(self) -> BVector4: ...

    @property
    def baaa(self) -> BVector4: ...

    @property
    def aaaa(self) -> BVector4: ...





    @property
    def s(self) -> bool: ...

    @property
    def t(self) -> bool: ...

    @property
    def q(self) -> bool: ...

    @property
    def p(self) -> bool: ...



    @property
    def ss(self) -> BVector2: ...

    @property
    def st(self) -> BVector2: ...

    @property
    def sq(self) -> BVector2: ...

    @property
    def sp(self) -> BVector2: ...

    @property
    def tt(self) -> BVector2: ...

    @property
    def tq(self) -> BVector2: ...

    @property
    def tp(self) -> BVector2: ...

    @property
    def qq(self) -> BVector2: ...

    @property
    def qp(self) -> BVector2: ...

    @property
    def pp(self) -> BVector2: ...



    @property
    def sss(self) -> BVector3: ...

    @property
    def sst(self) -> BVector3: ...

    @property
    def ssq(self) -> BVector3: ...

    @property
    def ssp(self) -> BVector3: ...

    @property
    def stt(self) -> BVector3: ...

    @property
    def stq(self) -> BVector3: ...

    @property
    def stp(self) -> BVector3: ...

    @property
    def sqq(self) -> BVector3: ...

    @property
    def sqp(self) -> BVector3: ...

    @property
    def spp(self) -> BVector3: ...

    @property
    def ttt(self) -> BVector3: ...

    @property
    def ttq(self) -> BVector3: ...

    @property
    def ttp(self) -> BVector3: ...

    @property
    def tqq(self) -> BVector3: ...

    @property
    def tqp(self) -> BVector3: ...

    @property
    def tpp(self) -> BVector3: ...

    @property
    def qqq(self) -> BVector3: ...

    @property
    def qqp(self) -> BVector3: ...

    @property
    def qpp(self) -> BVector3: ...

    @property
    def ppp(self) -> BVector3: ...



    @property
    def ssss(self) -> BVector4: ...

    @property
    def ssst(self) -> BVector4: ...

    @property
    def sssq(self) -> BVector4: ...

    @property
    def sssp(self) -> BVector4: ...

    @property
    def sstt(self) -> BVector4: ...

    @property
    def sstq(self) -> BVector4: ...

    @property
    def sstp(self) -> BVector4: ...

    @property
    def ssqq(self) -> BVector4: ...

    @property
    def ssqp(self) -> BVector4: ...

    @property
    def sspp(self) -> BVector4: ...

    @property
    def sttt(self) -> BVector4: ...

    @property
    def sttq(self) -> BVector4: ...

    @property
    def sttp(self) -> BVector4: ...

    @property
    def stqq(self) -> BVector4: ...

    @property
    def stqp(self) -> BVector4: ...

    @property
    def stpp(self) -> BVector4: ...

    @property
    def sqqq(self) -> BVector4: ...

    @property
    def sqqp(self) -> BVector4: ...

    @property
    def sqpp(self) -> BVector4: ...

    @property
    def sppp(self) -> BVector4: ...

    @property
    def tttt(self) -> BVector4: ...

    @property
    def tttq(self) -> BVector4: ...

    @property
    def tttp(self) -> BVector4: ...

    @property
    def ttqq(self) -> BVector4: ...

    @property
    def ttqp(self) -> BVector4: ...

    @property
    def ttpp(self) -> BVector4: ...

    @property
    def tqqq(self) -> BVector4: ...

    @property
    def tqqp(self) -> BVector4: ...

    @property
    def tqpp(self) -> BVector4: ...

    @property
    def tppp(self) -> BVector4: ...

    @property
    def qqqq(self) -> BVector4: ...

    @property
    def qqqp(self) -> BVector4: ...

    @property
    def qqpp(self) -> BVector4: ...

    @property
    def qppp(self) -> BVector4: ...

    @property
    def pppp(self) -> BVector4: ...





    @property
    def u(self) -> bool: ...

    @property
    def v(self) -> bool: ...



    @property
    def uu(self) -> BVector2: ...

    @property
    def uv(self) -> BVector2: ...

    @property
    def vv(self) -> BVector2: ...



    @property
    def uuu(self) -> BVector3: ...

    @property
    def uuv(self) -> BVector3: ...

    @property
    def uvv(self) -> BVector3: ...

    @property
    def vvv(self) -> BVector3: ...



    @property
    def uuuu(self) -> BVector4: ...

    @property
    def uuuv(self) -> BVector4: ...

    @property
    def uuvv(self) -> BVector4: ...

    @property
    def uvvv(self) -> BVector4: ...

    @property
    def vvvv(self) -> BVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[bool, bool]: ...









@final
class DVector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DVector4) -> DVector4: ...
    @overload
    def __add__(self, other: Number) -> DVector4: ...
    @overload
    def __radd__(self, other: DVector4) -> DVector4: ...
    @overload
    def __radd__(self, other: Number) -> DVector4: ...

    @overload
    def __sub__(self, other: DVector4) -> DVector4: ...
    @overload
    def __sub__(self, other: Number) -> DVector4: ...
    @overload
    def __rsub__(self, other: DVector4) -> DVector4: ...
    @overload
    def __rsub__(self, other: Number) -> DVector4: ...

    @overload
    def __mul__(self, other: DVector4) -> DVector4: ...
    @overload
    def __mul__(self, other: Number) -> DVector4: ...
    @overload
    def __rmul__(self, other: DVector4) -> DVector4: ...
    @overload
    def __rmul__(self, other: Number) -> DVector4: ...




    @overload
    def __truediv__(self, other: DVector4) -> DVector4: ...
    @overload
    def __truediv__(self, other: Number) -> DVector4: ...
    @overload
    def __rtruediv__(self, other: DVector4) -> DVector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> DVector4: ...




    def __abs__(self) -> DVector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> DVector2: ...

    @property
    def xy(self) -> DVector2: ...

    @property
    def xz(self) -> DVector2: ...

    @property
    def xw(self) -> DVector2: ...

    @property
    def yy(self) -> DVector2: ...

    @property
    def yz(self) -> DVector2: ...

    @property
    def yw(self) -> DVector2: ...

    @property
    def zz(self) -> DVector2: ...

    @property
    def zw(self) -> DVector2: ...

    @property
    def ww(self) -> DVector2: ...



    @property
    def xxx(self) -> DVector3: ...

    @property
    def xxy(self) -> DVector3: ...

    @property
    def xxz(self) -> DVector3: ...

    @property
    def xxw(self) -> DVector3: ...

    @property
    def xyy(self) -> DVector3: ...

    @property
    def xyz(self) -> DVector3: ...

    @property
    def xyw(self) -> DVector3: ...

    @property
    def xzz(self) -> DVector3: ...

    @property
    def xzw(self) -> DVector3: ...

    @property
    def xww(self) -> DVector3: ...

    @property
    def yyy(self) -> DVector3: ...

    @property
    def yyz(self) -> DVector3: ...

    @property
    def yyw(self) -> DVector3: ...

    @property
    def yzz(self) -> DVector3: ...

    @property
    def yzw(self) -> DVector3: ...

    @property
    def yww(self) -> DVector3: ...

    @property
    def zzz(self) -> DVector3: ...

    @property
    def zzw(self) -> DVector3: ...

    @property
    def zww(self) -> DVector3: ...

    @property
    def www(self) -> DVector3: ...



    @property
    def xxxx(self) -> DVector4: ...

    @property
    def xxxy(self) -> DVector4: ...

    @property
    def xxxz(self) -> DVector4: ...

    @property
    def xxxw(self) -> DVector4: ...

    @property
    def xxyy(self) -> DVector4: ...

    @property
    def xxyz(self) -> DVector4: ...

    @property
    def xxyw(self) -> DVector4: ...

    @property
    def xxzz(self) -> DVector4: ...

    @property
    def xxzw(self) -> DVector4: ...

    @property
    def xxww(self) -> DVector4: ...

    @property
    def xyyy(self) -> DVector4: ...

    @property
    def xyyz(self) -> DVector4: ...

    @property
    def xyyw(self) -> DVector4: ...

    @property
    def xyzz(self) -> DVector4: ...

    @property
    def xyzw(self) -> DVector4: ...

    @property
    def xyww(self) -> DVector4: ...

    @property
    def xzzz(self) -> DVector4: ...

    @property
    def xzzw(self) -> DVector4: ...

    @property
    def xzww(self) -> DVector4: ...

    @property
    def xwww(self) -> DVector4: ...

    @property
    def yyyy(self) -> DVector4: ...

    @property
    def yyyz(self) -> DVector4: ...

    @property
    def yyyw(self) -> DVector4: ...

    @property
    def yyzz(self) -> DVector4: ...

    @property
    def yyzw(self) -> DVector4: ...

    @property
    def yyww(self) -> DVector4: ...

    @property
    def yzzz(self) -> DVector4: ...

    @property
    def yzzw(self) -> DVector4: ...

    @property
    def yzww(self) -> DVector4: ...

    @property
    def ywww(self) -> DVector4: ...

    @property
    def zzzz(self) -> DVector4: ...

    @property
    def zzzw(self) -> DVector4: ...

    @property
    def zzww(self) -> DVector4: ...

    @property
    def zwww(self) -> DVector4: ...

    @property
    def wwww(self) -> DVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> DVector2: ...

    @property
    def rg(self) -> DVector2: ...

    @property
    def rb(self) -> DVector2: ...

    @property
    def ra(self) -> DVector2: ...

    @property
    def gg(self) -> DVector2: ...

    @property
    def gb(self) -> DVector2: ...

    @property
    def ga(self) -> DVector2: ...

    @property
    def bb(self) -> DVector2: ...

    @property
    def ba(self) -> DVector2: ...

    @property
    def aa(self) -> DVector2: ...



    @property
    def rrr(self) -> DVector3: ...

    @property
    def rrg(self) -> DVector3: ...

    @property
    def rrb(self) -> DVector3: ...

    @property
    def rra(self) -> DVector3: ...

    @property
    def rgg(self) -> DVector3: ...

    @property
    def rgb(self) -> DVector3: ...

    @property
    def rga(self) -> DVector3: ...

    @property
    def rbb(self) -> DVector3: ...

    @property
    def rba(self) -> DVector3: ...

    @property
    def raa(self) -> DVector3: ...

    @property
    def ggg(self) -> DVector3: ...

    @property
    def ggb(self) -> DVector3: ...

    @property
    def gga(self) -> DVector3: ...

    @property
    def gbb(self) -> DVector3: ...

    @property
    def gba(self) -> DVector3: ...

    @property
    def gaa(self) -> DVector3: ...

    @property
    def bbb(self) -> DVector3: ...

    @property
    def bba(self) -> DVector3: ...

    @property
    def baa(self) -> DVector3: ...

    @property
    def aaa(self) -> DVector3: ...



    @property
    def rrrr(self) -> DVector4: ...

    @property
    def rrrg(self) -> DVector4: ...

    @property
    def rrrb(self) -> DVector4: ...

    @property
    def rrra(self) -> DVector4: ...

    @property
    def rrgg(self) -> DVector4: ...

    @property
    def rrgb(self) -> DVector4: ...

    @property
    def rrga(self) -> DVector4: ...

    @property
    def rrbb(self) -> DVector4: ...

    @property
    def rrba(self) -> DVector4: ...

    @property
    def rraa(self) -> DVector4: ...

    @property
    def rggg(self) -> DVector4: ...

    @property
    def rggb(self) -> DVector4: ...

    @property
    def rgga(self) -> DVector4: ...

    @property
    def rgbb(self) -> DVector4: ...

    @property
    def rgba(self) -> DVector4: ...

    @property
    def rgaa(self) -> DVector4: ...

    @property
    def rbbb(self) -> DVector4: ...

    @property
    def rbba(self) -> DVector4: ...

    @property
    def rbaa(self) -> DVector4: ...

    @property
    def raaa(self) -> DVector4: ...

    @property
    def gggg(self) -> DVector4: ...

    @property
    def gggb(self) -> DVector4: ...

    @property
    def ggga(self) -> DVector4: ...

    @property
    def ggbb(self) -> DVector4: ...

    @property
    def ggba(self) -> DVector4: ...

    @property
    def ggaa(self) -> DVector4: ...

    @property
    def gbbb(self) -> DVector4: ...

    @property
    def gbba(self) -> DVector4: ...

    @property
    def gbaa(self) -> DVector4: ...

    @property
    def gaaa(self) -> DVector4: ...

    @property
    def bbbb(self) -> DVector4: ...

    @property
    def bbba(self) -> DVector4: ...

    @property
    def bbaa(self) -> DVector4: ...

    @property
    def baaa(self) -> DVector4: ...

    @property
    def aaaa(self) -> DVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> DVector2: ...

    @property
    def st(self) -> DVector2: ...

    @property
    def sq(self) -> DVector2: ...

    @property
    def sp(self) -> DVector2: ...

    @property
    def tt(self) -> DVector2: ...

    @property
    def tq(self) -> DVector2: ...

    @property
    def tp(self) -> DVector2: ...

    @property
    def qq(self) -> DVector2: ...

    @property
    def qp(self) -> DVector2: ...

    @property
    def pp(self) -> DVector2: ...



    @property
    def sss(self) -> DVector3: ...

    @property
    def sst(self) -> DVector3: ...

    @property
    def ssq(self) -> DVector3: ...

    @property
    def ssp(self) -> DVector3: ...

    @property
    def stt(self) -> DVector3: ...

    @property
    def stq(self) -> DVector3: ...

    @property
    def stp(self) -> DVector3: ...

    @property
    def sqq(self) -> DVector3: ...

    @property
    def sqp(self) -> DVector3: ...

    @property
    def spp(self) -> DVector3: ...

    @property
    def ttt(self) -> DVector3: ...

    @property
    def ttq(self) -> DVector3: ...

    @property
    def ttp(self) -> DVector3: ...

    @property
    def tqq(self) -> DVector3: ...

    @property
    def tqp(self) -> DVector3: ...

    @property
    def tpp(self) -> DVector3: ...

    @property
    def qqq(self) -> DVector3: ...

    @property
    def qqp(self) -> DVector3: ...

    @property
    def qpp(self) -> DVector3: ...

    @property
    def ppp(self) -> DVector3: ...



    @property
    def ssss(self) -> DVector4: ...

    @property
    def ssst(self) -> DVector4: ...

    @property
    def sssq(self) -> DVector4: ...

    @property
    def sssp(self) -> DVector4: ...

    @property
    def sstt(self) -> DVector4: ...

    @property
    def sstq(self) -> DVector4: ...

    @property
    def sstp(self) -> DVector4: ...

    @property
    def ssqq(self) -> DVector4: ...

    @property
    def ssqp(self) -> DVector4: ...

    @property
    def sspp(self) -> DVector4: ...

    @property
    def sttt(self) -> DVector4: ...

    @property
    def sttq(self) -> DVector4: ...

    @property
    def sttp(self) -> DVector4: ...

    @property
    def stqq(self) -> DVector4: ...

    @property
    def stqp(self) -> DVector4: ...

    @property
    def stpp(self) -> DVector4: ...

    @property
    def sqqq(self) -> DVector4: ...

    @property
    def sqqp(self) -> DVector4: ...

    @property
    def sqpp(self) -> DVector4: ...

    @property
    def sppp(self) -> DVector4: ...

    @property
    def tttt(self) -> DVector4: ...

    @property
    def tttq(self) -> DVector4: ...

    @property
    def tttp(self) -> DVector4: ...

    @property
    def ttqq(self) -> DVector4: ...

    @property
    def ttqp(self) -> DVector4: ...

    @property
    def ttpp(self) -> DVector4: ...

    @property
    def tqqq(self) -> DVector4: ...

    @property
    def tqqp(self) -> DVector4: ...

    @property
    def tqpp(self) -> DVector4: ...

    @property
    def tppp(self) -> DVector4: ...

    @property
    def qqqq(self) -> DVector4: ...

    @property
    def qqqp(self) -> DVector4: ...

    @property
    def qqpp(self) -> DVector4: ...

    @property
    def qppp(self) -> DVector4: ...

    @property
    def pppp(self) -> DVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> DVector2: ...

    @property
    def uv(self) -> DVector2: ...

    @property
    def vv(self) -> DVector2: ...



    @property
    def uuu(self) -> DVector3: ...

    @property
    def uuv(self) -> DVector3: ...

    @property
    def uvv(self) -> DVector3: ...

    @property
    def vvv(self) -> DVector3: ...



    @property
    def uuuu(self) -> DVector4: ...

    @property
    def uuuv(self) -> DVector4: ...

    @property
    def uuvv(self) -> DVector4: ...

    @property
    def uvvv(self) -> DVector4: ...

    @property
    def vvvv(self) -> DVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class FVector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> float: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FVector4) -> FVector4: ...
    @overload
    def __add__(self, other: Number) -> FVector4: ...
    @overload
    def __radd__(self, other: FVector4) -> FVector4: ...
    @overload
    def __radd__(self, other: Number) -> FVector4: ...

    @overload
    def __sub__(self, other: FVector4) -> FVector4: ...
    @overload
    def __sub__(self, other: Number) -> FVector4: ...
    @overload
    def __rsub__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rsub__(self, other: Number) -> FVector4: ...

    @overload
    def __mul__(self, other: FVector4) -> FVector4: ...
    @overload
    def __mul__(self, other: Number) -> FVector4: ...
    @overload
    def __rmul__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rmul__(self, other: Number) -> FVector4: ...


    def __matmul__(self, other: FVector4) -> FVector4: ...
    def __rmatmul__(self, other: FVector4) -> FVector4: ...

    @overload
    def __mod__(self, other: FVector4) -> FVector4: ...
    @overload
    def __mod__(self, other: Number) -> FVector4: ...
    @overload
    def __rmod__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rmod__(self, other: Number) -> FVector4: ...

    @overload
    def __pow__(self, other: FVector4) -> FVector4: ...
    @overload
    def __pow__(self, other: Number) -> FVector4: ...
    @overload
    def __rpow__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rpow__(self, other: Number) -> FVector4: ...



    @overload
    def __truediv__(self, other: FVector4) -> FVector4: ...
    @overload
    def __truediv__(self, other: Number) -> FVector4: ...
    @overload
    def __rtruediv__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> FVector4: ...




    def __abs__(self) -> FVector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...

    @property
    def z(self) -> float: ...

    @property
    def w(self) -> float: ...



    @property
    def xx(self) -> FVector2: ...

    @property
    def xy(self) -> FVector2: ...

    @property
    def xz(self) -> FVector2: ...

    @property
    def xw(self) -> FVector2: ...

    @property
    def yy(self) -> FVector2: ...

    @property
    def yz(self) -> FVector2: ...

    @property
    def yw(self) -> FVector2: ...

    @property
    def zz(self) -> FVector2: ...

    @property
    def zw(self) -> FVector2: ...

    @property
    def ww(self) -> FVector2: ...



    @property
    def xxx(self) -> FVector3: ...

    @property
    def xxy(self) -> FVector3: ...

    @property
    def xxz(self) -> FVector3: ...

    @property
    def xxw(self) -> FVector3: ...

    @property
    def xyy(self) -> FVector3: ...

    @property
    def xyz(self) -> FVector3: ...

    @property
    def xyw(self) -> FVector3: ...

    @property
    def xzz(self) -> FVector3: ...

    @property
    def xzw(self) -> FVector3: ...

    @property
    def xww(self) -> FVector3: ...

    @property
    def yyy(self) -> FVector3: ...

    @property
    def yyz(self) -> FVector3: ...

    @property
    def yyw(self) -> FVector3: ...

    @property
    def yzz(self) -> FVector3: ...

    @property
    def yzw(self) -> FVector3: ...

    @property
    def yww(self) -> FVector3: ...

    @property
    def zzz(self) -> FVector3: ...

    @property
    def zzw(self) -> FVector3: ...

    @property
    def zww(self) -> FVector3: ...

    @property
    def www(self) -> FVector3: ...



    @property
    def xxxx(self) -> FVector4: ...

    @property
    def xxxy(self) -> FVector4: ...

    @property
    def xxxz(self) -> FVector4: ...

    @property
    def xxxw(self) -> FVector4: ...

    @property
    def xxyy(self) -> FVector4: ...

    @property
    def xxyz(self) -> FVector4: ...

    @property
    def xxyw(self) -> FVector4: ...

    @property
    def xxzz(self) -> FVector4: ...

    @property
    def xxzw(self) -> FVector4: ...

    @property
    def xxww(self) -> FVector4: ...

    @property
    def xyyy(self) -> FVector4: ...

    @property
    def xyyz(self) -> FVector4: ...

    @property
    def xyyw(self) -> FVector4: ...

    @property
    def xyzz(self) -> FVector4: ...

    @property
    def xyzw(self) -> FVector4: ...

    @property
    def xyww(self) -> FVector4: ...

    @property
    def xzzz(self) -> FVector4: ...

    @property
    def xzzw(self) -> FVector4: ...

    @property
    def xzww(self) -> FVector4: ...

    @property
    def xwww(self) -> FVector4: ...

    @property
    def yyyy(self) -> FVector4: ...

    @property
    def yyyz(self) -> FVector4: ...

    @property
    def yyyw(self) -> FVector4: ...

    @property
    def yyzz(self) -> FVector4: ...

    @property
    def yyzw(self) -> FVector4: ...

    @property
    def yyww(self) -> FVector4: ...

    @property
    def yzzz(self) -> FVector4: ...

    @property
    def yzzw(self) -> FVector4: ...

    @property
    def yzww(self) -> FVector4: ...

    @property
    def ywww(self) -> FVector4: ...

    @property
    def zzzz(self) -> FVector4: ...

    @property
    def zzzw(self) -> FVector4: ...

    @property
    def zzww(self) -> FVector4: ...

    @property
    def zwww(self) -> FVector4: ...

    @property
    def wwww(self) -> FVector4: ...





    @property
    def r(self) -> float: ...

    @property
    def g(self) -> float: ...

    @property
    def b(self) -> float: ...

    @property
    def a(self) -> float: ...



    @property
    def rr(self) -> FVector2: ...

    @property
    def rg(self) -> FVector2: ...

    @property
    def rb(self) -> FVector2: ...

    @property
    def ra(self) -> FVector2: ...

    @property
    def gg(self) -> FVector2: ...

    @property
    def gb(self) -> FVector2: ...

    @property
    def ga(self) -> FVector2: ...

    @property
    def bb(self) -> FVector2: ...

    @property
    def ba(self) -> FVector2: ...

    @property
    def aa(self) -> FVector2: ...



    @property
    def rrr(self) -> FVector3: ...

    @property
    def rrg(self) -> FVector3: ...

    @property
    def rrb(self) -> FVector3: ...

    @property
    def rra(self) -> FVector3: ...

    @property
    def rgg(self) -> FVector3: ...

    @property
    def rgb(self) -> FVector3: ...

    @property
    def rga(self) -> FVector3: ...

    @property
    def rbb(self) -> FVector3: ...

    @property
    def rba(self) -> FVector3: ...

    @property
    def raa(self) -> FVector3: ...

    @property
    def ggg(self) -> FVector3: ...

    @property
    def ggb(self) -> FVector3: ...

    @property
    def gga(self) -> FVector3: ...

    @property
    def gbb(self) -> FVector3: ...

    @property
    def gba(self) -> FVector3: ...

    @property
    def gaa(self) -> FVector3: ...

    @property
    def bbb(self) -> FVector3: ...

    @property
    def bba(self) -> FVector3: ...

    @property
    def baa(self) -> FVector3: ...

    @property
    def aaa(self) -> FVector3: ...



    @property
    def rrrr(self) -> FVector4: ...

    @property
    def rrrg(self) -> FVector4: ...

    @property
    def rrrb(self) -> FVector4: ...

    @property
    def rrra(self) -> FVector4: ...

    @property
    def rrgg(self) -> FVector4: ...

    @property
    def rrgb(self) -> FVector4: ...

    @property
    def rrga(self) -> FVector4: ...

    @property
    def rrbb(self) -> FVector4: ...

    @property
    def rrba(self) -> FVector4: ...

    @property
    def rraa(self) -> FVector4: ...

    @property
    def rggg(self) -> FVector4: ...

    @property
    def rggb(self) -> FVector4: ...

    @property
    def rgga(self) -> FVector4: ...

    @property
    def rgbb(self) -> FVector4: ...

    @property
    def rgba(self) -> FVector4: ...

    @property
    def rgaa(self) -> FVector4: ...

    @property
    def rbbb(self) -> FVector4: ...

    @property
    def rbba(self) -> FVector4: ...

    @property
    def rbaa(self) -> FVector4: ...

    @property
    def raaa(self) -> FVector4: ...

    @property
    def gggg(self) -> FVector4: ...

    @property
    def gggb(self) -> FVector4: ...

    @property
    def ggga(self) -> FVector4: ...

    @property
    def ggbb(self) -> FVector4: ...

    @property
    def ggba(self) -> FVector4: ...

    @property
    def ggaa(self) -> FVector4: ...

    @property
    def gbbb(self) -> FVector4: ...

    @property
    def gbba(self) -> FVector4: ...

    @property
    def gbaa(self) -> FVector4: ...

    @property
    def gaaa(self) -> FVector4: ...

    @property
    def bbbb(self) -> FVector4: ...

    @property
    def bbba(self) -> FVector4: ...

    @property
    def bbaa(self) -> FVector4: ...

    @property
    def baaa(self) -> FVector4: ...

    @property
    def aaaa(self) -> FVector4: ...





    @property
    def s(self) -> float: ...

    @property
    def t(self) -> float: ...

    @property
    def q(self) -> float: ...

    @property
    def p(self) -> float: ...



    @property
    def ss(self) -> FVector2: ...

    @property
    def st(self) -> FVector2: ...

    @property
    def sq(self) -> FVector2: ...

    @property
    def sp(self) -> FVector2: ...

    @property
    def tt(self) -> FVector2: ...

    @property
    def tq(self) -> FVector2: ...

    @property
    def tp(self) -> FVector2: ...

    @property
    def qq(self) -> FVector2: ...

    @property
    def qp(self) -> FVector2: ...

    @property
    def pp(self) -> FVector2: ...



    @property
    def sss(self) -> FVector3: ...

    @property
    def sst(self) -> FVector3: ...

    @property
    def ssq(self) -> FVector3: ...

    @property
    def ssp(self) -> FVector3: ...

    @property
    def stt(self) -> FVector3: ...

    @property
    def stq(self) -> FVector3: ...

    @property
    def stp(self) -> FVector3: ...

    @property
    def sqq(self) -> FVector3: ...

    @property
    def sqp(self) -> FVector3: ...

    @property
    def spp(self) -> FVector3: ...

    @property
    def ttt(self) -> FVector3: ...

    @property
    def ttq(self) -> FVector3: ...

    @property
    def ttp(self) -> FVector3: ...

    @property
    def tqq(self) -> FVector3: ...

    @property
    def tqp(self) -> FVector3: ...

    @property
    def tpp(self) -> FVector3: ...

    @property
    def qqq(self) -> FVector3: ...

    @property
    def qqp(self) -> FVector3: ...

    @property
    def qpp(self) -> FVector3: ...

    @property
    def ppp(self) -> FVector3: ...



    @property
    def ssss(self) -> FVector4: ...

    @property
    def ssst(self) -> FVector4: ...

    @property
    def sssq(self) -> FVector4: ...

    @property
    def sssp(self) -> FVector4: ...

    @property
    def sstt(self) -> FVector4: ...

    @property
    def sstq(self) -> FVector4: ...

    @property
    def sstp(self) -> FVector4: ...

    @property
    def ssqq(self) -> FVector4: ...

    @property
    def ssqp(self) -> FVector4: ...

    @property
    def sspp(self) -> FVector4: ...

    @property
    def sttt(self) -> FVector4: ...

    @property
    def sttq(self) -> FVector4: ...

    @property
    def sttp(self) -> FVector4: ...

    @property
    def stqq(self) -> FVector4: ...

    @property
    def stqp(self) -> FVector4: ...

    @property
    def stpp(self) -> FVector4: ...

    @property
    def sqqq(self) -> FVector4: ...

    @property
    def sqqp(self) -> FVector4: ...

    @property
    def sqpp(self) -> FVector4: ...

    @property
    def sppp(self) -> FVector4: ...

    @property
    def tttt(self) -> FVector4: ...

    @property
    def tttq(self) -> FVector4: ...

    @property
    def tttp(self) -> FVector4: ...

    @property
    def ttqq(self) -> FVector4: ...

    @property
    def ttqp(self) -> FVector4: ...

    @property
    def ttpp(self) -> FVector4: ...

    @property
    def tqqq(self) -> FVector4: ...

    @property
    def tqqp(self) -> FVector4: ...

    @property
    def tqpp(self) -> FVector4: ...

    @property
    def tppp(self) -> FVector4: ...

    @property
    def qqqq(self) -> FVector4: ...

    @property
    def qqqp(self) -> FVector4: ...

    @property
    def qqpp(self) -> FVector4: ...

    @property
    def qppp(self) -> FVector4: ...

    @property
    def pppp(self) -> FVector4: ...





    @property
    def u(self) -> float: ...

    @property
    def v(self) -> float: ...



    @property
    def uu(self) -> FVector2: ...

    @property
    def uv(self) -> FVector2: ...

    @property
    def vv(self) -> FVector2: ...



    @property
    def uuu(self) -> FVector3: ...

    @property
    def uuv(self) -> FVector3: ...

    @property
    def uvv(self) -> FVector3: ...

    @property
    def vvv(self) -> FVector3: ...



    @property
    def uuuu(self) -> FVector4: ...

    @property
    def uuuv(self) -> FVector4: ...

    @property
    def uuvv(self) -> FVector4: ...

    @property
    def uvvv(self) -> FVector4: ...

    @property
    def vvvv(self) -> FVector4: ...





    @property
    def magnitude(self) -> float: ...

    def cross(self, other: FVector4, /) -> FVector4: ...
    def normalize(self) -> float: ...
    def distance(self, other: FVector4, /) -> float: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...









@final
class I8Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __add__(self, other: Number) -> I8Vector4: ...
    @overload
    def __radd__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __radd__(self, other: Number) -> I8Vector4: ...

    @overload
    def __sub__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __sub__(self, other: Number) -> I8Vector4: ...
    @overload
    def __rsub__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> I8Vector4: ...

    @overload
    def __mul__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __mul__(self, other: Number) -> I8Vector4: ...
    @overload
    def __rmul__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> I8Vector4: ...




    @overload
    def __truediv__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> I8Vector4: ...
    @overload
    def __rtruediv__(self, other: I8Vector4) -> I8Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> I8Vector4: ...




    def __abs__(self) -> I8Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> I8Vector2: ...

    @property
    def xy(self) -> I8Vector2: ...

    @property
    def xz(self) -> I8Vector2: ...

    @property
    def xw(self) -> I8Vector2: ...

    @property
    def yy(self) -> I8Vector2: ...

    @property
    def yz(self) -> I8Vector2: ...

    @property
    def yw(self) -> I8Vector2: ...

    @property
    def zz(self) -> I8Vector2: ...

    @property
    def zw(self) -> I8Vector2: ...

    @property
    def ww(self) -> I8Vector2: ...



    @property
    def xxx(self) -> I8Vector3: ...

    @property
    def xxy(self) -> I8Vector3: ...

    @property
    def xxz(self) -> I8Vector3: ...

    @property
    def xxw(self) -> I8Vector3: ...

    @property
    def xyy(self) -> I8Vector3: ...

    @property
    def xyz(self) -> I8Vector3: ...

    @property
    def xyw(self) -> I8Vector3: ...

    @property
    def xzz(self) -> I8Vector3: ...

    @property
    def xzw(self) -> I8Vector3: ...

    @property
    def xww(self) -> I8Vector3: ...

    @property
    def yyy(self) -> I8Vector3: ...

    @property
    def yyz(self) -> I8Vector3: ...

    @property
    def yyw(self) -> I8Vector3: ...

    @property
    def yzz(self) -> I8Vector3: ...

    @property
    def yzw(self) -> I8Vector3: ...

    @property
    def yww(self) -> I8Vector3: ...

    @property
    def zzz(self) -> I8Vector3: ...

    @property
    def zzw(self) -> I8Vector3: ...

    @property
    def zww(self) -> I8Vector3: ...

    @property
    def www(self) -> I8Vector3: ...



    @property
    def xxxx(self) -> I8Vector4: ...

    @property
    def xxxy(self) -> I8Vector4: ...

    @property
    def xxxz(self) -> I8Vector4: ...

    @property
    def xxxw(self) -> I8Vector4: ...

    @property
    def xxyy(self) -> I8Vector4: ...

    @property
    def xxyz(self) -> I8Vector4: ...

    @property
    def xxyw(self) -> I8Vector4: ...

    @property
    def xxzz(self) -> I8Vector4: ...

    @property
    def xxzw(self) -> I8Vector4: ...

    @property
    def xxww(self) -> I8Vector4: ...

    @property
    def xyyy(self) -> I8Vector4: ...

    @property
    def xyyz(self) -> I8Vector4: ...

    @property
    def xyyw(self) -> I8Vector4: ...

    @property
    def xyzz(self) -> I8Vector4: ...

    @property
    def xyzw(self) -> I8Vector4: ...

    @property
    def xyww(self) -> I8Vector4: ...

    @property
    def xzzz(self) -> I8Vector4: ...

    @property
    def xzzw(self) -> I8Vector4: ...

    @property
    def xzww(self) -> I8Vector4: ...

    @property
    def xwww(self) -> I8Vector4: ...

    @property
    def yyyy(self) -> I8Vector4: ...

    @property
    def yyyz(self) -> I8Vector4: ...

    @property
    def yyyw(self) -> I8Vector4: ...

    @property
    def yyzz(self) -> I8Vector4: ...

    @property
    def yyzw(self) -> I8Vector4: ...

    @property
    def yyww(self) -> I8Vector4: ...

    @property
    def yzzz(self) -> I8Vector4: ...

    @property
    def yzzw(self) -> I8Vector4: ...

    @property
    def yzww(self) -> I8Vector4: ...

    @property
    def ywww(self) -> I8Vector4: ...

    @property
    def zzzz(self) -> I8Vector4: ...

    @property
    def zzzw(self) -> I8Vector4: ...

    @property
    def zzww(self) -> I8Vector4: ...

    @property
    def zwww(self) -> I8Vector4: ...

    @property
    def wwww(self) -> I8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> I8Vector2: ...

    @property
    def rg(self) -> I8Vector2: ...

    @property
    def rb(self) -> I8Vector2: ...

    @property
    def ra(self) -> I8Vector2: ...

    @property
    def gg(self) -> I8Vector2: ...

    @property
    def gb(self) -> I8Vector2: ...

    @property
    def ga(self) -> I8Vector2: ...

    @property
    def bb(self) -> I8Vector2: ...

    @property
    def ba(self) -> I8Vector2: ...

    @property
    def aa(self) -> I8Vector2: ...



    @property
    def rrr(self) -> I8Vector3: ...

    @property
    def rrg(self) -> I8Vector3: ...

    @property
    def rrb(self) -> I8Vector3: ...

    @property
    def rra(self) -> I8Vector3: ...

    @property
    def rgg(self) -> I8Vector3: ...

    @property
    def rgb(self) -> I8Vector3: ...

    @property
    def rga(self) -> I8Vector3: ...

    @property
    def rbb(self) -> I8Vector3: ...

    @property
    def rba(self) -> I8Vector3: ...

    @property
    def raa(self) -> I8Vector3: ...

    @property
    def ggg(self) -> I8Vector3: ...

    @property
    def ggb(self) -> I8Vector3: ...

    @property
    def gga(self) -> I8Vector3: ...

    @property
    def gbb(self) -> I8Vector3: ...

    @property
    def gba(self) -> I8Vector3: ...

    @property
    def gaa(self) -> I8Vector3: ...

    @property
    def bbb(self) -> I8Vector3: ...

    @property
    def bba(self) -> I8Vector3: ...

    @property
    def baa(self) -> I8Vector3: ...

    @property
    def aaa(self) -> I8Vector3: ...



    @property
    def rrrr(self) -> I8Vector4: ...

    @property
    def rrrg(self) -> I8Vector4: ...

    @property
    def rrrb(self) -> I8Vector4: ...

    @property
    def rrra(self) -> I8Vector4: ...

    @property
    def rrgg(self) -> I8Vector4: ...

    @property
    def rrgb(self) -> I8Vector4: ...

    @property
    def rrga(self) -> I8Vector4: ...

    @property
    def rrbb(self) -> I8Vector4: ...

    @property
    def rrba(self) -> I8Vector4: ...

    @property
    def rraa(self) -> I8Vector4: ...

    @property
    def rggg(self) -> I8Vector4: ...

    @property
    def rggb(self) -> I8Vector4: ...

    @property
    def rgga(self) -> I8Vector4: ...

    @property
    def rgbb(self) -> I8Vector4: ...

    @property
    def rgba(self) -> I8Vector4: ...

    @property
    def rgaa(self) -> I8Vector4: ...

    @property
    def rbbb(self) -> I8Vector4: ...

    @property
    def rbba(self) -> I8Vector4: ...

    @property
    def rbaa(self) -> I8Vector4: ...

    @property
    def raaa(self) -> I8Vector4: ...

    @property
    def gggg(self) -> I8Vector4: ...

    @property
    def gggb(self) -> I8Vector4: ...

    @property
    def ggga(self) -> I8Vector4: ...

    @property
    def ggbb(self) -> I8Vector4: ...

    @property
    def ggba(self) -> I8Vector4: ...

    @property
    def ggaa(self) -> I8Vector4: ...

    @property
    def gbbb(self) -> I8Vector4: ...

    @property
    def gbba(self) -> I8Vector4: ...

    @property
    def gbaa(self) -> I8Vector4: ...

    @property
    def gaaa(self) -> I8Vector4: ...

    @property
    def bbbb(self) -> I8Vector4: ...

    @property
    def bbba(self) -> I8Vector4: ...

    @property
    def bbaa(self) -> I8Vector4: ...

    @property
    def baaa(self) -> I8Vector4: ...

    @property
    def aaaa(self) -> I8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> I8Vector2: ...

    @property
    def st(self) -> I8Vector2: ...

    @property
    def sq(self) -> I8Vector2: ...

    @property
    def sp(self) -> I8Vector2: ...

    @property
    def tt(self) -> I8Vector2: ...

    @property
    def tq(self) -> I8Vector2: ...

    @property
    def tp(self) -> I8Vector2: ...

    @property
    def qq(self) -> I8Vector2: ...

    @property
    def qp(self) -> I8Vector2: ...

    @property
    def pp(self) -> I8Vector2: ...



    @property
    def sss(self) -> I8Vector3: ...

    @property
    def sst(self) -> I8Vector3: ...

    @property
    def ssq(self) -> I8Vector3: ...

    @property
    def ssp(self) -> I8Vector3: ...

    @property
    def stt(self) -> I8Vector3: ...

    @property
    def stq(self) -> I8Vector3: ...

    @property
    def stp(self) -> I8Vector3: ...

    @property
    def sqq(self) -> I8Vector3: ...

    @property
    def sqp(self) -> I8Vector3: ...

    @property
    def spp(self) -> I8Vector3: ...

    @property
    def ttt(self) -> I8Vector3: ...

    @property
    def ttq(self) -> I8Vector3: ...

    @property
    def ttp(self) -> I8Vector3: ...

    @property
    def tqq(self) -> I8Vector3: ...

    @property
    def tqp(self) -> I8Vector3: ...

    @property
    def tpp(self) -> I8Vector3: ...

    @property
    def qqq(self) -> I8Vector3: ...

    @property
    def qqp(self) -> I8Vector3: ...

    @property
    def qpp(self) -> I8Vector3: ...

    @property
    def ppp(self) -> I8Vector3: ...



    @property
    def ssss(self) -> I8Vector4: ...

    @property
    def ssst(self) -> I8Vector4: ...

    @property
    def sssq(self) -> I8Vector4: ...

    @property
    def sssp(self) -> I8Vector4: ...

    @property
    def sstt(self) -> I8Vector4: ...

    @property
    def sstq(self) -> I8Vector4: ...

    @property
    def sstp(self) -> I8Vector4: ...

    @property
    def ssqq(self) -> I8Vector4: ...

    @property
    def ssqp(self) -> I8Vector4: ...

    @property
    def sspp(self) -> I8Vector4: ...

    @property
    def sttt(self) -> I8Vector4: ...

    @property
    def sttq(self) -> I8Vector4: ...

    @property
    def sttp(self) -> I8Vector4: ...

    @property
    def stqq(self) -> I8Vector4: ...

    @property
    def stqp(self) -> I8Vector4: ...

    @property
    def stpp(self) -> I8Vector4: ...

    @property
    def sqqq(self) -> I8Vector4: ...

    @property
    def sqqp(self) -> I8Vector4: ...

    @property
    def sqpp(self) -> I8Vector4: ...

    @property
    def sppp(self) -> I8Vector4: ...

    @property
    def tttt(self) -> I8Vector4: ...

    @property
    def tttq(self) -> I8Vector4: ...

    @property
    def tttp(self) -> I8Vector4: ...

    @property
    def ttqq(self) -> I8Vector4: ...

    @property
    def ttqp(self) -> I8Vector4: ...

    @property
    def ttpp(self) -> I8Vector4: ...

    @property
    def tqqq(self) -> I8Vector4: ...

    @property
    def tqqp(self) -> I8Vector4: ...

    @property
    def tqpp(self) -> I8Vector4: ...

    @property
    def tppp(self) -> I8Vector4: ...

    @property
    def qqqq(self) -> I8Vector4: ...

    @property
    def qqqp(self) -> I8Vector4: ...

    @property
    def qqpp(self) -> I8Vector4: ...

    @property
    def qppp(self) -> I8Vector4: ...

    @property
    def pppp(self) -> I8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I8Vector2: ...

    @property
    def uv(self) -> I8Vector2: ...

    @property
    def vv(self) -> I8Vector2: ...



    @property
    def uuu(self) -> I8Vector3: ...

    @property
    def uuv(self) -> I8Vector3: ...

    @property
    def uvv(self) -> I8Vector3: ...

    @property
    def vvv(self) -> I8Vector3: ...



    @property
    def uuuu(self) -> I8Vector4: ...

    @property
    def uuuv(self) -> I8Vector4: ...

    @property
    def uuvv(self) -> I8Vector4: ...

    @property
    def uvvv(self) -> I8Vector4: ...

    @property
    def vvvv(self) -> I8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U8Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __add__(self, other: Number) -> U8Vector4: ...
    @overload
    def __radd__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __radd__(self, other: Number) -> U8Vector4: ...

    @overload
    def __sub__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __sub__(self, other: Number) -> U8Vector4: ...
    @overload
    def __rsub__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> U8Vector4: ...

    @overload
    def __mul__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __mul__(self, other: Number) -> U8Vector4: ...
    @overload
    def __rmul__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> U8Vector4: ...




    @overload
    def __truediv__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> U8Vector4: ...
    @overload
    def __rtruediv__(self, other: U8Vector4) -> U8Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> U8Vector4: ...



    def __neg__(self) -> U8Vector4: ...


    def __abs__(self) -> U8Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> U8Vector2: ...

    @property
    def xy(self) -> U8Vector2: ...

    @property
    def xz(self) -> U8Vector2: ...

    @property
    def xw(self) -> U8Vector2: ...

    @property
    def yy(self) -> U8Vector2: ...

    @property
    def yz(self) -> U8Vector2: ...

    @property
    def yw(self) -> U8Vector2: ...

    @property
    def zz(self) -> U8Vector2: ...

    @property
    def zw(self) -> U8Vector2: ...

    @property
    def ww(self) -> U8Vector2: ...



    @property
    def xxx(self) -> U8Vector3: ...

    @property
    def xxy(self) -> U8Vector3: ...

    @property
    def xxz(self) -> U8Vector3: ...

    @property
    def xxw(self) -> U8Vector3: ...

    @property
    def xyy(self) -> U8Vector3: ...

    @property
    def xyz(self) -> U8Vector3: ...

    @property
    def xyw(self) -> U8Vector3: ...

    @property
    def xzz(self) -> U8Vector3: ...

    @property
    def xzw(self) -> U8Vector3: ...

    @property
    def xww(self) -> U8Vector3: ...

    @property
    def yyy(self) -> U8Vector3: ...

    @property
    def yyz(self) -> U8Vector3: ...

    @property
    def yyw(self) -> U8Vector3: ...

    @property
    def yzz(self) -> U8Vector3: ...

    @property
    def yzw(self) -> U8Vector3: ...

    @property
    def yww(self) -> U8Vector3: ...

    @property
    def zzz(self) -> U8Vector3: ...

    @property
    def zzw(self) -> U8Vector3: ...

    @property
    def zww(self) -> U8Vector3: ...

    @property
    def www(self) -> U8Vector3: ...



    @property
    def xxxx(self) -> U8Vector4: ...

    @property
    def xxxy(self) -> U8Vector4: ...

    @property
    def xxxz(self) -> U8Vector4: ...

    @property
    def xxxw(self) -> U8Vector4: ...

    @property
    def xxyy(self) -> U8Vector4: ...

    @property
    def xxyz(self) -> U8Vector4: ...

    @property
    def xxyw(self) -> U8Vector4: ...

    @property
    def xxzz(self) -> U8Vector4: ...

    @property
    def xxzw(self) -> U8Vector4: ...

    @property
    def xxww(self) -> U8Vector4: ...

    @property
    def xyyy(self) -> U8Vector4: ...

    @property
    def xyyz(self) -> U8Vector4: ...

    @property
    def xyyw(self) -> U8Vector4: ...

    @property
    def xyzz(self) -> U8Vector4: ...

    @property
    def xyzw(self) -> U8Vector4: ...

    @property
    def xyww(self) -> U8Vector4: ...

    @property
    def xzzz(self) -> U8Vector4: ...

    @property
    def xzzw(self) -> U8Vector4: ...

    @property
    def xzww(self) -> U8Vector4: ...

    @property
    def xwww(self) -> U8Vector4: ...

    @property
    def yyyy(self) -> U8Vector4: ...

    @property
    def yyyz(self) -> U8Vector4: ...

    @property
    def yyyw(self) -> U8Vector4: ...

    @property
    def yyzz(self) -> U8Vector4: ...

    @property
    def yyzw(self) -> U8Vector4: ...

    @property
    def yyww(self) -> U8Vector4: ...

    @property
    def yzzz(self) -> U8Vector4: ...

    @property
    def yzzw(self) -> U8Vector4: ...

    @property
    def yzww(self) -> U8Vector4: ...

    @property
    def ywww(self) -> U8Vector4: ...

    @property
    def zzzz(self) -> U8Vector4: ...

    @property
    def zzzw(self) -> U8Vector4: ...

    @property
    def zzww(self) -> U8Vector4: ...

    @property
    def zwww(self) -> U8Vector4: ...

    @property
    def wwww(self) -> U8Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> U8Vector2: ...

    @property
    def rg(self) -> U8Vector2: ...

    @property
    def rb(self) -> U8Vector2: ...

    @property
    def ra(self) -> U8Vector2: ...

    @property
    def gg(self) -> U8Vector2: ...

    @property
    def gb(self) -> U8Vector2: ...

    @property
    def ga(self) -> U8Vector2: ...

    @property
    def bb(self) -> U8Vector2: ...

    @property
    def ba(self) -> U8Vector2: ...

    @property
    def aa(self) -> U8Vector2: ...



    @property
    def rrr(self) -> U8Vector3: ...

    @property
    def rrg(self) -> U8Vector3: ...

    @property
    def rrb(self) -> U8Vector3: ...

    @property
    def rra(self) -> U8Vector3: ...

    @property
    def rgg(self) -> U8Vector3: ...

    @property
    def rgb(self) -> U8Vector3: ...

    @property
    def rga(self) -> U8Vector3: ...

    @property
    def rbb(self) -> U8Vector3: ...

    @property
    def rba(self) -> U8Vector3: ...

    @property
    def raa(self) -> U8Vector3: ...

    @property
    def ggg(self) -> U8Vector3: ...

    @property
    def ggb(self) -> U8Vector3: ...

    @property
    def gga(self) -> U8Vector3: ...

    @property
    def gbb(self) -> U8Vector3: ...

    @property
    def gba(self) -> U8Vector3: ...

    @property
    def gaa(self) -> U8Vector3: ...

    @property
    def bbb(self) -> U8Vector3: ...

    @property
    def bba(self) -> U8Vector3: ...

    @property
    def baa(self) -> U8Vector3: ...

    @property
    def aaa(self) -> U8Vector3: ...



    @property
    def rrrr(self) -> U8Vector4: ...

    @property
    def rrrg(self) -> U8Vector4: ...

    @property
    def rrrb(self) -> U8Vector4: ...

    @property
    def rrra(self) -> U8Vector4: ...

    @property
    def rrgg(self) -> U8Vector4: ...

    @property
    def rrgb(self) -> U8Vector4: ...

    @property
    def rrga(self) -> U8Vector4: ...

    @property
    def rrbb(self) -> U8Vector4: ...

    @property
    def rrba(self) -> U8Vector4: ...

    @property
    def rraa(self) -> U8Vector4: ...

    @property
    def rggg(self) -> U8Vector4: ...

    @property
    def rggb(self) -> U8Vector4: ...

    @property
    def rgga(self) -> U8Vector4: ...

    @property
    def rgbb(self) -> U8Vector4: ...

    @property
    def rgba(self) -> U8Vector4: ...

    @property
    def rgaa(self) -> U8Vector4: ...

    @property
    def rbbb(self) -> U8Vector4: ...

    @property
    def rbba(self) -> U8Vector4: ...

    @property
    def rbaa(self) -> U8Vector4: ...

    @property
    def raaa(self) -> U8Vector4: ...

    @property
    def gggg(self) -> U8Vector4: ...

    @property
    def gggb(self) -> U8Vector4: ...

    @property
    def ggga(self) -> U8Vector4: ...

    @property
    def ggbb(self) -> U8Vector4: ...

    @property
    def ggba(self) -> U8Vector4: ...

    @property
    def ggaa(self) -> U8Vector4: ...

    @property
    def gbbb(self) -> U8Vector4: ...

    @property
    def gbba(self) -> U8Vector4: ...

    @property
    def gbaa(self) -> U8Vector4: ...

    @property
    def gaaa(self) -> U8Vector4: ...

    @property
    def bbbb(self) -> U8Vector4: ...

    @property
    def bbba(self) -> U8Vector4: ...

    @property
    def bbaa(self) -> U8Vector4: ...

    @property
    def baaa(self) -> U8Vector4: ...

    @property
    def aaaa(self) -> U8Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> U8Vector2: ...

    @property
    def st(self) -> U8Vector2: ...

    @property
    def sq(self) -> U8Vector2: ...

    @property
    def sp(self) -> U8Vector2: ...

    @property
    def tt(self) -> U8Vector2: ...

    @property
    def tq(self) -> U8Vector2: ...

    @property
    def tp(self) -> U8Vector2: ...

    @property
    def qq(self) -> U8Vector2: ...

    @property
    def qp(self) -> U8Vector2: ...

    @property
    def pp(self) -> U8Vector2: ...



    @property
    def sss(self) -> U8Vector3: ...

    @property
    def sst(self) -> U8Vector3: ...

    @property
    def ssq(self) -> U8Vector3: ...

    @property
    def ssp(self) -> U8Vector3: ...

    @property
    def stt(self) -> U8Vector3: ...

    @property
    def stq(self) -> U8Vector3: ...

    @property
    def stp(self) -> U8Vector3: ...

    @property
    def sqq(self) -> U8Vector3: ...

    @property
    def sqp(self) -> U8Vector3: ...

    @property
    def spp(self) -> U8Vector3: ...

    @property
    def ttt(self) -> U8Vector3: ...

    @property
    def ttq(self) -> U8Vector3: ...

    @property
    def ttp(self) -> U8Vector3: ...

    @property
    def tqq(self) -> U8Vector3: ...

    @property
    def tqp(self) -> U8Vector3: ...

    @property
    def tpp(self) -> U8Vector3: ...

    @property
    def qqq(self) -> U8Vector3: ...

    @property
    def qqp(self) -> U8Vector3: ...

    @property
    def qpp(self) -> U8Vector3: ...

    @property
    def ppp(self) -> U8Vector3: ...



    @property
    def ssss(self) -> U8Vector4: ...

    @property
    def ssst(self) -> U8Vector4: ...

    @property
    def sssq(self) -> U8Vector4: ...

    @property
    def sssp(self) -> U8Vector4: ...

    @property
    def sstt(self) -> U8Vector4: ...

    @property
    def sstq(self) -> U8Vector4: ...

    @property
    def sstp(self) -> U8Vector4: ...

    @property
    def ssqq(self) -> U8Vector4: ...

    @property
    def ssqp(self) -> U8Vector4: ...

    @property
    def sspp(self) -> U8Vector4: ...

    @property
    def sttt(self) -> U8Vector4: ...

    @property
    def sttq(self) -> U8Vector4: ...

    @property
    def sttp(self) -> U8Vector4: ...

    @property
    def stqq(self) -> U8Vector4: ...

    @property
    def stqp(self) -> U8Vector4: ...

    @property
    def stpp(self) -> U8Vector4: ...

    @property
    def sqqq(self) -> U8Vector4: ...

    @property
    def sqqp(self) -> U8Vector4: ...

    @property
    def sqpp(self) -> U8Vector4: ...

    @property
    def sppp(self) -> U8Vector4: ...

    @property
    def tttt(self) -> U8Vector4: ...

    @property
    def tttq(self) -> U8Vector4: ...

    @property
    def tttp(self) -> U8Vector4: ...

    @property
    def ttqq(self) -> U8Vector4: ...

    @property
    def ttqp(self) -> U8Vector4: ...

    @property
    def ttpp(self) -> U8Vector4: ...

    @property
    def tqqq(self) -> U8Vector4: ...

    @property
    def tqqp(self) -> U8Vector4: ...

    @property
    def tqpp(self) -> U8Vector4: ...

    @property
    def tppp(self) -> U8Vector4: ...

    @property
    def qqqq(self) -> U8Vector4: ...

    @property
    def qqqp(self) -> U8Vector4: ...

    @property
    def qqpp(self) -> U8Vector4: ...

    @property
    def qppp(self) -> U8Vector4: ...

    @property
    def pppp(self) -> U8Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U8Vector2: ...

    @property
    def uv(self) -> U8Vector2: ...

    @property
    def vv(self) -> U8Vector2: ...



    @property
    def uuu(self) -> U8Vector3: ...

    @property
    def uuv(self) -> U8Vector3: ...

    @property
    def uvv(self) -> U8Vector3: ...

    @property
    def vvv(self) -> U8Vector3: ...



    @property
    def uuuu(self) -> U8Vector4: ...

    @property
    def uuuv(self) -> U8Vector4: ...

    @property
    def uuvv(self) -> U8Vector4: ...

    @property
    def uvvv(self) -> U8Vector4: ...

    @property
    def vvvv(self) -> U8Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I16Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __add__(self, other: Number) -> I16Vector4: ...
    @overload
    def __radd__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __radd__(self, other: Number) -> I16Vector4: ...

    @overload
    def __sub__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __sub__(self, other: Number) -> I16Vector4: ...
    @overload
    def __rsub__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> I16Vector4: ...

    @overload
    def __mul__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __mul__(self, other: Number) -> I16Vector4: ...
    @overload
    def __rmul__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> I16Vector4: ...




    @overload
    def __truediv__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> I16Vector4: ...
    @overload
    def __rtruediv__(self, other: I16Vector4) -> I16Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> I16Vector4: ...




    def __abs__(self) -> I16Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> I16Vector2: ...

    @property
    def xy(self) -> I16Vector2: ...

    @property
    def xz(self) -> I16Vector2: ...

    @property
    def xw(self) -> I16Vector2: ...

    @property
    def yy(self) -> I16Vector2: ...

    @property
    def yz(self) -> I16Vector2: ...

    @property
    def yw(self) -> I16Vector2: ...

    @property
    def zz(self) -> I16Vector2: ...

    @property
    def zw(self) -> I16Vector2: ...

    @property
    def ww(self) -> I16Vector2: ...



    @property
    def xxx(self) -> I16Vector3: ...

    @property
    def xxy(self) -> I16Vector3: ...

    @property
    def xxz(self) -> I16Vector3: ...

    @property
    def xxw(self) -> I16Vector3: ...

    @property
    def xyy(self) -> I16Vector3: ...

    @property
    def xyz(self) -> I16Vector3: ...

    @property
    def xyw(self) -> I16Vector3: ...

    @property
    def xzz(self) -> I16Vector3: ...

    @property
    def xzw(self) -> I16Vector3: ...

    @property
    def xww(self) -> I16Vector3: ...

    @property
    def yyy(self) -> I16Vector3: ...

    @property
    def yyz(self) -> I16Vector3: ...

    @property
    def yyw(self) -> I16Vector3: ...

    @property
    def yzz(self) -> I16Vector3: ...

    @property
    def yzw(self) -> I16Vector3: ...

    @property
    def yww(self) -> I16Vector3: ...

    @property
    def zzz(self) -> I16Vector3: ...

    @property
    def zzw(self) -> I16Vector3: ...

    @property
    def zww(self) -> I16Vector3: ...

    @property
    def www(self) -> I16Vector3: ...



    @property
    def xxxx(self) -> I16Vector4: ...

    @property
    def xxxy(self) -> I16Vector4: ...

    @property
    def xxxz(self) -> I16Vector4: ...

    @property
    def xxxw(self) -> I16Vector4: ...

    @property
    def xxyy(self) -> I16Vector4: ...

    @property
    def xxyz(self) -> I16Vector4: ...

    @property
    def xxyw(self) -> I16Vector4: ...

    @property
    def xxzz(self) -> I16Vector4: ...

    @property
    def xxzw(self) -> I16Vector4: ...

    @property
    def xxww(self) -> I16Vector4: ...

    @property
    def xyyy(self) -> I16Vector4: ...

    @property
    def xyyz(self) -> I16Vector4: ...

    @property
    def xyyw(self) -> I16Vector4: ...

    @property
    def xyzz(self) -> I16Vector4: ...

    @property
    def xyzw(self) -> I16Vector4: ...

    @property
    def xyww(self) -> I16Vector4: ...

    @property
    def xzzz(self) -> I16Vector4: ...

    @property
    def xzzw(self) -> I16Vector4: ...

    @property
    def xzww(self) -> I16Vector4: ...

    @property
    def xwww(self) -> I16Vector4: ...

    @property
    def yyyy(self) -> I16Vector4: ...

    @property
    def yyyz(self) -> I16Vector4: ...

    @property
    def yyyw(self) -> I16Vector4: ...

    @property
    def yyzz(self) -> I16Vector4: ...

    @property
    def yyzw(self) -> I16Vector4: ...

    @property
    def yyww(self) -> I16Vector4: ...

    @property
    def yzzz(self) -> I16Vector4: ...

    @property
    def yzzw(self) -> I16Vector4: ...

    @property
    def yzww(self) -> I16Vector4: ...

    @property
    def ywww(self) -> I16Vector4: ...

    @property
    def zzzz(self) -> I16Vector4: ...

    @property
    def zzzw(self) -> I16Vector4: ...

    @property
    def zzww(self) -> I16Vector4: ...

    @property
    def zwww(self) -> I16Vector4: ...

    @property
    def wwww(self) -> I16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> I16Vector2: ...

    @property
    def rg(self) -> I16Vector2: ...

    @property
    def rb(self) -> I16Vector2: ...

    @property
    def ra(self) -> I16Vector2: ...

    @property
    def gg(self) -> I16Vector2: ...

    @property
    def gb(self) -> I16Vector2: ...

    @property
    def ga(self) -> I16Vector2: ...

    @property
    def bb(self) -> I16Vector2: ...

    @property
    def ba(self) -> I16Vector2: ...

    @property
    def aa(self) -> I16Vector2: ...



    @property
    def rrr(self) -> I16Vector3: ...

    @property
    def rrg(self) -> I16Vector3: ...

    @property
    def rrb(self) -> I16Vector3: ...

    @property
    def rra(self) -> I16Vector3: ...

    @property
    def rgg(self) -> I16Vector3: ...

    @property
    def rgb(self) -> I16Vector3: ...

    @property
    def rga(self) -> I16Vector3: ...

    @property
    def rbb(self) -> I16Vector3: ...

    @property
    def rba(self) -> I16Vector3: ...

    @property
    def raa(self) -> I16Vector3: ...

    @property
    def ggg(self) -> I16Vector3: ...

    @property
    def ggb(self) -> I16Vector3: ...

    @property
    def gga(self) -> I16Vector3: ...

    @property
    def gbb(self) -> I16Vector3: ...

    @property
    def gba(self) -> I16Vector3: ...

    @property
    def gaa(self) -> I16Vector3: ...

    @property
    def bbb(self) -> I16Vector3: ...

    @property
    def bba(self) -> I16Vector3: ...

    @property
    def baa(self) -> I16Vector3: ...

    @property
    def aaa(self) -> I16Vector3: ...



    @property
    def rrrr(self) -> I16Vector4: ...

    @property
    def rrrg(self) -> I16Vector4: ...

    @property
    def rrrb(self) -> I16Vector4: ...

    @property
    def rrra(self) -> I16Vector4: ...

    @property
    def rrgg(self) -> I16Vector4: ...

    @property
    def rrgb(self) -> I16Vector4: ...

    @property
    def rrga(self) -> I16Vector4: ...

    @property
    def rrbb(self) -> I16Vector4: ...

    @property
    def rrba(self) -> I16Vector4: ...

    @property
    def rraa(self) -> I16Vector4: ...

    @property
    def rggg(self) -> I16Vector4: ...

    @property
    def rggb(self) -> I16Vector4: ...

    @property
    def rgga(self) -> I16Vector4: ...

    @property
    def rgbb(self) -> I16Vector4: ...

    @property
    def rgba(self) -> I16Vector4: ...

    @property
    def rgaa(self) -> I16Vector4: ...

    @property
    def rbbb(self) -> I16Vector4: ...

    @property
    def rbba(self) -> I16Vector4: ...

    @property
    def rbaa(self) -> I16Vector4: ...

    @property
    def raaa(self) -> I16Vector4: ...

    @property
    def gggg(self) -> I16Vector4: ...

    @property
    def gggb(self) -> I16Vector4: ...

    @property
    def ggga(self) -> I16Vector4: ...

    @property
    def ggbb(self) -> I16Vector4: ...

    @property
    def ggba(self) -> I16Vector4: ...

    @property
    def ggaa(self) -> I16Vector4: ...

    @property
    def gbbb(self) -> I16Vector4: ...

    @property
    def gbba(self) -> I16Vector4: ...

    @property
    def gbaa(self) -> I16Vector4: ...

    @property
    def gaaa(self) -> I16Vector4: ...

    @property
    def bbbb(self) -> I16Vector4: ...

    @property
    def bbba(self) -> I16Vector4: ...

    @property
    def bbaa(self) -> I16Vector4: ...

    @property
    def baaa(self) -> I16Vector4: ...

    @property
    def aaaa(self) -> I16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> I16Vector2: ...

    @property
    def st(self) -> I16Vector2: ...

    @property
    def sq(self) -> I16Vector2: ...

    @property
    def sp(self) -> I16Vector2: ...

    @property
    def tt(self) -> I16Vector2: ...

    @property
    def tq(self) -> I16Vector2: ...

    @property
    def tp(self) -> I16Vector2: ...

    @property
    def qq(self) -> I16Vector2: ...

    @property
    def qp(self) -> I16Vector2: ...

    @property
    def pp(self) -> I16Vector2: ...



    @property
    def sss(self) -> I16Vector3: ...

    @property
    def sst(self) -> I16Vector3: ...

    @property
    def ssq(self) -> I16Vector3: ...

    @property
    def ssp(self) -> I16Vector3: ...

    @property
    def stt(self) -> I16Vector3: ...

    @property
    def stq(self) -> I16Vector3: ...

    @property
    def stp(self) -> I16Vector3: ...

    @property
    def sqq(self) -> I16Vector3: ...

    @property
    def sqp(self) -> I16Vector3: ...

    @property
    def spp(self) -> I16Vector3: ...

    @property
    def ttt(self) -> I16Vector3: ...

    @property
    def ttq(self) -> I16Vector3: ...

    @property
    def ttp(self) -> I16Vector3: ...

    @property
    def tqq(self) -> I16Vector3: ...

    @property
    def tqp(self) -> I16Vector3: ...

    @property
    def tpp(self) -> I16Vector3: ...

    @property
    def qqq(self) -> I16Vector3: ...

    @property
    def qqp(self) -> I16Vector3: ...

    @property
    def qpp(self) -> I16Vector3: ...

    @property
    def ppp(self) -> I16Vector3: ...



    @property
    def ssss(self) -> I16Vector4: ...

    @property
    def ssst(self) -> I16Vector4: ...

    @property
    def sssq(self) -> I16Vector4: ...

    @property
    def sssp(self) -> I16Vector4: ...

    @property
    def sstt(self) -> I16Vector4: ...

    @property
    def sstq(self) -> I16Vector4: ...

    @property
    def sstp(self) -> I16Vector4: ...

    @property
    def ssqq(self) -> I16Vector4: ...

    @property
    def ssqp(self) -> I16Vector4: ...

    @property
    def sspp(self) -> I16Vector4: ...

    @property
    def sttt(self) -> I16Vector4: ...

    @property
    def sttq(self) -> I16Vector4: ...

    @property
    def sttp(self) -> I16Vector4: ...

    @property
    def stqq(self) -> I16Vector4: ...

    @property
    def stqp(self) -> I16Vector4: ...

    @property
    def stpp(self) -> I16Vector4: ...

    @property
    def sqqq(self) -> I16Vector4: ...

    @property
    def sqqp(self) -> I16Vector4: ...

    @property
    def sqpp(self) -> I16Vector4: ...

    @property
    def sppp(self) -> I16Vector4: ...

    @property
    def tttt(self) -> I16Vector4: ...

    @property
    def tttq(self) -> I16Vector4: ...

    @property
    def tttp(self) -> I16Vector4: ...

    @property
    def ttqq(self) -> I16Vector4: ...

    @property
    def ttqp(self) -> I16Vector4: ...

    @property
    def ttpp(self) -> I16Vector4: ...

    @property
    def tqqq(self) -> I16Vector4: ...

    @property
    def tqqp(self) -> I16Vector4: ...

    @property
    def tqpp(self) -> I16Vector4: ...

    @property
    def tppp(self) -> I16Vector4: ...

    @property
    def qqqq(self) -> I16Vector4: ...

    @property
    def qqqp(self) -> I16Vector4: ...

    @property
    def qqpp(self) -> I16Vector4: ...

    @property
    def qppp(self) -> I16Vector4: ...

    @property
    def pppp(self) -> I16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I16Vector2: ...

    @property
    def uv(self) -> I16Vector2: ...

    @property
    def vv(self) -> I16Vector2: ...



    @property
    def uuu(self) -> I16Vector3: ...

    @property
    def uuv(self) -> I16Vector3: ...

    @property
    def uvv(self) -> I16Vector3: ...

    @property
    def vvv(self) -> I16Vector3: ...



    @property
    def uuuu(self) -> I16Vector4: ...

    @property
    def uuuv(self) -> I16Vector4: ...

    @property
    def uuvv(self) -> I16Vector4: ...

    @property
    def uvvv(self) -> I16Vector4: ...

    @property
    def vvvv(self) -> I16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U16Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __add__(self, other: Number) -> U16Vector4: ...
    @overload
    def __radd__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __radd__(self, other: Number) -> U16Vector4: ...

    @overload
    def __sub__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __sub__(self, other: Number) -> U16Vector4: ...
    @overload
    def __rsub__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> U16Vector4: ...

    @overload
    def __mul__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __mul__(self, other: Number) -> U16Vector4: ...
    @overload
    def __rmul__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> U16Vector4: ...




    @overload
    def __truediv__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> U16Vector4: ...
    @overload
    def __rtruediv__(self, other: U16Vector4) -> U16Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> U16Vector4: ...



    def __neg__(self) -> U16Vector4: ...


    def __abs__(self) -> U16Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> U16Vector2: ...

    @property
    def xy(self) -> U16Vector2: ...

    @property
    def xz(self) -> U16Vector2: ...

    @property
    def xw(self) -> U16Vector2: ...

    @property
    def yy(self) -> U16Vector2: ...

    @property
    def yz(self) -> U16Vector2: ...

    @property
    def yw(self) -> U16Vector2: ...

    @property
    def zz(self) -> U16Vector2: ...

    @property
    def zw(self) -> U16Vector2: ...

    @property
    def ww(self) -> U16Vector2: ...



    @property
    def xxx(self) -> U16Vector3: ...

    @property
    def xxy(self) -> U16Vector3: ...

    @property
    def xxz(self) -> U16Vector3: ...

    @property
    def xxw(self) -> U16Vector3: ...

    @property
    def xyy(self) -> U16Vector3: ...

    @property
    def xyz(self) -> U16Vector3: ...

    @property
    def xyw(self) -> U16Vector3: ...

    @property
    def xzz(self) -> U16Vector3: ...

    @property
    def xzw(self) -> U16Vector3: ...

    @property
    def xww(self) -> U16Vector3: ...

    @property
    def yyy(self) -> U16Vector3: ...

    @property
    def yyz(self) -> U16Vector3: ...

    @property
    def yyw(self) -> U16Vector3: ...

    @property
    def yzz(self) -> U16Vector3: ...

    @property
    def yzw(self) -> U16Vector3: ...

    @property
    def yww(self) -> U16Vector3: ...

    @property
    def zzz(self) -> U16Vector3: ...

    @property
    def zzw(self) -> U16Vector3: ...

    @property
    def zww(self) -> U16Vector3: ...

    @property
    def www(self) -> U16Vector3: ...



    @property
    def xxxx(self) -> U16Vector4: ...

    @property
    def xxxy(self) -> U16Vector4: ...

    @property
    def xxxz(self) -> U16Vector4: ...

    @property
    def xxxw(self) -> U16Vector4: ...

    @property
    def xxyy(self) -> U16Vector4: ...

    @property
    def xxyz(self) -> U16Vector4: ...

    @property
    def xxyw(self) -> U16Vector4: ...

    @property
    def xxzz(self) -> U16Vector4: ...

    @property
    def xxzw(self) -> U16Vector4: ...

    @property
    def xxww(self) -> U16Vector4: ...

    @property
    def xyyy(self) -> U16Vector4: ...

    @property
    def xyyz(self) -> U16Vector4: ...

    @property
    def xyyw(self) -> U16Vector4: ...

    @property
    def xyzz(self) -> U16Vector4: ...

    @property
    def xyzw(self) -> U16Vector4: ...

    @property
    def xyww(self) -> U16Vector4: ...

    @property
    def xzzz(self) -> U16Vector4: ...

    @property
    def xzzw(self) -> U16Vector4: ...

    @property
    def xzww(self) -> U16Vector4: ...

    @property
    def xwww(self) -> U16Vector4: ...

    @property
    def yyyy(self) -> U16Vector4: ...

    @property
    def yyyz(self) -> U16Vector4: ...

    @property
    def yyyw(self) -> U16Vector4: ...

    @property
    def yyzz(self) -> U16Vector4: ...

    @property
    def yyzw(self) -> U16Vector4: ...

    @property
    def yyww(self) -> U16Vector4: ...

    @property
    def yzzz(self) -> U16Vector4: ...

    @property
    def yzzw(self) -> U16Vector4: ...

    @property
    def yzww(self) -> U16Vector4: ...

    @property
    def ywww(self) -> U16Vector4: ...

    @property
    def zzzz(self) -> U16Vector4: ...

    @property
    def zzzw(self) -> U16Vector4: ...

    @property
    def zzww(self) -> U16Vector4: ...

    @property
    def zwww(self) -> U16Vector4: ...

    @property
    def wwww(self) -> U16Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> U16Vector2: ...

    @property
    def rg(self) -> U16Vector2: ...

    @property
    def rb(self) -> U16Vector2: ...

    @property
    def ra(self) -> U16Vector2: ...

    @property
    def gg(self) -> U16Vector2: ...

    @property
    def gb(self) -> U16Vector2: ...

    @property
    def ga(self) -> U16Vector2: ...

    @property
    def bb(self) -> U16Vector2: ...

    @property
    def ba(self) -> U16Vector2: ...

    @property
    def aa(self) -> U16Vector2: ...



    @property
    def rrr(self) -> U16Vector3: ...

    @property
    def rrg(self) -> U16Vector3: ...

    @property
    def rrb(self) -> U16Vector3: ...

    @property
    def rra(self) -> U16Vector3: ...

    @property
    def rgg(self) -> U16Vector3: ...

    @property
    def rgb(self) -> U16Vector3: ...

    @property
    def rga(self) -> U16Vector3: ...

    @property
    def rbb(self) -> U16Vector3: ...

    @property
    def rba(self) -> U16Vector3: ...

    @property
    def raa(self) -> U16Vector3: ...

    @property
    def ggg(self) -> U16Vector3: ...

    @property
    def ggb(self) -> U16Vector3: ...

    @property
    def gga(self) -> U16Vector3: ...

    @property
    def gbb(self) -> U16Vector3: ...

    @property
    def gba(self) -> U16Vector3: ...

    @property
    def gaa(self) -> U16Vector3: ...

    @property
    def bbb(self) -> U16Vector3: ...

    @property
    def bba(self) -> U16Vector3: ...

    @property
    def baa(self) -> U16Vector3: ...

    @property
    def aaa(self) -> U16Vector3: ...



    @property
    def rrrr(self) -> U16Vector4: ...

    @property
    def rrrg(self) -> U16Vector4: ...

    @property
    def rrrb(self) -> U16Vector4: ...

    @property
    def rrra(self) -> U16Vector4: ...

    @property
    def rrgg(self) -> U16Vector4: ...

    @property
    def rrgb(self) -> U16Vector4: ...

    @property
    def rrga(self) -> U16Vector4: ...

    @property
    def rrbb(self) -> U16Vector4: ...

    @property
    def rrba(self) -> U16Vector4: ...

    @property
    def rraa(self) -> U16Vector4: ...

    @property
    def rggg(self) -> U16Vector4: ...

    @property
    def rggb(self) -> U16Vector4: ...

    @property
    def rgga(self) -> U16Vector4: ...

    @property
    def rgbb(self) -> U16Vector4: ...

    @property
    def rgba(self) -> U16Vector4: ...

    @property
    def rgaa(self) -> U16Vector4: ...

    @property
    def rbbb(self) -> U16Vector4: ...

    @property
    def rbba(self) -> U16Vector4: ...

    @property
    def rbaa(self) -> U16Vector4: ...

    @property
    def raaa(self) -> U16Vector4: ...

    @property
    def gggg(self) -> U16Vector4: ...

    @property
    def gggb(self) -> U16Vector4: ...

    @property
    def ggga(self) -> U16Vector4: ...

    @property
    def ggbb(self) -> U16Vector4: ...

    @property
    def ggba(self) -> U16Vector4: ...

    @property
    def ggaa(self) -> U16Vector4: ...

    @property
    def gbbb(self) -> U16Vector4: ...

    @property
    def gbba(self) -> U16Vector4: ...

    @property
    def gbaa(self) -> U16Vector4: ...

    @property
    def gaaa(self) -> U16Vector4: ...

    @property
    def bbbb(self) -> U16Vector4: ...

    @property
    def bbba(self) -> U16Vector4: ...

    @property
    def bbaa(self) -> U16Vector4: ...

    @property
    def baaa(self) -> U16Vector4: ...

    @property
    def aaaa(self) -> U16Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> U16Vector2: ...

    @property
    def st(self) -> U16Vector2: ...

    @property
    def sq(self) -> U16Vector2: ...

    @property
    def sp(self) -> U16Vector2: ...

    @property
    def tt(self) -> U16Vector2: ...

    @property
    def tq(self) -> U16Vector2: ...

    @property
    def tp(self) -> U16Vector2: ...

    @property
    def qq(self) -> U16Vector2: ...

    @property
    def qp(self) -> U16Vector2: ...

    @property
    def pp(self) -> U16Vector2: ...



    @property
    def sss(self) -> U16Vector3: ...

    @property
    def sst(self) -> U16Vector3: ...

    @property
    def ssq(self) -> U16Vector3: ...

    @property
    def ssp(self) -> U16Vector3: ...

    @property
    def stt(self) -> U16Vector3: ...

    @property
    def stq(self) -> U16Vector3: ...

    @property
    def stp(self) -> U16Vector3: ...

    @property
    def sqq(self) -> U16Vector3: ...

    @property
    def sqp(self) -> U16Vector3: ...

    @property
    def spp(self) -> U16Vector3: ...

    @property
    def ttt(self) -> U16Vector3: ...

    @property
    def ttq(self) -> U16Vector3: ...

    @property
    def ttp(self) -> U16Vector3: ...

    @property
    def tqq(self) -> U16Vector3: ...

    @property
    def tqp(self) -> U16Vector3: ...

    @property
    def tpp(self) -> U16Vector3: ...

    @property
    def qqq(self) -> U16Vector3: ...

    @property
    def qqp(self) -> U16Vector3: ...

    @property
    def qpp(self) -> U16Vector3: ...

    @property
    def ppp(self) -> U16Vector3: ...



    @property
    def ssss(self) -> U16Vector4: ...

    @property
    def ssst(self) -> U16Vector4: ...

    @property
    def sssq(self) -> U16Vector4: ...

    @property
    def sssp(self) -> U16Vector4: ...

    @property
    def sstt(self) -> U16Vector4: ...

    @property
    def sstq(self) -> U16Vector4: ...

    @property
    def sstp(self) -> U16Vector4: ...

    @property
    def ssqq(self) -> U16Vector4: ...

    @property
    def ssqp(self) -> U16Vector4: ...

    @property
    def sspp(self) -> U16Vector4: ...

    @property
    def sttt(self) -> U16Vector4: ...

    @property
    def sttq(self) -> U16Vector4: ...

    @property
    def sttp(self) -> U16Vector4: ...

    @property
    def stqq(self) -> U16Vector4: ...

    @property
    def stqp(self) -> U16Vector4: ...

    @property
    def stpp(self) -> U16Vector4: ...

    @property
    def sqqq(self) -> U16Vector4: ...

    @property
    def sqqp(self) -> U16Vector4: ...

    @property
    def sqpp(self) -> U16Vector4: ...

    @property
    def sppp(self) -> U16Vector4: ...

    @property
    def tttt(self) -> U16Vector4: ...

    @property
    def tttq(self) -> U16Vector4: ...

    @property
    def tttp(self) -> U16Vector4: ...

    @property
    def ttqq(self) -> U16Vector4: ...

    @property
    def ttqp(self) -> U16Vector4: ...

    @property
    def ttpp(self) -> U16Vector4: ...

    @property
    def tqqq(self) -> U16Vector4: ...

    @property
    def tqqp(self) -> U16Vector4: ...

    @property
    def tqpp(self) -> U16Vector4: ...

    @property
    def tppp(self) -> U16Vector4: ...

    @property
    def qqqq(self) -> U16Vector4: ...

    @property
    def qqqp(self) -> U16Vector4: ...

    @property
    def qqpp(self) -> U16Vector4: ...

    @property
    def qppp(self) -> U16Vector4: ...

    @property
    def pppp(self) -> U16Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U16Vector2: ...

    @property
    def uv(self) -> U16Vector2: ...

    @property
    def vv(self) -> U16Vector2: ...



    @property
    def uuu(self) -> U16Vector3: ...

    @property
    def uuv(self) -> U16Vector3: ...

    @property
    def uvv(self) -> U16Vector3: ...

    @property
    def vvv(self) -> U16Vector3: ...



    @property
    def uuuu(self) -> U16Vector4: ...

    @property
    def uuuv(self) -> U16Vector4: ...

    @property
    def uuvv(self) -> U16Vector4: ...

    @property
    def uvvv(self) -> U16Vector4: ...

    @property
    def vvvv(self) -> U16Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I32Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __add__(self, other: Number) -> I32Vector4: ...
    @overload
    def __radd__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __radd__(self, other: Number) -> I32Vector4: ...

    @overload
    def __sub__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __sub__(self, other: Number) -> I32Vector4: ...
    @overload
    def __rsub__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> I32Vector4: ...

    @overload
    def __mul__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __mul__(self, other: Number) -> I32Vector4: ...
    @overload
    def __rmul__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> I32Vector4: ...




    @overload
    def __truediv__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> I32Vector4: ...
    @overload
    def __rtruediv__(self, other: I32Vector4) -> I32Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> I32Vector4: ...




    def __abs__(self) -> I32Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> I32Vector2: ...

    @property
    def xy(self) -> I32Vector2: ...

    @property
    def xz(self) -> I32Vector2: ...

    @property
    def xw(self) -> I32Vector2: ...

    @property
    def yy(self) -> I32Vector2: ...

    @property
    def yz(self) -> I32Vector2: ...

    @property
    def yw(self) -> I32Vector2: ...

    @property
    def zz(self) -> I32Vector2: ...

    @property
    def zw(self) -> I32Vector2: ...

    @property
    def ww(self) -> I32Vector2: ...



    @property
    def xxx(self) -> I32Vector3: ...

    @property
    def xxy(self) -> I32Vector3: ...

    @property
    def xxz(self) -> I32Vector3: ...

    @property
    def xxw(self) -> I32Vector3: ...

    @property
    def xyy(self) -> I32Vector3: ...

    @property
    def xyz(self) -> I32Vector3: ...

    @property
    def xyw(self) -> I32Vector3: ...

    @property
    def xzz(self) -> I32Vector3: ...

    @property
    def xzw(self) -> I32Vector3: ...

    @property
    def xww(self) -> I32Vector3: ...

    @property
    def yyy(self) -> I32Vector3: ...

    @property
    def yyz(self) -> I32Vector3: ...

    @property
    def yyw(self) -> I32Vector3: ...

    @property
    def yzz(self) -> I32Vector3: ...

    @property
    def yzw(self) -> I32Vector3: ...

    @property
    def yww(self) -> I32Vector3: ...

    @property
    def zzz(self) -> I32Vector3: ...

    @property
    def zzw(self) -> I32Vector3: ...

    @property
    def zww(self) -> I32Vector3: ...

    @property
    def www(self) -> I32Vector3: ...



    @property
    def xxxx(self) -> I32Vector4: ...

    @property
    def xxxy(self) -> I32Vector4: ...

    @property
    def xxxz(self) -> I32Vector4: ...

    @property
    def xxxw(self) -> I32Vector4: ...

    @property
    def xxyy(self) -> I32Vector4: ...

    @property
    def xxyz(self) -> I32Vector4: ...

    @property
    def xxyw(self) -> I32Vector4: ...

    @property
    def xxzz(self) -> I32Vector4: ...

    @property
    def xxzw(self) -> I32Vector4: ...

    @property
    def xxww(self) -> I32Vector4: ...

    @property
    def xyyy(self) -> I32Vector4: ...

    @property
    def xyyz(self) -> I32Vector4: ...

    @property
    def xyyw(self) -> I32Vector4: ...

    @property
    def xyzz(self) -> I32Vector4: ...

    @property
    def xyzw(self) -> I32Vector4: ...

    @property
    def xyww(self) -> I32Vector4: ...

    @property
    def xzzz(self) -> I32Vector4: ...

    @property
    def xzzw(self) -> I32Vector4: ...

    @property
    def xzww(self) -> I32Vector4: ...

    @property
    def xwww(self) -> I32Vector4: ...

    @property
    def yyyy(self) -> I32Vector4: ...

    @property
    def yyyz(self) -> I32Vector4: ...

    @property
    def yyyw(self) -> I32Vector4: ...

    @property
    def yyzz(self) -> I32Vector4: ...

    @property
    def yyzw(self) -> I32Vector4: ...

    @property
    def yyww(self) -> I32Vector4: ...

    @property
    def yzzz(self) -> I32Vector4: ...

    @property
    def yzzw(self) -> I32Vector4: ...

    @property
    def yzww(self) -> I32Vector4: ...

    @property
    def ywww(self) -> I32Vector4: ...

    @property
    def zzzz(self) -> I32Vector4: ...

    @property
    def zzzw(self) -> I32Vector4: ...

    @property
    def zzww(self) -> I32Vector4: ...

    @property
    def zwww(self) -> I32Vector4: ...

    @property
    def wwww(self) -> I32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> I32Vector2: ...

    @property
    def rg(self) -> I32Vector2: ...

    @property
    def rb(self) -> I32Vector2: ...

    @property
    def ra(self) -> I32Vector2: ...

    @property
    def gg(self) -> I32Vector2: ...

    @property
    def gb(self) -> I32Vector2: ...

    @property
    def ga(self) -> I32Vector2: ...

    @property
    def bb(self) -> I32Vector2: ...

    @property
    def ba(self) -> I32Vector2: ...

    @property
    def aa(self) -> I32Vector2: ...



    @property
    def rrr(self) -> I32Vector3: ...

    @property
    def rrg(self) -> I32Vector3: ...

    @property
    def rrb(self) -> I32Vector3: ...

    @property
    def rra(self) -> I32Vector3: ...

    @property
    def rgg(self) -> I32Vector3: ...

    @property
    def rgb(self) -> I32Vector3: ...

    @property
    def rga(self) -> I32Vector3: ...

    @property
    def rbb(self) -> I32Vector3: ...

    @property
    def rba(self) -> I32Vector3: ...

    @property
    def raa(self) -> I32Vector3: ...

    @property
    def ggg(self) -> I32Vector3: ...

    @property
    def ggb(self) -> I32Vector3: ...

    @property
    def gga(self) -> I32Vector3: ...

    @property
    def gbb(self) -> I32Vector3: ...

    @property
    def gba(self) -> I32Vector3: ...

    @property
    def gaa(self) -> I32Vector3: ...

    @property
    def bbb(self) -> I32Vector3: ...

    @property
    def bba(self) -> I32Vector3: ...

    @property
    def baa(self) -> I32Vector3: ...

    @property
    def aaa(self) -> I32Vector3: ...



    @property
    def rrrr(self) -> I32Vector4: ...

    @property
    def rrrg(self) -> I32Vector4: ...

    @property
    def rrrb(self) -> I32Vector4: ...

    @property
    def rrra(self) -> I32Vector4: ...

    @property
    def rrgg(self) -> I32Vector4: ...

    @property
    def rrgb(self) -> I32Vector4: ...

    @property
    def rrga(self) -> I32Vector4: ...

    @property
    def rrbb(self) -> I32Vector4: ...

    @property
    def rrba(self) -> I32Vector4: ...

    @property
    def rraa(self) -> I32Vector4: ...

    @property
    def rggg(self) -> I32Vector4: ...

    @property
    def rggb(self) -> I32Vector4: ...

    @property
    def rgga(self) -> I32Vector4: ...

    @property
    def rgbb(self) -> I32Vector4: ...

    @property
    def rgba(self) -> I32Vector4: ...

    @property
    def rgaa(self) -> I32Vector4: ...

    @property
    def rbbb(self) -> I32Vector4: ...

    @property
    def rbba(self) -> I32Vector4: ...

    @property
    def rbaa(self) -> I32Vector4: ...

    @property
    def raaa(self) -> I32Vector4: ...

    @property
    def gggg(self) -> I32Vector4: ...

    @property
    def gggb(self) -> I32Vector4: ...

    @property
    def ggga(self) -> I32Vector4: ...

    @property
    def ggbb(self) -> I32Vector4: ...

    @property
    def ggba(self) -> I32Vector4: ...

    @property
    def ggaa(self) -> I32Vector4: ...

    @property
    def gbbb(self) -> I32Vector4: ...

    @property
    def gbba(self) -> I32Vector4: ...

    @property
    def gbaa(self) -> I32Vector4: ...

    @property
    def gaaa(self) -> I32Vector4: ...

    @property
    def bbbb(self) -> I32Vector4: ...

    @property
    def bbba(self) -> I32Vector4: ...

    @property
    def bbaa(self) -> I32Vector4: ...

    @property
    def baaa(self) -> I32Vector4: ...

    @property
    def aaaa(self) -> I32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> I32Vector2: ...

    @property
    def st(self) -> I32Vector2: ...

    @property
    def sq(self) -> I32Vector2: ...

    @property
    def sp(self) -> I32Vector2: ...

    @property
    def tt(self) -> I32Vector2: ...

    @property
    def tq(self) -> I32Vector2: ...

    @property
    def tp(self) -> I32Vector2: ...

    @property
    def qq(self) -> I32Vector2: ...

    @property
    def qp(self) -> I32Vector2: ...

    @property
    def pp(self) -> I32Vector2: ...



    @property
    def sss(self) -> I32Vector3: ...

    @property
    def sst(self) -> I32Vector3: ...

    @property
    def ssq(self) -> I32Vector3: ...

    @property
    def ssp(self) -> I32Vector3: ...

    @property
    def stt(self) -> I32Vector3: ...

    @property
    def stq(self) -> I32Vector3: ...

    @property
    def stp(self) -> I32Vector3: ...

    @property
    def sqq(self) -> I32Vector3: ...

    @property
    def sqp(self) -> I32Vector3: ...

    @property
    def spp(self) -> I32Vector3: ...

    @property
    def ttt(self) -> I32Vector3: ...

    @property
    def ttq(self) -> I32Vector3: ...

    @property
    def ttp(self) -> I32Vector3: ...

    @property
    def tqq(self) -> I32Vector3: ...

    @property
    def tqp(self) -> I32Vector3: ...

    @property
    def tpp(self) -> I32Vector3: ...

    @property
    def qqq(self) -> I32Vector3: ...

    @property
    def qqp(self) -> I32Vector3: ...

    @property
    def qpp(self) -> I32Vector3: ...

    @property
    def ppp(self) -> I32Vector3: ...



    @property
    def ssss(self) -> I32Vector4: ...

    @property
    def ssst(self) -> I32Vector4: ...

    @property
    def sssq(self) -> I32Vector4: ...

    @property
    def sssp(self) -> I32Vector4: ...

    @property
    def sstt(self) -> I32Vector4: ...

    @property
    def sstq(self) -> I32Vector4: ...

    @property
    def sstp(self) -> I32Vector4: ...

    @property
    def ssqq(self) -> I32Vector4: ...

    @property
    def ssqp(self) -> I32Vector4: ...

    @property
    def sspp(self) -> I32Vector4: ...

    @property
    def sttt(self) -> I32Vector4: ...

    @property
    def sttq(self) -> I32Vector4: ...

    @property
    def sttp(self) -> I32Vector4: ...

    @property
    def stqq(self) -> I32Vector4: ...

    @property
    def stqp(self) -> I32Vector4: ...

    @property
    def stpp(self) -> I32Vector4: ...

    @property
    def sqqq(self) -> I32Vector4: ...

    @property
    def sqqp(self) -> I32Vector4: ...

    @property
    def sqpp(self) -> I32Vector4: ...

    @property
    def sppp(self) -> I32Vector4: ...

    @property
    def tttt(self) -> I32Vector4: ...

    @property
    def tttq(self) -> I32Vector4: ...

    @property
    def tttp(self) -> I32Vector4: ...

    @property
    def ttqq(self) -> I32Vector4: ...

    @property
    def ttqp(self) -> I32Vector4: ...

    @property
    def ttpp(self) -> I32Vector4: ...

    @property
    def tqqq(self) -> I32Vector4: ...

    @property
    def tqqp(self) -> I32Vector4: ...

    @property
    def tqpp(self) -> I32Vector4: ...

    @property
    def tppp(self) -> I32Vector4: ...

    @property
    def qqqq(self) -> I32Vector4: ...

    @property
    def qqqp(self) -> I32Vector4: ...

    @property
    def qqpp(self) -> I32Vector4: ...

    @property
    def qppp(self) -> I32Vector4: ...

    @property
    def pppp(self) -> I32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I32Vector2: ...

    @property
    def uv(self) -> I32Vector2: ...

    @property
    def vv(self) -> I32Vector2: ...



    @property
    def uuu(self) -> I32Vector3: ...

    @property
    def uuv(self) -> I32Vector3: ...

    @property
    def uvv(self) -> I32Vector3: ...

    @property
    def vvv(self) -> I32Vector3: ...



    @property
    def uuuu(self) -> I32Vector4: ...

    @property
    def uuuv(self) -> I32Vector4: ...

    @property
    def uuvv(self) -> I32Vector4: ...

    @property
    def uvvv(self) -> I32Vector4: ...

    @property
    def vvvv(self) -> I32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U32Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __add__(self, other: Number) -> U32Vector4: ...
    @overload
    def __radd__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __radd__(self, other: Number) -> U32Vector4: ...

    @overload
    def __sub__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __sub__(self, other: Number) -> U32Vector4: ...
    @overload
    def __rsub__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> U32Vector4: ...

    @overload
    def __mul__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __mul__(self, other: Number) -> U32Vector4: ...
    @overload
    def __rmul__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> U32Vector4: ...




    @overload
    def __truediv__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> U32Vector4: ...
    @overload
    def __rtruediv__(self, other: U32Vector4) -> U32Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> U32Vector4: ...



    def __neg__(self) -> U32Vector4: ...


    def __abs__(self) -> U32Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> U32Vector2: ...

    @property
    def xy(self) -> U32Vector2: ...

    @property
    def xz(self) -> U32Vector2: ...

    @property
    def xw(self) -> U32Vector2: ...

    @property
    def yy(self) -> U32Vector2: ...

    @property
    def yz(self) -> U32Vector2: ...

    @property
    def yw(self) -> U32Vector2: ...

    @property
    def zz(self) -> U32Vector2: ...

    @property
    def zw(self) -> U32Vector2: ...

    @property
    def ww(self) -> U32Vector2: ...



    @property
    def xxx(self) -> U32Vector3: ...

    @property
    def xxy(self) -> U32Vector3: ...

    @property
    def xxz(self) -> U32Vector3: ...

    @property
    def xxw(self) -> U32Vector3: ...

    @property
    def xyy(self) -> U32Vector3: ...

    @property
    def xyz(self) -> U32Vector3: ...

    @property
    def xyw(self) -> U32Vector3: ...

    @property
    def xzz(self) -> U32Vector3: ...

    @property
    def xzw(self) -> U32Vector3: ...

    @property
    def xww(self) -> U32Vector3: ...

    @property
    def yyy(self) -> U32Vector3: ...

    @property
    def yyz(self) -> U32Vector3: ...

    @property
    def yyw(self) -> U32Vector3: ...

    @property
    def yzz(self) -> U32Vector3: ...

    @property
    def yzw(self) -> U32Vector3: ...

    @property
    def yww(self) -> U32Vector3: ...

    @property
    def zzz(self) -> U32Vector3: ...

    @property
    def zzw(self) -> U32Vector3: ...

    @property
    def zww(self) -> U32Vector3: ...

    @property
    def www(self) -> U32Vector3: ...



    @property
    def xxxx(self) -> U32Vector4: ...

    @property
    def xxxy(self) -> U32Vector4: ...

    @property
    def xxxz(self) -> U32Vector4: ...

    @property
    def xxxw(self) -> U32Vector4: ...

    @property
    def xxyy(self) -> U32Vector4: ...

    @property
    def xxyz(self) -> U32Vector4: ...

    @property
    def xxyw(self) -> U32Vector4: ...

    @property
    def xxzz(self) -> U32Vector4: ...

    @property
    def xxzw(self) -> U32Vector4: ...

    @property
    def xxww(self) -> U32Vector4: ...

    @property
    def xyyy(self) -> U32Vector4: ...

    @property
    def xyyz(self) -> U32Vector4: ...

    @property
    def xyyw(self) -> U32Vector4: ...

    @property
    def xyzz(self) -> U32Vector4: ...

    @property
    def xyzw(self) -> U32Vector4: ...

    @property
    def xyww(self) -> U32Vector4: ...

    @property
    def xzzz(self) -> U32Vector4: ...

    @property
    def xzzw(self) -> U32Vector4: ...

    @property
    def xzww(self) -> U32Vector4: ...

    @property
    def xwww(self) -> U32Vector4: ...

    @property
    def yyyy(self) -> U32Vector4: ...

    @property
    def yyyz(self) -> U32Vector4: ...

    @property
    def yyyw(self) -> U32Vector4: ...

    @property
    def yyzz(self) -> U32Vector4: ...

    @property
    def yyzw(self) -> U32Vector4: ...

    @property
    def yyww(self) -> U32Vector4: ...

    @property
    def yzzz(self) -> U32Vector4: ...

    @property
    def yzzw(self) -> U32Vector4: ...

    @property
    def yzww(self) -> U32Vector4: ...

    @property
    def ywww(self) -> U32Vector4: ...

    @property
    def zzzz(self) -> U32Vector4: ...

    @property
    def zzzw(self) -> U32Vector4: ...

    @property
    def zzww(self) -> U32Vector4: ...

    @property
    def zwww(self) -> U32Vector4: ...

    @property
    def wwww(self) -> U32Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> U32Vector2: ...

    @property
    def rg(self) -> U32Vector2: ...

    @property
    def rb(self) -> U32Vector2: ...

    @property
    def ra(self) -> U32Vector2: ...

    @property
    def gg(self) -> U32Vector2: ...

    @property
    def gb(self) -> U32Vector2: ...

    @property
    def ga(self) -> U32Vector2: ...

    @property
    def bb(self) -> U32Vector2: ...

    @property
    def ba(self) -> U32Vector2: ...

    @property
    def aa(self) -> U32Vector2: ...



    @property
    def rrr(self) -> U32Vector3: ...

    @property
    def rrg(self) -> U32Vector3: ...

    @property
    def rrb(self) -> U32Vector3: ...

    @property
    def rra(self) -> U32Vector3: ...

    @property
    def rgg(self) -> U32Vector3: ...

    @property
    def rgb(self) -> U32Vector3: ...

    @property
    def rga(self) -> U32Vector3: ...

    @property
    def rbb(self) -> U32Vector3: ...

    @property
    def rba(self) -> U32Vector3: ...

    @property
    def raa(self) -> U32Vector3: ...

    @property
    def ggg(self) -> U32Vector3: ...

    @property
    def ggb(self) -> U32Vector3: ...

    @property
    def gga(self) -> U32Vector3: ...

    @property
    def gbb(self) -> U32Vector3: ...

    @property
    def gba(self) -> U32Vector3: ...

    @property
    def gaa(self) -> U32Vector3: ...

    @property
    def bbb(self) -> U32Vector3: ...

    @property
    def bba(self) -> U32Vector3: ...

    @property
    def baa(self) -> U32Vector3: ...

    @property
    def aaa(self) -> U32Vector3: ...



    @property
    def rrrr(self) -> U32Vector4: ...

    @property
    def rrrg(self) -> U32Vector4: ...

    @property
    def rrrb(self) -> U32Vector4: ...

    @property
    def rrra(self) -> U32Vector4: ...

    @property
    def rrgg(self) -> U32Vector4: ...

    @property
    def rrgb(self) -> U32Vector4: ...

    @property
    def rrga(self) -> U32Vector4: ...

    @property
    def rrbb(self) -> U32Vector4: ...

    @property
    def rrba(self) -> U32Vector4: ...

    @property
    def rraa(self) -> U32Vector4: ...

    @property
    def rggg(self) -> U32Vector4: ...

    @property
    def rggb(self) -> U32Vector4: ...

    @property
    def rgga(self) -> U32Vector4: ...

    @property
    def rgbb(self) -> U32Vector4: ...

    @property
    def rgba(self) -> U32Vector4: ...

    @property
    def rgaa(self) -> U32Vector4: ...

    @property
    def rbbb(self) -> U32Vector4: ...

    @property
    def rbba(self) -> U32Vector4: ...

    @property
    def rbaa(self) -> U32Vector4: ...

    @property
    def raaa(self) -> U32Vector4: ...

    @property
    def gggg(self) -> U32Vector4: ...

    @property
    def gggb(self) -> U32Vector4: ...

    @property
    def ggga(self) -> U32Vector4: ...

    @property
    def ggbb(self) -> U32Vector4: ...

    @property
    def ggba(self) -> U32Vector4: ...

    @property
    def ggaa(self) -> U32Vector4: ...

    @property
    def gbbb(self) -> U32Vector4: ...

    @property
    def gbba(self) -> U32Vector4: ...

    @property
    def gbaa(self) -> U32Vector4: ...

    @property
    def gaaa(self) -> U32Vector4: ...

    @property
    def bbbb(self) -> U32Vector4: ...

    @property
    def bbba(self) -> U32Vector4: ...

    @property
    def bbaa(self) -> U32Vector4: ...

    @property
    def baaa(self) -> U32Vector4: ...

    @property
    def aaaa(self) -> U32Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> U32Vector2: ...

    @property
    def st(self) -> U32Vector2: ...

    @property
    def sq(self) -> U32Vector2: ...

    @property
    def sp(self) -> U32Vector2: ...

    @property
    def tt(self) -> U32Vector2: ...

    @property
    def tq(self) -> U32Vector2: ...

    @property
    def tp(self) -> U32Vector2: ...

    @property
    def qq(self) -> U32Vector2: ...

    @property
    def qp(self) -> U32Vector2: ...

    @property
    def pp(self) -> U32Vector2: ...



    @property
    def sss(self) -> U32Vector3: ...

    @property
    def sst(self) -> U32Vector3: ...

    @property
    def ssq(self) -> U32Vector3: ...

    @property
    def ssp(self) -> U32Vector3: ...

    @property
    def stt(self) -> U32Vector3: ...

    @property
    def stq(self) -> U32Vector3: ...

    @property
    def stp(self) -> U32Vector3: ...

    @property
    def sqq(self) -> U32Vector3: ...

    @property
    def sqp(self) -> U32Vector3: ...

    @property
    def spp(self) -> U32Vector3: ...

    @property
    def ttt(self) -> U32Vector3: ...

    @property
    def ttq(self) -> U32Vector3: ...

    @property
    def ttp(self) -> U32Vector3: ...

    @property
    def tqq(self) -> U32Vector3: ...

    @property
    def tqp(self) -> U32Vector3: ...

    @property
    def tpp(self) -> U32Vector3: ...

    @property
    def qqq(self) -> U32Vector3: ...

    @property
    def qqp(self) -> U32Vector3: ...

    @property
    def qpp(self) -> U32Vector3: ...

    @property
    def ppp(self) -> U32Vector3: ...



    @property
    def ssss(self) -> U32Vector4: ...

    @property
    def ssst(self) -> U32Vector4: ...

    @property
    def sssq(self) -> U32Vector4: ...

    @property
    def sssp(self) -> U32Vector4: ...

    @property
    def sstt(self) -> U32Vector4: ...

    @property
    def sstq(self) -> U32Vector4: ...

    @property
    def sstp(self) -> U32Vector4: ...

    @property
    def ssqq(self) -> U32Vector4: ...

    @property
    def ssqp(self) -> U32Vector4: ...

    @property
    def sspp(self) -> U32Vector4: ...

    @property
    def sttt(self) -> U32Vector4: ...

    @property
    def sttq(self) -> U32Vector4: ...

    @property
    def sttp(self) -> U32Vector4: ...

    @property
    def stqq(self) -> U32Vector4: ...

    @property
    def stqp(self) -> U32Vector4: ...

    @property
    def stpp(self) -> U32Vector4: ...

    @property
    def sqqq(self) -> U32Vector4: ...

    @property
    def sqqp(self) -> U32Vector4: ...

    @property
    def sqpp(self) -> U32Vector4: ...

    @property
    def sppp(self) -> U32Vector4: ...

    @property
    def tttt(self) -> U32Vector4: ...

    @property
    def tttq(self) -> U32Vector4: ...

    @property
    def tttp(self) -> U32Vector4: ...

    @property
    def ttqq(self) -> U32Vector4: ...

    @property
    def ttqp(self) -> U32Vector4: ...

    @property
    def ttpp(self) -> U32Vector4: ...

    @property
    def tqqq(self) -> U32Vector4: ...

    @property
    def tqqp(self) -> U32Vector4: ...

    @property
    def tqpp(self) -> U32Vector4: ...

    @property
    def tppp(self) -> U32Vector4: ...

    @property
    def qqqq(self) -> U32Vector4: ...

    @property
    def qqqp(self) -> U32Vector4: ...

    @property
    def qqpp(self) -> U32Vector4: ...

    @property
    def qppp(self) -> U32Vector4: ...

    @property
    def pppp(self) -> U32Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U32Vector2: ...

    @property
    def uv(self) -> U32Vector2: ...

    @property
    def vv(self) -> U32Vector2: ...



    @property
    def uuu(self) -> U32Vector3: ...

    @property
    def uuv(self) -> U32Vector3: ...

    @property
    def uvv(self) -> U32Vector3: ...

    @property
    def vvv(self) -> U32Vector3: ...



    @property
    def uuuu(self) -> U32Vector4: ...

    @property
    def uuuv(self) -> U32Vector4: ...

    @property
    def uuvv(self) -> U32Vector4: ...

    @property
    def uvvv(self) -> U32Vector4: ...

    @property
    def vvvv(self) -> U32Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class IVector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: IVector4) -> IVector4: ...
    @overload
    def __add__(self, other: Number) -> IVector4: ...
    @overload
    def __radd__(self, other: IVector4) -> IVector4: ...
    @overload
    def __radd__(self, other: Number) -> IVector4: ...

    @overload
    def __sub__(self, other: IVector4) -> IVector4: ...
    @overload
    def __sub__(self, other: Number) -> IVector4: ...
    @overload
    def __rsub__(self, other: IVector4) -> IVector4: ...
    @overload
    def __rsub__(self, other: Number) -> IVector4: ...

    @overload
    def __mul__(self, other: IVector4) -> IVector4: ...
    @overload
    def __mul__(self, other: Number) -> IVector4: ...
    @overload
    def __rmul__(self, other: IVector4) -> IVector4: ...
    @overload
    def __rmul__(self, other: Number) -> IVector4: ...




    @overload
    def __truediv__(self, other: IVector4) -> IVector4: ...
    @overload
    def __truediv__(self, other: Number) -> IVector4: ...
    @overload
    def __rtruediv__(self, other: IVector4) -> IVector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> IVector4: ...




    def __abs__(self) -> IVector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> IVector2: ...

    @property
    def xy(self) -> IVector2: ...

    @property
    def xz(self) -> IVector2: ...

    @property
    def xw(self) -> IVector2: ...

    @property
    def yy(self) -> IVector2: ...

    @property
    def yz(self) -> IVector2: ...

    @property
    def yw(self) -> IVector2: ...

    @property
    def zz(self) -> IVector2: ...

    @property
    def zw(self) -> IVector2: ...

    @property
    def ww(self) -> IVector2: ...



    @property
    def xxx(self) -> IVector3: ...

    @property
    def xxy(self) -> IVector3: ...

    @property
    def xxz(self) -> IVector3: ...

    @property
    def xxw(self) -> IVector3: ...

    @property
    def xyy(self) -> IVector3: ...

    @property
    def xyz(self) -> IVector3: ...

    @property
    def xyw(self) -> IVector3: ...

    @property
    def xzz(self) -> IVector3: ...

    @property
    def xzw(self) -> IVector3: ...

    @property
    def xww(self) -> IVector3: ...

    @property
    def yyy(self) -> IVector3: ...

    @property
    def yyz(self) -> IVector3: ...

    @property
    def yyw(self) -> IVector3: ...

    @property
    def yzz(self) -> IVector3: ...

    @property
    def yzw(self) -> IVector3: ...

    @property
    def yww(self) -> IVector3: ...

    @property
    def zzz(self) -> IVector3: ...

    @property
    def zzw(self) -> IVector3: ...

    @property
    def zww(self) -> IVector3: ...

    @property
    def www(self) -> IVector3: ...



    @property
    def xxxx(self) -> IVector4: ...

    @property
    def xxxy(self) -> IVector4: ...

    @property
    def xxxz(self) -> IVector4: ...

    @property
    def xxxw(self) -> IVector4: ...

    @property
    def xxyy(self) -> IVector4: ...

    @property
    def xxyz(self) -> IVector4: ...

    @property
    def xxyw(self) -> IVector4: ...

    @property
    def xxzz(self) -> IVector4: ...

    @property
    def xxzw(self) -> IVector4: ...

    @property
    def xxww(self) -> IVector4: ...

    @property
    def xyyy(self) -> IVector4: ...

    @property
    def xyyz(self) -> IVector4: ...

    @property
    def xyyw(self) -> IVector4: ...

    @property
    def xyzz(self) -> IVector4: ...

    @property
    def xyzw(self) -> IVector4: ...

    @property
    def xyww(self) -> IVector4: ...

    @property
    def xzzz(self) -> IVector4: ...

    @property
    def xzzw(self) -> IVector4: ...

    @property
    def xzww(self) -> IVector4: ...

    @property
    def xwww(self) -> IVector4: ...

    @property
    def yyyy(self) -> IVector4: ...

    @property
    def yyyz(self) -> IVector4: ...

    @property
    def yyyw(self) -> IVector4: ...

    @property
    def yyzz(self) -> IVector4: ...

    @property
    def yyzw(self) -> IVector4: ...

    @property
    def yyww(self) -> IVector4: ...

    @property
    def yzzz(self) -> IVector4: ...

    @property
    def yzzw(self) -> IVector4: ...

    @property
    def yzww(self) -> IVector4: ...

    @property
    def ywww(self) -> IVector4: ...

    @property
    def zzzz(self) -> IVector4: ...

    @property
    def zzzw(self) -> IVector4: ...

    @property
    def zzww(self) -> IVector4: ...

    @property
    def zwww(self) -> IVector4: ...

    @property
    def wwww(self) -> IVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> IVector2: ...

    @property
    def rg(self) -> IVector2: ...

    @property
    def rb(self) -> IVector2: ...

    @property
    def ra(self) -> IVector2: ...

    @property
    def gg(self) -> IVector2: ...

    @property
    def gb(self) -> IVector2: ...

    @property
    def ga(self) -> IVector2: ...

    @property
    def bb(self) -> IVector2: ...

    @property
    def ba(self) -> IVector2: ...

    @property
    def aa(self) -> IVector2: ...



    @property
    def rrr(self) -> IVector3: ...

    @property
    def rrg(self) -> IVector3: ...

    @property
    def rrb(self) -> IVector3: ...

    @property
    def rra(self) -> IVector3: ...

    @property
    def rgg(self) -> IVector3: ...

    @property
    def rgb(self) -> IVector3: ...

    @property
    def rga(self) -> IVector3: ...

    @property
    def rbb(self) -> IVector3: ...

    @property
    def rba(self) -> IVector3: ...

    @property
    def raa(self) -> IVector3: ...

    @property
    def ggg(self) -> IVector3: ...

    @property
    def ggb(self) -> IVector3: ...

    @property
    def gga(self) -> IVector3: ...

    @property
    def gbb(self) -> IVector3: ...

    @property
    def gba(self) -> IVector3: ...

    @property
    def gaa(self) -> IVector3: ...

    @property
    def bbb(self) -> IVector3: ...

    @property
    def bba(self) -> IVector3: ...

    @property
    def baa(self) -> IVector3: ...

    @property
    def aaa(self) -> IVector3: ...



    @property
    def rrrr(self) -> IVector4: ...

    @property
    def rrrg(self) -> IVector4: ...

    @property
    def rrrb(self) -> IVector4: ...

    @property
    def rrra(self) -> IVector4: ...

    @property
    def rrgg(self) -> IVector4: ...

    @property
    def rrgb(self) -> IVector4: ...

    @property
    def rrga(self) -> IVector4: ...

    @property
    def rrbb(self) -> IVector4: ...

    @property
    def rrba(self) -> IVector4: ...

    @property
    def rraa(self) -> IVector4: ...

    @property
    def rggg(self) -> IVector4: ...

    @property
    def rggb(self) -> IVector4: ...

    @property
    def rgga(self) -> IVector4: ...

    @property
    def rgbb(self) -> IVector4: ...

    @property
    def rgba(self) -> IVector4: ...

    @property
    def rgaa(self) -> IVector4: ...

    @property
    def rbbb(self) -> IVector4: ...

    @property
    def rbba(self) -> IVector4: ...

    @property
    def rbaa(self) -> IVector4: ...

    @property
    def raaa(self) -> IVector4: ...

    @property
    def gggg(self) -> IVector4: ...

    @property
    def gggb(self) -> IVector4: ...

    @property
    def ggga(self) -> IVector4: ...

    @property
    def ggbb(self) -> IVector4: ...

    @property
    def ggba(self) -> IVector4: ...

    @property
    def ggaa(self) -> IVector4: ...

    @property
    def gbbb(self) -> IVector4: ...

    @property
    def gbba(self) -> IVector4: ...

    @property
    def gbaa(self) -> IVector4: ...

    @property
    def gaaa(self) -> IVector4: ...

    @property
    def bbbb(self) -> IVector4: ...

    @property
    def bbba(self) -> IVector4: ...

    @property
    def bbaa(self) -> IVector4: ...

    @property
    def baaa(self) -> IVector4: ...

    @property
    def aaaa(self) -> IVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> IVector2: ...

    @property
    def st(self) -> IVector2: ...

    @property
    def sq(self) -> IVector2: ...

    @property
    def sp(self) -> IVector2: ...

    @property
    def tt(self) -> IVector2: ...

    @property
    def tq(self) -> IVector2: ...

    @property
    def tp(self) -> IVector2: ...

    @property
    def qq(self) -> IVector2: ...

    @property
    def qp(self) -> IVector2: ...

    @property
    def pp(self) -> IVector2: ...



    @property
    def sss(self) -> IVector3: ...

    @property
    def sst(self) -> IVector3: ...

    @property
    def ssq(self) -> IVector3: ...

    @property
    def ssp(self) -> IVector3: ...

    @property
    def stt(self) -> IVector3: ...

    @property
    def stq(self) -> IVector3: ...

    @property
    def stp(self) -> IVector3: ...

    @property
    def sqq(self) -> IVector3: ...

    @property
    def sqp(self) -> IVector3: ...

    @property
    def spp(self) -> IVector3: ...

    @property
    def ttt(self) -> IVector3: ...

    @property
    def ttq(self) -> IVector3: ...

    @property
    def ttp(self) -> IVector3: ...

    @property
    def tqq(self) -> IVector3: ...

    @property
    def tqp(self) -> IVector3: ...

    @property
    def tpp(self) -> IVector3: ...

    @property
    def qqq(self) -> IVector3: ...

    @property
    def qqp(self) -> IVector3: ...

    @property
    def qpp(self) -> IVector3: ...

    @property
    def ppp(self) -> IVector3: ...



    @property
    def ssss(self) -> IVector4: ...

    @property
    def ssst(self) -> IVector4: ...

    @property
    def sssq(self) -> IVector4: ...

    @property
    def sssp(self) -> IVector4: ...

    @property
    def sstt(self) -> IVector4: ...

    @property
    def sstq(self) -> IVector4: ...

    @property
    def sstp(self) -> IVector4: ...

    @property
    def ssqq(self) -> IVector4: ...

    @property
    def ssqp(self) -> IVector4: ...

    @property
    def sspp(self) -> IVector4: ...

    @property
    def sttt(self) -> IVector4: ...

    @property
    def sttq(self) -> IVector4: ...

    @property
    def sttp(self) -> IVector4: ...

    @property
    def stqq(self) -> IVector4: ...

    @property
    def stqp(self) -> IVector4: ...

    @property
    def stpp(self) -> IVector4: ...

    @property
    def sqqq(self) -> IVector4: ...

    @property
    def sqqp(self) -> IVector4: ...

    @property
    def sqpp(self) -> IVector4: ...

    @property
    def sppp(self) -> IVector4: ...

    @property
    def tttt(self) -> IVector4: ...

    @property
    def tttq(self) -> IVector4: ...

    @property
    def tttp(self) -> IVector4: ...

    @property
    def ttqq(self) -> IVector4: ...

    @property
    def ttqp(self) -> IVector4: ...

    @property
    def ttpp(self) -> IVector4: ...

    @property
    def tqqq(self) -> IVector4: ...

    @property
    def tqqp(self) -> IVector4: ...

    @property
    def tqpp(self) -> IVector4: ...

    @property
    def tppp(self) -> IVector4: ...

    @property
    def qqqq(self) -> IVector4: ...

    @property
    def qqqp(self) -> IVector4: ...

    @property
    def qqpp(self) -> IVector4: ...

    @property
    def qppp(self) -> IVector4: ...

    @property
    def pppp(self) -> IVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> IVector2: ...

    @property
    def uv(self) -> IVector2: ...

    @property
    def vv(self) -> IVector2: ...



    @property
    def uuu(self) -> IVector3: ...

    @property
    def uuv(self) -> IVector3: ...

    @property
    def uvv(self) -> IVector3: ...

    @property
    def vvv(self) -> IVector3: ...



    @property
    def uuuu(self) -> IVector4: ...

    @property
    def uuuv(self) -> IVector4: ...

    @property
    def uuvv(self) -> IVector4: ...

    @property
    def uvvv(self) -> IVector4: ...

    @property
    def vvvv(self) -> IVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class UVector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: UVector4) -> UVector4: ...
    @overload
    def __add__(self, other: Number) -> UVector4: ...
    @overload
    def __radd__(self, other: UVector4) -> UVector4: ...
    @overload
    def __radd__(self, other: Number) -> UVector4: ...

    @overload
    def __sub__(self, other: UVector4) -> UVector4: ...
    @overload
    def __sub__(self, other: Number) -> UVector4: ...
    @overload
    def __rsub__(self, other: UVector4) -> UVector4: ...
    @overload
    def __rsub__(self, other: Number) -> UVector4: ...

    @overload
    def __mul__(self, other: UVector4) -> UVector4: ...
    @overload
    def __mul__(self, other: Number) -> UVector4: ...
    @overload
    def __rmul__(self, other: UVector4) -> UVector4: ...
    @overload
    def __rmul__(self, other: Number) -> UVector4: ...




    @overload
    def __truediv__(self, other: UVector4) -> UVector4: ...
    @overload
    def __truediv__(self, other: Number) -> UVector4: ...
    @overload
    def __rtruediv__(self, other: UVector4) -> UVector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> UVector4: ...



    def __neg__(self) -> UVector4: ...


    def __abs__(self) -> UVector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> UVector2: ...

    @property
    def xy(self) -> UVector2: ...

    @property
    def xz(self) -> UVector2: ...

    @property
    def xw(self) -> UVector2: ...

    @property
    def yy(self) -> UVector2: ...

    @property
    def yz(self) -> UVector2: ...

    @property
    def yw(self) -> UVector2: ...

    @property
    def zz(self) -> UVector2: ...

    @property
    def zw(self) -> UVector2: ...

    @property
    def ww(self) -> UVector2: ...



    @property
    def xxx(self) -> UVector3: ...

    @property
    def xxy(self) -> UVector3: ...

    @property
    def xxz(self) -> UVector3: ...

    @property
    def xxw(self) -> UVector3: ...

    @property
    def xyy(self) -> UVector3: ...

    @property
    def xyz(self) -> UVector3: ...

    @property
    def xyw(self) -> UVector3: ...

    @property
    def xzz(self) -> UVector3: ...

    @property
    def xzw(self) -> UVector3: ...

    @property
    def xww(self) -> UVector3: ...

    @property
    def yyy(self) -> UVector3: ...

    @property
    def yyz(self) -> UVector3: ...

    @property
    def yyw(self) -> UVector3: ...

    @property
    def yzz(self) -> UVector3: ...

    @property
    def yzw(self) -> UVector3: ...

    @property
    def yww(self) -> UVector3: ...

    @property
    def zzz(self) -> UVector3: ...

    @property
    def zzw(self) -> UVector3: ...

    @property
    def zww(self) -> UVector3: ...

    @property
    def www(self) -> UVector3: ...



    @property
    def xxxx(self) -> UVector4: ...

    @property
    def xxxy(self) -> UVector4: ...

    @property
    def xxxz(self) -> UVector4: ...

    @property
    def xxxw(self) -> UVector4: ...

    @property
    def xxyy(self) -> UVector4: ...

    @property
    def xxyz(self) -> UVector4: ...

    @property
    def xxyw(self) -> UVector4: ...

    @property
    def xxzz(self) -> UVector4: ...

    @property
    def xxzw(self) -> UVector4: ...

    @property
    def xxww(self) -> UVector4: ...

    @property
    def xyyy(self) -> UVector4: ...

    @property
    def xyyz(self) -> UVector4: ...

    @property
    def xyyw(self) -> UVector4: ...

    @property
    def xyzz(self) -> UVector4: ...

    @property
    def xyzw(self) -> UVector4: ...

    @property
    def xyww(self) -> UVector4: ...

    @property
    def xzzz(self) -> UVector4: ...

    @property
    def xzzw(self) -> UVector4: ...

    @property
    def xzww(self) -> UVector4: ...

    @property
    def xwww(self) -> UVector4: ...

    @property
    def yyyy(self) -> UVector4: ...

    @property
    def yyyz(self) -> UVector4: ...

    @property
    def yyyw(self) -> UVector4: ...

    @property
    def yyzz(self) -> UVector4: ...

    @property
    def yyzw(self) -> UVector4: ...

    @property
    def yyww(self) -> UVector4: ...

    @property
    def yzzz(self) -> UVector4: ...

    @property
    def yzzw(self) -> UVector4: ...

    @property
    def yzww(self) -> UVector4: ...

    @property
    def ywww(self) -> UVector4: ...

    @property
    def zzzz(self) -> UVector4: ...

    @property
    def zzzw(self) -> UVector4: ...

    @property
    def zzww(self) -> UVector4: ...

    @property
    def zwww(self) -> UVector4: ...

    @property
    def wwww(self) -> UVector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> UVector2: ...

    @property
    def rg(self) -> UVector2: ...

    @property
    def rb(self) -> UVector2: ...

    @property
    def ra(self) -> UVector2: ...

    @property
    def gg(self) -> UVector2: ...

    @property
    def gb(self) -> UVector2: ...

    @property
    def ga(self) -> UVector2: ...

    @property
    def bb(self) -> UVector2: ...

    @property
    def ba(self) -> UVector2: ...

    @property
    def aa(self) -> UVector2: ...



    @property
    def rrr(self) -> UVector3: ...

    @property
    def rrg(self) -> UVector3: ...

    @property
    def rrb(self) -> UVector3: ...

    @property
    def rra(self) -> UVector3: ...

    @property
    def rgg(self) -> UVector3: ...

    @property
    def rgb(self) -> UVector3: ...

    @property
    def rga(self) -> UVector3: ...

    @property
    def rbb(self) -> UVector3: ...

    @property
    def rba(self) -> UVector3: ...

    @property
    def raa(self) -> UVector3: ...

    @property
    def ggg(self) -> UVector3: ...

    @property
    def ggb(self) -> UVector3: ...

    @property
    def gga(self) -> UVector3: ...

    @property
    def gbb(self) -> UVector3: ...

    @property
    def gba(self) -> UVector3: ...

    @property
    def gaa(self) -> UVector3: ...

    @property
    def bbb(self) -> UVector3: ...

    @property
    def bba(self) -> UVector3: ...

    @property
    def baa(self) -> UVector3: ...

    @property
    def aaa(self) -> UVector3: ...



    @property
    def rrrr(self) -> UVector4: ...

    @property
    def rrrg(self) -> UVector4: ...

    @property
    def rrrb(self) -> UVector4: ...

    @property
    def rrra(self) -> UVector4: ...

    @property
    def rrgg(self) -> UVector4: ...

    @property
    def rrgb(self) -> UVector4: ...

    @property
    def rrga(self) -> UVector4: ...

    @property
    def rrbb(self) -> UVector4: ...

    @property
    def rrba(self) -> UVector4: ...

    @property
    def rraa(self) -> UVector4: ...

    @property
    def rggg(self) -> UVector4: ...

    @property
    def rggb(self) -> UVector4: ...

    @property
    def rgga(self) -> UVector4: ...

    @property
    def rgbb(self) -> UVector4: ...

    @property
    def rgba(self) -> UVector4: ...

    @property
    def rgaa(self) -> UVector4: ...

    @property
    def rbbb(self) -> UVector4: ...

    @property
    def rbba(self) -> UVector4: ...

    @property
    def rbaa(self) -> UVector4: ...

    @property
    def raaa(self) -> UVector4: ...

    @property
    def gggg(self) -> UVector4: ...

    @property
    def gggb(self) -> UVector4: ...

    @property
    def ggga(self) -> UVector4: ...

    @property
    def ggbb(self) -> UVector4: ...

    @property
    def ggba(self) -> UVector4: ...

    @property
    def ggaa(self) -> UVector4: ...

    @property
    def gbbb(self) -> UVector4: ...

    @property
    def gbba(self) -> UVector4: ...

    @property
    def gbaa(self) -> UVector4: ...

    @property
    def gaaa(self) -> UVector4: ...

    @property
    def bbbb(self) -> UVector4: ...

    @property
    def bbba(self) -> UVector4: ...

    @property
    def bbaa(self) -> UVector4: ...

    @property
    def baaa(self) -> UVector4: ...

    @property
    def aaaa(self) -> UVector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> UVector2: ...

    @property
    def st(self) -> UVector2: ...

    @property
    def sq(self) -> UVector2: ...

    @property
    def sp(self) -> UVector2: ...

    @property
    def tt(self) -> UVector2: ...

    @property
    def tq(self) -> UVector2: ...

    @property
    def tp(self) -> UVector2: ...

    @property
    def qq(self) -> UVector2: ...

    @property
    def qp(self) -> UVector2: ...

    @property
    def pp(self) -> UVector2: ...



    @property
    def sss(self) -> UVector3: ...

    @property
    def sst(self) -> UVector3: ...

    @property
    def ssq(self) -> UVector3: ...

    @property
    def ssp(self) -> UVector3: ...

    @property
    def stt(self) -> UVector3: ...

    @property
    def stq(self) -> UVector3: ...

    @property
    def stp(self) -> UVector3: ...

    @property
    def sqq(self) -> UVector3: ...

    @property
    def sqp(self) -> UVector3: ...

    @property
    def spp(self) -> UVector3: ...

    @property
    def ttt(self) -> UVector3: ...

    @property
    def ttq(self) -> UVector3: ...

    @property
    def ttp(self) -> UVector3: ...

    @property
    def tqq(self) -> UVector3: ...

    @property
    def tqp(self) -> UVector3: ...

    @property
    def tpp(self) -> UVector3: ...

    @property
    def qqq(self) -> UVector3: ...

    @property
    def qqp(self) -> UVector3: ...

    @property
    def qpp(self) -> UVector3: ...

    @property
    def ppp(self) -> UVector3: ...



    @property
    def ssss(self) -> UVector4: ...

    @property
    def ssst(self) -> UVector4: ...

    @property
    def sssq(self) -> UVector4: ...

    @property
    def sssp(self) -> UVector4: ...

    @property
    def sstt(self) -> UVector4: ...

    @property
    def sstq(self) -> UVector4: ...

    @property
    def sstp(self) -> UVector4: ...

    @property
    def ssqq(self) -> UVector4: ...

    @property
    def ssqp(self) -> UVector4: ...

    @property
    def sspp(self) -> UVector4: ...

    @property
    def sttt(self) -> UVector4: ...

    @property
    def sttq(self) -> UVector4: ...

    @property
    def sttp(self) -> UVector4: ...

    @property
    def stqq(self) -> UVector4: ...

    @property
    def stqp(self) -> UVector4: ...

    @property
    def stpp(self) -> UVector4: ...

    @property
    def sqqq(self) -> UVector4: ...

    @property
    def sqqp(self) -> UVector4: ...

    @property
    def sqpp(self) -> UVector4: ...

    @property
    def sppp(self) -> UVector4: ...

    @property
    def tttt(self) -> UVector4: ...

    @property
    def tttq(self) -> UVector4: ...

    @property
    def tttp(self) -> UVector4: ...

    @property
    def ttqq(self) -> UVector4: ...

    @property
    def ttqp(self) -> UVector4: ...

    @property
    def ttpp(self) -> UVector4: ...

    @property
    def tqqq(self) -> UVector4: ...

    @property
    def tqqp(self) -> UVector4: ...

    @property
    def tqpp(self) -> UVector4: ...

    @property
    def tppp(self) -> UVector4: ...

    @property
    def qqqq(self) -> UVector4: ...

    @property
    def qqqp(self) -> UVector4: ...

    @property
    def qqpp(self) -> UVector4: ...

    @property
    def qppp(self) -> UVector4: ...

    @property
    def pppp(self) -> UVector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> UVector2: ...

    @property
    def uv(self) -> UVector2: ...

    @property
    def vv(self) -> UVector2: ...



    @property
    def uuu(self) -> UVector3: ...

    @property
    def uuv(self) -> UVector3: ...

    @property
    def uvv(self) -> UVector3: ...

    @property
    def vvv(self) -> UVector3: ...



    @property
    def uuuu(self) -> UVector4: ...

    @property
    def uuuv(self) -> UVector4: ...

    @property
    def uuvv(self) -> UVector4: ...

    @property
    def uvvv(self) -> UVector4: ...

    @property
    def vvvv(self) -> UVector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class I64Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __add__(self, other: Number) -> I64Vector4: ...
    @overload
    def __radd__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __radd__(self, other: Number) -> I64Vector4: ...

    @overload
    def __sub__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __sub__(self, other: Number) -> I64Vector4: ...
    @overload
    def __rsub__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> I64Vector4: ...

    @overload
    def __mul__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __mul__(self, other: Number) -> I64Vector4: ...
    @overload
    def __rmul__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> I64Vector4: ...




    @overload
    def __truediv__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> I64Vector4: ...
    @overload
    def __rtruediv__(self, other: I64Vector4) -> I64Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> I64Vector4: ...




    def __abs__(self) -> I64Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> I64Vector2: ...

    @property
    def xy(self) -> I64Vector2: ...

    @property
    def xz(self) -> I64Vector2: ...

    @property
    def xw(self) -> I64Vector2: ...

    @property
    def yy(self) -> I64Vector2: ...

    @property
    def yz(self) -> I64Vector2: ...

    @property
    def yw(self) -> I64Vector2: ...

    @property
    def zz(self) -> I64Vector2: ...

    @property
    def zw(self) -> I64Vector2: ...

    @property
    def ww(self) -> I64Vector2: ...



    @property
    def xxx(self) -> I64Vector3: ...

    @property
    def xxy(self) -> I64Vector3: ...

    @property
    def xxz(self) -> I64Vector3: ...

    @property
    def xxw(self) -> I64Vector3: ...

    @property
    def xyy(self) -> I64Vector3: ...

    @property
    def xyz(self) -> I64Vector3: ...

    @property
    def xyw(self) -> I64Vector3: ...

    @property
    def xzz(self) -> I64Vector3: ...

    @property
    def xzw(self) -> I64Vector3: ...

    @property
    def xww(self) -> I64Vector3: ...

    @property
    def yyy(self) -> I64Vector3: ...

    @property
    def yyz(self) -> I64Vector3: ...

    @property
    def yyw(self) -> I64Vector3: ...

    @property
    def yzz(self) -> I64Vector3: ...

    @property
    def yzw(self) -> I64Vector3: ...

    @property
    def yww(self) -> I64Vector3: ...

    @property
    def zzz(self) -> I64Vector3: ...

    @property
    def zzw(self) -> I64Vector3: ...

    @property
    def zww(self) -> I64Vector3: ...

    @property
    def www(self) -> I64Vector3: ...



    @property
    def xxxx(self) -> I64Vector4: ...

    @property
    def xxxy(self) -> I64Vector4: ...

    @property
    def xxxz(self) -> I64Vector4: ...

    @property
    def xxxw(self) -> I64Vector4: ...

    @property
    def xxyy(self) -> I64Vector4: ...

    @property
    def xxyz(self) -> I64Vector4: ...

    @property
    def xxyw(self) -> I64Vector4: ...

    @property
    def xxzz(self) -> I64Vector4: ...

    @property
    def xxzw(self) -> I64Vector4: ...

    @property
    def xxww(self) -> I64Vector4: ...

    @property
    def xyyy(self) -> I64Vector4: ...

    @property
    def xyyz(self) -> I64Vector4: ...

    @property
    def xyyw(self) -> I64Vector4: ...

    @property
    def xyzz(self) -> I64Vector4: ...

    @property
    def xyzw(self) -> I64Vector4: ...

    @property
    def xyww(self) -> I64Vector4: ...

    @property
    def xzzz(self) -> I64Vector4: ...

    @property
    def xzzw(self) -> I64Vector4: ...

    @property
    def xzww(self) -> I64Vector4: ...

    @property
    def xwww(self) -> I64Vector4: ...

    @property
    def yyyy(self) -> I64Vector4: ...

    @property
    def yyyz(self) -> I64Vector4: ...

    @property
    def yyyw(self) -> I64Vector4: ...

    @property
    def yyzz(self) -> I64Vector4: ...

    @property
    def yyzw(self) -> I64Vector4: ...

    @property
    def yyww(self) -> I64Vector4: ...

    @property
    def yzzz(self) -> I64Vector4: ...

    @property
    def yzzw(self) -> I64Vector4: ...

    @property
    def yzww(self) -> I64Vector4: ...

    @property
    def ywww(self) -> I64Vector4: ...

    @property
    def zzzz(self) -> I64Vector4: ...

    @property
    def zzzw(self) -> I64Vector4: ...

    @property
    def zzww(self) -> I64Vector4: ...

    @property
    def zwww(self) -> I64Vector4: ...

    @property
    def wwww(self) -> I64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> I64Vector2: ...

    @property
    def rg(self) -> I64Vector2: ...

    @property
    def rb(self) -> I64Vector2: ...

    @property
    def ra(self) -> I64Vector2: ...

    @property
    def gg(self) -> I64Vector2: ...

    @property
    def gb(self) -> I64Vector2: ...

    @property
    def ga(self) -> I64Vector2: ...

    @property
    def bb(self) -> I64Vector2: ...

    @property
    def ba(self) -> I64Vector2: ...

    @property
    def aa(self) -> I64Vector2: ...



    @property
    def rrr(self) -> I64Vector3: ...

    @property
    def rrg(self) -> I64Vector3: ...

    @property
    def rrb(self) -> I64Vector3: ...

    @property
    def rra(self) -> I64Vector3: ...

    @property
    def rgg(self) -> I64Vector3: ...

    @property
    def rgb(self) -> I64Vector3: ...

    @property
    def rga(self) -> I64Vector3: ...

    @property
    def rbb(self) -> I64Vector3: ...

    @property
    def rba(self) -> I64Vector3: ...

    @property
    def raa(self) -> I64Vector3: ...

    @property
    def ggg(self) -> I64Vector3: ...

    @property
    def ggb(self) -> I64Vector3: ...

    @property
    def gga(self) -> I64Vector3: ...

    @property
    def gbb(self) -> I64Vector3: ...

    @property
    def gba(self) -> I64Vector3: ...

    @property
    def gaa(self) -> I64Vector3: ...

    @property
    def bbb(self) -> I64Vector3: ...

    @property
    def bba(self) -> I64Vector3: ...

    @property
    def baa(self) -> I64Vector3: ...

    @property
    def aaa(self) -> I64Vector3: ...



    @property
    def rrrr(self) -> I64Vector4: ...

    @property
    def rrrg(self) -> I64Vector4: ...

    @property
    def rrrb(self) -> I64Vector4: ...

    @property
    def rrra(self) -> I64Vector4: ...

    @property
    def rrgg(self) -> I64Vector4: ...

    @property
    def rrgb(self) -> I64Vector4: ...

    @property
    def rrga(self) -> I64Vector4: ...

    @property
    def rrbb(self) -> I64Vector4: ...

    @property
    def rrba(self) -> I64Vector4: ...

    @property
    def rraa(self) -> I64Vector4: ...

    @property
    def rggg(self) -> I64Vector4: ...

    @property
    def rggb(self) -> I64Vector4: ...

    @property
    def rgga(self) -> I64Vector4: ...

    @property
    def rgbb(self) -> I64Vector4: ...

    @property
    def rgba(self) -> I64Vector4: ...

    @property
    def rgaa(self) -> I64Vector4: ...

    @property
    def rbbb(self) -> I64Vector4: ...

    @property
    def rbba(self) -> I64Vector4: ...

    @property
    def rbaa(self) -> I64Vector4: ...

    @property
    def raaa(self) -> I64Vector4: ...

    @property
    def gggg(self) -> I64Vector4: ...

    @property
    def gggb(self) -> I64Vector4: ...

    @property
    def ggga(self) -> I64Vector4: ...

    @property
    def ggbb(self) -> I64Vector4: ...

    @property
    def ggba(self) -> I64Vector4: ...

    @property
    def ggaa(self) -> I64Vector4: ...

    @property
    def gbbb(self) -> I64Vector4: ...

    @property
    def gbba(self) -> I64Vector4: ...

    @property
    def gbaa(self) -> I64Vector4: ...

    @property
    def gaaa(self) -> I64Vector4: ...

    @property
    def bbbb(self) -> I64Vector4: ...

    @property
    def bbba(self) -> I64Vector4: ...

    @property
    def bbaa(self) -> I64Vector4: ...

    @property
    def baaa(self) -> I64Vector4: ...

    @property
    def aaaa(self) -> I64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> I64Vector2: ...

    @property
    def st(self) -> I64Vector2: ...

    @property
    def sq(self) -> I64Vector2: ...

    @property
    def sp(self) -> I64Vector2: ...

    @property
    def tt(self) -> I64Vector2: ...

    @property
    def tq(self) -> I64Vector2: ...

    @property
    def tp(self) -> I64Vector2: ...

    @property
    def qq(self) -> I64Vector2: ...

    @property
    def qp(self) -> I64Vector2: ...

    @property
    def pp(self) -> I64Vector2: ...



    @property
    def sss(self) -> I64Vector3: ...

    @property
    def sst(self) -> I64Vector3: ...

    @property
    def ssq(self) -> I64Vector3: ...

    @property
    def ssp(self) -> I64Vector3: ...

    @property
    def stt(self) -> I64Vector3: ...

    @property
    def stq(self) -> I64Vector3: ...

    @property
    def stp(self) -> I64Vector3: ...

    @property
    def sqq(self) -> I64Vector3: ...

    @property
    def sqp(self) -> I64Vector3: ...

    @property
    def spp(self) -> I64Vector3: ...

    @property
    def ttt(self) -> I64Vector3: ...

    @property
    def ttq(self) -> I64Vector3: ...

    @property
    def ttp(self) -> I64Vector3: ...

    @property
    def tqq(self) -> I64Vector3: ...

    @property
    def tqp(self) -> I64Vector3: ...

    @property
    def tpp(self) -> I64Vector3: ...

    @property
    def qqq(self) -> I64Vector3: ...

    @property
    def qqp(self) -> I64Vector3: ...

    @property
    def qpp(self) -> I64Vector3: ...

    @property
    def ppp(self) -> I64Vector3: ...



    @property
    def ssss(self) -> I64Vector4: ...

    @property
    def ssst(self) -> I64Vector4: ...

    @property
    def sssq(self) -> I64Vector4: ...

    @property
    def sssp(self) -> I64Vector4: ...

    @property
    def sstt(self) -> I64Vector4: ...

    @property
    def sstq(self) -> I64Vector4: ...

    @property
    def sstp(self) -> I64Vector4: ...

    @property
    def ssqq(self) -> I64Vector4: ...

    @property
    def ssqp(self) -> I64Vector4: ...

    @property
    def sspp(self) -> I64Vector4: ...

    @property
    def sttt(self) -> I64Vector4: ...

    @property
    def sttq(self) -> I64Vector4: ...

    @property
    def sttp(self) -> I64Vector4: ...

    @property
    def stqq(self) -> I64Vector4: ...

    @property
    def stqp(self) -> I64Vector4: ...

    @property
    def stpp(self) -> I64Vector4: ...

    @property
    def sqqq(self) -> I64Vector4: ...

    @property
    def sqqp(self) -> I64Vector4: ...

    @property
    def sqpp(self) -> I64Vector4: ...

    @property
    def sppp(self) -> I64Vector4: ...

    @property
    def tttt(self) -> I64Vector4: ...

    @property
    def tttq(self) -> I64Vector4: ...

    @property
    def tttp(self) -> I64Vector4: ...

    @property
    def ttqq(self) -> I64Vector4: ...

    @property
    def ttqp(self) -> I64Vector4: ...

    @property
    def ttpp(self) -> I64Vector4: ...

    @property
    def tqqq(self) -> I64Vector4: ...

    @property
    def tqqp(self) -> I64Vector4: ...

    @property
    def tqpp(self) -> I64Vector4: ...

    @property
    def tppp(self) -> I64Vector4: ...

    @property
    def qqqq(self) -> I64Vector4: ...

    @property
    def qqqp(self) -> I64Vector4: ...

    @property
    def qqpp(self) -> I64Vector4: ...

    @property
    def qppp(self) -> I64Vector4: ...

    @property
    def pppp(self) -> I64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> I64Vector2: ...

    @property
    def uv(self) -> I64Vector2: ...

    @property
    def vv(self) -> I64Vector2: ...



    @property
    def uuu(self) -> I64Vector3: ...

    @property
    def uuv(self) -> I64Vector3: ...

    @property
    def uvv(self) -> I64Vector3: ...

    @property
    def vvv(self) -> I64Vector3: ...



    @property
    def uuuu(self) -> I64Vector4: ...

    @property
    def uuuv(self) -> I64Vector4: ...

    @property
    def uuvv(self) -> I64Vector4: ...

    @property
    def uvvv(self) -> I64Vector4: ...

    @property
    def vvvv(self) -> I64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...









@final
class U64Vector4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...




    @overload
    def __init__(self, x: Number, y: Number, z: Number, w: Number, /): ...


    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __add__(self, other: Number) -> U64Vector4: ...
    @overload
    def __radd__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __radd__(self, other: Number) -> U64Vector4: ...

    @overload
    def __sub__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __sub__(self, other: Number) -> U64Vector4: ...
    @overload
    def __rsub__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __rsub__(self, other: Number) -> U64Vector4: ...

    @overload
    def __mul__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __mul__(self, other: Number) -> U64Vector4: ...
    @overload
    def __rmul__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __rmul__(self, other: Number) -> U64Vector4: ...




    @overload
    def __truediv__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __truediv__(self, other: Number) -> U64Vector4: ...
    @overload
    def __rtruediv__(self, other: U64Vector4) -> U64Vector4: ...
    @overload
    def __rtruediv__(self, other: Number) -> U64Vector4: ...



    def __neg__(self) -> U64Vector4: ...


    def __abs__(self) -> U64Vector4: ...
    def __bool__(self) -> bool: ...




    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def z(self) -> int: ...

    @property
    def w(self) -> int: ...



    @property
    def xx(self) -> U64Vector2: ...

    @property
    def xy(self) -> U64Vector2: ...

    @property
    def xz(self) -> U64Vector2: ...

    @property
    def xw(self) -> U64Vector2: ...

    @property
    def yy(self) -> U64Vector2: ...

    @property
    def yz(self) -> U64Vector2: ...

    @property
    def yw(self) -> U64Vector2: ...

    @property
    def zz(self) -> U64Vector2: ...

    @property
    def zw(self) -> U64Vector2: ...

    @property
    def ww(self) -> U64Vector2: ...



    @property
    def xxx(self) -> U64Vector3: ...

    @property
    def xxy(self) -> U64Vector3: ...

    @property
    def xxz(self) -> U64Vector3: ...

    @property
    def xxw(self) -> U64Vector3: ...

    @property
    def xyy(self) -> U64Vector3: ...

    @property
    def xyz(self) -> U64Vector3: ...

    @property
    def xyw(self) -> U64Vector3: ...

    @property
    def xzz(self) -> U64Vector3: ...

    @property
    def xzw(self) -> U64Vector3: ...

    @property
    def xww(self) -> U64Vector3: ...

    @property
    def yyy(self) -> U64Vector3: ...

    @property
    def yyz(self) -> U64Vector3: ...

    @property
    def yyw(self) -> U64Vector3: ...

    @property
    def yzz(self) -> U64Vector3: ...

    @property
    def yzw(self) -> U64Vector3: ...

    @property
    def yww(self) -> U64Vector3: ...

    @property
    def zzz(self) -> U64Vector3: ...

    @property
    def zzw(self) -> U64Vector3: ...

    @property
    def zww(self) -> U64Vector3: ...

    @property
    def www(self) -> U64Vector3: ...



    @property
    def xxxx(self) -> U64Vector4: ...

    @property
    def xxxy(self) -> U64Vector4: ...

    @property
    def xxxz(self) -> U64Vector4: ...

    @property
    def xxxw(self) -> U64Vector4: ...

    @property
    def xxyy(self) -> U64Vector4: ...

    @property
    def xxyz(self) -> U64Vector4: ...

    @property
    def xxyw(self) -> U64Vector4: ...

    @property
    def xxzz(self) -> U64Vector4: ...

    @property
    def xxzw(self) -> U64Vector4: ...

    @property
    def xxww(self) -> U64Vector4: ...

    @property
    def xyyy(self) -> U64Vector4: ...

    @property
    def xyyz(self) -> U64Vector4: ...

    @property
    def xyyw(self) -> U64Vector4: ...

    @property
    def xyzz(self) -> U64Vector4: ...

    @property
    def xyzw(self) -> U64Vector4: ...

    @property
    def xyww(self) -> U64Vector4: ...

    @property
    def xzzz(self) -> U64Vector4: ...

    @property
    def xzzw(self) -> U64Vector4: ...

    @property
    def xzww(self) -> U64Vector4: ...

    @property
    def xwww(self) -> U64Vector4: ...

    @property
    def yyyy(self) -> U64Vector4: ...

    @property
    def yyyz(self) -> U64Vector4: ...

    @property
    def yyyw(self) -> U64Vector4: ...

    @property
    def yyzz(self) -> U64Vector4: ...

    @property
    def yyzw(self) -> U64Vector4: ...

    @property
    def yyww(self) -> U64Vector4: ...

    @property
    def yzzz(self) -> U64Vector4: ...

    @property
    def yzzw(self) -> U64Vector4: ...

    @property
    def yzww(self) -> U64Vector4: ...

    @property
    def ywww(self) -> U64Vector4: ...

    @property
    def zzzz(self) -> U64Vector4: ...

    @property
    def zzzw(self) -> U64Vector4: ...

    @property
    def zzww(self) -> U64Vector4: ...

    @property
    def zwww(self) -> U64Vector4: ...

    @property
    def wwww(self) -> U64Vector4: ...





    @property
    def r(self) -> int: ...

    @property
    def g(self) -> int: ...

    @property
    def b(self) -> int: ...

    @property
    def a(self) -> int: ...



    @property
    def rr(self) -> U64Vector2: ...

    @property
    def rg(self) -> U64Vector2: ...

    @property
    def rb(self) -> U64Vector2: ...

    @property
    def ra(self) -> U64Vector2: ...

    @property
    def gg(self) -> U64Vector2: ...

    @property
    def gb(self) -> U64Vector2: ...

    @property
    def ga(self) -> U64Vector2: ...

    @property
    def bb(self) -> U64Vector2: ...

    @property
    def ba(self) -> U64Vector2: ...

    @property
    def aa(self) -> U64Vector2: ...



    @property
    def rrr(self) -> U64Vector3: ...

    @property
    def rrg(self) -> U64Vector3: ...

    @property
    def rrb(self) -> U64Vector3: ...

    @property
    def rra(self) -> U64Vector3: ...

    @property
    def rgg(self) -> U64Vector3: ...

    @property
    def rgb(self) -> U64Vector3: ...

    @property
    def rga(self) -> U64Vector3: ...

    @property
    def rbb(self) -> U64Vector3: ...

    @property
    def rba(self) -> U64Vector3: ...

    @property
    def raa(self) -> U64Vector3: ...

    @property
    def ggg(self) -> U64Vector3: ...

    @property
    def ggb(self) -> U64Vector3: ...

    @property
    def gga(self) -> U64Vector3: ...

    @property
    def gbb(self) -> U64Vector3: ...

    @property
    def gba(self) -> U64Vector3: ...

    @property
    def gaa(self) -> U64Vector3: ...

    @property
    def bbb(self) -> U64Vector3: ...

    @property
    def bba(self) -> U64Vector3: ...

    @property
    def baa(self) -> U64Vector3: ...

    @property
    def aaa(self) -> U64Vector3: ...



    @property
    def rrrr(self) -> U64Vector4: ...

    @property
    def rrrg(self) -> U64Vector4: ...

    @property
    def rrrb(self) -> U64Vector4: ...

    @property
    def rrra(self) -> U64Vector4: ...

    @property
    def rrgg(self) -> U64Vector4: ...

    @property
    def rrgb(self) -> U64Vector4: ...

    @property
    def rrga(self) -> U64Vector4: ...

    @property
    def rrbb(self) -> U64Vector4: ...

    @property
    def rrba(self) -> U64Vector4: ...

    @property
    def rraa(self) -> U64Vector4: ...

    @property
    def rggg(self) -> U64Vector4: ...

    @property
    def rggb(self) -> U64Vector4: ...

    @property
    def rgga(self) -> U64Vector4: ...

    @property
    def rgbb(self) -> U64Vector4: ...

    @property
    def rgba(self) -> U64Vector4: ...

    @property
    def rgaa(self) -> U64Vector4: ...

    @property
    def rbbb(self) -> U64Vector4: ...

    @property
    def rbba(self) -> U64Vector4: ...

    @property
    def rbaa(self) -> U64Vector4: ...

    @property
    def raaa(self) -> U64Vector4: ...

    @property
    def gggg(self) -> U64Vector4: ...

    @property
    def gggb(self) -> U64Vector4: ...

    @property
    def ggga(self) -> U64Vector4: ...

    @property
    def ggbb(self) -> U64Vector4: ...

    @property
    def ggba(self) -> U64Vector4: ...

    @property
    def ggaa(self) -> U64Vector4: ...

    @property
    def gbbb(self) -> U64Vector4: ...

    @property
    def gbba(self) -> U64Vector4: ...

    @property
    def gbaa(self) -> U64Vector4: ...

    @property
    def gaaa(self) -> U64Vector4: ...

    @property
    def bbbb(self) -> U64Vector4: ...

    @property
    def bbba(self) -> U64Vector4: ...

    @property
    def bbaa(self) -> U64Vector4: ...

    @property
    def baaa(self) -> U64Vector4: ...

    @property
    def aaaa(self) -> U64Vector4: ...





    @property
    def s(self) -> int: ...

    @property
    def t(self) -> int: ...

    @property
    def q(self) -> int: ...

    @property
    def p(self) -> int: ...



    @property
    def ss(self) -> U64Vector2: ...

    @property
    def st(self) -> U64Vector2: ...

    @property
    def sq(self) -> U64Vector2: ...

    @property
    def sp(self) -> U64Vector2: ...

    @property
    def tt(self) -> U64Vector2: ...

    @property
    def tq(self) -> U64Vector2: ...

    @property
    def tp(self) -> U64Vector2: ...

    @property
    def qq(self) -> U64Vector2: ...

    @property
    def qp(self) -> U64Vector2: ...

    @property
    def pp(self) -> U64Vector2: ...



    @property
    def sss(self) -> U64Vector3: ...

    @property
    def sst(self) -> U64Vector3: ...

    @property
    def ssq(self) -> U64Vector3: ...

    @property
    def ssp(self) -> U64Vector3: ...

    @property
    def stt(self) -> U64Vector3: ...

    @property
    def stq(self) -> U64Vector3: ...

    @property
    def stp(self) -> U64Vector3: ...

    @property
    def sqq(self) -> U64Vector3: ...

    @property
    def sqp(self) -> U64Vector3: ...

    @property
    def spp(self) -> U64Vector3: ...

    @property
    def ttt(self) -> U64Vector3: ...

    @property
    def ttq(self) -> U64Vector3: ...

    @property
    def ttp(self) -> U64Vector3: ...

    @property
    def tqq(self) -> U64Vector3: ...

    @property
    def tqp(self) -> U64Vector3: ...

    @property
    def tpp(self) -> U64Vector3: ...

    @property
    def qqq(self) -> U64Vector3: ...

    @property
    def qqp(self) -> U64Vector3: ...

    @property
    def qpp(self) -> U64Vector3: ...

    @property
    def ppp(self) -> U64Vector3: ...



    @property
    def ssss(self) -> U64Vector4: ...

    @property
    def ssst(self) -> U64Vector4: ...

    @property
    def sssq(self) -> U64Vector4: ...

    @property
    def sssp(self) -> U64Vector4: ...

    @property
    def sstt(self) -> U64Vector4: ...

    @property
    def sstq(self) -> U64Vector4: ...

    @property
    def sstp(self) -> U64Vector4: ...

    @property
    def ssqq(self) -> U64Vector4: ...

    @property
    def ssqp(self) -> U64Vector4: ...

    @property
    def sspp(self) -> U64Vector4: ...

    @property
    def sttt(self) -> U64Vector4: ...

    @property
    def sttq(self) -> U64Vector4: ...

    @property
    def sttp(self) -> U64Vector4: ...

    @property
    def stqq(self) -> U64Vector4: ...

    @property
    def stqp(self) -> U64Vector4: ...

    @property
    def stpp(self) -> U64Vector4: ...

    @property
    def sqqq(self) -> U64Vector4: ...

    @property
    def sqqp(self) -> U64Vector4: ...

    @property
    def sqpp(self) -> U64Vector4: ...

    @property
    def sppp(self) -> U64Vector4: ...

    @property
    def tttt(self) -> U64Vector4: ...

    @property
    def tttq(self) -> U64Vector4: ...

    @property
    def tttp(self) -> U64Vector4: ...

    @property
    def ttqq(self) -> U64Vector4: ...

    @property
    def ttqp(self) -> U64Vector4: ...

    @property
    def ttpp(self) -> U64Vector4: ...

    @property
    def tqqq(self) -> U64Vector4: ...

    @property
    def tqqp(self) -> U64Vector4: ...

    @property
    def tqpp(self) -> U64Vector4: ...

    @property
    def tppp(self) -> U64Vector4: ...

    @property
    def qqqq(self) -> U64Vector4: ...

    @property
    def qqqp(self) -> U64Vector4: ...

    @property
    def qqpp(self) -> U64Vector4: ...

    @property
    def qppp(self) -> U64Vector4: ...

    @property
    def pppp(self) -> U64Vector4: ...





    @property
    def u(self) -> int: ...

    @property
    def v(self) -> int: ...



    @property
    def uu(self) -> U64Vector2: ...

    @property
    def uv(self) -> U64Vector2: ...

    @property
    def vv(self) -> U64Vector2: ...



    @property
    def uuu(self) -> U64Vector3: ...

    @property
    def uuv(self) -> U64Vector3: ...

    @property
    def uvv(self) -> U64Vector3: ...

    @property
    def vvv(self) -> U64Vector3: ...



    @property
    def uuuu(self) -> U64Vector4: ...

    @property
    def uuuv(self) -> U64Vector4: ...

    @property
    def uuvv(self) -> U64Vector4: ...

    @property
    def uvvv(self) -> U64Vector4: ...

    @property
    def vvvv(self) -> U64Vector4: ...






    @classmethod
    def get_limits(cls) -> tuple[int, int]: ...














@final
class DMatrix2x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector2,

            _1: DVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix2x2) -> DMatrix2x2: ...
    @overload
    def __add__(self, other: Number) -> DMatrix2x2: ...
    @overload
    def __radd__(self, other: DMatrix2x2) -> DMatrix2x2: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix2x2: ...

    @overload
    def __sub__(self, other: DMatrix2x2) -> DMatrix2x2: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix2x2: ...
    @overload
    def __rsub__(self, other: DMatrix2x2) -> DMatrix2x2: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix2x2: ...

    def __mul__(self, other: Number) -> DMatrix2x2: ...
    def __rmul__(self, other: Number) -> DMatrix2x2: ...




    @overload
    def __matmul__(self, other: DMatrix2x2) -> DMatrix2x2: ...





    @overload
    def __matmul__(self, other: DMatrix3x2) -> DMatrix3x2: ...





    @overload
    def __matmul__(self, other: DMatrix4x2) -> DMatrix4x2: ...



    @overload
    def __matmul__(self, other: DVector2) -> DVector2: ...

    def __rmatmul__(self, other: DVector2) -> DVector2: ...


    @overload

    def __truediv__(self, other: Number) -> DMatrix2x2: ...

    @overload
    def __truediv__(self, other: DMatrix2x2) -> DMatrix2x2: ...
    @overload
    def __truediv__(self, other: DVector2) -> DVector2: ...
    @overload
    def __rtruediv__(self, other: DVector2) -> DVector2: ...
    @overload

    def __rtruediv__(self, other: Number) -> DMatrix2x2: ...

    def __neg__(self) -> DMatrix2x2: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> DMatrix2x2: ...



    def transpose(self) -> DMatrix2x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix2x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector2,

            _1: FVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix2x2) -> FMatrix2x2: ...
    @overload
    def __add__(self, other: Number) -> FMatrix2x2: ...
    @overload
    def __radd__(self, other: FMatrix2x2) -> FMatrix2x2: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix2x2: ...

    @overload
    def __sub__(self, other: FMatrix2x2) -> FMatrix2x2: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix2x2: ...
    @overload
    def __rsub__(self, other: FMatrix2x2) -> FMatrix2x2: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix2x2: ...

    def __mul__(self, other: Number) -> FMatrix2x2: ...
    def __rmul__(self, other: Number) -> FMatrix2x2: ...




    @overload
    def __matmul__(self, other: FMatrix2x2) -> FMatrix2x2: ...





    @overload
    def __matmul__(self, other: FMatrix3x2) -> FMatrix3x2: ...





    @overload
    def __matmul__(self, other: FMatrix4x2) -> FMatrix4x2: ...



    @overload
    def __matmul__(self, other: FVector2) -> FVector2: ...

    def __rmatmul__(self, other: FVector2) -> FVector2: ...


    @overload

    def __truediv__(self, other: Number) -> FMatrix2x2: ...

    @overload
    def __truediv__(self, other: FMatrix2x2) -> FMatrix2x2: ...
    @overload
    def __truediv__(self, other: FVector2) -> FVector2: ...
    @overload
    def __rtruediv__(self, other: FVector2) -> FVector2: ...
    @overload

    def __rtruediv__(self, other: Number) -> FMatrix2x2: ...

    def __neg__(self) -> FMatrix2x2: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> FMatrix2x2: ...



    def transpose(self) -> FMatrix2x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix2x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector3,

            _1: DVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix2x3) -> DMatrix2x3: ...
    @overload
    def __add__(self, other: Number) -> DMatrix2x3: ...
    @overload
    def __radd__(self, other: DMatrix2x3) -> DMatrix2x3: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix2x3: ...

    @overload
    def __sub__(self, other: DMatrix2x3) -> DMatrix2x3: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix2x3: ...
    @overload
    def __rsub__(self, other: DMatrix2x3) -> DMatrix2x3: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix2x3: ...

    def __mul__(self, other: Number) -> DMatrix2x3: ...
    def __rmul__(self, other: Number) -> DMatrix2x3: ...




    @overload
    def __matmul__(self, other: DMatrix2x2) -> DMatrix2x3: ...





    @overload
    def __matmul__(self, other: DMatrix3x2) -> DMatrix3x3: ...





    @overload
    def __matmul__(self, other: DMatrix4x2) -> DMatrix4x3: ...



    @overload
    def __matmul__(self, other: DVector2) -> DVector3: ...

    def __rmatmul__(self, other: DVector3) -> DVector2: ...


    def __truediv__(self, other: Number) -> DMatrix2x3: ...

    def __rtruediv__(self, other: Number) -> DMatrix2x3: ...

    def __neg__(self) -> DMatrix2x3: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix3x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix2x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector3,

            _1: FVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix2x3) -> FMatrix2x3: ...
    @overload
    def __add__(self, other: Number) -> FMatrix2x3: ...
    @overload
    def __radd__(self, other: FMatrix2x3) -> FMatrix2x3: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix2x3: ...

    @overload
    def __sub__(self, other: FMatrix2x3) -> FMatrix2x3: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix2x3: ...
    @overload
    def __rsub__(self, other: FMatrix2x3) -> FMatrix2x3: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix2x3: ...

    def __mul__(self, other: Number) -> FMatrix2x3: ...
    def __rmul__(self, other: Number) -> FMatrix2x3: ...




    @overload
    def __matmul__(self, other: FMatrix2x2) -> FMatrix2x3: ...





    @overload
    def __matmul__(self, other: FMatrix3x2) -> FMatrix3x3: ...





    @overload
    def __matmul__(self, other: FMatrix4x2) -> FMatrix4x3: ...



    @overload
    def __matmul__(self, other: FVector2) -> FVector3: ...

    def __rmatmul__(self, other: FVector3) -> FVector2: ...


    def __truediv__(self, other: Number) -> FMatrix2x3: ...

    def __rtruediv__(self, other: Number) -> FMatrix2x3: ...

    def __neg__(self) -> FMatrix2x3: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix3x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix2x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector4,

            _1: DVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix2x4) -> DMatrix2x4: ...
    @overload
    def __add__(self, other: Number) -> DMatrix2x4: ...
    @overload
    def __radd__(self, other: DMatrix2x4) -> DMatrix2x4: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix2x4: ...

    @overload
    def __sub__(self, other: DMatrix2x4) -> DMatrix2x4: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix2x4: ...
    @overload
    def __rsub__(self, other: DMatrix2x4) -> DMatrix2x4: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix2x4: ...

    def __mul__(self, other: Number) -> DMatrix2x4: ...
    def __rmul__(self, other: Number) -> DMatrix2x4: ...




    @overload
    def __matmul__(self, other: DMatrix2x2) -> DMatrix2x4: ...





    @overload
    def __matmul__(self, other: DMatrix3x2) -> DMatrix3x4: ...





    @overload
    def __matmul__(self, other: DMatrix4x2) -> DMatrix4x4: ...



    @overload
    def __matmul__(self, other: DVector2) -> DVector4: ...

    def __rmatmul__(self, other: DVector4) -> DVector2: ...


    def __truediv__(self, other: Number) -> DMatrix2x4: ...

    def __rtruediv__(self, other: Number) -> DMatrix2x4: ...

    def __neg__(self) -> DMatrix2x4: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix4x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix2x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector4,

            _1: FVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix2x4) -> FMatrix2x4: ...
    @overload
    def __add__(self, other: Number) -> FMatrix2x4: ...
    @overload
    def __radd__(self, other: FMatrix2x4) -> FMatrix2x4: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix2x4: ...

    @overload
    def __sub__(self, other: FMatrix2x4) -> FMatrix2x4: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix2x4: ...
    @overload
    def __rsub__(self, other: FMatrix2x4) -> FMatrix2x4: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix2x4: ...

    def __mul__(self, other: Number) -> FMatrix2x4: ...
    def __rmul__(self, other: Number) -> FMatrix2x4: ...




    @overload
    def __matmul__(self, other: FMatrix2x2) -> FMatrix2x4: ...





    @overload
    def __matmul__(self, other: FMatrix3x2) -> FMatrix3x4: ...





    @overload
    def __matmul__(self, other: FMatrix4x2) -> FMatrix4x4: ...



    @overload
    def __matmul__(self, other: FVector2) -> FVector4: ...

    def __rmatmul__(self, other: FVector4) -> FVector2: ...


    def __truediv__(self, other: Number) -> FMatrix2x4: ...

    def __rtruediv__(self, other: Number) -> FMatrix2x4: ...

    def __neg__(self) -> FMatrix2x4: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix4x2: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix3x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector2,

            _1: DVector2,

            _2: DVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix3x2) -> DMatrix3x2: ...
    @overload
    def __add__(self, other: Number) -> DMatrix3x2: ...
    @overload
    def __radd__(self, other: DMatrix3x2) -> DMatrix3x2: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix3x2: ...

    @overload
    def __sub__(self, other: DMatrix3x2) -> DMatrix3x2: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix3x2: ...
    @overload
    def __rsub__(self, other: DMatrix3x2) -> DMatrix3x2: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix3x2: ...

    def __mul__(self, other: Number) -> DMatrix3x2: ...
    def __rmul__(self, other: Number) -> DMatrix3x2: ...




    @overload
    def __matmul__(self, other: DMatrix2x3) -> DMatrix2x2: ...





    @overload
    def __matmul__(self, other: DMatrix3x3) -> DMatrix3x2: ...





    @overload
    def __matmul__(self, other: DMatrix4x3) -> DMatrix4x2: ...



    @overload
    def __matmul__(self, other: DVector3) -> DVector2: ...

    def __rmatmul__(self, other: DVector2) -> DVector3: ...


    def __truediv__(self, other: Number) -> DMatrix3x2: ...

    def __rtruediv__(self, other: Number) -> DMatrix3x2: ...

    def __neg__(self) -> DMatrix3x2: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix2x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix3x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector2,

            _1: FVector2,

            _2: FVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix3x2) -> FMatrix3x2: ...
    @overload
    def __add__(self, other: Number) -> FMatrix3x2: ...
    @overload
    def __radd__(self, other: FMatrix3x2) -> FMatrix3x2: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix3x2: ...

    @overload
    def __sub__(self, other: FMatrix3x2) -> FMatrix3x2: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix3x2: ...
    @overload
    def __rsub__(self, other: FMatrix3x2) -> FMatrix3x2: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix3x2: ...

    def __mul__(self, other: Number) -> FMatrix3x2: ...
    def __rmul__(self, other: Number) -> FMatrix3x2: ...




    @overload
    def __matmul__(self, other: FMatrix2x3) -> FMatrix2x2: ...





    @overload
    def __matmul__(self, other: FMatrix3x3) -> FMatrix3x2: ...





    @overload
    def __matmul__(self, other: FMatrix4x3) -> FMatrix4x2: ...



    @overload
    def __matmul__(self, other: FVector3) -> FVector2: ...

    def __rmatmul__(self, other: FVector2) -> FVector3: ...


    def __truediv__(self, other: Number) -> FMatrix3x2: ...

    def __rtruediv__(self, other: Number) -> FMatrix3x2: ...

    def __neg__(self) -> FMatrix3x2: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix2x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix3x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector3,

            _1: DVector3,

            _2: DVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix3x3) -> DMatrix3x3: ...
    @overload
    def __add__(self, other: Number) -> DMatrix3x3: ...
    @overload
    def __radd__(self, other: DMatrix3x3) -> DMatrix3x3: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix3x3: ...

    @overload
    def __sub__(self, other: DMatrix3x3) -> DMatrix3x3: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix3x3: ...
    @overload
    def __rsub__(self, other: DMatrix3x3) -> DMatrix3x3: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix3x3: ...

    def __mul__(self, other: Number) -> DMatrix3x3: ...
    def __rmul__(self, other: Number) -> DMatrix3x3: ...




    @overload
    def __matmul__(self, other: DMatrix2x3) -> DMatrix2x3: ...





    @overload
    def __matmul__(self, other: DMatrix3x3) -> DMatrix3x3: ...





    @overload
    def __matmul__(self, other: DMatrix4x3) -> DMatrix4x3: ...



    @overload
    def __matmul__(self, other: DVector3) -> DVector3: ...

    def __rmatmul__(self, other: DVector3) -> DVector3: ...


    @overload

    def __truediv__(self, other: Number) -> DMatrix3x3: ...

    @overload
    def __truediv__(self, other: DMatrix3x3) -> DMatrix3x3: ...
    @overload
    def __truediv__(self, other: DVector3) -> DVector3: ...
    @overload
    def __rtruediv__(self, other: DVector3) -> DVector3: ...
    @overload

    def __rtruediv__(self, other: Number) -> DMatrix3x3: ...

    def __neg__(self) -> DMatrix3x3: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> DMatrix3x3: ...



    def transpose(self) -> DMatrix3x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix3x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector3,

            _1: FVector3,

            _2: FVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix3x3) -> FMatrix3x3: ...
    @overload
    def __add__(self, other: Number) -> FMatrix3x3: ...
    @overload
    def __radd__(self, other: FMatrix3x3) -> FMatrix3x3: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix3x3: ...

    @overload
    def __sub__(self, other: FMatrix3x3) -> FMatrix3x3: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix3x3: ...
    @overload
    def __rsub__(self, other: FMatrix3x3) -> FMatrix3x3: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix3x3: ...

    def __mul__(self, other: Number) -> FMatrix3x3: ...
    def __rmul__(self, other: Number) -> FMatrix3x3: ...




    @overload
    def __matmul__(self, other: FMatrix2x3) -> FMatrix2x3: ...





    @overload
    def __matmul__(self, other: FMatrix3x3) -> FMatrix3x3: ...





    @overload
    def __matmul__(self, other: FMatrix4x3) -> FMatrix4x3: ...



    @overload
    def __matmul__(self, other: FVector3) -> FVector3: ...

    def __rmatmul__(self, other: FVector3) -> FVector3: ...


    @overload

    def __truediv__(self, other: Number) -> FMatrix3x3: ...

    @overload
    def __truediv__(self, other: FMatrix3x3) -> FMatrix3x3: ...
    @overload
    def __truediv__(self, other: FVector3) -> FVector3: ...
    @overload
    def __rtruediv__(self, other: FVector3) -> FVector3: ...
    @overload

    def __rtruediv__(self, other: Number) -> FMatrix3x3: ...

    def __neg__(self) -> FMatrix3x3: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> FMatrix3x3: ...



    def transpose(self) -> FMatrix3x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix3x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector4,

            _1: DVector4,

            _2: DVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix3x4) -> DMatrix3x4: ...
    @overload
    def __add__(self, other: Number) -> DMatrix3x4: ...
    @overload
    def __radd__(self, other: DMatrix3x4) -> DMatrix3x4: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix3x4: ...

    @overload
    def __sub__(self, other: DMatrix3x4) -> DMatrix3x4: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix3x4: ...
    @overload
    def __rsub__(self, other: DMatrix3x4) -> DMatrix3x4: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix3x4: ...

    def __mul__(self, other: Number) -> DMatrix3x4: ...
    def __rmul__(self, other: Number) -> DMatrix3x4: ...




    @overload
    def __matmul__(self, other: DMatrix2x3) -> DMatrix2x4: ...





    @overload
    def __matmul__(self, other: DMatrix3x3) -> DMatrix3x4: ...





    @overload
    def __matmul__(self, other: DMatrix4x3) -> DMatrix4x4: ...



    @overload
    def __matmul__(self, other: DVector3) -> DVector4: ...

    def __rmatmul__(self, other: DVector4) -> DVector3: ...


    def __truediv__(self, other: Number) -> DMatrix3x4: ...

    def __rtruediv__(self, other: Number) -> DMatrix3x4: ...

    def __neg__(self) -> DMatrix3x4: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix4x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix3x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector4,

            _1: FVector4,

            _2: FVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix3x4) -> FMatrix3x4: ...
    @overload
    def __add__(self, other: Number) -> FMatrix3x4: ...
    @overload
    def __radd__(self, other: FMatrix3x4) -> FMatrix3x4: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix3x4: ...

    @overload
    def __sub__(self, other: FMatrix3x4) -> FMatrix3x4: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix3x4: ...
    @overload
    def __rsub__(self, other: FMatrix3x4) -> FMatrix3x4: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix3x4: ...

    def __mul__(self, other: Number) -> FMatrix3x4: ...
    def __rmul__(self, other: Number) -> FMatrix3x4: ...




    @overload
    def __matmul__(self, other: FMatrix2x3) -> FMatrix2x4: ...





    @overload
    def __matmul__(self, other: FMatrix3x3) -> FMatrix3x4: ...





    @overload
    def __matmul__(self, other: FMatrix4x3) -> FMatrix4x4: ...



    @overload
    def __matmul__(self, other: FVector3) -> FVector4: ...

    def __rmatmul__(self, other: FVector4) -> FVector3: ...


    def __truediv__(self, other: Number) -> FMatrix3x4: ...

    def __rtruediv__(self, other: Number) -> FMatrix3x4: ...

    def __neg__(self) -> FMatrix3x4: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix4x3: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix4x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector2,

            _1: DVector2,

            _2: DVector2,

            _3: DVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix4x2) -> DMatrix4x2: ...
    @overload
    def __add__(self, other: Number) -> DMatrix4x2: ...
    @overload
    def __radd__(self, other: DMatrix4x2) -> DMatrix4x2: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix4x2: ...

    @overload
    def __sub__(self, other: DMatrix4x2) -> DMatrix4x2: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix4x2: ...
    @overload
    def __rsub__(self, other: DMatrix4x2) -> DMatrix4x2: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix4x2: ...

    def __mul__(self, other: Number) -> DMatrix4x2: ...
    def __rmul__(self, other: Number) -> DMatrix4x2: ...




    @overload
    def __matmul__(self, other: DMatrix2x4) -> DMatrix2x2: ...





    @overload
    def __matmul__(self, other: DMatrix3x4) -> DMatrix3x2: ...





    @overload
    def __matmul__(self, other: DMatrix4x4) -> DMatrix4x2: ...



    @overload
    def __matmul__(self, other: DVector4) -> DVector2: ...

    def __rmatmul__(self, other: DVector2) -> DVector4: ...


    def __truediv__(self, other: Number) -> DMatrix4x2: ...

    def __rtruediv__(self, other: Number) -> DMatrix4x2: ...

    def __neg__(self) -> DMatrix4x2: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix2x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix4x2:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector2,

            _1: FVector2,

            _2: FVector2,

            _3: FVector2,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector2: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix4x2) -> FMatrix4x2: ...
    @overload
    def __add__(self, other: Number) -> FMatrix4x2: ...
    @overload
    def __radd__(self, other: FMatrix4x2) -> FMatrix4x2: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix4x2: ...

    @overload
    def __sub__(self, other: FMatrix4x2) -> FMatrix4x2: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix4x2: ...
    @overload
    def __rsub__(self, other: FMatrix4x2) -> FMatrix4x2: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix4x2: ...

    def __mul__(self, other: Number) -> FMatrix4x2: ...
    def __rmul__(self, other: Number) -> FMatrix4x2: ...




    @overload
    def __matmul__(self, other: FMatrix2x4) -> FMatrix2x2: ...





    @overload
    def __matmul__(self, other: FMatrix3x4) -> FMatrix3x2: ...





    @overload
    def __matmul__(self, other: FMatrix4x4) -> FMatrix4x2: ...



    @overload
    def __matmul__(self, other: FVector4) -> FVector2: ...

    def __rmatmul__(self, other: FVector2) -> FVector4: ...


    def __truediv__(self, other: Number) -> FMatrix4x2: ...

    def __rtruediv__(self, other: Number) -> FMatrix4x2: ...

    def __neg__(self) -> FMatrix4x2: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix2x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix4x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector3,

            _1: DVector3,

            _2: DVector3,

            _3: DVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix4x3) -> DMatrix4x3: ...
    @overload
    def __add__(self, other: Number) -> DMatrix4x3: ...
    @overload
    def __radd__(self, other: DMatrix4x3) -> DMatrix4x3: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix4x3: ...

    @overload
    def __sub__(self, other: DMatrix4x3) -> DMatrix4x3: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix4x3: ...
    @overload
    def __rsub__(self, other: DMatrix4x3) -> DMatrix4x3: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix4x3: ...

    def __mul__(self, other: Number) -> DMatrix4x3: ...
    def __rmul__(self, other: Number) -> DMatrix4x3: ...




    @overload
    def __matmul__(self, other: DMatrix2x4) -> DMatrix2x3: ...





    @overload
    def __matmul__(self, other: DMatrix3x4) -> DMatrix3x3: ...





    @overload
    def __matmul__(self, other: DMatrix4x4) -> DMatrix4x3: ...



    @overload
    def __matmul__(self, other: DVector4) -> DVector3: ...

    def __rmatmul__(self, other: DVector3) -> DVector4: ...


    def __truediv__(self, other: Number) -> DMatrix4x3: ...

    def __rtruediv__(self, other: Number) -> DMatrix4x3: ...

    def __neg__(self) -> DMatrix4x3: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> DMatrix3x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix4x3:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector3,

            _1: FVector3,

            _2: FVector3,

            _3: FVector3,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector3: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix4x3) -> FMatrix4x3: ...
    @overload
    def __add__(self, other: Number) -> FMatrix4x3: ...
    @overload
    def __radd__(self, other: FMatrix4x3) -> FMatrix4x3: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix4x3: ...

    @overload
    def __sub__(self, other: FMatrix4x3) -> FMatrix4x3: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix4x3: ...
    @overload
    def __rsub__(self, other: FMatrix4x3) -> FMatrix4x3: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix4x3: ...

    def __mul__(self, other: Number) -> FMatrix4x3: ...
    def __rmul__(self, other: Number) -> FMatrix4x3: ...




    @overload
    def __matmul__(self, other: FMatrix2x4) -> FMatrix2x3: ...





    @overload
    def __matmul__(self, other: FMatrix3x4) -> FMatrix3x3: ...





    @overload
    def __matmul__(self, other: FMatrix4x4) -> FMatrix4x3: ...



    @overload
    def __matmul__(self, other: FVector4) -> FVector3: ...

    def __rmatmul__(self, other: FVector3) -> FVector4: ...


    def __truediv__(self, other: Number) -> FMatrix4x3: ...

    def __rtruediv__(self, other: Number) -> FMatrix4x3: ...

    def __neg__(self) -> FMatrix4x3: ...
    def __bool__(self) -> bool: ...




    def transpose(self) -> FMatrix3x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class DMatrix4x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: DVector4,

            _1: DVector4,

            _2: DVector4,

            _3: DVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

            _12: Number,

            _13: Number,

            _14: Number,

            _15: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> DVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: DMatrix4x4) -> DMatrix4x4: ...
    @overload
    def __add__(self, other: Number) -> DMatrix4x4: ...
    @overload
    def __radd__(self, other: DMatrix4x4) -> DMatrix4x4: ...
    @overload
    def __radd__(self, other: Number) -> DMatrix4x4: ...

    @overload
    def __sub__(self, other: DMatrix4x4) -> DMatrix4x4: ...
    @overload
    def __sub__(self, other: Number) -> DMatrix4x4: ...
    @overload
    def __rsub__(self, other: DMatrix4x4) -> DMatrix4x4: ...
    @overload
    def __rsub__(self, other: Number) -> DMatrix4x4: ...

    def __mul__(self, other: Number) -> DMatrix4x4: ...
    def __rmul__(self, other: Number) -> DMatrix4x4: ...




    @overload
    def __matmul__(self, other: DMatrix2x4) -> DMatrix2x4: ...





    @overload
    def __matmul__(self, other: DMatrix3x4) -> DMatrix3x4: ...





    @overload
    def __matmul__(self, other: DMatrix4x4) -> DMatrix4x4: ...



    @overload
    def __matmul__(self, other: DVector4) -> DVector4: ...

    def __rmatmul__(self, other: DVector4) -> DVector4: ...


    @overload

    def __truediv__(self, other: Number) -> DMatrix4x4: ...

    @overload
    def __truediv__(self, other: DMatrix4x4) -> DMatrix4x4: ...
    @overload
    def __truediv__(self, other: DVector4) -> DVector4: ...
    @overload
    def __rtruediv__(self, other: DVector4) -> DVector4: ...
    @overload

    def __rtruediv__(self, other: Number) -> DMatrix4x4: ...

    def __neg__(self) -> DMatrix4x4: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> DMatrix4x4: ...



    def transpose(self) -> DMatrix4x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...













@final
class FMatrix4x4:

    __slots__ = ['__weakref__']

    @overload
    def __init__(self, all: Number, /): ...

    @overload
    def __init__(
        self,

            _0: FVector4,

            _1: FVector4,

            _2: FVector4,

            _3: FVector4,

        /
    ): ...

    @overload
    def __init__(
        self,

            _0: Number,

            _1: Number,

            _2: Number,

            _3: Number,

            _4: Number,

            _5: Number,

            _6: Number,

            _7: Number,

            _8: Number,

            _9: Number,

            _10: Number,

            _11: Number,

            _12: Number,

            _13: Number,

            _14: Number,

            _15: Number,

        /
    ): ...

    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self) -> FVector4: ...
    def __eq__(self, other: Any) -> bool: ...
    def __neq__(self, other: Any) -> bool: ...

    @overload
    def __add__(self, other: FMatrix4x4) -> FMatrix4x4: ...
    @overload
    def __add__(self, other: Number) -> FMatrix4x4: ...
    @overload
    def __radd__(self, other: FMatrix4x4) -> FMatrix4x4: ...
    @overload
    def __radd__(self, other: Number) -> FMatrix4x4: ...

    @overload
    def __sub__(self, other: FMatrix4x4) -> FMatrix4x4: ...
    @overload
    def __sub__(self, other: Number) -> FMatrix4x4: ...
    @overload
    def __rsub__(self, other: FMatrix4x4) -> FMatrix4x4: ...
    @overload
    def __rsub__(self, other: Number) -> FMatrix4x4: ...

    def __mul__(self, other: Number) -> FMatrix4x4: ...
    def __rmul__(self, other: Number) -> FMatrix4x4: ...




    @overload
    def __matmul__(self, other: FMatrix2x4) -> FMatrix2x4: ...





    @overload
    def __matmul__(self, other: FMatrix3x4) -> FMatrix3x4: ...





    @overload
    def __matmul__(self, other: FMatrix4x4) -> FMatrix4x4: ...



    @overload
    def __matmul__(self, other: FVector4) -> FVector4: ...

    def __rmatmul__(self, other: FVector4) -> FVector4: ...


    @overload

    def __truediv__(self, other: Number) -> FMatrix4x4: ...

    @overload
    def __truediv__(self, other: FMatrix4x4) -> FMatrix4x4: ...
    @overload
    def __truediv__(self, other: FVector4) -> FVector4: ...
    @overload
    def __rtruediv__(self, other: FVector4) -> FVector4: ...
    @overload

    def __rtruediv__(self, other: Number) -> FMatrix4x4: ...

    def __neg__(self) -> FMatrix4x4: ...
    def __bool__(self) -> bool: ...


    def inverse(self) -> FMatrix4x4: ...



    def transpose(self) -> FMatrix4x4: ...


    @classmethod
    def get_limits(cls) -> tuple[float, float]: ...





