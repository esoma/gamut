
__all__ = ['Plugin']

# mypy
from mypy.fastparse import parse
from mypy.plugin import ClassDefContext, Plugin as _Plugin
from mypy.plugins.common import add_method, add_method_to_class
from mypy.nodes import ARG_POS, ARG_OPT, Argument, ClassDef, AssignmentStmt, TypeInfo, Block, FuncDef, SymbolTable, NameExpr, MDEF, SymbolTableNode, TempNode, Var
from mypy.mro import calculate_mro
from mypy.semanal import SemanticAnalyzer
from mypy.types import AnyType, get_proper_type, Instance, NoneType, Type as MypyType, TypeOfAny
from mypy.typevars import fill_typevars
# python
from dataclasses import dataclass
import logging
from functools import partial
import textwrap
from typing import Any, Callable, Generator, Optional, Type

log = logging.getLogger(__name__)


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
        
        
def plugin(version: str) -> Type[Plugin]:
    return Plugin
    
    
@dataclass
class _EventField:
    name: str
    has_default: bool
    is_static: bool
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
    fields: dict[str, _EventField]
    
    
class _Context:
    
    def __init__(self) -> None:
        self.events = {
            'gamut.event._event.Event': _Event('gamut.event._event.Event', {})
        }


def _transform_event_subclass(ctx: ClassDefContext, context: _Context) -> None:
    # hack the name of the metaclass so that mypy will typecheck
    # __init_subclass__
    # see: https://github.com/python/mypy/issues/11057
    assert ctx.cls.info.metaclass_type
    ctx.cls.info.metaclass_type.type._fullname = 'builtins.type'
    
    context.events[ctx.cls.fullname] = event = _Event(
        ctx.cls.fullname,
        _get_fields(ctx, context),
    )
    if "__init__" not in ctx.cls.info.names:
        add_method(
            ctx,
            '__init__',
            [ef.to_init_argument() for ef in event.fields.values() if not ef.is_static],
            NoneType(),
        )
    if "__init_subclass__" not in ctx.cls.info.names:
        add_method(
            ctx,
            '__init_subclass__',
            [ef.to_init_subclass_argument() for ef in event.fields.values() if not ef.is_static],
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
    context: _Context,
) -> dict[str, _EventField]:
    fields = {ef.name: ef for ef in _get_direct_fields(ctx)}
    
    for base in ctx.cls.info.bases:
        base_event = context.events[base.type.fullname]
        for field in base_event.fields.values():
            if field.name in ctx.cls.keywords:
                field.is_static = True
            adjacent_field = fields.get(field.name, None)
            if adjacent_field:
                if field.has_default and not adjacent_field.has_default:
                    adjacent_field.has_default = True
            else:
                fields[field.name] = _EventField(
                    field.name,
                    field.has_default,
                    field.is_static,
                    field.type,
                    field.node,
                )
    
    return fields


def _get_direct_fields(
    ctx: ClassDefContext
) -> Generator[_EventField, None, None]:
    for node in ctx.cls.defs.body:
        if isinstance(node, AssignmentStmt) and node.type is not None:
            has_default = not (
                isinstance(node.rvalue, TempNode) and
                isinstance(get_proper_type(node.rvalue.type), AnyType)
            )
            for lvalue in node.lvalues:
                if isinstance(lvalue, NameExpr):
                    yield _EventField(
                        lvalue.name,
                        has_default,
                        False,
                        node.type,
                        node
                    )
    
