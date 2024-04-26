"""ClutchHalfAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7076,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2735
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ClutchHalfAdvancedTimeSteppingAnalysisForModulation")


class ClutchHalfAdvancedTimeSteppingAnalysisForModulation(
    _7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
):
    """ClutchHalfAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ClutchHalfAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
            parent: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ClutchHalfAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6860.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2735.ClutchHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection

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
    ) -> "ClutchHalfAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ClutchHalfAdvancedTimeSteppingAnalysisForModulation(self)
