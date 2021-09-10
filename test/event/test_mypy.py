
# python
from dataclasses import dataclass
from os import path
import re
import textwrap
from typing import Callable
# mypy
import mypy.api
# pytest
import pytest

mypy_error_pattern = re.compile(r'<string>:(\d+): (.+)')

directory = path.dirname(path.realpath(__file__))

@dataclass
class MypyResult:
    line: int
    text: str


def run_mypy_with_config(src: str, config_file: str) -> list[MypyResult]:
    report, _, _ = mypy.api.run([
        '--config-file', config_file,
        '-c', textwrap.dedent(src),
        '--no-incremental',
        '--show-traceback',
    ])
    errors: list[MypyResult] = []
    for line in report.split('\n'):
        print(line)
        match = mypy_error_pattern.match(line)
        if match:
            errors.append(MypyResult(int(match.group(1)), match.group(2)))
    return errors


def run_mypy_with_main_plugin(src: str) -> list[MypyResult]:
    return run_mypy_with_config(
        src,
        path.join(directory, 'mypy-main-plugin.ini')
    )


def run_mypy_with_event_plugin(src: str) -> list[MypyResult]:
    return run_mypy_with_config(
        src,
        path.join(directory, 'mypy-event-plugin.ini')
    )


parametrize_run_mypy = pytest.mark.parametrize("run_mypy", [
    run_mypy_with_main_plugin,
    run_mypy_with_event_plugin,
])


@parametrize_run_mypy
def test_event_init(run_mypy: Callable[[str], list[MypyResult]]) -> None:
    assert run_mypy("""
        from gamut.event import Event
        reveal_type(Event.__init__)
        Event()
        Event(1)
    """) == [
        MypyResult(3, 'note: Revealed type is '
                      '"def (self: gamut.event._event.Event)"'),
        MypyResult(5, 'error: Too many arguments for "Event"')
    ]


@parametrize_run_mypy
def test_event_init_subclass(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        reveal_type(Event.__init_subclass__)
        class SubEvent(Event): ...
        class SubEventFail(Event, keyword=1): ...
    """) == [
        MypyResult(3, 'note: Revealed type is "def ()"'),
        MypyResult(5, 'error: Unexpected keyword argument "keyword" for '
                      '"__init_subclass__" of "Event"')
    ]


@parametrize_run_mypy
def test_event_await(run_mypy: Callable[[str], list[MypyResult]]) -> None:
    assert run_mypy("""
        from gamut.event import Event
        reveal_type(Event.__await__)
        async def _() -> None:
            result = await Event
            reveal_type(result)
    """) == [
        MypyResult(3,
            'note: Revealed type is "def () -> typing.Generator['
                'gamut.event._future.Future['
                    'gamut.event._event.Event*, '
                    'gamut.event._task.Task[gamut.event._event.Event*]'
                '], '
                'None, '
                'gamut.event._event.Event*'
            ']"'),
        MypyResult(6, 'note: Revealed type is "gamut.event._event.Event*"')
    ]


@parametrize_run_mypy
def test_event_subclass_no_attrs_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event): ...
        reveal_type(SubEvent.__init__)
        SubEvent()
        SubEvent(1)
    """) == [
        MypyResult(4, 'note: Revealed type is '
                      '"def (self: __main__.SubEvent)"'),
        MypyResult(6, 'error: Too many arguments for "SubEvent"')
    ]


@parametrize_run_mypy
def test_event_subclass_no_attrs_init_subclass(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event): ...
        reveal_type(SubEvent.__init_subclass__)
        class SubSubEvent(SubEvent): ...
        class SubSubEventFail(SubEvent, keyword=1): ...
    """) == [
        MypyResult(4, 'note: Revealed type is "def ()"'),
        MypyResult(6, 'error: Unexpected keyword argument "keyword" for '
                      '"__init_subclass__" of "SubEvent"')
    ]


@parametrize_run_mypy
def test_event_subclass_await(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event): ...
        reveal_type(SubEvent.__await__)
        async def _() -> None:
            result = await SubEvent
            reveal_type(result)
    """) == [
        MypyResult(4,
            'note: Revealed type is "def () -> typing.Generator['
                'gamut.event._future.Future['
                    '__main__.SubEvent*, '
                    'gamut.event._task.Task[__main__.SubEvent*]'
                '], '
                'None, '
                '__main__.SubEvent*'
            ']"'),
        MypyResult(7, 'note: Revealed type is "__main__.SubEvent*"')
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_no_defaults_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int
        reveal_type(SubEvent.__init__)
        SubEvent(1, "2", 3)
        SubEvent(c=1, a=2, b="3")
        SubEvent(1, "2")
        SubEvent(1, "2", "3")
    """) == [
        MypyResult(7,
            'note: Revealed type is "def ('
                'self: __main__.SubEvent, '
                'a: builtins.int, '
                'b: builtins.str, '
                'c: builtins.int'
            ')"'),
        MypyResult(10,
            'error: Missing positional argument "c" in call to "SubEvent"'),
        MypyResult(11,
            'error: Argument 3 to "SubEvent" has incompatible type "str"; '
            'expected "int"')
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_override_type(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class A: pass
        class SubA(A): pass
        class SubEvent(Event):
            a: A
        class SubEvent2(SubEvent):
            a: SubA
        reveal_type(SubEvent2.__init__)
        reveal_type(SubEvent2.__init_subclass__)
    """) == [
        MypyResult(9,
            'note: Revealed type is "def ('
                'self: __main__.SubEvent2, '
                'a: __main__.SubA'
            ')"'),
        MypyResult(10,
            'note: Revealed type is "def ('
                'a: __main__.SubA ='
            ')"'),
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_override_type_invalid(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class A: pass
        class SubA(A): pass
        class SubEvent(Event):
            a: A
        class SubEvent2(SubEvent):
            a: int
    """) == [
        MypyResult(8,
            'error: Incompatible types in assignment ('
                'expression has type "int", '
                'base class "SubEvent" defined the type as "A"'
            ')'),
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_class_var(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        from typing import ClassVar
        class SubEvent(Event):
            a: int
            b: ClassVar[str]
            c: int
        reveal_type(SubEvent.__init__)
        reveal_type(SubEvent.__init_subclass__)
    """) == [
        MypyResult(8,
            'note: Revealed type is "def ('
                'self: __main__.SubEvent, '
                'a: builtins.int, '
                'c: builtins.int'
            ')"'),
        MypyResult(9,
            'note: Revealed type is "def ('
                'a: builtins.int =, '
                'c: builtins.int ='
            ')"'),
    ]


@parametrize_run_mypy
def test_event_subclass_non_event_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
        class NonEvent:
            b: int
        class TestEvent(SubEvent, NonEvent): ...
        reveal_type(TestEvent.__init__)
        SubEvent(1)
        reveal_type(TestEvent.a)
        reveal_type(TestEvent.b)
    """) == [
        MypyResult(8,
            'note: Revealed type is "def ('
                'self: __main__.TestEvent, '
                'a: builtins.int'
            ')"'),
        MypyResult(10, 'note: Revealed type is "builtins.int"'),
        MypyResult(11, 'note: Revealed type is "builtins.int"'),
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_defaults_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int = 1
            b: str = "b"
            c: int
        reveal_type(SubEvent.__init__)
        SubEvent(c=1)
        SubEvent(c=1, a=2, b="3")
        SubEvent(1, "2")
        SubEvent(1, "2", "3")
    """) == [
        MypyResult(7,
            'note: Revealed type is "def ('
                'self: __main__.SubEvent, '
                'a: builtins.int =, '
                'b: builtins.str =, '
                'c: builtins.int'
            ')"'),
        MypyResult(10, 'error: Too few arguments for "SubEvent"'),
        MypyResult(11,
            'error: Argument 3 to "SubEvent" has incompatible type "str"; '
            'expected "int"')
    ]


@parametrize_run_mypy
def test_event_subclass_inherited_attrs_defaults_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int
        class DefaultEvent(SubEvent):
            c: int = 3
        reveal_type(DefaultEvent.__init__)
        DefaultEvent(1, "b")
        DefaultEvent(1, "b", 4)
        DefaultEvent(c=1, a=2, b="3")
    """) == [
        MypyResult(9,
            'note: Revealed type is "def ('
                'self: __main__.DefaultEvent, '
                'a: builtins.int, '
                'b: builtins.str, '
                'c: builtins.int ='
            ')"'),
    ]


@parametrize_run_mypy
def test_event_subclass_attrs_init_subclass(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int = 4
        reveal_type(SubEvent.__init_subclass__)
        class SubSubEvent(SubEvent): ...
        class SubSubEventStaticA(SubEvent, a=1): ...
        class SubSubEventNotAKeyword(SubEvent, keyword=1): ...
        class SubSubEventBadType(SubEvent, a="1"): ...
    """) == [
        MypyResult(7,
            'note: Revealed type is "def ('
                'a: builtins.int =, '
                'b: builtins.str =, '
                'c: builtins.int ='
            ')"'),
        MypyResult(10, 'error: Unexpected keyword argument "keyword" for '
                      '"__init_subclass__" of "SubEvent"'),
        MypyResult(11,
            'error: Argument "a" to "__init_subclass__" of "SubEvent" has '
            'incompatible type "str"; expected "int"')
    ]


@parametrize_run_mypy
def test_event_subclass_static_attrs_init(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int
        class StaticEvent(SubEvent, b="test"): ...
        reveal_type(StaticEvent.__init__)
        StaticEvent(1, 3)
        StaticEvent(1, 3, b="2")
    """) == [
        MypyResult(8,
            'note: Revealed type is "def ('
                'self: __main__.StaticEvent, '
                'a: builtins.int, '
                'c: builtins.int'
            ')"'),
        MypyResult(10,
            'error: Unexpected keyword argument "b" for "StaticEvent"'),
    ]


@parametrize_run_mypy
def test_event_subclass_static_attrs_init_subclass(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int
        class StaticEvent(SubEvent, b="test"): ...
        reveal_type(StaticEvent.__init_subclass__)
        class SubStaticEvent(StaticEvent): ...
        class SubStaticEventStaticA(StaticEvent, a=1): ...
        class SubStaticEventBAgain(StaticEvent, b="test"): ...
    """) == [
        MypyResult(8,
            'note: Revealed type is "def ('
                'a: builtins.int =, '
                'c: builtins.int ='
            ')"'),
        MypyResult(11, 'error: Unexpected keyword argument "b" for '
                      '"__init_subclass__" of "StaticEvent"'),
    ]


@parametrize_run_mypy
def test_event_subclass_multi_inherit_static_attrs_init_subclass(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class SubEvent(Event):
            a: int
            b: str
            c: int
        class StaticEvent(SubEvent, b="test"): ...
        class ParallelEvent(SubEvent): ...
        class TestEvent(ParallelEvent, StaticEvent): ...
        reveal_type(TestEvent.__init_subclass__)
        class SubTestEvent(TestEvent): ...
        class SubTestEventStaticA(TestEvent, a=1): ...
        class SubTestEventBAgain(TestEvent, b="test"): ...
    """) == [
        MypyResult(10,
            'note: Revealed type is "def ('
                'a: builtins.int =, '
                'c: builtins.int ='
            ')"'),
        MypyResult(13, 'error: Unexpected keyword argument "b" for '
                      '"__init_subclass__" of "TestEvent"'),
    ]


@parametrize_run_mypy
def test_or_event(run_mypy: Callable[[str], list[MypyResult]]) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class EventA(Event):
            pass
        class EventB(Event):
            pass
        or_events = EventA | EventB
        reveal_type(or_events)
        reveal_type(or_events.__await__)
    """) == [
        MypyResult(8,
            'note: Revealed type is "gamut.event._event.OrEvents['
                'def () -> __main__.EventA, '
                'def () -> __main__.EventB'
            ']"'),
        MypyResult(9,
            'note: Revealed type is "def () -> typing.Generator['
                'gamut.event._future.Future['
                    'Union[__main__.EventA, __main__.EventB], '
                    'gamut.event._task.Task['
                        'Union[__main__.EventA, __main__.EventB]'
                    ']'
                '], '
                'None, '
                'Union[__main__.EventA, __main__.EventB]'
            ']"'),
    ]


@parametrize_run_mypy
def test_non_existent_field_prototyped(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
            b: int
        class ProtoEvent(BaseEvent, c=...):
            pass
    """) == [
        MypyResult(6,
            'error: Unexpected keyword argument '
            '"c" for "__init_subclass__" of "BaseEvent"')
    ]


@parametrize_run_mypy
def test_instantiate_prototype(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
        class ProtoEvent(BaseEvent, a=...):
            pass
        reveal_type(ProtoEvent.__init__)
        ProtoEvent()
    """) == [
        MypyResult(7,
            'note: Revealed type is "def (self: __main__.ProtoEvent)"'),
    ]


@parametrize_run_mypy
def test_use_prototype(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
        class ProtoEvent(BaseEvent, a=...):
            pass
        class UseProtoEvent(ProtoEvent, a=5):
            pass
        reveal_type(UseProtoEvent.__init__)
        event = UseProtoEvent()
        reveal_type(event)
    """) == [
        MypyResult(9,
            'note: Revealed type is "def (self: __main__.UseProtoEvent)"'),
        MypyResult(11,
            'note: Revealed type is "__main__.UseProtoEvent"')
    ]


@parametrize_run_mypy
def test_use_prototype_multiple_fields(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
            b: int
        class ProtoEvent(BaseEvent, a=..., b=...):
            pass
        class UseProtoEvent(ProtoEvent, a=5, b=10):
            pass
        reveal_type(UseProtoEvent.__init__)
        event = UseProtoEvent()
        reveal_type(event)
    """) == [
        MypyResult(10,
            'note: Revealed type is "def (self: __main__.UseProtoEvent)"'),
        MypyResult(12,
            'note: Revealed type is "__main__.UseProtoEvent"')
    ]


@parametrize_run_mypy
def test_use_multiple_prototype_multiple_fields(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
            b: int
        class ProtoEventA(BaseEvent, a=...):
            pass
        class ProtoEventB(BaseEvent, b=...):
            pass
        class UseProtoEvent(ProtoEventA, ProtoEventB, a=5, b=10):
            pass
        reveal_type(UseProtoEvent.__init__)
        event = UseProtoEvent()
        reveal_type(event)
    """) == [
        MypyResult(12,
            'note: Revealed type is "def (self: __main__.UseProtoEvent)"'),
        MypyResult(14,
            'note: Revealed type is "__main__.UseProtoEvent"')
    ]


@parametrize_run_mypy
def test_use_prototype_field_not_provided(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
        class ProtoEvent(BaseEvent, a=...):
            pass
        class UseProtoEvent(ProtoEvent):
            pass
    """) == [
        MypyResult(7,
            'error: Missing named argument '
            '"a" for "__init_subclass__" of "ProtoEvent"')
    ]


@parametrize_run_mypy
def test_use_prototype_multiple_fields_not_provided(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
            b: int
        class ProtoEvent(BaseEvent, a=..., b=...):
            pass
        class UseProtoEvent(ProtoEvent):
            pass
    """) == [
        MypyResult(8,
            'error: Missing named argument '
            '"a" for "__init_subclass__" of "ProtoEvent"'),
        MypyResult(8,
            'error: Missing named argument '
            '"b" for "__init_subclass__" of "ProtoEvent"')
    ]


@parametrize_run_mypy
def test_use_multiple_prototype_multiple_fields_not_provided(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
            b: int
        class ProtoEventA(BaseEvent, a=...):
            pass
        class ProtoEventB(BaseEvent, b=...):
            pass
        class UseProtoEvent(ProtoEventA, ProtoEventB):
            pass
    """) == [
        MypyResult(10,
            'error: Missing named argument '
            '"a" for "__init_subclass__" of "ProtoEventA"'),
        MypyResult(10,
            'error: Missing named argument '
            '"b" for "__init_subclass__" of "ProtoEventB"')
    ]


@parametrize_run_mypy
def test_use_prototype_inherit_static(
    run_mypy: Callable[[str], list[MypyResult]]
) -> None:
    assert run_mypy("""
        from gamut.event import Event
        class BaseEvent(Event):
            a: int
        class ProtoEventA(BaseEvent, a=...):
            pass
        class BaseStaticA(BaseEvent, a=1):
            pass
        class UseProtoEvent(ProtoEventA, BaseStaticA):
            pass
        reveal_type(UseProtoEvent.__init__)
        event = UseProtoEvent()
        reveal_type(event)
    """) == [
        MypyResult(11,
            'note: Revealed type is "def (self: __main__.UseProtoEvent)"'),
        MypyResult(13,
            'note: Revealed type is "__main__.UseProtoEvent"')
    ]
