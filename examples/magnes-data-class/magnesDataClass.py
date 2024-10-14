#!/usr/bin/env python3 -d
"""!
    Magnes Data Class
    =================

    @author C. Mangiante
    @copyright Magnes AG, (C) 2024.
"""

import dataclasses
from typing import Any


# @dataclasses.dataclass
# class MagnesDataClass:
#    def __iter__(self):
#        for field in dataclasses.fields(self):
#            yield getattr(self, field.name)
#
#    def asdict(self):
#        return dataclasses.asdict(self)
#
#    # TODO Json Encoder
#
#    def __post_init__(self):
#        child_class = type(self)
#        parent_attrs = set(dir(MagnesDataClass))
#
#        child_fields = dataclasses.fields(child_class)
#        for f in child_fields:
#            if f.name not in parent_attrs:
#                # Check for methods
#                assert not (
#                    callable(getattr(child_class, f.name)) and f.name.startswith("__")
#                ), f"Adding methods to a data structure is not allowed. Found: {f.name}"
#
#                # Check for default fields
#                assert (
#                    f.default == dataclasses.field
#                    and f.default_factory == dataclasses.field
#                ), f"Adding fields with default values is not allowed. Found: {f.name}"


class MagnesDataClass:
    def __iter__(self):
        return iter(getattr(self, f.name) for f in dataclasses.fields(self))

    def asdict(self):
        return dataclasses.asdict(self)

    # TODO Json Encoder


# see https://github.com/python/cpython/blob/main/Lib/dataclasses.py line 1337 to see the definition for the decorator function of python dataclasses
def magnes_dataclass(
    _cls=None,
    *,
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
):
    def wrap(cls):
        # Perform checks before creating the dataclass
        for name, value in cls.__dict__.items():
            if name.startswith("__"):
                continue

            assert not callable(
                value
            ), f"Adding methods to this data structure is not allowed. Found: {name}"

            if isinstance(value, dataclasses.Field):
                assert (
                    value.default == dataclasses.field
                    and value.default_factory == dataclasses.field
                ), f"Adding fields with default values is not allowed. Found: {name}"

        # Create the dataclass
        cls = dataclasses.dataclass(
            cls,
            init=init,
            repr=repr,
            eq=eq,
            order=order,
            unsafe_hash=unsafe_hash,
            frozen=frozen,
        )
        return type(cls.__name__, (cls, MagnesDataClass), {})

    if _cls is None:
        return wrap

    return wrap(_cls)
