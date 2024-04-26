"""StraightBevelPlanetGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3898
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3804,
        _3792,
        _3820,
        _3848,
        _3865,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearStabilityAnalysis")


class StraightBevelPlanetGearStabilityAnalysis(
    _3898.StraightBevelDiffGearStabilityAnalysis
):
    """StraightBevelPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearStabilityAnalysis"
    )

    class _Cast_StraightBevelPlanetGearStabilityAnalysis:
        """Special nested class for casting StraightBevelPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
            parent: "StraightBevelPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3898.StraightBevelDiffGearStabilityAnalysis":
            return self._parent._cast(_3898.StraightBevelDiffGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3804.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3792.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3820.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3848.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "StraightBevelPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis":
        return self._Cast_StraightBevelPlanetGearStabilityAnalysis(self)
