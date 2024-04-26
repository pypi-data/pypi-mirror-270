"""PlanetaryGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetaryGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6632,
        _6670,
        _6569,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCriticalSpeedAnalysis")


class PlanetaryGearSetCriticalSpeedAnalysis(
    _6621.CylindricalGearSetCriticalSpeedAnalysis
):
    """PlanetaryGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCriticalSpeedAnalysis"
    )

    class _Cast_PlanetaryGearSetCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
            parent: "PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_6621.CylindricalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6621.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_6632.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_6670.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_6569.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "PlanetaryGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCriticalSpeedAnalysis.TYPE"
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
    ) -> "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis":
        return self._Cast_PlanetaryGearSetCriticalSpeedAnalysis(self)
