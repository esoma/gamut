
__all__ = ['ALL_GROUPS', 'verify_groups', 'verify_mask']

# python
# DVector4
import struct
from typing import Final

ALL_GROUPS: Final = -1


def verify_groups(value: int) -> int:
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise TypeError('groups must be int')
    try:
        struct.pack('=i', value)
    except struct.error:
        raise ValueError('groups must be 32 bit signed int')
    return value


def verify_mask(value: int) -> int:
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise TypeError('mask must be int')
    try:
        struct.pack('=i', value)
    except struct.error:
        raise ValueError('mask must be 32 bit signed int')
    return value
