"""PlanetaryGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PlanetaryGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3847,
        _3886,
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetStabilityAnalysis")


class PlanetaryGearSetStabilityAnalysis(_3835.CylindricalGearSetStabilityAnalysis):
    """PlanetaryGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetStabilityAnalysis")

    class _Cast_PlanetaryGearSetStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
            parent: "PlanetaryGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3835.CylindricalGearSetStabilityAnalysis":
            return self._parent._cast(_3835.CylindricalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3847.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "PlanetaryGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2560.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis":
        return self._Cast_PlanetaryGearSetStabilityAnalysis(self)
