"""DrawStyleBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE_BASE = python_net_import("SMT.MastaAPI.Geometry", "DrawStyleBase")

if TYPE_CHECKING:
    from mastapy.geometry import _314
    from mastapy.system_model.drawing import _2264, _2270
    from mastapy.system_model.analyses_and_results.system_deflections import _2849
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3113,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import _3894
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4049
    from mastapy.system_model.analyses_and_results.power_flows import _4102, _4146
    from mastapy.system_model.analyses_and_results.modal_analyses import _4679
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5484
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610


__docformat__ = "restructuredtext en"
__all__ = ("DrawStyleBase",)


Self = TypeVar("Self", bound="DrawStyleBase")


class DrawStyleBase(_0.APIBase):
    """DrawStyleBase

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DrawStyleBase")

    class _Cast_DrawStyleBase:
        """Special nested class for casting DrawStyleBase to subclasses."""

        def __init__(
            self: "DrawStyleBase._Cast_DrawStyleBase", parent: "DrawStyleBase"
        ):
            self._parent = parent

        @property
        def draw_style(self: "DrawStyleBase._Cast_DrawStyleBase") -> "_314.DrawStyle":
            from mastapy.geometry import _314

            return self._parent._cast(_314.DrawStyle)

        @property
        def contour_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2264.ContourDrawStyle":
            from mastapy.system_model.drawing import _2264

            return self._parent._cast(_2264.ContourDrawStyle)

        @property
        def model_view_options_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2270.ModelViewOptionsDrawStyle":
            from mastapy.system_model.drawing import _2270

            return self._parent._cast(_2270.ModelViewOptionsDrawStyle)

        @property
        def system_deflection_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_2849.SystemDeflectionDrawStyle":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.SystemDeflectionDrawStyle)

        @property
        def steady_state_synchronous_response_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_3113.SteadyStateSynchronousResponseDrawStyle":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(_3113.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_3894.StabilityAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.StabilityAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4049.RotorDynamicsDrawStyle":
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4049

            return self._parent._cast(_4049.RotorDynamicsDrawStyle)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4102.CylindricalGearGeometricEntityDrawStyle":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4146.PowerFlowDrawStyle":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.PowerFlowDrawStyle)

        @property
        def modal_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_4679.ModalAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.ModalAnalysisDrawStyle)

        @property
        def mbd_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_5484.MBDAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(_5484.MBDAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_5788.HarmonicAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_6356.DynamicAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.DynamicAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "_6610.CriticalSpeedAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.CriticalSpeedAnalysisDrawStyle)

        @property
        def draw_style_base(
            self: "DrawStyleBase._Cast_DrawStyleBase",
        ) -> "DrawStyleBase":
            return self._parent

        def __getattr__(self: "DrawStyleBase._Cast_DrawStyleBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DrawStyleBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DrawStyleBase._Cast_DrawStyleBase":
        return self._Cast_DrawStyleBase(self)
