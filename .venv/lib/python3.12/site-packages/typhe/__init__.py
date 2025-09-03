"""Typhe library for more types in Python.
struct: Struct like C (Experiemental)
uint??: Unsigned Integer
sint??: Signed Integer
mint: Modified Integer
mstr: Modified String

This library also includes informations about all unsigned / signeds.

usbit_sinfo: Unsigned Bit Information Function.
sbit_sinfo: Signed Bit Information Function.
"""

from typhe.main import *

__all__ = [
    'usbit_sinfo', 'sbit_sinfo',
    'usinfo8', 'sinfo8', 'usinfo16', 'sinfo16', 'usinfo32', 'sinfo32', 'usinfo64', 'sinfo64',
    'mint', 'mstr',
    'uint8', 'sint8', 'uint16', 'sint16', 'uint32', 'sint32', 'uint64', 'sint64', 'char',
    'struct'
]