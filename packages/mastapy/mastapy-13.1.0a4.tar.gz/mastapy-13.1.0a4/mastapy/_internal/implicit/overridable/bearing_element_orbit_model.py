"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_BearingElementOrbitModel",)


Self = TypeVar("Self", bound="Overridable_BearingElementOrbitModel")


class Overridable_BearingElementOrbitModel(mixins.OverridableMixin, Enum):
    """Overridable_BearingElementOrbitModel

    A specific implementation of 'Overridable' for 'BearingElementOrbitModel' types.
    """

    __qualname__ = "BearingElementOrbitModel"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_5408.BearingElementOrbitModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5408.BearingElementOrbitModel

    @classmethod
    def implicit_type(cls) -> "_5408.BearingElementOrbitModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5408.BearingElementOrbitModel.type_()

    @property
    def value(self: Self) -> "_5408.BearingElementOrbitModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingElementOrbitModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        return None

    @property
    def override_value(self: Self) -> "_5408.BearingElementOrbitModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingElementOrbitModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_5408.BearingElementOrbitModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingElementOrbitModel

        Note:
            This property is readonly.
        """
        return None
