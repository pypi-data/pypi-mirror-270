"""IntegrationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_INTEGRATION_METHOD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "IntegrationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("IntegrationMethod",)


Self = TypeVar("Self", bound="IntegrationMethod")


class IntegrationMethod(Enum):
    """IntegrationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INTEGRATION_METHOD

    NEWMARK = 0
    WILSON_THETA = 1
    BACKWARD_EULER_VELOCITY = 2
    LOBATTO3C_ORDER_2 = 3
    ESDIRK_ORDER_2 = 4
    ESDIRK_ORDER_4 = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


IntegrationMethod.__setattr__ = __enum_setattr
IntegrationMethod.__delattr__ = __enum_delattr
