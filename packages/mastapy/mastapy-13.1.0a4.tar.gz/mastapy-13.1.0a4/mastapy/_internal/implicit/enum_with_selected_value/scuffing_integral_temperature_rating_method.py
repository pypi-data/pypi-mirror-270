"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.rating.cylindrical import _489
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod"
)


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    """

    __qualname__ = "ScuffingIntegralTemperatureRatingMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_489.ScuffingIntegralTemperatureRatingMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _489.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> "_489.ScuffingIntegralTemperatureRatingMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _489.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self: Self) -> "_489.ScuffingIntegralTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_489.ScuffingIntegralTemperatureRatingMethod]":
        """List[mastapy.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod]

        Note:
            This property is readonly.
        """
        return None
