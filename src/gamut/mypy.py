
from __future__ import annotations

__all__ = ['plugin']

# gamut
from .event.mypy import Plugin as EventPlugin
# python
from typing import Callable
# mypy
from mypy.plugin import AttributeContext
from mypy.types import AnyType, Instance, Type, TypeOfAny


class Plugin(EventPlugin):

    def get_attribute_hook(
        self,
        fullname: str
    ) -> Callable[[AttributeContext], Type] | None:
        if fullname == 'gamut._transformnode.TransformNode.children':
            return _fix_transform_node_children_return_type
        return super().get_attribute_hook(fullname)


def plugin(version: str) -> type[Plugin]:
    return Plugin


def _fix_transform_node_children_return_type(ctx: AttributeContext) -> Type:
    return_type = ctx.default_attr_type
    if isinstance(return_type, Instance):
        assert return_type.type.fullname == 'builtins.set'
        assert len(return_type.args) == 1
        set_type = return_type.args[0]
        if isinstance(set_type, AnyType):
            tn_type = ctx.type
            assert isinstance(tn_type, Instance)
            for base_type in tn_type.type.mro:
                if base_type.fullname == 'gamut._transformnode.TransformNode':
                    break
            else:
                assert False
            type_checker = ctx.api
            return type_checker.named_generic_type(
                'builtins.set',
                [Instance(base_type, [AnyType(TypeOfAny.explicit)])]
            )
    return return_type
