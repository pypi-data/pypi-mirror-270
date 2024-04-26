"""BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7048,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.system_deflections import _2727
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7053,
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
__all__ = ("BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
)


class BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation(
    _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _BEVEL_DIFFERENTIAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection

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
    ) -> "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation(
            self
        )
