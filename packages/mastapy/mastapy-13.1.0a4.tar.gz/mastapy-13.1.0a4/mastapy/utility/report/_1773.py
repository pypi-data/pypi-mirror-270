"""CustomReportDefinitionItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportDefinitionItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import (
        _1755,
        _1763,
        _1764,
        _1765,
        _1766,
        _1775,
        _1787,
        _1790,
        _1792,
        _1776,
    )
    from mastapy.bearings.bearing_results import _1965
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportDefinitionItem",)


Self = TypeVar("Self", bound="CustomReportDefinitionItem")


class CustomReportDefinitionItem(_1784.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_DEFINITION_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportDefinitionItem")

    class _Cast_CustomReportDefinitionItem:
        """Special nested class for casting CustomReportDefinitionItem to subclasses."""

        def __init__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            parent: "CustomReportDefinitionItem",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1784.CustomReportNameableItem":
            return self._parent._cast(_1784.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1776.CustomReportItem":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportItem)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1755.AdHocCustomTable":
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1763.CustomChart":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1764.CustomDrawing":
            from mastapy.utility.report import _1764

            return self._parent._cast(_1764.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1765.CustomGraphic":
            from mastapy.utility.report import _1765

            return self._parent._cast(_1765.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1766.CustomImage":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.CustomImage)

        @property
        def custom_report_html_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1775.CustomReportHtmlItem":
            from mastapy.utility.report import _1775

            return self._parent._cast(_1775.CustomReportHtmlItem)

        @property
        def custom_report_status_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1787.CustomReportStatusItem":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1790.CustomReportText":
            from mastapy.utility.report import _1790

            return self._parent._cast(_1790.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1792.CustomSubReport":
            from mastapy.utility.report import _1792

            return self._parent._cast(_1792.CustomSubReport)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_1965.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.LoadedBearingChartReporter)

        @property
        def parametric_study_histogram(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "_4409.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ParametricStudyHistogram)

        @property
        def custom_report_definition_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "CustomReportDefinitionItem":
            return self._parent

        def __getattr__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportDefinitionItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem":
        return self._Cast_CustomReportDefinitionItem(self)
