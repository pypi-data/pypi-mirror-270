"""MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7289,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7114,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7244,
        _7192,
        _7246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7289.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7289.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7289.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7244.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
