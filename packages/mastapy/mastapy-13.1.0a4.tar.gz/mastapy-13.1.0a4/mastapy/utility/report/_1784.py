"""CustomReportNameableItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportNameableItem"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1043
    from mastapy.utility.report import (
        _1755,
        _1763,
        _1764,
        _1765,
        _1766,
        _1768,
        _1769,
        _1773,
        _1775,
        _1782,
        _1783,
        _1785,
        _1787,
        _1790,
        _1792,
        _1793,
        _1795,
    )
    from mastapy.utility_gui.charts import _1871, _1872
    from mastapy.bearings.bearing_results import _1964, _1965, _1968, _1976
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2872,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4740,
        _4744,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportNameableItem",)


Self = TypeVar("Self", bound="CustomReportNameableItem")


class CustomReportNameableItem(_1776.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMEABLE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportNameableItem")

    class _Cast_CustomReportNameableItem:
        """Special nested class for casting CustomReportNameableItem to subclasses."""

        def __init__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
            parent: "CustomReportNameableItem",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1776.CustomReportItem":
            return self._parent._cast(_1776.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1043.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1043

            return self._parent._cast(_1043.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1755.AdHocCustomTable":
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1763.CustomChart":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1764.CustomDrawing":
            from mastapy.utility.report import _1764

            return self._parent._cast(_1764.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1765.CustomGraphic":
            from mastapy.utility.report import _1765

            return self._parent._cast(_1765.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1766.CustomImage":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.CustomImage)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1768.CustomReportCadDrawing":
            from mastapy.utility.report import _1768

            return self._parent._cast(_1768.CustomReportCadDrawing)

        @property
        def custom_report_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1769.CustomReportChart":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportChart)

        @property
        def custom_report_definition_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1773.CustomReportDefinitionItem":
            from mastapy.utility.report import _1773

            return self._parent._cast(_1773.CustomReportDefinitionItem)

        @property
        def custom_report_html_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1775.CustomReportHtmlItem":
            from mastapy.utility.report import _1775

            return self._parent._cast(_1775.CustomReportHtmlItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1782.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1783.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1783

            return self._parent._cast(_1783.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_named_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1785.CustomReportNamedItem":
            from mastapy.utility.report import _1785

            return self._parent._cast(_1785.CustomReportNamedItem)

        @property
        def custom_report_status_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1787.CustomReportStatusItem":
            from mastapy.utility.report import _1787

            return self._parent._cast(_1787.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1790.CustomReportText":
            from mastapy.utility.report import _1790

            return self._parent._cast(_1790.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1792.CustomSubReport":
            from mastapy.utility.report import _1792

            return self._parent._cast(_1792.CustomSubReport)

        @property
        def custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1793.CustomTable":
            from mastapy.utility.report import _1793

            return self._parent._cast(_1793.CustomTable)

        @property
        def dynamic_custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1795.DynamicCustomReportItem":
            from mastapy.utility.report import _1795

            return self._parent._cast(_1795.DynamicCustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1871.CustomLineChart":
            from mastapy.utility_gui.charts import _1871

            return self._parent._cast(_1871.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1872.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1872

            return self._parent._cast(_1872.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1964.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1965.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1965

            return self._parent._cast(_1965.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1968.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1968

            return self._parent._cast(_1968.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1976.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1976

            return self._parent._cast(_1976.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_2872.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2872,
            )

            return self._parent._cast(_2872.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4409.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4740.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4740,
            )

            return self._parent._cast(_4740.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4744.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4744,
            )

            return self._parent._cast(_4744.PerModeResultsReport)

        @property
        def custom_report_nameable_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "CustomReportNameableItem":
            return self._parent

        def __getattr__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportNameableItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def x_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    @enforce_parameter_types
    def x_position_for_cad(self: Self, value: "float"):
        self.wrapped.XPositionForCAD = float(value) if value is not None else 0.0

    @property
    def y_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    @enforce_parameter_types
    def y_position_for_cad(self: Self, value: "float"):
        self.wrapped.YPositionForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportNameableItem._Cast_CustomReportNameableItem":
        return self._Cast_CustomReportNameableItem(self)
