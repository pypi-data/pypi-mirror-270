"""BevelDifferentialPlanetGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6585,
        _6573,
        _6601,
        _6630,
        _6649,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCriticalSpeedAnalysis")


class BevelDifferentialPlanetGearCriticalSpeedAnalysis(
    _6580.BevelDifferentialGearCriticalSpeedAnalysis
):
    """BevelDifferentialPlanetGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
            parent: "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6580.BevelDifferentialGearCriticalSpeedAnalysis":
            return self._parent._cast(_6580.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6585.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6630.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCriticalSpeedAnalysis.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis(self)
