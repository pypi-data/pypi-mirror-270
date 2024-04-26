"""AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.system_deflections import _2714
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7048,
        _7051,
        _7052,
        _7053,
        _7100,
        _7137,
        _7143,
        _7146,
        _7149,
        _7150,
        _7164,
        _7095,
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"
)


class AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation(
    _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7149,
            )

            return self._parent._cast(
                _7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7150,
            )

            return self._parent._cast(
                _7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7164,
            )

            return self._parent._cast(
                _7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

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
    ) -> "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
