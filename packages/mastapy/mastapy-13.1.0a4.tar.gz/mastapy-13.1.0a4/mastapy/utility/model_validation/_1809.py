"""StatusItemWrapper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATUS_ITEM_WRAPPER = python_net_import(
    "SMT.MastaAPI.Utility.ModelValidation", "StatusItemWrapper"
)

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1807


__docformat__ = "restructuredtext en"
__all__ = ("StatusItemWrapper",)


Self = TypeVar("Self", bound="StatusItemWrapper")


class StatusItemWrapper(_0.APIBase):
    """StatusItemWrapper

    This is a mastapy class.
    """

    TYPE = _STATUS_ITEM_WRAPPER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatusItemWrapper")

    class _Cast_StatusItemWrapper:
        """Special nested class for casting StatusItemWrapper to subclasses."""

        def __init__(
            self: "StatusItemWrapper._Cast_StatusItemWrapper",
            parent: "StatusItemWrapper",
        ):
            self._parent = parent

        @property
        def status_item_wrapper(
            self: "StatusItemWrapper._Cast_StatusItemWrapper",
        ) -> "StatusItemWrapper":
            return self._parent

        def __getattr__(self: "StatusItemWrapper._Cast_StatusItemWrapper", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatusItemWrapper.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def category(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Category

        if temp is None:
            return ""

        return temp

    @property
    def description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Description

        if temp is None:
            return ""

        return temp

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def status_item(self: Self) -> "_1807.StatusItem":
        """mastapy.utility.model_validation.StatusItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatusItem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StatusItemWrapper._Cast_StatusItemWrapper":
        return self._Cast_StatusItemWrapper(self)
