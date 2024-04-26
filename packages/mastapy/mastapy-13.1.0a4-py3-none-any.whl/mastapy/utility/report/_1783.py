"""CustomReportMultiPropertyItemBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItemBase"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1043
    from mastapy.utility.report import _1769, _1782, _1793, _1776
    from mastapy.utility_gui.charts import _1871, _1872
    from mastapy.bearings.bearing_results import _1964, _1968, _1976
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2872,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4740,
        _4744,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportMultiPropertyItemBase",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItemBase")


class CustomReportMultiPropertyItemBase(_1784.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItemBase")

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            parent: "CustomReportMultiPropertyItemBase",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1784.CustomReportNameableItem":
            return self._parent._cast(_1784.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1776.CustomReportItem":
            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1043.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1043

            return self._parent._cast(_1043.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1769.CustomReportChart":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1782.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.CustomReportMultiPropertyItem)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1793.CustomTable":
            from mastapy.utility.report import _1793

            return self._parent._cast(_1793.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1871.CustomLineChart":
            from mastapy.utility_gui.charts import _1871

            return self._parent._cast(_1871.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1872.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1872

            return self._parent._cast(_1872.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1964.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1968.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1968

            return self._parent._cast(_1968.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_1976.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1976

            return self._parent._cast(_1976.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_2872.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2872,
            )

            return self._parent._cast(_2872.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4740.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4740,
            )

            return self._parent._cast(_4740.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "_4744.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4744,
            )

            return self._parent._cast(_4744.PerModeResultsReport)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "CustomReportMultiPropertyItemBase":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CustomReportMultiPropertyItemBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase":
        return self._Cast_CustomReportMultiPropertyItemBase(self)
