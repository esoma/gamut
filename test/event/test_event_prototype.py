
from __future__ import annotations
# gamut
from gamut.event import Event
# pytest
import pytest


def test_non_existent_field_prototyped() -> None:
    class BaseEvent(Event):
        a: int
    with pytest.raises(TypeError) as excinfo:
        class ProtoEvent(BaseEvent, b=...): # type: ignore
            pass
    assert str(excinfo.value) == (
        'test_non_existent_field_prototyped.<locals>.ProtoEvent.'
        '__init_subclass__() takes no keyword arguments'
    )


def test_instantiate_prototype() -> None:
    class BaseEvent(Event):
        a: int
    class ProtoEvent(BaseEvent, a=...):
        pass
    with pytest.raises(TypeError) as excinfo:
        ProtoEvent() # type: ignore
    assert str(excinfo.value) == 'cannot instantiate a prototype event'


def test_use_prototype() -> None:
    class BaseEvent(Event):
        a: int
    class ProtoEvent(BaseEvent, a=...):
        pass
    class UseProtoEvent(ProtoEvent, a=5):
        pass
    event = UseProtoEvent()
    assert event.a == 5


def test_use_prototype_multiple_fields() -> None:
    class BaseEvent(Event):
        a: int
        b: int
    class ProtoEvent(BaseEvent, a=..., b=...):
        pass
    class UseProtoEvent(ProtoEvent, a=5, b=10):
        pass
    event = UseProtoEvent()
    assert event.a == 5
    assert event.b == 10


def test_use_multiple_prototype_multiple_fields() -> None:
    class BaseEvent(Event):
        a: int
        b: int
    class ProtoEventA(BaseEvent, a=...):
        pass
    class ProtoEventB(BaseEvent, b=...):
        pass
    class UseProtoEvent(ProtoEventA, ProtoEventB, a=5, b=10):
        pass
    event = UseProtoEvent()
    assert event.a == 5
    assert event.b == 10


def test_use_prototype_field_not_provided() -> None:
    class BaseEvent(Event):
        a: int
    class ProtoEvent(BaseEvent, a=...):
        pass
    with pytest.raises(TypeError) as excinfo:
        class UseProtoEvent(ProtoEvent): # type: ignore
            pass
    assert str(excinfo.value) == 'missing required keyword-only argument(s): a'


def test_use_prototype_multiple_fields_not_provided() -> None:
    class BaseEvent(Event):
        a: int
        b: int
    class ProtoEvent(BaseEvent, a=..., b=...):
        pass
    with pytest.raises(TypeError) as excinfo:
        class UseProtoEvent(ProtoEvent): # type: ignore
            pass
    assert str(excinfo.value) == (
        'missing required keyword-only argument(s): a, b'
    )


def test_use_multiple_prototype_multiple_fields_not_provided() -> None:
    class BaseEvent(Event):
        a: int
        b: int
    class ProtoEventA(BaseEvent, a=...):
        pass
    class ProtoEventB(BaseEvent, b=...):
        pass
    with pytest.raises(TypeError) as excinfo:
        class UseProtoEvent(ProtoEventA, ProtoEventB): # type: ignore
            pass
    assert str(excinfo.value) == (
        'missing required keyword-only argument(s): a, b'
    )
