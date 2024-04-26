"""CylindricalPlanetGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3848,
        _3865,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearStabilityAnalysis")


class CylindricalPlanetGearStabilityAnalysis(_3836.CylindricalGearStabilityAnalysis):
    """CylindricalPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearStabilityAnalysis"
    )

    class _Cast_CylindricalPlanetGearStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
            parent: "CylindricalPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3836.CylindricalGearStabilityAnalysis":
            return self._parent._cast(_3836.CylindricalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3848.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "CylindricalPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearStabilityAnalysis(self)
