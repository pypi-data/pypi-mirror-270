"""ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7053,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7012
    from mastapy.system_model.analyses_and_results.system_deflections import _2864
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7040,
        _7069,
        _7095,
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation")


class ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation(
    _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
):
    """ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7012.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2864.ZerolBevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection

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
    ) -> "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation(self)
