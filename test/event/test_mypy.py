
# python
import re
import textwrap
from dataclasses import dataclass
# mypy
import mypy.api

mypy_error_pattern = re.compile(r'<string>:(\d+): (.+)')


@dataclass
class MypyResult:
    line: int
    text: str


def run_mypy(src: str) -> list[MypyResult]:
    report, _, _ = mypy.api.run(['-c', textwrap.dedent(src), '--strict'])
    errors: list[MypyResult] = []
    for line in report.split('\n'):
        print(line)
        match = mypy_error_pattern.match(line)
        if match:
            errors.append(MypyResult(int(match.group(1)), match.group(2)))
    return errors


def test_event_init() -> None:
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


def test_event_init_subclass() -> None:
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


def test_event_await() -> None:
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


def test_event_subclass_no_attrs_init() -> None:
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


def test_event_subclass_no_attrs_init_subclass() -> None:
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


def test_event_subclass_await() -> None:
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


def test_event_subclass_attrs_no_defaults_init() -> None:
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


def test_event_subclass_attrs_defaults_init() -> None:
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


def test_event_subclass_attrs_init_subclass() -> None:
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


def test_event_subclass_static_attrs_init() -> None:
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


def test_event_subclass_static_attrs_init_subclass() -> None:
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
