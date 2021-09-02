
__all__ = ['Bind', 'BindClosed', 'BindKind', 'Event']

from ._bind import Bind, BindClosed, BindKind
from ._event import Event

"""
from __future__ import annotations

__all__ = ['Event', 'Eventful', 'on']

# python
from collections import deque
from enum import Enum
import inspect
from typing import (Any, Callable, ClassVar, Coroutine, final, Generator,
                    Generic, Optional, TypeVar, Union)
from weakref import ref, WeakSet


T = TypeVar('T')
        
        












                
                






class Eventful:

    _events: Dict[str, Type[Event]]
    _event_kwargs: Dict[str, Any]
    _when_methods: List[Any]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        cls._event_kwargs = kwargs
        cls._events = {}
        cls._generate_class_events(**kwargs)

        cls._when_methods = []
        for key in dir(cls):
            value = getattr(cls, key)
            try:
                value._when_event_names
            except AttributeError:
                continue
            cls._when_methods.append(value)

    def __init__(
        self,
        *args: Any,
        event_kwargs: Dict[str, str]={},
        event_extra_bases: List[type] = [],
        **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs) # type: ignore
        if event_kwargs:
            self._generate_instance_events(event_extra_bases, **event_kwargs)
        for method in self._when_methods:
            for event_finder in method._when_events:
                event = event_finder(self)
                # bind event

    def _generate_instance_events(
        self,
        extra_bases: List[type],
        **kwargs: Any
    ) -> None:
        events: Dict[Type[Event], Type[Event]] = {}
        for name, event in self._events.items():
            bases = []
            for extra_base in extra_bases:
                bases.append(getattr(extra_base, name))
            bases.append(event)
            for mro in inspect.getmro(event):
                if mro in events:
                    bases.append(events[mro])
            def _() -> Type[Event]:
                X = type(event.__name__, tuple(bases), {}, **kwargs)
                return X
            X = _()
            events[event] = X
            setattr(self, name, X)

    @classmethod
    def _generate_class_events(cls, **kwargs: Any) -> None:
        events = cls._events
        gen_events: Dict[Type[Event], Type[Event]] = {}
        for key in dir(cls):
            value = getattr(cls, key)
            try:
                if issubclass(value, Event):
                    events[key] = value
            except TypeError:
                pass

        if kwargs:
            for name, event in tuple(events.items()):
                bases = [event]
                for mro in inspect.getmro(event):
                    if mro in gen_events:
                        bases.append(gen_events[mro])
                def _():
                    X = type(event.__name__, tuple(bases), {}, **kwargs)
                    return X
                X = _()
                gen_events[event] = X
                events[name] = X
                setattr(cls, name, X)
"""