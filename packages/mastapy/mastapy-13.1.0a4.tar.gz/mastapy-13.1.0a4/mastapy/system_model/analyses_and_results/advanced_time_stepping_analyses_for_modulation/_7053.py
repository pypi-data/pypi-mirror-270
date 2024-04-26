"""BevelGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7040,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.system_deflections import _2731
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7048,
        _7051,
        _7052,
        _7137,
        _7143,
        _7146,
        _7149,
        _7150,
        _7164,
        _7069,
        _7095,
        _7115,
        _7062,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BevelGearAdvancedTimeSteppingAnalysisForModulation")


class BevelGearAdvancedTimeSteppingAnalysisForModulation(
    _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
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
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7149,
            )

            return self._parent._cast(
                _7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7150,
            )

            return self._parent._cast(
                _7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7164,
            )

            return self._parent._cast(
                _7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2731.BevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection

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
    ) -> "BevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearAdvancedTimeSteppingAnalysisForModulation(self)
