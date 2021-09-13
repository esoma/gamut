
__all__ = ['Plugin']

# python
from dataclasses import dataclass
from functools import partial
from typing import Any, Callable, Generator, Optional, Type
# mypy
from mypy.nodes import (ARG_NAMED, ARG_OPT, ARG_POS, Argument, AssignmentStmt,
                        EllipsisExpr, Expression, FuncDef, is_class_var,
                        NameExpr, TempNode, Var)
from mypy.plugin import ClassDefContext, MethodSigContext
from mypy.plugin import Plugin as _Plugin
from mypy.plugins.common import add_method
from mypy.semanal import SemanticAnalyzer
from mypy.types import AnyType, CallableType, get_proper_type, NoneType
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny


class Plugin(_Plugin):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._context = _Context()

    def get_base_class_hook(
        self, fullname: str
    ) -> Optional[Callable[[ClassDefContext], None]]:
        result = super().get_base_class_hook(fullname)
        if result is not None:
            return result

        if fullname in self._context.events:
            return partial(_transform_event_subclass, context=self._context)

        return None

    def get_metaclass_hook(
        self,
        fullname: str
    ) -> Optional[Callable[[ClassDefContext], None]]:
        result = super().get_base_class_hook(fullname)
        if result is not None:
            return result

        if fullname == 'gamut.event._event.EventType':
            return _transform_event

        return None

    def get_method_signature_hook(
        self,
        fullname: str
    ) -> Optional[Callable[[MethodSigContext], CallableType]]:
        result = super().get_method_signature_hook(fullname)
        if result is not None:
            return result

        if fullname.endswith('.__init_subclass__'):
            cls_fullname = fullname[:-len('.__init_subclass__')]
            if cls_fullname in self._context.events:
                return partial(
                    _transform_event_init_subclass,
                    context=self._context
                )

        return None


def plugin(version: str) -> Type[Plugin]:
    return Plugin


@dataclass
class _EventField:
    name: str
    has_default: bool
    is_static: bool
    is_prototype: bool
    type: MypyType
    node: AssignmentStmt

    def to_init_argument(self) -> Argument:
        return Argument(
            Var(self.name, self.type),
            self.type,
            None,
            ARG_OPT if self.has_default else ARG_POS
        )

    def to_init_subclass_argument(self) -> Argument:
        return Argument(
            Var(self.name, self.type),
            self.type,
            None,
            ARG_OPT
        )


@dataclass
class _Event:
    name: str
    bases: list[str]
    fields: dict[str, _EventField]
    keywords: dict[str, Expression]


class _Context:

    def __init__(self) -> None:
        self.events = {
            'gamut.event._event.Event': _Event(
                'gamut.event._event.Event', [], {}, {}
            )
        }
        self.events_by_line: dict[tuple[str, int], _Event] = {}


def _transform_event(ctx: ClassDefContext) -> None:
    # the only class that should use EventType is the Event class
    assert ctx.cls.info.fullname == 'gamut.event._event.Event'

    add_method(ctx, '__init__', [], NoneType())
    add_method(
        ctx, '__init_subclass__', [], NoneType(),
        self_type=AnyType(TypeOfAny.explicit)
    )


def _transform_event_subclass(ctx: ClassDefContext, context: _Context) -> None:
    # hack the name of the metaclass so that mypy will typecheck
    # __init_subclass__
    # see: https://github.com/python/mypy/issues/11057
    assert ctx.cls.info.metaclass_type
    ctx.cls.info.metaclass_type.type._fullname = 'builtins.type'

    context.events[ctx.cls.fullname] = event = _Event(
        ctx.cls.fullname,
        [base.type.fullname for base in ctx.cls.info.bases],
        _get_fields(ctx, context),
        ctx.cls.keywords
    )
    path = ctx.api.modules[ctx.cls.info.module_name].path
    context.events_by_line[(path, ctx.cls.line)] = event

    if "__init__" not in ctx.cls.info.names:
        add_method(
            ctx,
            '__init__',
            [
                ef.to_init_argument()
                for ef in event.fields.values()
                if not ef.is_static and not ef.is_prototype
            ],
            NoneType(),
        )
    if "__init_subclass__" not in ctx.cls.info.names:
        add_method(
            ctx,
            '__init_subclass__',
            [
                ef.to_init_subclass_argument()
                for ef in event.fields.values()
                if not ef.is_static
            ],
            NoneType(),
            self_type=AnyType(TypeOfAny.explicit),
        )
        # for some reason if the Event is defined within a function the
        # semantic analyzer won't visit __init_subclass__ and we get strange
        # errors because the first argument (cls/self) isn't bound
        init_subclass_node = ctx.cls.info.names["__init_subclass__"]
        assert isinstance(ctx.api, SemanticAnalyzer)
        assert isinstance(init_subclass_node.node, FuncDef)
        ctx.api.visit_func_def(init_subclass_node.node)


def _get_fields(
    ctx: ClassDefContext,
    context: _Context
) -> dict[str, _EventField]:
    fields: dict[str, _EventField] = {}

    def _apply_field(field: _EventField) -> None:
        adjacent_field = fields.get(field.name, None)
        if adjacent_field:
            if field.is_static:
                adjacent_field.is_static = True
            if field.has_default and not adjacent_field.has_default:
                adjacent_field.has_default = True
            if field.type != adjacent_field.type:
                adjacent_field.type = field.type
        else:
            fields[field.name] = _EventField(
                field.name,
                field.has_default,
                field.is_static,
                False,
                field.type,
                field.node,
            )
        try:
            keyword_expr = ctx.cls.keywords[field.name]
        except KeyError:
            return
        if isinstance(keyword_expr, EllipsisExpr):
            fields[field.name].is_prototype = True
        else:
            fields[field.name].is_static = True
            fields[field.name].is_prototype = False

    for base in ctx.cls.info.bases:
        try:
            base_event = context.events[base.type.fullname]
        except KeyError:
            continue
        for field in base_event.fields.values():
            _apply_field(field)

    for field in _get_direct_fields(ctx):
        _apply_field(field)

    return fields


def _get_direct_fields(
    ctx: ClassDefContext,
) -> Generator[_EventField, None, None]:
    for node in ctx.cls.defs.body:
        if isinstance(node, AssignmentStmt) and node.type is not None:
            has_default = not (
                isinstance(node.rvalue, TempNode) and
                isinstance(get_proper_type(node.rvalue.type), AnyType)
            )
            for lvalue in node.lvalues:
                if isinstance(lvalue, NameExpr):
                    if is_class_var(lvalue):
                        continue
                    yield _EventField(
                        lvalue.name,
                        has_default,
                        False,
                        False,
                        node.type,
                        node
                    )

@dataclass
class _SubclassParam:
    name: str
    type: MypyType
    is_required: bool
    is_static: bool


def _transform_event_init_subclass(
    ctx: MethodSigContext,
    context: _Context
) -> CallableType:
    # combine the fields on the base classes and the defined class to determine
    # the signature for class instantiation
    event = context.events_by_line[(ctx.api.path, ctx.context.line)]
    params: dict[str, _SubclassParam] = {}
    for base_name in event.bases:
        try:
            base = context.events[base_name]
        except KeyError:
            # this base is not an event
            continue
        for field in base.fields.values():
            try:
                param = params[field.name]
            except KeyError:
                param = params[field.name] = _SubclassParam(
                    field.name,
                    field.type,
                    False,
                    False
                )
            if field.is_prototype:
                param.is_required = True
            if field.is_static:
                param.is_static = True
    # fields may be defined on the instantiated event itself that can be made
    # static or prototypes
    for field in event.fields.values():
        try:
            param = params[field.name]
        except KeyError:
            param = params[field.name] = _SubclassParam(
                field.name,
                field.type,
                False,
                False
            )
    # remove static parameters, they cannot be parameters
    params = {
        name: param
        for name, param in params.items()
        if not param.is_static
    }
    # any parameters may be prototypes
    for param in params.values():
        kwarg: Optional[Expression] = None
        try:
            kwarg = event.keywords[param.name]
        except KeyError:
            pass
        if kwarg and isinstance(kwarg, EllipsisExpr):
            param.type = AnyType(TypeOfAny.explicit)

    return ctx.default_signature.copy_modified(
        name=None,
        arg_kinds=[
            ARG_NAMED if p.is_required else ARG_OPT
            for p in params.values()
        ],
        arg_types=[p.type for p in params.values()],
        arg_names=[p.name for p in params.values()],
    )
