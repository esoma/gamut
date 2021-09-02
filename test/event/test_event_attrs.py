
# gamut
from gamut.event import Event
# pytest
import pytest
# python
from typing import Any, Sequence


@pytest.mark.parametrize(
    "args, kwargs, expected_number, expected_text", [
    [(1, 'test'), {}, 1, 'test'],
    [(99, 'test2'), {}, 99, 'test2'],
    [(1,), {"text": 'test'}, 1, 'test'],
    [(99,), {"text": 'test2'}, 99, 'test2'],
    [(), {"number": 1, "text": 'test'}, 1, 'test'],
    [(), {"number": 99, "text": 'test2'}, 99, 'test2'],
])
def test_direct(
    args: Sequence[Any],
    kwargs: dict[str, Any],
    expected_number: int,
    expected_text: str,
) -> None:
    class AttrEvent(Event):
        number: int
        text: str

    event = AttrEvent(*args, **kwargs)
    assert event.number == expected_number
    assert event.text == expected_text
    
    
def test_multi_inherit() -> None:
    class X(Event):
        a: int
        b: int
    class Y(Event):
        b: int
        c: int
    class Z(X, Y):
        pass
        
    z = Z(1, 2, 3)
    assert z.a == 1
    assert z.b == 2
    assert z.c == 3
    
    
def test_mutli_inherit_conflicting_defaults() -> None:
    class X(Event):
        a: int
        b: int = 20
    class Y(Event):
        b: int = 2
        c: int
    class Z(X, Y):
        pass
        
    z = Z(1, c=3)
    assert z.a == 1
    assert z.b == 20
    assert z.c == 3
    
    
def test_set_static_does_not_exist() -> None:
    with pytest.raises(TypeError):
        class AttrEvent(Event, thing=1):
            thing: int
            
            
def test_override_static_same() -> None:
    class Base(Event):
        thing: int
    class Child(Base, thing=1):
        pass
    class Same(Child, thing=1):
        pass
        
    same = Same()
    assert same.thing == 1
    

def test_override_static_different() -> None:
    class Base(Event):
        thing: int
    class Child(Base, thing=1):
        pass
    
    with pytest.raises(TypeError):
        class Different(Child, thing=2):
            pass
    

def test_multi_static_first_inherit() -> None:
    class O(Event):
        a: int
    class X(O, a=1):
        pass
    class Y(O):
        pass
    class Z(X, Y):
        pass
        
    z = Z()
    assert z.a == 1
       
       
def test_multi_static_second_inherit() -> None:
    class O(Event):
        a: int
    class X(O, a=1):
        pass
    class Y(O):
        pass
    class Z(Y, X):
        pass
        
    z = Z()
    assert z.a == 1
       
            
def test_multi_static_same() -> None:
    class O(Event):
        a: int
    class X(O, a=1):
        pass
    class Y(O, a=1):
        pass
    class Z(X, Y):
        pass
        
    
    z = Z()
    assert z.a == 1
    
    
def test_multi_static_different() -> None:
    class O(Event):
        a: int
    class X(O, a=1):
        pass
    class Y(O, a=2):
        pass
        
    with pytest.raises(TypeError):
        class Z(X, Y):
            pass
    

def test_instantiate_with_multiple_values() -> None:
    class AttrEvent(Event):
        a: int
        b: int
        c: int

    with pytest.raises(TypeError):
        AttrEvent(1, 2, b=4)
    
    
@pytest.mark.parametrize(
    "args, kwargs, "
    "expected_number, expected_text, "
    "default_number, default_text", [
    [(), {}, -1, 'default', -1, 'default'],
    [(1,), {}, 1, 'default', -1, 'default'],
    [(), {"number": 1}, 1, 'default', -1, 'default'],
    [(), {"text": 'test'}, -1, 'test', -1, 'default'],
])
def test_default(
    args: Sequence[Any],
    kwargs: dict[str, Any],
    expected_number: int,
    expected_text: str,
    default_number: int,
    default_text: str,
) -> None:
    class AttrEvent(Event):
        number: int = default_number
        text: str = default_text

    event = AttrEvent(*args, **kwargs)
    assert event.number == expected_number
    assert event.text == expected_text
    
    
@pytest.mark.parametrize(
    "args, kwargs, expected_number, text", [
    [(1,), {}, 1, 'test'],
    [(99,), {}, 99, 'test2'],
    [(), {"number": 1}, 1, 'test'],
    [(), {"number": 99}, 99, 'test2'],
])
def test_static(
    args: Sequence[Any],
    kwargs: dict[str, Any],
    expected_number: int,
    text: str,
) -> None:
    class AttrEvent(Event):
        number: int
        text: str
    class StaticAttrEvent(AttrEvent, text=text):
        pass

    event = StaticAttrEvent(*args, **kwargs)
    assert event.number == expected_number
    assert event.text == text  


@pytest.mark.parametrize(
    "args, kwargs", [
    [('test',), {}],
    [(), {"text": 'test'}],
])
def test_instantiate_specify_static(
    args: Sequence[Any],
    kwargs: dict[str, Any],
) -> None:
    class AttrEvent(Event):
        number: int
        text: str
    class StaticAttrEvent(AttrEvent, text='__test__'):
        pass

    with pytest.raises(TypeError):
        event = StaticAttrEvent(1, *args, **kwargs)
