"""ContactDampingModel"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONTACT_DAMPING_MODEL = python_net_import(
    "SMT.MastaAPI.MathUtility.HertzianContact", "ContactDampingModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactDampingModel",)


Self = TypeVar("Self", bound="ContactDampingModel")


class ContactDampingModel(Enum):
    """ContactDampingModel

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_DAMPING_MODEL

    RAYLEIGH = 0
    CONSTANT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ContactDampingModel.__setattr__ = __enum_setattr
ContactDampingModel.__delattr__ = __enum_delattr
