"""GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7062,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.system_deflections import _2785
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="GuideDxfModelAdvancedTimeSteppingAnalysisForModulation")


class GuideDxfModelAdvancedTimeSteppingAnalysisForModulation(
    _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """GuideDxfModelAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GuideDxfModelAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
            parent: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
        ) -> "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6923.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2785.GuideDxfModelSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation(self)
