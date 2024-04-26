"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.geometry.two_d.curves import _320
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BasicCurveTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BasicCurveTypes")


class EnumWithSelectedValue_BasicCurveTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicCurveTypes

    A specific implementation of 'EnumWithSelectedValue' for 'BasicCurveTypes' types.
    """

    __qualname__ = "BasicCurveTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_320.BasicCurveTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _320.BasicCurveTypes

    @classmethod
    def implicit_type(cls) -> "_320.BasicCurveTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _320.BasicCurveTypes.type_()

    @property
    def selected_value(self: Self) -> "_320.BasicCurveTypes":
        """mastapy.geometry.two_d.curves.BasicCurveTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_320.BasicCurveTypes]":
        """List[mastapy.geometry.two_d.curves.BasicCurveTypes]

        Note:
            This property is readonly.
        """
        return None
