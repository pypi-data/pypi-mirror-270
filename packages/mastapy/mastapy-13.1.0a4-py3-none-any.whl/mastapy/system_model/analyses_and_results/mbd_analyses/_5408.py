"""BearingElementOrbitModel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_ELEMENT_ORBIT_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BearingElementOrbitModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingElementOrbitModel",)


Self = TypeVar("Self", bound="BearingElementOrbitModel")


class BearingElementOrbitModel(Enum):
    """BearingElementOrbitModel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_ELEMENT_ORBIT_MODEL

    FIXED_ANGLE = 0
    NOMINAL_CONTACT_ANGLE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingElementOrbitModel.__setattr__ = __enum_setattr
BearingElementOrbitModel.__delattr__ = __enum_delattr
