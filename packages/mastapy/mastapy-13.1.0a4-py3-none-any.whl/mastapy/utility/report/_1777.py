"""CustomReportItemContainer"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainer"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1767, _1771, _1780, _1788


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainer",)


Self = TypeVar("Self", bound="CustomReportItemContainer")


class CustomReportItemContainer(_1776.CustomReportItem):
    """CustomReportItemContainer

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportItemContainer")

    class _Cast_CustomReportItemContainer:
        """Special nested class for casting CustomReportItemContainer to subclasses."""

        def __init__(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
            parent: "CustomReportItemContainer",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1776.CustomReportItem":
            return self._parent._cast(_1776.CustomReportItem)

        @property
        def custom_report(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1767.CustomReport":
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReport)

        @property
        def custom_report_column(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1771.CustomReportColumn":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportColumn)

        @property
        def custom_report_item_container_collection_item(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1780.CustomReportItemContainerCollectionItem":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_tab(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "_1788.CustomReportTab":
            from mastapy.utility.report import _1788

            return self._parent._cast(_1788.CustomReportTab)

        @property
        def custom_report_item_container(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer",
        ) -> "CustomReportItemContainer":
            return self._parent

        def __getattr__(
            self: "CustomReportItemContainer._Cast_CustomReportItemContainer", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportItemContainer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportItemContainer._Cast_CustomReportItemContainer":
        return self._Cast_CustomReportItemContainer(self)
